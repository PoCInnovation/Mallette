<html>

<head>

    <div align="center"><h1>Epreuve</h1></div>
    <title>Acceder au compte admin</title>
    <script src="/script.js"></script> 
</head>

<body>

    <br><br>
    <div align="center">
        <?php
        if (isset($_GET["msg"]) && $_GET["msg"] == 'password') {
            echo "Wrong Password";
        }
        if (isset($_GET["msg"]) && $_GET["msg"] == 'username') {
            echo "Wrong Username";
        }
        ?>
    <form enctype='application/json' name="loginform" action="./auth.php" onsubmit="return validateForm()" method="POST">
        <table>
            <tr>
                <td>Login</td>
                <td><input type="text" name="pseudo" maxlength="30"></td> </tr>
            <tr>
                <td>Pass</td>
                <td><input type="password" name="mdp" maxlength="30"></td> </tr>
            <tr><td colspan=2 align="center"><input type="submit" name="login" value="Login"></td></tr>
        </table> 
    </form>
    </div>

</body>

</html>
