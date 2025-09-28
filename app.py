#Trabalho de Python - E-commerce de Calçados

import hashlib

clientes_cadastrados = {}

def cadastro_cliente(usuarios):
    print('\nCadastre seu usuário aqui!\n')
    email = input('Digite seu e-mail: ')
    if email in usuarios:
        print('Erro. Este e-mail já está cadastrado, tente o login.')
        return
    
    senha = input('Digite sua senha: ')
    nome = input('Digite seu nome completo: ')
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    usuarios[email] = {
        'senha_hash': senha_hash,
        'nome': nome
    }

    print(f'Usuário {nome} adicionado com sucesso!')


def login_cliente(usuarios):
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
            cadastro_cliente(clientes_cadastrados)
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