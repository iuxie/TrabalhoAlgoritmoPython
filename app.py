#Trabalho de Python - E-commerce de Calçados

def cadastro_cliente():
    print()

def login_cliente():
    print()
    
def navegacao_calcados():
    print()

def buscar_calcados():
    print()

def visualizar_carrinho():
    print()
     
while True:
    print('\nPassos Calçados: Sua loja de calçados online com as melhores ofertas e condições!\n')
    print('1. Cadastre-se')
    print('2. Login')
    print('3. Navegar por calçados')
    print('4. Buscar')
    print('5. Visualizar carrinho')
    print('6. Sair')

    try:
        selection = int(input('Selecione sua opção (1-6): '))

        if selection == 1:
            cadastro_cliente()
        elif selection == 2:
            login_cliente()
        elif selection == 3:
            navegacao_calcados()
        elif selection == 4:
            buscar_calcados()
        elif selection == 5:
            visualizar_carrinho()
        elif selection == 6:
            print('Saindo... Obrigado por visitar a Passos Calçados!')
            break
        else:
            print('\nOpção inválida! Por favor, escolha um número entre 1 e 6.')

    except ValueError:
        print('\nEntrada inválida! Por favor, digite apenas um número.')