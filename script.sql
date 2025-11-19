CREATE DATABASE erp_db;

USE erp_db;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    categoria VARCHAR(100),
    preco DECIMAL(10,2),
    quantidade INT,
    data_pedido DATE,
    data_chegada DATE
);
