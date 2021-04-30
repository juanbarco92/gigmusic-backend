CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(200),
    email VARCHAR(50) NOT NULL UNIQUE,
    is_admin BOOLEAN,
    is_premium BOOLEAN,
    is_eliminated TIMESTAMP,
    PRIMARY KEY (id)
);