<?php
  $dest = $_GET['who'];
  mail($dest, "subject", "message", "", "-f" . $_GET['from']);
?>
