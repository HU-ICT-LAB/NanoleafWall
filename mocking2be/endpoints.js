var bodyParser = require('body-parser');
//npm install body-parser
var http = require("http");
//npm install http
var express = require("express");
//npm install express
var app = express();
var sessionkey = null;

var allowCrossDomain = function (req, res, next) {
    res.header('Access-Control-Allow-Origin', "*");
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type');
    next();
}

app.use(allowCrossDomain);

function authkey() {
    var key = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
    sessionkey = key;
    console.log(sessionkey);
    return key;
}

function generatecolorstring(){
    var totalpanels;
    var anidata = "103 ";

    for (totalpanels = 1; totalpanels < 103; totalpanels++) {
        var role1 = totalpanels.toString() + " ";
        var role2 = "1 "
        var role3 = Math.floor(Math.random() * 255).toString() + " ";
        var role4 = Math.floor(Math.random() * 255).toString() + " ";
        var role5 = Math.floor(Math.random() * 255).toString() + " ";
        var role6 = Math.floor(Math.random() * 255).toString() + " ";
        var role7 = "200 ";
        anidata = anidata + role1 + role2 + role3 + role4 + role5 + role6 + role7;
    }
return anidata
}

app.get("/authkey", function (req, res) {
    res.send(authkey())
});

app.get("/Startbutton", function (req, res) {
    res.send(
        {
            "command": "display/add",
            "animType": "static",
            "animData": generatecolorstring().toString(),
            "loop": false
        }

    )
});

app.get("/distance", function (req, res) {

});

http.createServer(app).listen(3000, function () {
    console.log("Server started at port 3000")
})

