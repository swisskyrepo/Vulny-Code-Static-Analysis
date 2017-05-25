<html>
	<article>
				<?php
					if(isset($_GET['patisserie'])){
							include($_GET['patisserie']);
					}

					$mail = $_POST['mail'];
					include($_POST['mail']);
					include($mail);
				?>
</html>
