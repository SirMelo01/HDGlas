const realmap = document.querySelector("#map");
const covermap = document.querySelector("#covermap");

var map;



//Map

function mapLoad() {
  if (cookiemapselect === null || cookiemapselect === "false") {
    covermap.classList.remove("hidden");
    realmap.classList.add("hidden");
  } else {
    covermap.classList.add("hidden");
    realmap.classList.remove("hidden");

    // Karte wird geladen, 
    map.setView([48.777909, 12.878083], 14);
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map);
    
    L.marker([48.777909, 12.878083]).addTo(map)
    .bindPopup('HD-Glas <br> Deggendorfer Str. 36, 94447 Plattling')
    .openPopup();
    map.scrollWheelZoom.disable();
  }
}


var csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

//FQA
$(document).ready(function() {
  $(".faq-toggle").click(function() {
    var content = $(this).siblings(".faq-content");
    var arrow = $(this).find(".faq-arrow");
    
    if (content.hasClass("hidden")) {
      content.removeClass("hidden");
      arrow.addClass("rotate-180");
    } else {
      content.addClass("hidden");
      arrow.removeClass("rotate-180");
    }
  });
  $('#emailForm').submit(function(event) {
    event.preventDefault(); // Prevent the default form submission
    console.log("Sende email...")
    var formData = {
        name: $('#firstName').val() + " " + $('#lastName').val(),
        email: $('#email').val(),
        title: $('#subject').val(),
        number: $('#number').val(),
        message: $('#message').val(),
        csrfmiddlewaretoken: csrftoken,
    };
    // Send form data to the server using AJAX
    $.ajax({
        type: 'POST',
        url: '/cms/email/request/',
        data: formData,
        success: function(response) {
            // Handle successful response here
            if(response.success) {
              sendNotif("Ihre Nachricht wurde erfolgreich gesendet", "success")
            }
            $('#emailForm')[0].reset();
        },
        error: function(xhr, status, error) {
            // Handle error response here
            console.error('Form submission failed');
            sendNotif("Etwas ist schief gelaufen. Versuchen Sie es bitte später nochmal.", "error")
        }
    });
});
});

setTimeout(() => {
  if (cookiemapselect !== null && cookiemapselect !== "false") {
    map = L.map("map");
    map.on("focus", function () {
      map.scrollWheelZoom.enable();
    });
    map.on("blur", function () {
      map.scrollWheelZoom.disable();
    });
  }
  mapLoad();
}, 500);
