/* -- Ready function --*/
$(document).ready(function () {
    flashed_messages();
    $('.sidenav').sidenav();
});



/* -- Js for Materialize init -- */

function materializeInit() {
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('select').formSelect();
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
}
materializeInit();


/* -- Flash Messages -- */
function flashed_messages() {
	$("#message").addClass("show");
    setTimeout(function () {
        $("#message").removeClass("show");
    }, 3000);
}
flashed_messages();