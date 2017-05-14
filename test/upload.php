<html>
	<head>
		<meta charset="UTF-8" />
		<link rel='stylesheet' type='text/css' href='index.css' />
		<title>Security Challs : Univers Upload</title>
	</head>
	<body>
		<header>
			<h1><a href='index.php'>Univers Upload</a></h1>
		</header>

		<?php
			if(isset($_FILES['nom'])){
				$name = htmlentities($_FILES['nom']['name']);

				if(stristr($name, ".jpg")==true || stristr($name, ".png")==true){
					echo "<h3>The file ".$name." has been uploaded</h3>";
					echo "<a href='./index.php' id='button'>UPLOAD AGAIN</a><br>";
					if(stristr($name, ".php")==true){
						echo "<h3>Well done, you just bypass the filter.</h3>";
						echo "<h3>The Challenge is over :) </h3>";
					}
				}
				else{
					echo "<h3>Only JPG/PNG Files are allowed !</h3>";
					echo "<a href='./index.php' id='button'>RETRY</a>";
				}


			}
			else{
				?>
				<form method="post" action="index.php" enctype="multipart/form-data">
					<div id='iconDl'>
						<input type="file" name="nom" id='upload' onchange='this.form.submit()' />
					</div>
				</form>
				<p>Clic to upload</p>
				<?php
			}
		?>
	</body>
	<footer>
		<a href='#'>Copyright® Swissky</a> -
		<a href='../../index.php'>Challenges</a>
	</footer>
</html>
