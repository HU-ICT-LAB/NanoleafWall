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
      console.log(LijstVanArray);
      var LengteVanArray = LijstVanArray.length;
      console.log(LengteVanArray);
      var i;
      var j;

      for (i = 1; i < LengteVanArray + 1; i++) {
        var IDieNietBegintBijEen = i - 1;
        console.log(LijstVanArray[IDieNietBegintBijEen]);
        var woord = LijstVanArray[IDieNietBegintBijEen]
        console.log(
            document.getElementById(i.toString()))
        document.getElementById(i.toString()).innerHTML = woord;
      }
      runStyleAutomation()
    });
}
sturen()
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
