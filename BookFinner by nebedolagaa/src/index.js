import express from "express";
import path from "path";
import { fileURLToPath } from "url";
import bookRoutes from "./routes/books.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const port = 3000;

// Konfigurerer EJS som templatemotor
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views")); // Mappe med EJS-filer

// Statisk innhold (CSS) fra /src/public
app.use(express.static(path.join(__dirname, "public")));

// Statisk innhold for favicon og manifest (ligger utenfor /src/public)
// Denne mappen inneholder genererte favicon-filer (png, ico, manifest)
app.use(express.static(path.join(__dirname, "..", "favicon")));

// Rot-side: søkeskjema
app.get("/", (req, res) => {
  res.render("index");
});

// Ruter for /books/search
app.use("/books", bookRoutes);

// Starter serveren
app.listen(port, () => {
  console.log(`Server kjører: http://localhost:${port}`);
});