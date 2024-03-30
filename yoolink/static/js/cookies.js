var form = document.querySelector("form");
var cookieslider = document.getElementById("cookie");
var mapslider = document.getElementById("map");
var fontslider = document.getElementById("font");

function cookiereload2() {
  if (cookieslider.checked === true) {
    document.cookie =
      "Cookie-Consent=true; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  } else {
    document.cookie =
      "Cookie-Consent=false; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  }

  if (mapslider.checked === true) {
    document.cookie =
      "Cookie-Map=true; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  } else {
    document.cookie =
      "Cookie-Map=false; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  }

  if (fontslider.checked === true) {
    document.cookie =
      "Cookie-Font=true; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  } else {
    document.cookie =
      "Cookie-Font=false; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  }
}

onload = function () {
  if (cookieselect === "true") {
    cookieslider.checked = true;
  }

  if (cookiemapselect === "true") {
    mapslider.checked = true;
  }

  if (cookiefontselect === "true") {
    fontslider.checked = true;
  }
};

cookieslider.addEventListener("change", (e) => {
  if (cookieslider.checked === true) {
    mapslider.checked = true;
    fontslider.checked = true;
  } else {
    mapslider.checked = false;
    fontslider.checked = false;
  }
  cookiereload2();
});

mapslider.addEventListener("change", (e) => {
  if (mapslider.checked === true) {
    if (fontslider.checked === true) {
      cookieslider.checked = true;
    }
  } else {
    cookieslider.checked = false;
  }
  cookiereload2();
});

fontslider.addEventListener("change", (e) => {
  if (fontslider.checked === true) {
    if (mapslider.checked === true) {
      cookieslider.checked = true;
    }
  } else {
    cookieslider.checked = false;
  }
  cookiereload2();
});