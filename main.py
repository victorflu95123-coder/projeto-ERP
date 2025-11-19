import mysql.connector
from datetime import datetime, timedelta

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="95123", 
    database="erp_db"
)
cursor = con.cursor()


def cadastrar_produto():
    print("\n=== CADASTRAR PRODUTO ===")
    nome = input("Nome: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade inicial: "))

    data_pedido = datetime.today().date()
    data_chegada = data_pedido + timedelta(days=7)  

    sql = "INSERT INTO produtos (nome, categoria, preco, quantidade, data_pedido, data_chegada) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (nome, categoria, preco, quantidade, data_pedido, data_chegada))
    con.commit()

    print(f"\n✔ Produto cadastrado com sucesso!")
    print(f"Data do pedido: {data_pedido} | Previsão de chegada: {data_chegada}\n")


def excluir_produto():
    print("\n=== EXCLUIR PRODUTO ===")
    print("1 - Excluir por ID")
    print("2 - Excluir por Nome")
    opc = input("Escolha: ")

    if opc == "1":
        pid = input("Informe o ID: ")
        cursor.execute("DELETE FROM produtos WHERE id = %s", (pid,))
    elif opc == "2":
        nome = input("Informe o nome: ")
        cursor.execute("DELETE FROM produtos WHERE nome = %s", (nome,))
    else:
        print("Opção inválida.")
        return

    con.commit()
    print("✔ Produto removido.\n")


def menu():
    while True:
        print("\n===== MENU ERP =====")
        print("1 - Cadastrar produto")
        print("2 - Excluir produto")
        print("3 - Sair")
        opc = input("Escolha: ")

        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            excluir_produto()
        elif opc == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
cursor.close()
con.close()