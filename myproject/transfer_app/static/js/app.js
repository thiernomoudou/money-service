
// jQuery(document).ready(function(){

// $(".btn-operation").on('click', function(){
	
// 	var element = $(this);
	
// 	    if(confirm("did you process this transactions")){

// 	        $.ajax({
// 	        	type: "POST",
// 	        	url: "/delete/",
// 	        	data: {pk: element.attr("data-pk")},
// 	        	success: function(response){
// 	        		swal("Good job!", "the transaction has been processed", "success")
	        		
// 	        	}
//         });

//         element.closest('tr').remove();
//     }
    



// $('#table_id').DataTable();



// });


// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie != '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

// var csrftoken = getCookie('csrftoken');

// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }
// $.ajaxSetup({
//     beforeSend: function(xhr, settings) {
//         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }
// });

// });




jQuery(document).ready(function(){

$(".btn-operation").on('click', function(){
	
	var element = $(this);

	deleteTransaction(element);

	function deleteTransaction(photoId) {
    swal({
      title: "Are you sure?", 
      text: "Are you sure that you have processed this transaction?", 
      type: "warning",
      showCancelButton: true,
      closeOnConfirm: false,
      confirmButtonText: "Yes, remove it!",
      confirmButtonColor: "#ec6c62"
    }, function() {
       $.ajax({
	        	type: "POST",
	        	url: "/delete/",
	        	data: {pk: element.attr("data-pk")},
	        	success: function(response){element.closest('tr').remove();}
      })
      .done(function(data) {
        swal("Deleted!", "Your transaction has been successfuly removed!", "success");
        // element.closest('tr').remove();
      })
      .error(function(data) {
        swal("Oops", "We couldn't connect to the server!", "error");
      });
    });
  }

});

$('#table_id').DataTable();

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});





});
	
	    