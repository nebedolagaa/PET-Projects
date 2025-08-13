import { Router } from "express";
import axios from "axios";

const router = Router();

// Rute for å behandle søk /books/search?q=...
router.get("/search", async (req, res) => {
  const q = (req.query.q || "").trim();              // Brukerens søketekst
  const page = Math.max(parseInt(req.query.page || "1", 10), 1); // Nåværende side (>=1)
  const perPage = (() => {                           // Antall bøker per side (justerbart)
    const raw = parseInt(req.query.perPage || "24", 10);
    if ([12, 24, 36, 48].includes(raw)) return raw;
    return 24;
  })();

  // Dersom tom streng – viser tomt resultat (uten feil)
  if (!q) {
    return res.render("results", { books: [], query: q, error: null, page, totalPages: 0 });
  }

  try {
    // OpenLibrary returnerer inntil 100 docs per page. Vi bruker samme sideparameter.
    const API_URL = `https://openlibrary.org/search.json?q=${encodeURIComponent(q)}&page=${page}`;

    const { data } = await axios.get(API_URL);

    const totalFound = typeof data.numFound === 'number' ? data.numFound : 0;
    const totalPages = totalFound ? Math.ceil(totalFound / perPage) : 0;

    // Begrens docs til perPage (vi viser bare de første 24 av det settet vi får denne runden)
    const docs = Array.isArray(data.docs) ? data.docs.slice(0, perPage) : [];

    const books = docs.map(d => ({
      title: d.title || "Ingen tittel",
      author: (d.author_name && d.author_name[0]) || "Ukjent forfatter",
      year: d.first_publish_year || "—",
      coverId: d.cover_i || null
    }));

    // Hvis valgt page er > totalPages (kan skje hvis bruker manuelt endrer i URL) – redirect til siste
    if (totalPages && page > totalPages) {
      return res.redirect(`/books/search?q=${encodeURIComponent(q)}&page=${totalPages}&perPage=${perPage}`);
    }
    // Bygging av avkortet sidetallsliste (numerisk paginering)
    const pages = [];
    const maxButtons = 7;
    if (totalPages <= maxButtons) {
      for (let p = 1; p <= totalPages; p++) pages.push(p);
    } else {
      const showLeft = Math.max(2, page - 1);
      const showRight = Math.min(totalPages - 1, page + 1);
      pages.push(1);
      if (showLeft > 2) pages.push('…');
      for (let p = showLeft; p <= showRight; p++) pages.push(p);
      if (showRight < totalPages - 1) pages.push('…');
      pages.push(totalPages);
    }

    res.render("results", { books, query: q, error: null, page, totalPages, perPage, pages });
  } catch (err) {
    console.error("Feil ved forespørsel:", err.message);
    res.render("results", { books: [], query: q, error: "Feil ved forespørsel til OpenLibrary", page: 1, totalPages: 0, perPage: 24, pages: [] });
  }
});

export default router;