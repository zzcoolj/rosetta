var abouts = ['english-about', 'french-about'];


function myFunction(id1, id2, id3, id4) {
  var x = document.getElementById(id1);
  var y = document.getElementById(id2);

  if (x.style.display === "none" || x.style.display === "") {
    x.style.display = "block";
  }
  y.style.display = "none";

  var i;
  for (i = 0; i < abouts.length; i++) {
    if(abouts[i] != id1) {
        var n = document.getElementById(abouts[i]);
        n.style.display = "none";
    }
  }

  var a = document.getElementById(id3);
  var b = document.getElementById(id4);

  if (a.style.fontWeight === "normal" || a.style.fontWeight === "") {
    a.style.fontWeight = "bold";
  }
  b.style.fontWeight = "normal";

}

function fade(id) {
    document.getElementById(id).style.opacity = "0.7";
}
function unFade(id) {
    document.getElementById(id).style.opacity = "1.0";
}


var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}