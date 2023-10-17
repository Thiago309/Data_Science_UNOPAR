class Filhos:
    def __init__(self):
        # cria uma lista Python vazia
        self._vertices = list()

    def representacao_com_parenteses(self):
        representacoes = []
        for vertice in self._vertices:
            representacoes.append(
                vertice.representacao_com_parenteses()
            )
        return "".join(representacoes)

    def representacao_com_recuo(self, numero_de_espacos = 0):
        representacoes = []
        for vertice in self._vertices:
            representacoes.append(
                vertice.representacao_com_recuo(numero_de_espacos + 2)
            )
        return "\n".join(representacoes)

    def inserir(self, dado):
        vertice_novo = Vertice(dado)
        self._vertices.append(vertice_novo)
        return vertice_novo

    def imprimir_percurso_pre_ordem(self):
        """
        Percorre a árvore em pré ordem (vértice, esquerda, direita)
        e imprime o dado do vértice
        :return: None
        """
        # imprime o dado do vértice
        for vertice in self._vertices:
            vertice.imprimir_percurso_pre_ordem()

    def imprimir_percurso_pos_ordem(self):
        """
        Percorre a árvore em pré ordem (esquerda, direita, vértice)
        e imprime o dado do vértice
        :return: None
        """
        for vertice in self._vertices:
            vertice.imprimir_percurso_pos_ordem()

    def imprimir(self):
        for vertice in self._vertices:
            vertice.imprimir()


class Vertice:
    """
    Vertice de Arvore N-aria
    """
    def __init__(self, dado):
        # dado propriamente dito, conteúdo do vértice
        self.dado = dado
        # classe para instanciar filhos do vértice
        self.filhos = None

    def __str__(self):
        return str(self.dado)

    def representacao_com_parenteses(self):
        filhos = ""
        if self.filhos:
            filhos = self.filhos.representacao_com_parenteses()
        return "({}{})".format(str(self), filhos)

    def representacao_com_recuo(self, numero_de_espacos=0):
        filhos = ""
        if self.filhos:
            filhos = self.filhos.representacao_com_recuo(numero_de_espacos + 2)
        return (
            "{espacos}- {self}\n"
            "{filhos}"
        ).format(
            espacos=' ' * numero_de_espacos,
            self=str(self),
            filhos=filhos,
        )

    def inserir_filho(self, dado):
        """
        Inserir um filho no vértice atual
        """
        if self.filhos is None:
            self.filhos = Filhos()
        return self.filhos.inserir(dado)

    def imprimir_percurso_pre_ordem(self):
        """
        Percorre a árvore em pré ordem (vértice, filhos)
        e imprime o dado do vértice
        :return: None
        """
        # imprime o dado do vértice
        print(self)
        if self.filhos:
            # recursividade: executa o mesmo atributo para seus filhos
            self.filhos.imprimir_percurso_pre_ordem()

    def imprimir_percurso_pos_ordem(self):
        """
        Percorre a árvore em pré ordem (filhos, vértice)
        e imprime o dado do vértice
        :return: None
        """
        if self.filhos:
            # recursividade: executa o mesmo atributo para seus filhos
            self.filhos.imprimir_percurso_pos_ordem()
        # imprime o dado do vértice
        print(self)

    def imprimir(self):
        if self.filhos:
            self.filhos.imprimir()
        else:
            print(self.dado)


# criacao de objetos da classe Vertice
filmes = Vertice("Filmes")

# classificação filmes
classif_menores_de_18 = filmes.inserir_filho("classif_menores_de_18")
classif_18 = filmes.inserir_filho("classif_18")

# classificação menores de 18 anos
classif_menores_de_16 = classif_menores_de_18.inserir_filho(
    "classif_menores_de_16")
classif_16 = classif_menores_de_18.inserir_filho("classif_16")

# classificação menores de 16 anos
classif_menores_de_14 = classif_menores_de_16.inserir_filho(
    "classif_menores_de_14")
classif_14 = classif_menores_de_16.inserir_filho("classif_14")

# classificação menores de 14 anos
classif_menores_de_12 = classif_menores_de_14.inserir_filho(
    "classif_menores_de_12")
classif_12 = classif_menores_de_14.inserir_filho("classif_12")

# classificação menores de 12 anos
classif_menores_de_10 = classif_menores_de_12.inserir_filho(
    "classif_menores_de_10")
classif_10 = classif_menores_de_12.inserir_filho(
    "classif_10")


# insere filmes em menores de 10 anos
classif_menores_de_10.inserir_filho("Filme código m10A - para menores de 10 anos")
classif_menores_de_10.inserir_filho("Filme código m10B - para menores de 10 anos")
classif_menores_de_10.inserir_filho("Filme código m10C - para menores de 10 anos")

# insere filmes a partir de 10 anos
classif_10.inserir_filho("Filme código 10A - classificação 10 anos")
classif_10.inserir_filho("Filme código 10B - classificação 10 anos")
classif_10.inserir_filho("Filme código 10C - classificação 10 anos")

# insere filmes a partir de 12 anos
classif_12.inserir_filho("Filme código 12A - classificação 12 anos")
classif_12.inserir_filho("Filme código 12B - classificação 12 anos")
classif_12.inserir_filho("Filme código 12C - classificação 12 anos")

# insere filmes a partir de 14 anos
classif_14.inserir_filho("Filme código 14A - classificação 14 anos")
classif_14.inserir_filho("Filme código 14B - classificação 14 anos")
classif_14.inserir_filho("Filme código 14C - classificação 14 anos")

# insere filmes a partir de 16 anos
classif_16.inserir_filho("Filme código 16A - classificação 16 anos")
classif_16.inserir_filho("Filme código 16B - classificação 16 anos")
classif_16.inserir_filho("Filme código 16C - classificação 16 anos")

# insere filmes a partir de 18 anos
classif_18.inserir_filho("Filme código 18A - classificação 18 anos")
classif_18.inserir_filho("Filme código 18B - classificação 18 anos")
classif_18.inserir_filho("Filme código 18C - classificação 18 anos")


while True:
    print("")
    idade = int(input("Qual é a idade? "))
    print("")
    print(".........")
    print("Recomendações para {} anos:".format(idade))
    if idade < 10:
        classif_menores_de_10.imprimir()
        continue
    if idade < 12:
        classif_menores_de_12.imprimir()
        continue
    if idade < 14:
        classif_menores_de_14.imprimir()
        continue
    if idade < 16:
        classif_menores_de_16.imprimir()
        continue
    if idade < 18:
        classif_menores_de_18.imprimir()
        continue
    filmes.imprimir()
    print("....")
