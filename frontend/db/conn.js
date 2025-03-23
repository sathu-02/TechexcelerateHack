const mongoose = require("mongoose");

const uri = "mongodb+srv://edithvision3000:edithvision@cluster0.dqjqi.mongodb.net/anomalydetectiondb?retryWrites=true&w=majority";

let isConnected = false;

const connectDB = async () => {
    if (isConnected) {
        console.log("Using existing database connection");
        return;
    }

    try {
        await mongoose.connect(uri, {
            useNewUrlParser: true,
            useUnifiedTopology: true
        });

        isConnected = true;
        console.log("Database connected successfully");
    } catch (error) {
        console.error("Database connection failed:", error);
        throw error;
    }
};

// Define Schema & Model
const Loginschema = new mongoose.Schema({
    name: { type: String, required: true },
    password: { type: String, required: true }
});

const User = mongoose.model("users", Loginschema);

module.exports = { connectDB, User };
