#Trabalho de Python - E-commerce de Calçados

def cadastroCliente():
    print()

def loginCliente():
    print()
    
print('\nPassos Calçados: Sua loja de calçados online com as melhores ofertas e condições!\n')
print('1. Cadastre-se')
print('2. Login')
print('3. Navegar por calçados')
print('4. Buscar')
print('5. Visualizar carrinho')
print('6. Sair')

selection = int(input('Selecione sua opção (1-6): '))
if selection in [1, 2, 3, 4, 5, 6]:
    if selection == 1:
        cadastroCliente()
    elif selection == 2:
        loginCliente()