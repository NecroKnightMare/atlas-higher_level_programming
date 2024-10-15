-- create user if doesn't exist that has all priveleges and set password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVELEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVELEGES;