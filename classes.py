class Pessoa:
    def __init__(self, nome):
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


class Cliente(Pessoa):
    def __init__(self, nome, email):
        super().__init__(nome)
        self._email = email
        self.compras = []

    def registrar_compra(self, produto):
        self.compras.append(produto)

    def listar_compras(self):
        if not self.compras:
            print("Nenhuma compra registrada.")
        else:
            for item in self.compras:
                print(f"{item.marca} - {item.modelo} - {item.preco:.2f}")


class Funcionario(Pessoa):
    def __init__(self, nome, cargo):
        super().__init__(nome)
        self._cargo = cargo

    def __str__(self):
        return f"Nome: {self.nome} | Cargo: {self._cargo}"


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
