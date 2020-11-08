import MySQLdb

connection = MySQLdb.connect(host="localhost", user="root", password="")
cursor = connection.cursor()

cursor.execute("CREATE DATABASE testetsp")

cursor.execute("USE testetsp")

cursor.execute("CREATE TABLE `testetsp`.`categories` ("
               "`id` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(45) NOT NULL, "
               "PRIMARY KEY (`id`));")

cursor.execute("CREATE TABLE `testetsp`.`products` ("
               "`id` INT NOT NULL AUTO_INCREMENT,"
               "`name` VARCHAR(45) NOT NULL,"
               "`description` VARCHAR(45) NOT NULL,"
               "`value` VARCHAR(45) NOT NULL,"
               "`categories` INT NOT NULL,"
               "PRIMARY KEY (`id`),"
               "CONSTRAINT `categories_fk`"
               "FOREIGN KEY (`categories`)"
               "REFERENCES `testetsp`.`categories` (`id`)"
               "ON DELETE NO ACTION "
               "ON UPDATE NO ACTION);")
