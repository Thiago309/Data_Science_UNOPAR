class Dados:
    """permite a criação de uma estrutura para gravar dados"""
    def __init__(self):     # O construtor __init__ inicializa a classe Dados com a variavel itens vazia.
        self.itens = []

    def __repr__(self):     # Metodo __repr__ retorna os dados armazenados da classe Dados sempre como string.
        return str(self.itens)

    def insere(self, valor):    # Esse metodo insere novos dados a lista itens.
        """ adiciona itens a sua lista de dados"""

        self.itens.append(valor) # Comando append, adiciona o valor a lista.

    def remove(self):   # Remove qualquer valor da lista.

        # modifica o valor do último item
        self.itens.pop()


def main():

    # cria um novo objeto do tipo Dados
    dados = Dados()

    # adicionando itens
    dados.insere(1)
    dados.insere(2)
    dados.insere(3)  # último item adicionado

    print(dados)  # [1, 2, 3]

    # removendo itens
    dados.remove()

    print(dados)  # [1, 2]


if __name__ == "__main__":
    main()
