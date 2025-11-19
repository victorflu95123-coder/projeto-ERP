Este é um projeto de um ERP simples que visa automatizar processos empresariais. 
A ERP esta diretamente integrada com o banco de dados Mysql.

Suas principais funções são:

-Cadastro de produtos
-Exclusão de produtos
-Relatório completo de itens cadastrados
-Destaque de produtos com estoque baixo
-Cálculo automático da data do pedido e data estimada de chegada (usando datetime)

PASSO A PASSO PARA EXECUTAR O PROGRAMA:

1- INSTALE O CONECTOR MYSQL NO SEU TERMINAL COM O COMANDO:
"pip install mysql-connector-pythonpip install mysql-connector-python"

2- AJUSTE A ESTRUTURA MYSQL NO ARQUIVO "MAIN.PY" PARA FUNCIONAR COM SEU BANCO (NAO ESQUEÇA DE AJUSTAR A SENHA).

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="erp_db"
)

3- NO SEU MYSQL EXECUTE O ARQUIVO "SCRIPT.SQL" PARA A CRIAÇAO DO BANCO DE DADOS.

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

4- PRONTO!! CERTIFIQUE-SE QUE O CODIGO .PY ESTA CONECTADO COM O MYSQL E EXECUTE O PROGRAMA.


autor: VICTOR NUNES DA COSTA - 44396481