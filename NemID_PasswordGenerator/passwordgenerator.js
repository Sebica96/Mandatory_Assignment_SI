const express = require('express');
const bodyParser = require('body-parser')

let app = express()

app.use(bodyParser.json())

app.post("/generate-password-nemID", (req, res) => {
    let nemID = req.body.nemId;
    console.log(nemID);
    let cpr = req.body.cpr._;
    console.log(cpr);
    let password = nemID.slice(0, 2) + cpr.slice(-2);
    console.log(password);


    res.json({
        status: 200,
        nemIdPassword: password
    });
});

app.listen(8089, (err) => {
    if(err){
        console.log(err);
    }
    else{
        console.log('Listening on port 8089...');
    }
});