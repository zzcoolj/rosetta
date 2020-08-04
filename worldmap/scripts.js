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