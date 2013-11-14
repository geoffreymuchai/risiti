var risiti
$(function(){
	risiti = new Risiti();
});
var Risiti = function() {

	var enableDatePicker = function() {
		$('#datepicker').datepicker();
	};

	function init_ui() {
		enableDatePicker();
	}

	this.init_ui = init_ui;
	init_ui();
}
