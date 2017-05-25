<html>
		<?php
			if(isset($_FILES['nom'])){
				$name = htmlentities($_FILES['nom']['name']);
				if(stristr($name, ".jpg")==true || stristr($name, ".png")==true){
					echo "<h3>The file ".$name." has been uploaded</h3>";
					echo "<a href='./index.php' id='button'>UPLOAD AGAIN</a><br>";
				}
				else{
					echo "<h3>Only JPG/PNG Files are allowed !</h3>";
					echo "<a href='./index.php' id='button'>RETRY</a>";
			}
			else{
				?>
				<form method="post" action="index.php" enctype="multipart/form-data">
					<div id='iconDl'>
						<input type="file" name="nom" id='upload' onchange='this.form.submit()' />
					</div>
				</form>
				<p>Click to upload</p>
				<?php
			}
		?>
</html>
