-- creates the database with id INT unique, auto generated, can’t be null and is a primary key hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, name VARCHAR(256) NOT NULL);
