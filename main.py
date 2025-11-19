import mysql.connector
from datetime import datetime, timedelta

# conexão com mysql
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


def relatorio():
    print("\n=== RELATÓRIO DE PRODUTOS ===")
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return

    for p in produtos:
        id, nome, categoria, preco, quantidade, data_pedido, data_chegada = p
        alerta = "ESTOQUE BAIXO !!!" if quantidade < 5 else ""
        print("------------------------------")
        print(f"ID: {id} | Nome: {nome} | Categoria: {categoria}")
        print(f"Preço: R$ {preco} | Quantidade: {quantidade} {alerta}")
        print(f"Pedido: {data_pedido} | Chegada prevista: {data_chegada}")
    print("------------------------------\n")


def menu():
    while True:
        print("\n===== MENU ERP =====")
        print("1 - Cadastrar produto")
        print("2 - Excluir produto")
        print("3 - Relatório de produtos")
        print("4 - Sair")
        opc = input("Escolha: ")

        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            excluir_produto()
        elif opc == "3":
            relatorio()
        elif opc == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
cursor.close()
con.close()