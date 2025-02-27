<?php
require('./base.inc');
require(BASE .'/../config.inc');

require(BASE .'/../includes/header.inc');

...

// Si filtre sur groupe projet
if(count($_SESSION['filtreGroupeProjet']) > 0) {
    $sql.= " AND planning_periode.projet_id IN ('" . implode("','", $_SESSION['filtreGroupeProjet']) . "')";
}

...

//echo $sql;die;
$periodes->db_loadSQL($sql);
$nbLignesTotal = $periodes->getCount();

...