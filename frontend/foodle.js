
$(document).ready(function () {

    $('#hamburger').click(function () {
        $(this).toggleClass('open');
        $('nav').toggleClass('show');
    });


    

});

// $(document).ready(function() {
//     const btn = document.querySelectorAll(".btn");
// 	btn.forEach(btn => {
//   btn.addEventListener('click',  function() {
//     btn.classList.toggle('orange');
//   });
// });
//  });

//  $(document).ready(function() {
//     const heart = document.querySelectorAll(".fa-heart");
// 	heart.forEach(heart => {
//   heart.addEventListener('click',  function() {
//     heart.classList.toggle('red');
//   });
// });
//  });

