AOS.init({
  startEvent: 'load'
});


var $jumbotron = $(".jumbotron");
var $name = $(".jumbotron .container h1");
var $Jobtitle = $(".jumbotron .container p");
var $about = $("#about");
var $work = $("#work");
var $contact = $("footer");
var $pointerEffect = $("a.btn-outline-warning, .card > picture, ul.nav li");

//add mouse class to the elements
$pointerEffect.addClass("mouse");
//add box-shadow effect whenever the selected elements are hovered
$pointerEffect.hover(function() {
  $(this).css("box-shadow", "0 0 8px 6px rgba(255,255,255, 0.5), 0 0 20px 5px rgba(152,173,131, 0.5)");
}, function() {
$(this).css("box-shadow", "none");
});


$jumbotron.attr("data-aos", "fade-down");
$Jobtitle.attr({
  "data-aos": "flip-down",
  "data-aos-delay": "500"
});
$name.attr({
  "data-aos": "flip-up",
  "data-aos-delay": "1300"
});
$about.attr({
  "data-aos-offset": "300",
  "data-aos": "fade-right"
});
$work.attr("data-aos", "fade-right");
$contact.attr({
  "data-aos-offset": "25",
  "data-aos": "fade-right"
});
