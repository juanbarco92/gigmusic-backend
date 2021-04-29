CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(200),
    email VARCHAR(50) UNIQUE,
    is_admin BOOLEAN,
    PRIMARY KEY (id)
);