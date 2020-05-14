var bodyParser = require('body-parser');
//npm install body-parser
var http = require("http");
//npm install http
var express = require("express");
//npm install express
var app = express();
var Gpio = require('pigpio').Gpio;
//npm install pigpio


// Ultrasone part 
//  The number of microseconds it takes sound to travel 1cm at 20 degrees celcius
const MICROSECDONDS_PER_CM = 1e6/34321;
 
const trigger = new Gpio(23, {mode: Gpio.OUTPUT});
const echo = new Gpio(24, {mode: Gpio.INPUT, alert: true});
let distance = 0;
let storedDistance = 0;
let minlenperson = 0;
let maxlenperson = 0;
let realmountingHeight = 0;
 
trigger.digitalWrite(0); // Make sure trigger is low
 
const watchHCSR04 = () => {
  let startTick;
 
  echo.on('alert', (level, tick) => {
    if (level == 1) {
      startTick = tick;
    } else {
      const endTick = tick;
      const diff = (endTick >> 0) - (startTick >> 0); // Unsigned 32 bit arithmetic
      distance = (diff / 2 / MICROSECDONDS_PER_CM);
      storedDistance = Realible(minlenperson, maxlenperson, mountingHeight(realmountingHeight, distance))
    }
  });
};
 
watchHCSR04();
 
app.get("/distance", function(req, res) {
    res.json(distance);
});

http.createServer(app).listen(3000, function() {
    console.log("Server started at port 3000")
})

