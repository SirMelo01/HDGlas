const cookie = document.querySelector("#menu-cookie");
const menu = document.querySelector("#navbar-cta");


function toggle() {
  const menu = document.querySelector("#menu");
  if (menu.classList.contains("hidden")) {
    menu.classList.remove("hidden");
    menu.classList.add("absolute");
  } else {
    menu.classList.add("hidden");
    menu.classList.remove("absolute");
  }
}

function cookieRefresh() {
  if (cookieselect == null) {
    cookie.classList.add("block");
    cookie.classList.remove("hidden");
  } else {
    cookie.classList.add("hidden");
  }
}


function acceptCookie() {
  document.cookie =
    "Cookie-Consent=true; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  document.cookie =
    "Cookie-Map=true; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  document.cookie =
    "Cookie-Font=true; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  location.reload();
  cookieRefresh();
}

function refuseCookie() {
  document.cookie =
    "Cookie-Consent=false; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  document.cookie =
    "Cookie-Map=false; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  document.cookie =
    "Cookie-Font=false; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  location.reload();
  cookieRefresh();
}

cookieRefresh();
