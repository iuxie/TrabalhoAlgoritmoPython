class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) < 2:
            print("Nome inválido.")
        else:
            self._nome = novo_nome


class Cliente(Pessoa):
    def __init__(self, nome, email):
        super().__init__(nome)
        self._email = email
        self.compras = []  # lista de produtos comprados

    def registrar_compra(self, produto):
        self.compras.append(produto)

    def listar_compras(self):
        if not self.compras:
            print("Nenhuma compra registrada.")
        else:
            for item in self.compras:
                print(f"{item.marca} - {item.modelo} - R${item.preco:.2f}")


class Funcionario(Pessoa):
    def __init__(self, nome, cargo):
        super().__init__(nome)
        self._cargo = cargo

    def __str__(self):
        return f"Funcionário: {self.nome} | Cargo: {self._cargo}"


class Produto:
    def __init__(self, marca, modelo, tamanho, preco, categoria):
        self._marca = marca
        self._modelo = modelo
        self._tamanho = tamanho
        self._preco = preco
        self._categoria = categoria

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            print("Preço inválido.")
        else:
            self._preco = valor

    def __str__(self):
        return f"{self._marca} - {self._modelo} ({self._categoria}) - Tam: {self._tamanho} - R${self._preco:.2f}"
