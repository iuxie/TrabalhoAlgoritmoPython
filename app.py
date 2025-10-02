import functions

estoque = {}
MARCAS = ['NIKE', 'ADIDAS', 'ASICS', 'OLYMPIKUS', 'PUMA', 'NEW BALANCE', 'MIZUNO']
CATEGORIAS = ['TÊNIS DE CORRIDA', 'CHUTEIRA', 'TÊNIS DE VÔLEI', 'TÊNIS DE BASQUETE']

while True:
    print('\n--- PASSOS CALÇADOS ESPORTIVOS ---')
    print('1. Cadastrar Produto')
    print('2. Listar Produto')
    print('3. Modificar Produto')
    print('4. Deletar Produto')
    print('5. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        functions.cadastrar_calcado(estoque)
    elif opcao == '2':
        functions.listar_calcados(estoque)
    elif opcao == '3':
        functions.modificar_calcado(estoque)
    elif opcao == '4':
        functions.deletar_calcado(estoque)
    elif opcao == '5':
        print('Saindo do sistema.')
        break
    else:
        print('Opção inválida.')



