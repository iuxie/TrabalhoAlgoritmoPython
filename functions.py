from classes import Produto, Cliente

CATEGORIAS = ('TÊNIS DE CORRIDA', 'CHUTEIRA', 'TÊNIS DE VÔLEI', 'TÊNIS DE BASQUETE')
MARCAS = ('NIKE', 'ADIDAS', 'ASICS', 'OLYMPIKUS', 'PUMA', 'NEW BALANCE', 'MIZUNO')

def cadastrar_produto(estoque):
    try:
        marca = input("Marca: ").upper()
        modelo = input("Modelo: ")
        tamanho = int(input("Tamanho: "))
        preco = float(input("Preço: "))
        categoria = input("Categoria: ").upper()

        if marca not in MARCAS:
            print("Marca inválida.")
            return
        if categoria not in CATEGORIAS:
            print("Categoria inválida.")
            return

        produto = Produto(marca, modelo, tamanho, preco, categoria)
        estoque.append(produto)
        print("Produto cadastrado com sucesso.")
    except ValueError:
        print("Erro: informe números válidos para tamanho e preço.")


def listar_produtos(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
    else:
        for i, produto in enumerate(estoque, 1):
            print(f"{i}. {produto}")


def cadastrar_cliente(clientes):
    nome = input("Nome do cliente: ")
    email = input("Email do cliente: ")
    cliente = Cliente(nome, email)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso.")


def registrar_compra(clientes, estoque):
    if not clientes or not estoque:
        print("Necessário ter pelo menos 1 cliente e 1 produto.")
        return

    listar_produtos(estoque)

    try:
        id_cliente = int(input("Número do cliente (posição na lista): ")) - 1
        id_produto = int(input("Número do produto: ")) - 1

        cliente = clientes[id_cliente]
        produto = estoque[id_produto]

        cliente.registrar_compra(produto)
        print(f"Compra registrada para {cliente.nome}.")
    except (ValueError, IndexError):
        print("Erro: índice inválido.")


def listar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. {cliente.nome} - {cliente._email}")
