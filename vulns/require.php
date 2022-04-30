<?php

if (isset($_GET['which']))
{
    $which = $_GET['which'];
    require_once $which.'noparenthesis.php';
    require_once($which.'parenthesis.php');
}

?>