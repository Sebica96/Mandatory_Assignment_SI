const express = require('express');
let app = express();
app.use(express.json());

app.post("/generate-nemID", (req, res) => {
    let cpr = req.body.cpr;
    let email = req.body.email;
    let randomNumber = Math.floor(10000 + Math.random() * 90000);
    let nemId = randomNumber + cpr.slice(-4);

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