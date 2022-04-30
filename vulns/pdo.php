<!doctype html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Coffee Database</title>
	<link rel="stylesheet" href="css/style.css" />
</head>

<body>
	<form action='' method="POST">
		<img src='./image/logo.png' id='logo'>
		<h2>Coffee Database</h2>
		<?php
			if(isset($_POST['username']) && isset($_POST['password'])){
				try{
				    $pdo = new PDO('sqlite:'.dirname(__FILE__).'/afaad186a9343b96963edf168cdb5587.sqlite');
				    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
				    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // ERRMODE_WARNING | ERRMODE_EXCEPTION | ERRMODE_SILENT

				    $stmt = $pdo->query("SELECT * FROM users WHERE username ='".$_POST['username']."' and password='".$_POST['password']."'");
					if($result = $stmt->fetchAll()){
						echo "<p id='left'>Welcome  ".$result[0]['username']." <br>Your password is ".$result[0]['password']."</p>";
						echo '<input type="submit" value="LOG IN" href="./index.php" class="button" />';
					}
					else{
						echo "Unknown user or password";
						goto login_input;
					}

				}
				catch(Exception $e) {
				    echo "Impossible d'accéder à la base de données SQLite : ".$e->getMessage();
				    echo '<br><input type="submit" value="RETRY" href="./index.php" class="button" />';
				}
			}
			else{
login_input:
				?>
				<input type="text" name="username" class="text-field" placeholder="Username" />
	    		<input type="password" name="password" class="text-field" placeholder="Password" />
	   			<input type="submit" value="LOG IN" class="button" />
				<?php
			}
		?>

	</form>
</body>
</html>
