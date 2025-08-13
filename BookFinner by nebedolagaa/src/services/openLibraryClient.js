import axios from "axios";

// Funksjon for å søke etter bøker etter tittel via OpenLibrary API
export const searchBooks = async (title) => {
    try {
        // Sender en GET-forespørsel til OpenLibrary API med boktittelen
        const response = await axios.get(`https://openlibrary.org/search.json?title=${encodeURIComponent(title)}`);
        // Returnerer bokdata
        return response.data;
    } catch (error) {
        // Håndterer feil ved forespørselen
        console.error("Feil ved henting av data fra OpenLibrary API:", error);
        throw error;
    }
};