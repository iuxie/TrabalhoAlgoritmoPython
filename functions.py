from classes import Produto, Cliente

CATEGORIAS = ('TÊNIS DE CORRIDA', 'CHUTEIRA', 'TÊNIS DE VÔLEI', 'TÊNIS DE BASQUETE')
MARCAS = ('NIKE', 'ADIDAS', 'ASICS', 'OLYMPIKUS', 'PUMA', 'NEW BALANCE', 'MIZUNO')

def cadastrar_produto(estoque):
    try:
        print(f"\nMarcas disponíveis: {', '.join(MARCAS)}")
        marca = input("Digite a marca do produto: ").strip().upper() 

        if marca not in MARCAS:
            print("\nErro: Marca inválida. Por favor, escolha uma das opções acima.")
            return

        modelo = input("Modelo: ")
        tamanho = int(input("Tamanho (número): "))
        preco = float(input("Preço: R$ "))

        print(f"\nCategorias disponíveis: {', '.join(CATEGORIAS)}")
        categoria = input("Digite a categoria do produto: ").strip().upper() 

        if categoria not in CATEGORIAS:
            print("\nErro: Categoria inválida. Por favor, escolha uma das opções acima.")
            return

        produto = Produto(marca, modelo, tamanho, preco, categoria)
        estoque.append(produto)
        print("\n>> Produto cadastrado com sucesso! <<")
    except ValueError:
        print("\nErro: Informe um número válido para tamanho e/ou preço.")

def listar_produtos(estoque):
    print("\n--- LISTA DE PRODUTOS ---")
    if not estoque:
        print("Nenhum produto cadastrado.")
    else:
        for i, produto in enumerate(estoque, 1):
            print(f"{i}. {produto}")
    print("-------------------------")


def cadastrar_cliente(clientes):
    nome = input("Nome do cliente: ").strip()
    email = input("Email do cliente: ").strip()
    cliente = Cliente(nome, email)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso.")


def registrar_compra(clientes, estoque):
    if not clientes or not estoque:
        print("Necessário ter pelo menos 1 cliente e 1 produto.")
        return
        
    listar_clientes(clientes)
    try:
        id_cliente = int(input("Número do cliente (posição na lista): ")) - 1
        cliente = clientes[id_cliente]
    except (ValueError, IndexError):
        print("Erro: ID de cliente inválido.")
        return

    listar_produtos(estoque)
    try:
        id_produto = int(input("Número do produto: ")) - 1
        produto = estoque[id_produto]
    except (ValueError, IndexError):
        print("Erro: ID de produto inválido.")
        return

    cliente.registrar_compra(produto)
    print(f"\n>> Compra registrada para {cliente.nome}. <<")


def listar_clientes(clientes):
    print("\n--- LISTA DE CLIENTES ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. {cliente.nome} - {cliente._email}")
    print("-------------------------")

def visualizar_compra(clientes):
    """
    Pede o nome e email de um cliente e exibe o histórico de compras dele,
    mostrando a data e o valor de cada transação.
    """
    if not clientes:
        print("Nenhum cliente cadastrado para buscar.")
        return

    nome_busca = input("Nome do cliente que deseja visualizar: ").strip()
    email_busca = input("Email do mesmo cliente: ").strip()

    cliente_encontrado = None

    for cliente in clientes:
        if cliente.nome.lower() == nome_busca.lower() and cliente._email.lower() == email_busca.lower():
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        print(f"\n--- Histórico de Compras de {cliente_encontrado.nome} ---")
        if not cliente_encontrado.compras:
            print("Este cliente ainda não realizou compras.")
        else:
            for compra in cliente_encontrado.compras:
                data_formatada = compra['data'].strftime('%d/%m/%Y às %H:%M:%S')
                valor = compra['valor']
                print(f"Data: {data_formatada} - Valor: R$ {valor:.2f}")
        print("-------------------------------------------------")
    
    else:
        print("\nErro: Cliente não encontrado com os dados informados.")