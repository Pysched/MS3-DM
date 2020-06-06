/* -- Ready function --*/
$(document).ready(function () {
    flashed_messages();
    $('.sidenav').sidenav();
    $('.slider').slider({fullwidth: true});
});



/* -- Js for Materialize init -- */
function materializeInit() {
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('select').formSelect();
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('.datepicker').datepicker();
    $('.timepicker').timepicker();
}
materializeInit();


/* -- Flash Messages -- */
function flashed_messages() {
	$("#message").addClass("show");
    setTimeout(function () {
        $("#message").removeClass("show");
    }, 5000);
}

/* -- Carousel activation -- */
  $(document).ready(function(){
    $('.carousel').carousel();
  });

/* -- Date Picker Activation -- */
  $(document).ready(function(){
    $('.datepicker').datepicker();
  });

/* -- Time Picker -- */
 $(document).ready(function(){
    $('.timepicker').timepicker();
  });