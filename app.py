import functions

estoque = []
clientes = []

while True:
    print("\n--- PASSOS CALÇADOS ESPORTIVOS ---")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Cadastrar cliente")
    print("4. Listar clientes")
    print("5. Registrar compra")
    print("6. Visualizar Compras")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        functions.cadastrar_produto(estoque)
    elif opcao == '2':
        functions.listar_produtos(estoque)
    elif opcao == '3':
        functions.cadastrar_cliente(clientes)
    elif opcao == '4':
        functions.listar_clientes(clientes)
    elif opcao == '5':
        functions.registrar_compra(clientes, estoque)
    elif opcao == '6':
        functions.visualizar_compra(clientes)
    elif opcao == '7':
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida.")