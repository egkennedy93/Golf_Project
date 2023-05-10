
// for the course list, highlights the rows on hover
$(document).ready(function(){
  $(".course-row").hover(
    function () {
      $(this).css("cursor", "pointer");
    }, 
    function () {
      $(this).css("background","");
    }
  )});

// When the row for the course list (which is tees) is selected, trigger the href asocaited with the row
$(document).ready(function(){
  $('.course-row').click(function(){
    window.location = $(this).data('href');
    return false;
  });
});


$(document).ready(function(){
  $('[data-toggle="popover"]').popover();
  
});

$(document).ready(function(){
  $('[data-toggle="popover"]').hover(
    function () {
      $(this).css("cursor", "pointer");
    }
    )});

