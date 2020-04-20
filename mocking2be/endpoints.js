var bodyParser = require('body-parser');
//npm install body-parser
var http = require("http");
//npm install http
var express = require("express");
//npm install express
var app = express();
var sessionkey = null;
var totalNumberOfPanels = 102;


var allowCrossDomain = function (req, res, next) {
    res.header('Access-Control-Allow-Origin', "*");
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type');
    next();
}

app.use(allowCrossDomain);
app.use(express.urlencoded());
app.use(express.json());


function authkey() {
    var key = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
    sessionkey = key;
    console.log(sessionkey);
    return key;
}

function generatecolorstring(){
    var totalpanels;
    var anidata = totalNumberOfPanels + " ";

    for (totalpanels = 1; totalpanels < totalNumberOfPanels + 1; totalpanels++) {
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

app.get("/level1", function (req, res) {
    res.send({
        "command": "display/add",
        "animType": "static",
        "animData": firstSetMoles(),
        "loop": false
    });
});

function firstSetMoles() {
    var totalpanels;
    var anidata = "103 ";

    for (totalpanels = 1; totalpanels < 103; totalpanels++) {
        var role1 = totalpanels.toString() + " ";
        var role2 = "1 "
        var role3 = 105 + " ";
        var role4 = 0 + " ";
        var role5 = 0 + " ";
        var role6 = 0 + " ";
        var role7 = "200 ";
        anidata = anidata + role1 + role2 + role3 + role4 + role5 + role6 + role7;
    }
    var TimesMoleParTime = 1;
    for (TimesMoleParTime = 1; TimesMoleParTime < 4; TimesMoleParTime++){
        var TempTileNumber = Math.floor(Math.random() * totalNumberOfPanels);
        var OldTileRed = TempTileNumber + " 1 105 0 0 0 200";
        console.log(OldTileRed);
        var MakeTileGreen = TempTileNumber + " 1 0 255 0 0 200";
        console.log(MakeTileGreen);
        anidata = anidata.toString();
        anidata = anidata.replace(OldTileRed, MakeTileGreen);
    }
return anidata
}

app.post("/levelContinuation", function (request, res) {
    var touchedTile = request.body.data;
    var oldColors = request.body.colorstring;
    
    var numberOfTouchedTile = touchedTile.replace("tile", "");
    var TouchedTileData = numberOfTouchedTile + " 1 105 0 0 200";
    var NewTouchedTileData = numberOfTouchedTile + " 1 0 255 0 200";
    var newColor = oldColors.replace(NewTouchedTileData, TouchedTileData);
    console.log(NewTouchedTileData + TouchedTileData + oldColors + newColor);
    res.send({
    "command": "display/add",
    "animType": "static",
    "animData": newColor,
    "loop": false
    })
});


http.createServer(app).listen(3000, function () {
    console.log("Server started at port 3000")
})

