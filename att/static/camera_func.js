var active_box;


$(".box").each(function () {
  $.data(this, 'value', {
    'id':this.id,
    'skip': 5,
  });
});



$(".box").on('click', function() {
  if (active_box) {
    $('#'+active_box).toggleClass('box_active');
  };
  active_box = $.data(this, 'value').id;
  $("#camera_func>b").text(active_box);
  $("#camera_func").removeClass('none');
  $('#'+active_box).toggleClass('box_active');
})

$('#skip').on('change', function () {
  var skip = parseInt(this.value);
  $('#'+active_box+">.img").removeClass('kill');
  $('#'+active_box+">.img").each(
    function (idx) {
      if (idx%skip!=0) {$("#"+this.id.split('.').join("\\.")).addClass('kill');};
    }
  );

});
