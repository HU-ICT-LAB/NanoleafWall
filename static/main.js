//Onlane mode
function sturen() {
  fetch("http://127.0.0.1:5000/effecten")
    .then(response => {
      console.log(response);
      return response.json();
    })
    .then(json => {
      console.log("GET response json:");
      console.log(json);
      var LijstVanArray = json;
      LijstVanArray.forEach(optionVuller);

      function optionVuller(item, index) {
        var node = document.createElement("OPTION");
        var textnode = document.createTextNode(item);
        node.appendChild(textnode);
        document.getElementById("select1").appendChild(node);
      }
      runStyleAutomation();
    });
}

// //localmode
// function sturen() {
//   var LijstVanArray = [
//     "Color Burst",
//     "Falling Whites",
//     "Fireworks",
//     "Flames",
//     "Forest",
//     "Inner Peace",
//     "Meteor Shower",
//     "Nemo",
//     "Northern Lights",
//     "Paint Splatter",
//     "Pulse PopBeats",
//     "Radial Sound Bar",
//     "Rhythmic Northern Lights",
//     "Romantic",
//     "Sound Bar",
//     "Streaking Notes"
//   ];
//   // hierboven hoort normaal "json"

//   LijstVanArray.forEach(optionVuller);

//   function optionVuller(item, index) {
//     var node = document.createElement("OPTION");
//     var textnode = document.createTextNode(item);
//     node.appendChild(textnode);
//     document.getElementById("select1").appendChild(node);
//   }

//   runStyleAutomation();
// }

sturen();

function KnopjeGedrukt() {
  var dropdown = document.getElementById("select1");
  var dropdownvalue = dropdown.options[dropdown.selectedIndex].text;
  if (dropdownvalue == "Selecteer effect") {
    alert("Selecteer een effect");
  } else {
    console.log(dropdownvalue);
  }
}

function effect() {
  const data = { effect: "*" };
  fetch("http://localhost:5000/effect", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(data => {
      console.log("Success:", data);
    })
    .catch(error => {
      console.error("Error:", error);
    });
}
// return krijgen()
//   fetch('/send_effect/')
//   .then((response) => {
//     return response.text();
//   })
//   .then((text) => {
//     console.log('GET response text:')
//     console.log(text);
//   });
// var express = require('express');
// var app = express();
// console.log("hallo");
