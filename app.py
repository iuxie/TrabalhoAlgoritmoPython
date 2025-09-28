#Trabalho de Python - E-commerce de Calçados

clientes_cadastrados = {}

def cadastro_cliente(usuarios):
    print('\n--- Cadastrando Usuário ---\n')
    email = input('Digite seu E-mail: ')
    if email in usuarios:
        print('E-mail já cadastrado. Tente o login.')
        return
    senha_cliente = input('Digite sua senha: ')
    nome_cliente = input('Digite seu nome completo: ')

    usuarios[email] = {
            'senha': senha_cliente,
            'nome': nome_cliente
    }

    print(f'\nUsuário {nome_cliente} cadastrado com sucesso!')


def login_cliente(usuarios):
    print('\n--- Página de Login ---\n')
    email = input('Digite seu E-mail: ')
    senha_cliente = input('Digite sua senha: ')

    if email in usuarios:
        senha_armazenada = usuarios[email]['senha']
        if senha_cliente == senha_armazenada:
            print(f'\nLogin efetuado com suceso! Bem-vindo(a) {usuarios[email]['nome']}')
            return email
    else:
        print('\nE-mail ou senha incorretos.')
        return None

    
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
            cadastro_cliente(clientes_cadastrados)
        elif selection == 2:
            login_cliente(clientes_cadastrados)
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