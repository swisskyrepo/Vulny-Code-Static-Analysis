<?php
require 'base.inc';
require BASE . '/../config.inc';
require BASE . '/../includes/header.inc';

if(!$user->checkDroit('parameters_all')) {
    $_SESSION['erreur'] = 'droitsInsuffisants';
    header('Location: index.php');
    exit;
}

$type=$_POST['type'];
$type_restauration=$_POST['type_restauration'];
$type_fichier_import_seul=$_POST['type_fichier_import'];
$upload_dir = SAVE_DIR; // upload directory 
// Si on fait un upload de fichiers
if ($type=='upload')
{
    // Pour tous les fichiers, on tente de les uploader
    for($i=0; $i<count($_FILES); $i++){ 
    $filename = replaceAccents(utf8_decode($_FILES["fichier-$i"]['name']));
    $tmp_dir = $_FILES["fichier-$i"]['tmp_name'];
    $fileSize = $_FILES["fichier-$i"]['size'];

    $dest_dir=$upload_dir.$filename.".tmp";

    // Vidage du contenu d'uploaddir sans suppresion du r�pertoire
    rrmdir($upload_dir,false);

    // Verification du r�pertoire
    if(!file_exists(SAVE_DIR) || !is__writable(SAVE_DIR)) {
        $msg=preg_replace('/filename/',$filename,$smarty->getConfigVars('upload_fichier_erreur_ecriture_repertoire'));
        echo $msg;
        exit;
    }else
    {
        // Si le fichier existe, on l'efface
        if (file_exists($upload_dir.$filename))
        {
            @unlink($upload_dir.$filename);
        }
        // V�rification de la taille du fichier
        if ($fileSize > MAX_SIZE_UPLOAD)
        {
            $msg=preg_replace('/filename/',$filename,$smarty->getConfigVars('upload_fichier_erreur_taille'));
            echo $msg;
            exit;
        }

        // Chargement du fichier
        if(!(move_uploaded_file($tmp_dir,$upload_dir.$filename)))
        {
            $msg=preg_replace('/filename/',$filename,$smarty->getConfigVars('upload_fichier_erreur_chargement'));
            echo $msg;
            exit;
        }else
        {
            // V�rification du bon chargement du fichier
            if (!file_exists($upload_dir.$filename))
            {
                $msg=preg_replace('/filename/',$filename,$smarty->getConfigVars('upload_fichier_erreur_chargement'));
                echo $msg;
                exit;
            }else
            {
                @mkdir($dest_dir);
                $info = pathinfo($upload_dir.$filename);

                // Test si c'est une archive on l'extrait
                if ($type_restauration=="sauvegarde" && $info["extension"] == "zip") 
                { 
                    // Extraction de l'archive
                    $zip = new ZipArchive(); 
                    if($zip->open($upload_dir.$filename) === true)
                    {
                        $zip->extractTo($dest_dir);
                        $zip->close();
                      } else {
                        @unlink($upload_dir.$filename);
                        $msg=preg_replace('/filename/',$filename,$smarty->getConfigVars('erreur_extraction_sauvegarde'));
                        echo $msg;
                        exit;
                    exit;
                    }

                    ...

                }

                ...

                }
            }
    }
    }
}
?>