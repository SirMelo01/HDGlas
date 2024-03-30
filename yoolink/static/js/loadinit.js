var link = document.createElement("link");
link.rel = "stylesheet";
link.href = "https://unpkg.com/leaflet@1.9.3/dist/leaflet.css";
link.integrity = "sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI=";
link.crossOrigin = "";

var script = document.createElement("script");
script.src = "https://unpkg.com/leaflet@1.9.3/dist/leaflet.js";
script.integrity = "sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM=";
script.crossOrigin = "";

var font1 = document.createElement("link");
font1.rel = "preconnect";
font1.href = "https://fonts.googleapis.com";

var font2 = document.createElement("link");
font2.rel = "preconnect";
font2.href = "https://fonts.gstatic.com";
font2.crossOrigin = "";

var font3 = document.createElement("link");
font3.href = "https://fonts.googleapis.com/css2?family=Roboto&display=swap";
font3.rel = "stylesheet";


var cookieselect = getCookie("Cookie-Consent");
var cookiefontselect = getCookie("Cookie-Font");
var cookiemapselect = getCookie("Cookie-Map");

if(cookiemapselect === "true"){
  document.head.appendChild(link);
  document.head.appendChild(script);
  //hier dann weiter scripte einbinden
}
if(cookiefontselect === "true"){
  document.head.appendChild(font1);
  document.head.appendChild(font2);
  document.head.appendChild(font3);
}



//Cookies raussuchen per Name
function getCookie(name) {
  // Split cookie string and get all individual name=value pairs in an array
  var cookieArr = document.cookie.split(";");
  // Loop through the array elements
  for (var i = 0; i < cookieArr.length; i++) {
    var cookiePair = cookieArr[i].split("=");
    /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
    if (name == cookiePair[0].trim()) {
      // Decode the cookie value and return
      return decodeURIComponent(cookiePair[1]);
    }
  }
  return null;
}
