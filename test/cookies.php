<?php
$value = $_GET['name'];
setcookie("TestCookie", $value, time()+3600);
setcookie("TestCookie", $value);
?>