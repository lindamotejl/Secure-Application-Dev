
$(document).ready(function () {

    $('#hamburger').click(function () {
        $(this).toggleClass('open');
        $('nav').toggleClass('show');
    });

    // var header = document.getElementById("myDIV");
    // var btns = header.getElementsByClassName("btn");
    // for (var i = 0; i < btns.length; i++) {
    //     btns[i].addEventListener("click", function() {
    //     var current = document.getElementsByClassName("active");
    //     if (current.length > 0) { 
    //         current[0].className = current[0].className.replace(" active", "");
    //     }
    //     this.className += " active";
    //     });
    // }
    

});

$(document).ready(function() {
    const btn = document.querySelectorAll(".btn");
	btn.forEach(btn => {
  btn.addEventListener('click',  function() {
    btn.classList.toggle('orange');
  });
});
 });

//  $(document).ready(function() {
//     const heart = document.querySelectorAll(".fa-heart");
// 	heart.forEach(heart => {
//   heart.addEventListener('click',  function() {
//     heart.classList.toggle('red');
//   });
// });
//  });

