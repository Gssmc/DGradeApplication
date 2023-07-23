
$(".modal-trigger").click(function(e){
    e.preventDefault();
    dataModal = $(this).attr("data-modal");
    $("#" + dataModal).css({"display":"block"});
    // $("body").css({"overflow-y": "hidden"}); //Prevent double scrollbar.
  });
  
  $(".close-modal, .modal-sandbox").click(function(){
    $(".modal").css({"display":"none"});
    // $("body").css({"overflow-y": "auto"}); //Prevent double scrollbar.
  });