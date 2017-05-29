<?php
$ds=ldap_connect("localhost");
 if ($ds)
 {
    $ok=ldap_bind($ds);
 // anonymously bind for read-only access
    $surname=$_GET['surname'];
    $filter = "(sn=" . $surname . ")";
    $sr=ldap_search($ds, "o=My Company, c=".$_GET['language'], $filter);
    $info = ldap_get_entries($ds, $sr);
    echo "<p>There are " . $info["count"] . " entries for that search:<p>";

    for ($i=0; $i<$info["count"]; $i++)
{
        echo "common name: " . $info[$i]["cn"][0] . "<br />";
        echo "telephone: " . $info[$i]["telephoneNumber"][0] . "<br />";
        echo "email: " . $info[$i]["mail"][0] . "<br /><hr />";
}

    ldap_close($ds);

}
 else
{
    echo "<h4>connection error</h4>";
}
?>
