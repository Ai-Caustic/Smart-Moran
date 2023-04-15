section1 = document.getElementById("section1");
section2 = document.getElementById("section2");

function load() {
  section1.style.display = "block";
  section2.style.display = "none";
  setInterval(slider, 4000);
  setInterval(slider2, 4000);
  setInterval(slider3, 4000);
  setInterval(slider4, 4000);
  setInterval(slider5, 4000);
  setInterval(slider6, 4000);
  setInterval(slider7, 4000);
  setInterval(slider8, 4000);
  setInterval(slider9, 4000);
  setInterval(slider10, 4000);
  setInterval(slider11, 4000);
}

function displaySec1() {
  section1.style.display = "block";
  section2.style.display = "none";
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
function displaySec2() {
  section1.style.display = "none";
  section2.style.display = "block";
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
