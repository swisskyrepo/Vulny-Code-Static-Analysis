<html>
	<head>
		<meta charset="UTF-8" />
		<link rel='stylesheet' type='text/css' href='index.css' />
		<title>Security Challs : Graduate CMS</title>
	</head>
	<body>
		<h1>Graduate CMS</h1>
		<article>
		<?php
		//CONFIGURATION
		include('configuration.php');
		mysql_connect($DB_HOST,$DB_USER,$DB_PASS);
		mysql_select_db($DB_NAME);

		if(isset($_POST['username']) and isset($_POST['password'])){
			$sql = mysql_query("SELECT * FROM users WHERE username='".$_POST['username']."' AND password = '".$_POST['password']."'") or die(mysql_error());
			if(mysql_num_rows($sql) > 0){
				$data = mysql_fetch_assoc($sql);
				echo "Welcome ".$data['username']."<br>";
				if($data['username'] == 'Administrator'){
					echo "<p>Good job, you're logged as Administrator<br></p>";
				}
				else{
					echo "<p>Congratulation, you're graduated !<br></p>";
				}
				echo "<a href='index.php' id='connection'>Log Out</a>";
			}
			else{
				echo "Error<br>";
				echo "Unknown username or password<br><br>";
				echo "<a href='index.php' id='connection'>Retry</a>";
			}
		}
		else{
			?>
			<form method=POST action="index.php">
				<input type=text name='username' id='username' placeholder='Username'><br>
				<input type=password name='password' id='password' placeholder='Password'><br>
				<input type=submit id='connection' value='Log In'>
			</form>
			<?php
		}
		?>
		</article>
	</body>
	<footer>
		<a href='#'>Copyright® Swissky</a> -
		<a href='../../index.php'>Challenges</a>
	</footer>
</html>
