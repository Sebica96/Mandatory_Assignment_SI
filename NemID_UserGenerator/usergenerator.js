const express = require('express');
const bodyParser = require('body-parser')

let app = express();

app.use(bodyParser.json());

app.post("/generate-nemID", (req, res) => {
    console.log("Body: " + req.body);
    const cpr = req.body.cpr._;
    console.log(cpr);
    const randomNumber = Math.floor(10000 + Math.random() * 90000);
    const last4cprnumbers = cpr.slice(-4);
    const nemId = randomNumber + last4cprnumbers;
    console.log(nemId);

    res.json({
        status: 201,
        nemId: nemId
    });
});

app.listen(8088, (err) => {
    if(err){
        console.log(err);
    }
    else{
        console.log('Listening on port 8088...');
    }
});