$(function(){
	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;
	$('#user_name').blur(function() {
			check_user_name();
		});

		$('#pwd').blur(function() {
			check_pwd();
		});

		

		$('#email').blur(function() {
			check_email();
		});




    function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			
			$('#email').next().show();
			error_check_password = true;
		}

	}
    function check_user_name(){
		var len = $('#user_name').val().length;
		if(len>14)
		{
			
			$('#user_name').next().show();
			error_name = true;
		}
		else
		{
			$('#user_name').next().hide();
			error_name = false;
		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}

	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();
		
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});

	})