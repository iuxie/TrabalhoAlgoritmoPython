class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) < 2:
            print("Nome inválido")
        else:
            self._nome = novo_nome

class Calcado:
    def __init__(self, marca, modelo, tamanho, preco, categoria):
        self.marca = marca
        self.modelo = modelo
        self.tamanho = tamanho
        self.preco = preco
        self.categoria = categoria

    def entrou_no_estoque(self, estoque):
        if self.marca not in ['NIKE', 'ADIDAS', 'ASICS', 'OLYMPIKUS', 'PUMA', 'NEW BALANCE', 'MIZUNO']:
            print('Marca inválida.')
        elif not (32 <= self.tamanho <= 45):
            print('Tamanho fora do permitido (32 a 45).')
        elif self.categoria not in ['TÊNIS DE CORRIDA', 'CHUTEIRA', 'TÊNIS DE VÔLEI', 'TÊNIS DE BASQUETE']:
            print('Categoria inválida.')
        else:
            novo_id = len(estoque) + 1
            estoque[novo_id] = {
                'marca': self.marca,
                'modelo': self.modelo,
                'tamanho': self.tamanho,
                'categoria': self.categoria,
                'preco': self.preco
            }
            print(f'Calçado {self.modelo} cadastrado com sucesso.')
