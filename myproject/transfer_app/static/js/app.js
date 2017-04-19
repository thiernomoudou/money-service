
// jQuery(document).ready(function(){

$(".btn-operation").on('click', function(){
	var element = $(this);
	if (confirm('Did you process this transaction?')){
        $.ajax({
        	type: "GET",
        	url: "/delete/",
        	data: {pk: element.attr("data-pk")},
        	// beforeSend: function(xhr){
        	// 	xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        	// },
        	success: function(response){
        		alert(element + 'has been removed');
        	}
        });

        element.closest('tr').remove();
	}
});




// var stat = document.querySelector('.btn-operation');
// stat.onclick=function(){
// 	alert('hello world');
// };