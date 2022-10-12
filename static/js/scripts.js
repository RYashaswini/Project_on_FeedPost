


$(document).ready(function () {

	$('#datatrigg').DataTable();
	$('.dropify').dropify();
});

$(document).ready(() => {
	$("#imgUpload").change(function () {
		const file = this.files[0];
		if (file) {
			let reader = new FileReader();
			reader.onload = function (event) {
				$("#imgPreview")
					.attr("src", event.target.result);
			};
			reader.readAsDataURL(file);
		}
	});
});

$(document).ready(function () {
	$("#myInput").on("keyup", function () {
		var value = $(this).val().toLowerCase();
		$("#myTable tr").filter(function () {
			$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
		});
	});
});

window.addEventListener('DOMContentLoaded', event => {

	// Toggle the side navigation
	const sidebarToggle = document.body.querySelector('#sidebarToggle');

	if (sidebarToggle) {

		// Uncomment Below to persist sidebar toggle between refreshes
		//     document.body.classList.toggle('sb-sidenav-toggled');
		// }
		sidebarToggle.addEventListener('click', event => {

			event.preventDefault();
			document.body.classList.toggle('sb-sidenav-toggled');
			localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
			$('#content-body-wrapper').toggleClass('body-content content-move')
			// $('#sidebar-wrapper').toggleClass('sidebar-mod')
		});
	}

});

function RejectID(x) {
	alert(x)
	console.log(x)
	$('#rejectform').attr('action', '/addstatus/' + x + '/')
}

function validatePost() {
	let post_name = document.forms["formPost"]["txtPostName"].value;
	if (post_name == "") {
		alert("Post name should not be empty");
		return false;
	}
	let upload_image = document.forms["formPost"]["imgUpload"].value;
	if (upload_image == "") {
		alert("Should upload image");
		return false;
	}
}


$(document).ready(function () {
	$(".alert").hide(5000);
});


function validateForm() {
	let val_name = document.forms["formRegister"]["txtUserName"].value;
	if (val_name == "") {
		alert("Username should not be empty");
		return false;
	}
	let val_email = document.forms["formRegister"]["txtEmail"].value;
	if (val_email == "") {
		alert("Email should not be empty");
		return false;
	}
	let val_password = document.forms["formRegister"]["txtPwd1"].value;
	if (val_password == "") {
		alert("Password should not be empty");
		return false;
	}
	let val_password2 = document.forms["formRegister"]["txtpwd2"].value;
	if (val_password2 == "") {
		alert("Confirm password should not be empty");
		return false;
	}
}

function validateFormLogin() {
	let val_name = document.forms["formLogin"]["txtUserName"].value;
	if (val_name == "") {
		alert("Username should not be empty");
		return false;
	}
	let val_password = document.forms["formLogin"]["txtPwd"].value;
	if (val_password == "") {
		alert("Password should not be empty");
		return false;
	}
}


var properties = [
	'sno',
	'postname',
	'description',
	'status',

];

$.each(properties, function (i, val) {

	var orderClass = '';

	$("#" + val).click(function (e) {
		e.preventDefault();
		$('.filter__link.filter__link--active').not(this).removeClass('filter__link--active');
		$(this).toggleClass('filter__link--active');
		$('.filter__link').removeClass('asc desc');

		if (orderClass == 'desc' || orderClass == '') {
			$(this).addClass('asc');
			orderClass = 'asc';
		} else {
			$(this).addClass('desc');
			orderClass = 'desc';
		}

		var parent = $(this).closest('.header__item');
		var index = $(".header__item").index(parent);
		var $table = $('.table-content');
		var rows = $table.find('.table-row').get();
		var isSelected = $(this).hasClass('filter__link--active');
		var isNumber = $(this).hasClass('filter__link--number');

		rows.sort(function (a, b) {

			var x = $(a).find('.table-data').eq(index).text();
			var y = $(b).find('.table-data').eq(index).text();

			if (isNumber == true) {

				if (isSelected) {
					return x - y;
				} else {
					return y - x;
				}

			} else {

				if (isSelected) {
					if (x < y) return -1;
					if (x > y) return 1;
					return 0;
				} else {
					if (x > y) return -1;
					if (x < y) return 1;
					return 0;
				}
			}
		});

		$.each(rows, function (index, row) {
			$table.append(row);
		});

		return false;
	});

});



var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}
