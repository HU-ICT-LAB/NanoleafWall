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

function generatecolorstring() {
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

function random(scope) {
    return Math.floor(Math.random() * scope).toString();
}

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
    for (TimesMoleParTime = 1; TimesMoleParTime < 4; TimesMoleParTime++) {
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
    var TouchedTileData = numberOfTouchedTile + " 1 105 0 0 0 200";
    var NewTouchedTileData = numberOfTouchedTile + " 1 0 255 0 0 200";
    var oldColors = oldColors.toString();
    var newColor = oldColors.replace(NewTouchedTileData, TouchedTileData);

    //make new tile
    var NewTile = random(102);
    var NewTouchableTileGreen = NewTile + " 1 0 255 0 0 200";
    var NewTouchableTileRed = NewTile + " 1 105 0 0 0 200";
    var newColor = newColor.replace(NewTouchableTileRed, NewTouchableTileGreen);

    console.log("1" + NewTouchedTileData);
    console.log("2" + TouchedTileData);
    console.log(newColor);
    console.log(oldColors);
    res.send({
        "command": "display/add",
        "animType": "static",
        "animData": newColor,
        "loop": false
    })
});

// Offical Features to FE
var ColorstringFromFE;
var ClickedTileArray = ["000"];
var PostedColorstring;

app.post("/currentColorStringFormFE", function (request, res) {
    console.log(request.body)
    ColorstringFromFE = request.body.colorstring;
    console.log(ColorstringFromFE)
    res.send("done")
});

app.post("/singleClickEvent", function (request, res) {
    console.log("djkal");
    var touchedTile = request.body.data;
    res.send("Single Click Event Transmitted");
    console.log(touchedTile);
    touchedTile = touchedTile.replace("tile", "");
    console.log(touchedTile);
    if (ClickedTileArray[0] == "000") {
        ClickedTileArray[0] = touchedTile;
        console.log(ClickedTileArray);
    }
    else {
        ClickedTileArray.push(touchedTile);
        console.log(ClickedTileArray);
    }
});


app.get("/PostNewColorString", function (req, res) {
        res.send(
            {
                "command": "display/add",
                "animType": "static",
                "animData": PostedColorstring,
                "loop": false
            }
        )
    });

function range(start, end) {
    var ans = [];
    for (let i = start; i <= end; i++) {
        ans.push(i);
    }
    return ans;
}

// Offical Endpoints
app.get("/currentColorString", function (req, res) {
    res.send(
        {
            "command": "display/add",
            "animType": "static",
            "animData": ColorstringFromFE,
            "loop": false
        }
    )
});

app.get("/lastTouchedTiles", function (req, res) {
    var TileNumbers;
    console.log(ClickedTileArray);
    if (ClickedTileArray.length == 1) {
        var tempTileName = ClickedTileArray[0];
        var ArrayOfEvents = [{ "gesture": 0, "panelId": tempTileName}];
    }
    else {
        var tempTileName = ClickedTileArray[0].toString();
        var ArrayOfEvents = [{ "gesture": 0, "panelId": tempTileName }];
        for (TileNumbers = 1; TileNumbers < ClickedTileArray.length; TileNumbers++) {
            var SmallTouchDict = { "gesture": 0, "panelId": ClickedTileArray[TileNumbers] };
            ArrayOfEvents.push(SmallTouchDict);
        }
    }
    res.send(
        {
            "events": ArrayOfEvents
        }
    )
    ClickedTileArray = [];
});

app.post("/colorString", function (req, res) {
    console.log("function started");
    PostedColorstring = req.body.animData;
    console.log(PostedColorstring);
    res.send("Done.");
});


http.createServer(app).listen(3000, function () {
    console.log("Server started at port 3000")
})

