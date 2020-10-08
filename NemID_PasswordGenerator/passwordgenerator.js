const express = require('express');
let app = express();
app.use(express.json());

app.post("/generate-password-nemID", (req, res) => {
    let nemID = req.body.nemId;
    let cpr = req.body.cpr;
    let password = nemID.slice(0, 2) + cpr.slice(-2);

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