var express = require('express')
var path    = require("path");
var app = express();
app.use(express.json());
app.use(express.urlencoded());
let logCollection = [];

app.all('/*', function(req, res, next) {
    console.log(req.headers)
    console.log("all");
    res.header("Access-Control-Allow-Origin","*");
    res.header('Access-Control-Allow-Methods','PUT, GET, POST, DELETE, OPTIONS');
    res.header("Access-Control-Allow-Headers","Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token");
    next();
})

app.get('/log', function (req,res) {
    res.sendFile(path.join(__dirname+'/index.html'));
})

app.post('/log', function (req, res) {

    res.send(logCollection);
    logCollection = []
})

app.put('/log', function (req, res) {
    if (req.body.log)
        logCollection.push(req.body.log)
    res.send('ok');

})

app.options('/*', function (req, res) {
    res.send('ok');

})

app.listen(8881, function() {
    console.log('CROS-enable');
});
