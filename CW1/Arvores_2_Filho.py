class Vertice:
    """
    Vertice de Arvore Binária
    """
    def __init__(self, dado):
        # dado propriamente dito, conteúdo do vértice
        self.dado = dado
        # filho da esquerda e da direita
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.dado)

    def representacao_com_parenteses(self):
        """
        Retorna a representação da árvore com aninhamento por parênteses
        :return: (str)
        """
        if self.esquerda:
            # recursividade
            esq = self.esquerda.representacao_com_parenteses()
        else:
            esq = ""
        if self.direita:
            # recursividade
            dir = self.direita.representacao_com_parenteses()
        else:
            dir = ""
        return "({}{}{})".format(str(self), esq, dir)

    def representacao_com_recuo(self, numero_de_espacos=0):
        """
        Retorna a representação da árvore com recuo
        :return: (str)
        """
        if self.esquerda:
            esq = self.esquerda.representacao_com_recuo(numero_de_espacos + 4)
        else:
            esq = ""
        if self.direita:
            dir = self.direita.representacao_com_recuo(numero_de_espacos + 4)
        else:
            dir = ""
        return "{espacos}{self}\n{esq}{dir}".format(
            espacos=' '*numero_de_espacos,
            self=str(self),
            esq=esq,
            dir=dir,
        )

    def imprimir_percurso_em_ordem(self):
        """
        Percorre a árvore em ordem simétrica (esquerda, vértice, direita)
        e imprime o dado do vértice
        :return: None
        """
        if self.esquerda:
            # recursividade: executa o mesmo atributo para seu filho esquerdo
            self.esquerda.imprimir_percurso_em_ordem()
        # imprime o dado do vértice
        print(self)
        if self.direita:
            # recursividade: executa o mesmo atributo para seu filho direito
            self.direita.imprimir_percurso_em_ordem()

    def imprimir_percurso_pre_ordem(self):
        """
        Percorre a árvore em pré ordem (vértice, esquerda, direita)
        e imprime o dado do vértice
        :return: None
        """
        # imprime o dado do vértice
        print(self)
        if self.esquerda:
            # recursividade: executa o mesmo atributo para seu filho esquerdo
            self.esquerda.imprimir_percurso_pre_ordem()
        if self.direita:
            # recursividade: executa o mesmo atributo para seu filho direito
            self.direita.imprimir_percurso_pre_ordem()

    def imprimir_percurso_pos_ordem(self):
        """
        Percorre a árvore em pré ordem (esquerda, direita, vértice)
        e imprime o dado do vértice
        :return: None
        """
        if self.esquerda:
            # recursividade: executa o mesmo atributo para seu filho esquerdo
            self.esquerda.imprimir_percurso_pos_ordem()
        if self.direita:
            # recursividade: executa o mesmo atributo para seu filho direito
            self.direita.imprimir_percurso_pos_ordem()
        # imprime o dado do vértice
        print(self)


print(
"""
                           Passeio
                        /           \\
                  Diurno               Noturno
               /         \\             /       \\
           Frio           Calor   Restaurante  Cinema
           /   \\         /    \\
    Planetario  Museu  Parque  Praia
"""
)

# Criar os vértices
passeio = Vertice("Passeio")

diurno = Vertice("Diurno")
frio = Vertice("Frio")
planetario = Vertice("Planetário")
museu = Vertice("Museu")
calor = Vertice("Calor")
parque = Vertice("Parque")
praia = Vertice("Praia")

noturno = Vertice("Noturno")
restaurante = Vertice("Restaurante")
ciname_noturno = Vertice("Cinema")

# Vincula os filhos de passeio
passeio.esquerda = diurno
passeio.direita = noturno

# Vincula os filhos de diurno
diurno.esquerda = frio
diurno.direita = calor

# Vincula os filhos de frio
frio.esquerda = planetario
frio.direita = museu

# Vincula os filhos de calor
calor.esquerda = parque
calor.direita = praia

# Vincula os filhos de noturno
noturno.esquerda = restaurante
noturno.direita = ciname_noturno

# Imprime representacao com parenteses
print("")
print("Imprime representacao com parenteses")
print(passeio.representacao_com_parenteses())

# Imprime representacao com recuo
print("")
print("Imprime representacao com recuo")
print(passeio.representacao_com_recuo())

# Imprime os dados dos vértices
print("")
print("Imprime os dados dos vértices no percurso em ordem")
passeio.imprimir_percurso_em_ordem()
print("")
print("Imprime os dados dos vértices no percurso pré ordem")
passeio.imprimir_percurso_pre_ordem()
print("")
print("Imprime os dados dos vértices no percurso pós ordem")
passeio.imprimir_percurso_pos_ordem()

