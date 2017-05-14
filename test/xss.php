<html>
	<head>
		<meta charset="UTF-8" />
		<link rel='stylesheet' type='text/css' href='index.css' />
		<title>Security Challs : Go to the Moon</title>
	</head>

	<body>
		<h1>Welcome to the Moon Club !</h1>
		<h2>It's time to party on another planet !</h2>
		<div id='moonShow'>
			
		</div>
		<p>Suscribe to our newsletter try to <strong>win a travel to the Moon</strong></p>
		<form  method="POST" action='index.php'>
			<input type='text' name='mail' id='mail' placeholder='example@mail.com' />
			<input type='submit' id='suscribe' value='Suscribe' />
		</form>	
		<?php
			if (isset($_POST['mail'])){
				$mail = $_POST['mail'];
				//$mail = str_replace("script", "", $mail);
				//$mail = str_ireplace("script", "replace", $mail);
				$mail = str_ireplace("img", "replace", $mail);
				//$mail = str_ireplace("prompt", "", $mail);
				$mail = str_ireplace("alert", "", $mail);
				//$mail = str_ireplace("data", "", $mail);
				//$mail = str_ireplace("on", "", $mail);
				echo "<p>The mail ".$mail." has been registered in our database.</p>";
			}
		?>
	</body>
	<footer>
		<a href='#'>Copyright® Swissky</a> - 
		<a href='../../index.php'>Challenges</a>
	</footer>
</html>

