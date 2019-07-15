<?php
 if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], image1)) {
        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
?>
