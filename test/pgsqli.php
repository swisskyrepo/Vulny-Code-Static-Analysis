<?php

$conn = pg_pconnect("dbname=publisher");
if (!$conn) {
  echo "An error occurred.\n";
  exit;
}

$result = pg_query($conn, "SELECT author, email FROM authors WHERE id=".$_GET['vuln']);
if (!$result) {
  echo "An error occurred.\n";
  exit;
}

while ($row = pg_fetch_row($result)) {
  echo "Author: $row[0]  E-mail: $row[1]";
  echo "<br />\n";
}

?>
