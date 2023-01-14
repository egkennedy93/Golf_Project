$(document).ready(function(){
  $("tr").not(':first').hover(
    function () {
      $(this).css("background","gray");
    }, 
    function () {
      $(this).css("background","");
    }
  )});

$(document).ready(function(){
      $('table tr').click(function(){
        window.location = $(this).data('href');
        return false;
      });
    });
