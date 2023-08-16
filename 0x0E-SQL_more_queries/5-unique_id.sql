-- creates table in the current database with default  and not null in your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
