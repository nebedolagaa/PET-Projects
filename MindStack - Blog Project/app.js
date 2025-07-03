import express from "express";
import bodyParser from "body-parser";
import methodOverride from "method-override";

const app = express();
const port = 3000;

app.set("view engine", "ejs");

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(methodOverride('_method'));

let posts = [
    { id: 1, title: "Tip: Use const and let instead of var", content: "In modern JavaScript, it is recommended to use const for immutable variables and let for mutable ones. This helps avoid errors related to scope and variable redeclaration." },
    { id: 2, title: "Node.js: Asynchronous code with async/await", content: "Instead of nested callbacks, use async/await for asynchronous code. This makes your code cleaner and easier to understand." },
    { id: 3, title: "Express.js: Use middleware for error handling", content: "Create a separate middleware for centralized error handling. This simplifies debugging and increases application stability." },
    { id: 4, title: "Tip: Use template literals", content: "Template literals allow you to conveniently insert variables and expressions into strings: `Hello, ${name}!`." },
    { id: 5, title: "Node.js: Don’t block the event loop", content: "Avoid long synchronous operations in Node.js to prevent blocking the event loop. Use asynchronous methods for file and network operations." },
    { id: 6, title: "Express.js: Split routes into modules", content: "Organize Express routes into separate modules for better structure and code readability." },
    { id: 7, title: "Tip: Use strict mode", content: "Add 'use strict' at the beginning of files or functions to prevent certain errors and improve code safety." },
    { id: 8, title: "Node.js: Use dotenv for environment variables", content: "Store sensitive data (like API keys) in a .env file and use the dotenv package to load them into process.env." }
];

app.get("/", (req, res) => {
    const page = parseInt(req.query.page) || 1;
    const postsPerPage = 6;
    const totalPosts = posts.length;
    const totalPages = Math.ceil(totalPosts / postsPerPage);
    const startIndex = (page - 1) * postsPerPage;
    const endIndex = startIndex + postsPerPage;
    const currentPosts = posts.slice(startIndex, endIndex);
    
    res.render("index", { 
        posts: currentPosts,
        currentPage: page,
        totalPages: totalPages,
        totalPosts: totalPosts
    });
});

app.get("/new", (req, res) => {
    res.render("new");
});

app.post("/posts", (req, res) => {
    const { title, content } = req.body;
    posts.push({ id: Date.now(), title, content });
    res.redirect("/");
});

app.get("/edit/:id", (req, res) => {
    const post = posts.find(p => p.id == req.params.id);
    res.render("edit", { post });
});

app.put("/posts/:id", (req, res) => {
    const { title, content } = req.body;
    const post = posts.find(p => p.id == req.params.id);
    post.title = title;
    post.content = content;
    res.redirect("/");
});

app.delete("/posts/:id", (req, res) => {
    posts = posts.filter(p => p.id != req.params.id);
    res.redirect("/");
});

app.get("/posts/:id", (req, res) => {
    const post = posts.find(p => p.id == req.params.id);
    if (!post) {
        return res.status(404).send("Post not found");
    }
    res.render("view", { post });
});

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});