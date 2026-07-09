    <?php
     
        // auth.php - Authentification des admins Bases Hacking

        $json = json_decode($_POST["json"], true);
        $login = $json["username"];
        $mdp = $json["password"];
    if ($login != "" && $mdp != "") {
            @mysql_connect("localhost", "root", "password46387463248database") or print("Impossible de se connecter à la base de données");
            @mysql_select_db("app") or die("Table inexistante");
	    $query = sprintf("SELECT * from users WHERE username='%s';", mysql_real_escape_string($login));
            $res = mysql_query($query);
            $resultat = mysql_numrows($res);
            mysql_close();
            $res = mysql_fetch_assoc($res);
            if ($resultat == 1 && $res['password'] == $mdp) {
                if ($res['perm'] == 'admin')
                    echo  "le digit est 6";
                else
                    echo "You don't have permissions";
            }
            else if ($resultat == 1) {
                header(  "Location: ./?msg=password");
            } else {
                header(  "Location: ./?msg=username");
            }
        } else {
            header("Location: ./");
     }
     
    ?>
