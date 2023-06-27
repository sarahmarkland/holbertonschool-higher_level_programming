-- lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
SELECT user, host, Grant_priv, Super_priv FROM mysql.user;