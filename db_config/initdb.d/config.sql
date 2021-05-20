CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    username VARCHAR(50) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    password VARCHAR(200) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    is_admin BOOLEAN NOT NULL,
    is_premium BOOLEAN NOT NULL,
    is_eliminated TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE analytics (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    user_id INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    objeto VARCHAR(100) NOT NULL,
    fecha TIMESTAMP,
    PRIMARY KEY (id)
);