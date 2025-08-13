# BokFinner (pet-prosjekt)

Mitt personlig pet-prosjekt som demonstrerer et enkelt, moderne boksøkeverktøy bygget med Node.js, Express, EJS og Axios. Applikasjonen henter bokdata fra det åpne OpenLibrary API og viser raske resultater med fokus på enkelhet og lesbarhet.

## Funksjoner
- Søk etter bøker via tittel (delvise treff støttes)
- Visning av: tittel, forfatter, første utgivelsesår og omslag (hvis tilgjengelig)
- Plassholder vises når omslag mangler
- Paginering:
  - Forrige / Neste
  - "Til start" og "Til slutt" knapper
  - Justerbar størrelse per side (12 / 24 / 36 / 48)
  - Kompakt numerisk paginering med ellipser (…)

## Teknologi-stack
| Teknologi | Bruk |
|-----------|------|
| Node.js   | Runtime | 
| Express   | HTTP-server og ruting |
| EJS       | Serverside templating (views & partials) |
| Axios     | HTTP-klient mot OpenLibrary API |
| CSS (plain) | Layout, responsive grid og paginering |
| OpenLibrary API | Datakilde for boksøk |

## Mappestruktur (forenklet)
```
book-search-app/
  package.json
  src/
    index.js
    routes/
      books.js
    views/
      index.ejs
      results.ejs
      partials/
        header.ejs
        footer.ejs
    public/
      css/
        styles.css
```

## Oppsett og kjøring
Forutsetning: Du har Node.js (>=18 anbefalt) og npm installert.

1. Klon (eller last ned) prosjektet.
2. Installer avhengigheter:
```
npm install
```
3. Start serveren (standard port 3000):
```
npm start
```
   Eller med nodemon (hvis lagt til dev-script):
```
npm run dev
```
4. Åpne i nettleseren:
```
http://localhost:3000
```
5. Skriv inn et søk (f.eks. "Harry Potter") og naviger med pagineringen.

## Miljøvariabler
Ingen nødvendige. Alle kall går direkte mot offentlig OpenLibrary-endepunkt.

## Tilpasning
- Endre antall elementer per side: oppdater listen [12, 24, 36, 48] i `routes/books.js`.
- Endre maks antall pagineringsknapper: juster `maxButtons` i samme fil.
- Endre navn / branding: rediger `partials/header.ejs` + README.

## Feilhåndtering
- Nettverksfeil eller API-problemer gir en rød feilmelding på resultatsiden.
- Ugyldig side (`page` > siste) omdirigeres til siste gyldige.

## Lisens
Prosjektet er laget som et lærings-/pet-prosjekt. Bruk fritt, men sjekk OpenLibrary sine bruksvilkår for API.

---
Laget som et personlig øvingsprosjekt for å styrke ferdigheter i fullstack JS og strukturering av små Express-applikasjoner.
