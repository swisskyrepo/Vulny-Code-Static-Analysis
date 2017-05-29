<?php

if (isset($_GET['page'])) {
$page = $_GET['page'];
} else {
$page = "home";
}
// I heard '..' is dangerous!
assert("strpos('templates/'" . $page . "'.php', '..') === false") or die("Detected hacking attempt!");

// TODO: Make this look nice
assert("file_exists('templates/'". $page . "'.php')") or die("That file doesn't exist!");
?>
