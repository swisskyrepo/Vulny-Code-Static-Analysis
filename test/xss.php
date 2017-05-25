<html>
		<?php
			if (isset($_POST['mail'])){
				$mail = $_POST['mail'];
				echo "<p>The mail ".$mail." has been registered in our database.</p>";
			}
			else{
				echo "<p>The mail ".$_GET['mail']." has been registered in our database.</p>";
			}
		?>
</html>
