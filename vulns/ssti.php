<?php

$output = $twig->render($_GET['custom_email'],  array("first_name" => $user.first_name) );


// from XVWA
if (isset($_GET['submit'])) {
    $name=$_GET['name'];
    // include and register Twig auto-loader
    include 'vendor/twig/twig/lib/Twig/Autoloader.php';
    Twig_Autoloader::register();
    try {
      // specify where to look for templates
      $loader = new Twig_Loader_String();
      
      // initialize Twig environment
      $twig = new Twig_Environment($loader);
     // set template variables
     // render template
    $result= $twig->render($name);



$smarty=new vtigerCRM_Smarty;
$smarty->assign("APP",$app_strings);
$record=$_REQUEST['record'];
$smarty->assign("record",$record);
$mode=$_REQUEST["mode"];

?>