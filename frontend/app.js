const express = require("express");
const path = require("path");
const collection = require("./db/conn");
const bcrypt = require("bcrypt");
const cors = require("cors");


const app = express();
const port = process.env.PORT || 3000;

const staticPath = path.join(__dirname, "../public");

// Middleware
app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.static(staticPath));
app.use(express.static(path.join(__dirname, "../frontend")));

app.use(cors());
// Routes
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "../frontend/home.html"));
});

app.get("/signup", (req, res) => {
    res.sendFile(path.join(__dirname, "../frontend/signup.html"));
});

app.get("/login", (req, res) => {
    res.sendFile(path.join(__dirname, "../frontend/login.html"));
});

app.get("/main", (req, res) => {
    res.sendFile(path.join(__dirname, "../frontend/main.html"));
});

app.get("/history", (req, res) => {
    res.sendFile(path.join(__dirname, "../frontend/history.html"));
});


app.post("/signup", async (req, res) => {
    const { username, password } = req.body;

    try {
        const existingUser = await collection.findOne({ name: username });

        if (existingUser) {
            return res.send("<script>alert('User already exists. Choose a different username.'); window.location='/signup';</script>");
        }

        const hashedPassword = await bcrypt.hash(password, 10);
        await collection.create({ name: username, password: hashedPassword });

        res.sendFile(path.join(__dirname, "../frontend/main.html"));
    } catch (error) {
        console.error(error);
        res.status(500).send("Internal Server Error");
    }
});

app.post("/login", async (req, res) => {
    try {
        const user = await collection.findOne({ name: req.body.username });

        if (!user || !(await bcrypt.compare(req.body.password, user.password))) {
            return res.send("<script>alert('Invalid Username or Password'); window.location='/login';</script>");
        }

        res.sendFile(path.join(__dirname, "../frontend/main.html"));
    } catch (error) {
        console.error(error);
        res.status(500).send("Internal Server Error");
    }
});

// Start Server
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});

