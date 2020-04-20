var lastColorCode = null;

function loadKey() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText);
      }
    };
    xhttp.open("GET", "http://localhost:3000/authkey", true);
    xhttp.send();
}


function colorProccesor(dict){
    var stringOfColors = dict.toString();
    var arrayOfColors = stringOfColors.split(" ");
    var numberInArray;
    console.log(arrayOfColors[0]);
    for (numberInArray = 1; numberInArray < 102 * 7; numberInArray += 7) {
        var tile = arrayOfColors[numberInArray];
        var red = arrayOfColors[numberInArray + 2];
        var green = arrayOfColors[numberInArray + 3];
        var blue = arrayOfColors[numberInArray + 4];
        var white = arrayOfColors[numberInArray + 5];
        var time = arrayOfColors[numberInArray + 6];
        var tileName = "tile" + tile;
        var PanelInHtml = document.getElementById(tileName);
        var RGBcolorInString = "rgb(" + red + ", " + green + ", " + blue + ")";   
        console.log(PanelInHtml, RGBcolorInString);
        PanelInHtml.style.backgroundColor = RGBcolorInString;
    } 
}

function Start(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText);
        var dict = JSON.parse(this.responseText);
        console.log(dict)
        var lastColorCode = dict["animData"]
        console.log(lastColorCode);
        colorProccesor(lastColorCode);
      }
    };
    xhttp.open("GET", "http://localhost:3000/Startbutton", true);
    xhttp.send();
}

Start();