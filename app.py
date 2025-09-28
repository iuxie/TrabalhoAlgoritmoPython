clientes_cadastrados = {}
EMAILS_ADMIN = ['iurexavier@gmail.com', 'guilhermepassos@gmail.com']

def cadastro_cliente(usuarios):
    print('\n--- Cadastrando Usuário ---\n')
    email = input('Digite seu E-mail: ')
    if email in usuarios:
        print('E-mail já cadastrado. Tente o login.')
        return
    senha_cliente = input('Digite sua senha: ')
    nome_cliente = input('Digite seu nome completo: ')
    if email in EMAILS_ADMIN:
        cargo = 'admin'
        print('Acesso de administrador concedido')
    else:
        cargo = 'cliente'

    usuarios[email] = {
            'senha': senha_cliente,
            'nome': nome_cliente,
            'cargo': cargo
    }
    print(f'\nUsuário {nome_cliente} cadastrado com sucesso!')

def login_cliente(usuarios):
    print('\n--- Página de Login ---\n')
    email = input('Digite seu E-mail: ')
    senha_cliente = input('Digite sua senha: ')

    if email in usuarios and usuarios[email]['senha'] == senha_cliente:
        print(f"\nLogin efetuado com sucesso! Bem-vindo(a), {usuarios[email]['nome']}!")
        return email
    
    print('\nE-mail ou senha incorretos.')
    return None

def navegacao_calcados(): 
    print("\n-- Navegando por Calçados... --")
def buscar_calcados(): 
    print("\n-- Buscando Calçados... --")
def visualizar_carrinho(): 
    print("\n-- Visualizando Carrinho... --")
def gerenciar_produtos(): 
    print("\n-- Gerenciando Produtos... --")

usuario_logado = None
    
while True:
    if usuario_logado is None:
        try:
            print('\n--- PASSOS CALÇADOS ---\n')
            print('1. Login')
            print('2. Cadastre-se')
            print('3. Sair')

            opcao = int(input('Selecione sua opção (1-3): '))

            if opcao == 1:
                resultado_login = login_cliente(clientes_cadastrados)
                if resultado_login is not None:
                    usuario_logado = resultado_login
            elif opcao == 2:
                cadastro_cliente(clientes_cadastrados)
            elif opcao == 3:
                print('\nSaindo...')
                break
            else:
                print('\nOpção inválida.')
        except ValueError:
            print('Erro: digite apenas um número.')

    else:
        dados_do_usuario = clientes_cadastrados[usuario_logado]
        cargo_do_usuario = dados_do_usuario['cargo']
        nome_do_usuario = dados_do_usuario['nome']
        
        print(f'\n--- Logado como: {nome_do_usuario} ({cargo_do_usuario}) ---')

        if cargo_do_usuario == 'admin':
            print('1. Gerenciar Produtos')
            print('2. Logout')
            opcao_admin = input('Sua opção de admin: ')

            if opcao_admin == '1':
                gerenciar_produtos()
            elif opcao_admin == '2':
                usuario_logado = None
                print("\nLogout efetuado.")
            else:
                print("\nOpção inválida.")

        elif cargo_do_usuario == 'cliente':
            print('1. Navegar por calçados')
            print('2. Buscar calçados')
            print('3. Visualizar carrinho')
            print('4. Logout')
            
            opcao_cliente = input('Sua opção: ')
            if opcao_cliente == '1':
                navegacao_calcados()
            elif opcao_cliente == '2':
                buscar_calcados()
            elif opcao_cliente == '3':
                visualizar_carrinho()
            elif opcao_cliente == '4':
                usuario_logado = None
                print("\nLogout efetuado.")
            else:
                print("\nOpção inválida.")