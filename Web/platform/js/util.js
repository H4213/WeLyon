var URL = "http://jsonplaceholder.typicode.com/posts/1";

function doGet (parameters)
{
	var result = null;
	$.ajax({
		url : URL,
		dataType : "json",
		method : "GET",
		async : false,
		data : parameters,
		success : function (data) {
			console.log('Success');
			result = data;
		},
		error : function () {
			console.log('Error');
		}
	});
	return result;	
}

function doPost (parameters){
	$.ajax({
		url : URL,
		dataType : "json",
		method : "POST",
		async : false,
		data : parameters,
		success : function () {
			console.log('Success');
		},
		error : function () {
			console.log('Error');
		}
	});
}


function doPut (parameters) {
	$.ajax({
		url : URL,
		dataType : "json",
		method : "PUT",
		async : false,
		data : parameters,
		success : function (resp) {
			console.log('Success');
		},
		error : function () {
			console.log('Error');
		}
	});
}

function doDelete (parameters) {
	$.ajax({
		url : URL,
		dataType : "json",
		method : "DELETE",
		async : false,
		data : parameters,
		success : function (resp) {
			console.log('Success');
		},
		error : function () {
			console.log('Error');
		}
	});
}
