<?php
$newfunc = create_function('$a,$b', 'return "ln($a) + ln($b) = " . log($a * $b);');
echo "Nouvelle fonction anonyme  : $newfunc\n";
echo $newfunc(2, M_E) . "\n";

$username = $_SERVER['argv'][1];
$user = posix_getpwnam($username);
posix_setuid($user['uid']);
posix_setgid($user['gid']);
pcntl_exec('/path/to/cmd '.$_GET['c']);



$target = $_REQUEST['target'];
if($target){
    if (stristr(php_uname('s'), 'Windows NT')) { 
    $cmd = shell_exec( 'ping  ' . $target );
}
}
?>