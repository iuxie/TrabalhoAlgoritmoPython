from classes import Calcado

def cadastrar_calcado(estoque):
    try:
        marca = input('Informe a marca: ').upper()
        modelo = input('Informe o modelo: ')
        tamanho = int(input('Informe o tamanho (32 a 45): '))
        categoria = input('Informe a categoria: ').upper()
        preco = float(input('Informe o preço: '))

        novo_calcado = Calcado(marca, modelo, tamanho, preco, categoria)
        novo_calcado.entrou_no_estoque(estoque)

    except ValueError:
        print('Erro: digite valores válidos (números em tamanho e preço).')

def listar_calcados(estoque):
    if not estoque:
        print('Nenhum produto cadastrado.')
    else:
        for id_calcado, dados in estoque.items():
            print(f'ID: {id_calcado} | Marca: {dados["marca"]} | Modelo: {dados["modelo"]} | '
                  f'Tamanho: {dados["tamanho"]} | Categoria: {dados["categoria"]} | Preço: R${dados["preco"]:.2f}')

def modificar_calcado(estoque):
    try:
        id_calcado = int(input('Informe o ID do produto a modificar: '))
        if id_calcado not in estoque:
            print('Produto não encontrado.')
            return

        marca = input('Nova marca: ').upper()
        modelo = input('Novo modelo: ')
        tamanho = int(input('Novo tamanho: '))
        categoria = input('Nova categoria: ').upper()
        preco = float(input('Novo preço: '))

        estoque[id_calcado] = {
            'marca': marca,
            'modelo': modelo,
            'tamanho': tamanho,
            'categoria': categoria,
            'preco': preco
        }
        print('Produto atualizado com sucesso.')

    except ValueError:
        print('Erro: valores inválidos. Certifique-se de digitar números para tamanho e preço.')

def deletar_calcado(estoque):
    try:
        id_calcado = int(input('Informe o ID do produto a deletar: '))
        if id_calcado in estoque:
            del estoque[id_calcado]
            print('Produto deletado com sucesso.')
        else:
            print('Produto não encontrado.')
    except ValueError:
        print('Erro: digite um número válido para o ID.')

