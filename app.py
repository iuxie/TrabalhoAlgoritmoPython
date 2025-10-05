import functions

estoque = []
clientes = []

while True:
    print("\n--- LOJA DE CALÇADOS ---")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Cadastrar cliente")
    print("4. Registrar compra")
    print("5. Listar clientes")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        functions.cadastrar_produto(estoque)
    elif opcao == '2':
        functions.listar_produtos(estoque)
    elif opcao == '3':
        functions.cadastrar_cliente(clientes)
    elif opcao == '4':
        functions.registrar_compra(clientes, estoque)
    elif opcao == '5':
        functions.listar_clientes(clientes)
    elif opcao == '6':
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida.")