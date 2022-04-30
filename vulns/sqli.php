<html>
	<head>
		<meta charset="UTF-8" />
		<link rel='stylesheet' type='text/css' href='index.css' />
		<title>Security Challs : Android Compare</title>
	</head>
	<body>
		<header>
			<h1><a href='./index.php'>Android Compare</a></h1>
		</header>
		<article>
			<?php
				//Connexion à la BDD
				include('configuration.php');
				mysql_connect($DB_HOST,$DB_USER,$DB_PASS);
				mysql_select_db($DB_NAME);
				mysql_query("SET NAMES 'utf8'");

				if(isset($_GET['id'])){
					//Affichage du smartphone
					$news_dbg = mysql_query("SELECT id,name,image,specifications FROM ".$_GET['id']." WHERE id=".$DB_CHALL_TWO) or die(mysql_error());
					$news = mysql_query("SELECT id,name,image,specifications FROM ".$DB_CHALL_TWO." WHERE id=".$_GET['id']) or die(mysql_error());
					while($phone = mysql_fetch_array($news)){
						echo "<div id='noidea'>";
						echo "<a href='?id=".$phone['id']."' id='containers'><img src='./img/".$phone['image']."' alt='phone'></a>";
						echo "<p id='spec'><span>".$phone['name']."</span>".nl2br($phone['specifications']);
						echo "<br><a href='#BUYIT' onclick=\"alert('Indisponible en magasin !');\" id='buy'>ACHETER</a></p>";
						echo "</div>";
					}

				}
				else{
					//Recuperation des 3 derniers telephones
					echo "<p>Sélectionner un téléphone pour accéder à ses caractéristiques</p>";
					echo "<div id='androphone'>";
					$news = mysql_query("SELECT name,image,id FROM ".$DB_CHALL_TWO." ORDER BY id DESC LIMIT 0,3") or die(mysql_error());
					while($phone = mysql_fetch_array($news)){
						echo "<a href='?id=".$phone['id']."' id='containers'><span>".$phone['name']."</span><img src='./img/".$phone['image']."' alt='phone'></a>";
					}
					echo "</div>";
				}
			?>
		</article>
	</body>
	<footer>
		<a href='#'>Copyright® Swissky</a> -
		<a href='../../index.php'>Challenges</a>
	</footer>
</html>
