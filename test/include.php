<?php error_reporting(0); ?>
<html>
	<head>
		<meta charset="UTF-8" />
		<link rel='stylesheet' type='text/css' href='index.css' />
		<title>Security Challs : Sublime Patisserie</title>
	</head>
	<body>
		<h1><a href='./index.php'>Sublime Patisserie</a></h1>
		<article>
			<div id='container'>
				<a href='?patisserie=patisserie1.php'><img src='./img/eclairs.jpg' id='carre' alt='patisserie'></a>
				<a href='?patisserie=patisserie2.php'><img src='./img/millefeuille.jpg' id='carre' alt='patisserie'></a>
				<a href='?patisserie=patisserie3.php'><img src='./img/paris_brest.jpg' id='carre' alt='patisserie'></a>
				<a href='?patisserie=patisserie4.php'><img src='./img/saint_honore.jpg' id='carre' alt='patisserie'></a>
				<?php
					if(isset($_GET['patisserie'])){						
						echo "<div id='texte'>";
						if(strstr($_GET['patisserie'], 'patisserie') || strstr($_GET['patisserie'], 'index') || strstr($_GET['patisserie'], 'flag') ){
							include($_GET['patisserie']);
						}
						else{
							echo "<h2>Hacker Spotted !</h2>";
						}						
						echo "</div>";
					}
					else{
						?>
						<div id='contact'>
							Bienvenue à <br>
							Sublime Patisserie !<br>
							<span id='little'>
								sublimepatisserie@yopmail.com<br>
								01 23 45 67 89<br>
							</span>
						</div>
						<?php
					}
				?>
				<a href='?patisserie=patisserie5.php'><img src='./img/tarte_citron.jpg' id='carre' alt='patisserie'></a>
				<a href='?patisserie=patisserie6.php'><img src='./img/tarte_fraises.jpg' id='carre' alt='patisserie'></a>
				<a href='?patisserie=patisserie7.php'><img src='./img/tarte_orange.jpg' id='carre' alt='patisserie'></a>
				<a href='?patisserie=patisserie8.php'><img src='./img/viennoiseries.jpg' id='carre' alt='patisserie'></a>
			</div>
		</article>
	</body>
	<footer>
		<a href='#'>Copyright® Swissky</a> - 
		<a href='../../index.php'>Challenges</a>
	</footer>
</html>