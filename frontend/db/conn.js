const mongoose = require("mongoose");

//creating a database
const connect = mongoose.connect("mongodb+srv://edithvision3000:edithvision@cluster0.dqjqi.mongodb.net/anomalydetectiondb?retryWrites=true&w=majority");

connect.then(()=>{
    console.log("connection successful");
}).catch((error)=>{
    console.log(error);
});

//create schema
const Loginschema = new mongoose.Schema({
    name: {
        type:String,
        required: true
    },
    password: {
        type: String,
        required: true
    }
});

// collection part
const collection = new mongoose.model("users", Loginschema);

module.exports = collection;
