-- creates the table id_not_null
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL UNIQUE,
    name VARCHAR(256) DEFAULT NULL
);
