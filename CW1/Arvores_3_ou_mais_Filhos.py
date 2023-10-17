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

    def representacao_com_recuo(self, numero_de_espacos=0):
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


print(
    """
                    Pacotes Turisticos
                  /              |        \\
         Tranquilidade       Aventura      Luxo
                          /     |     \\
                    Rafting  Escalada   Tirolesa

    """
)

# criacao de objetos da classe Vertice
raiz = Vertice("Pacotes Turisticos")
# criação de filhos de raiz
tranquilidade = raiz.inserir_filho("Traquilidade")
aventura = raiz.inserir_filho("Aventura")
luxo = raiz.inserir_filho("Luxo")

# criação de filhos de aventura
rafting = aventura.inserir_filho("Rafting")
escalada = aventura.inserir_filho("Escalada")
tirolesa = aventura.inserir_filho("Tirolesa")

print("")
print("Impressão da árvore")
print(raiz.representacao_com_recuo())
print(raiz.representacao_com_parenteses())

print("")
print("Imprimir o percurso pré-ordem a partir de raiz")
raiz.imprimir_percurso_pre_ordem()
print("")
print("Imprimir o percurso pós-ordem a partir de raiz")
raiz.imprimir_percurso_pos_ordem()

print("")
print("Imprimir o percurso pré-ordem a partir de Aventura")
aventura.imprimir_percurso_pre_ordem()
print("")
print("Imprimir o percurso pós-ordem a partir de Aventura")
aventura.imprimir_percurso_pos_ordem()
