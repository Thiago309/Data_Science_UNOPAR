class Vertice:
    """
    Vertice de Arvore Binária de Busca
    """

    def __init__(self, chave, pai=None):
        # será usada na busca
        self.chave = chave
        # vértice pai
        self.pai = pai
        # filho menor (à esquerda) e maior (à direita)
        self.menor = None
        self.maior = None

    def __str__(self):
        return str(self.chave)

    def apresentar(self, num_espacos=0, sentido=""):
        espacos = " " * num_espacos
        if self.menor:
            self.menor.apresentar(num_espacos + 10, sentido="/")

        print("{}{}----> [{}]".format(espacos, sentido, self.chave))

        if self.maior:
            self.maior.apresentar(num_espacos + 10, sentido="\\")

    def representacao_com_parenteses(self):
        """
        Retorna a representação da árvore com aninhamento por parênteses
        :return: (str)
        """
        dir = esq = ""
        if self.menor:
            # recursividade
            esq = self.menor.representacao_com_parenteses()

        if self.maior:
            # recursividade
            dir = self.maior.representacao_com_parenteses()

        return "({}{}{})".format(str(self), esq, dir)

    def representacao_com_recuo(self, numero_de_espacos=0):
        """
        Retorna a representação da árvore com recuo
        :return: (str)
        """
        esq = dir = ""
        if self.menor:
            esq = self.menor.representacao_com_recuo(numero_de_espacos + 4)

        if self.maior:
            dir = self.maior.representacao_com_recuo(numero_de_espacos + 4)

        return "{esq}{espacos}{self}\n{dir}".format(
            espacos=' ' * numero_de_espacos, self=str(self), esq=esq, dir=dir,
        )

    def inserir(self, chave_nova):
        """
        Executa a inserção
        :param chave_nova: chave da chave a ser inserido
        :return: vértice inserido
        """
        print("Inserir {} (chave atual: {})".format(chave_nova, self.chave))
        if chave_nova < self.chave:
            # é menor, procura no lado esquerdo
            if self.menor:
                print("Inserir {} no lado menor".format(chave_nova))
                return self.menor.inserir(chave_nova)

            # cria Vertice no lado menor
            self.menor = Vertice(chave_nova, self)
            # retorna vertice criado
            return self.menor
        elif chave_nova > self.chave:
            # é maior, procura no lado direito
            if self.maior:
                print("Inserir {} no lado maior".format(chave_nova))
                return self.maior.inserir(chave_nova)

            # cria Vertice no lado maior e o retorna
            self.maior = Vertice(chave_nova, self)
            # retorna vertice criado
            return self.maior
        else:
            # encontrou, retorna o próprio, não faz inserção
            return self

    def _remover_folha(self):
        """
        Remove o vértice folha
        :return: vértice removido
        """
        print("Remover FOLHA. Sou folha")
        if self.pai:
            # tem pai, então não sou a raiz
            if self.pai.menor is self:
                # sou filho da esquerda, me desvincula da esquerda
                self.pai.menor = None
            else:
                # sou filho da direita, me desvincula da direita
                self.pai.maior = None
            # me desvinculo do meu pai
            self.pai = None
        # retorna o vértice removido
        return self

    def _remover_pai_de_um_filho(self):
        """
        Remove o vértice que tem um filho seja à direita ou à esquerda
        :return: vértice removido
        """
        print("Remover PAI de 1 filho. Sou pai de 1 filho")
        # identifico meu pai
        meu_pai = self.pai
        # tenho só 1 filho, identifico meu filho (esquerdo ou direito)
        meu_filho = self.menor or self.maior

        if meu_pai is None:
            # sou raiz, a árvore está apontando para mim,
            # não posso ser removido
            # então, vou trocar de lugar com meu filho
            meu_filho.chave, self.chave = self.chave, meu_filho.chave

            # agora estou no lugar do meu filho e posso ser removido
            # a recursividade tratará a forma como serei removido
            return meu_filho.remover(meu_filho.chave)

        # meu pai, é pai do meu filho
        meu_filho.pai = meu_pai

        # meu filho, passa a ser filho do meu pai
        if meu_pai.menor is self:
            # sou filho da direita,
            # meu filho passa a ser seu filho da direita
            meu_pai.menor = meu_filho
        else:
            # sou filho da esquerda,
            # meu filho passa a ser seu filho da esquerda
            meu_pai.maior = meu_filho

        # me desvinculo do meu pai e do meu filhho
        self.pai = None
        self.menor = None
        self.maior = None
        return self

    def _remover_pai_de_dois_filhos(self):
        """
        Remove o vértice que tem 2 filhos
        :return: vértice removido
        """
        print("Remover PAI de 2 filhos. Sou pai de 2 filhos")
        # sou pai de dois filhos

        # obter o menor do lado menor
        menor = self.maior.buscar_menor()

        # troca valor da chave entre o nó atual e o menor
        self.chave, menor.chave = menor.chave, self.chave

        # remover o menor / recursividade
        return menor.remover(menor.chave)

    def remover(self, chave):
        print("Remover {} (chave atual: {})".format(chave, self.chave))
        if chave < self.chave:
            # se menor existe, continua a busca pelo menor
            # senão a busca encerra e None é retornado
            return self.menor and self.menor.remover(chave)
        elif chave > self.chave:
            # se maior existe, continua a busca pelo maior
            # senão a busca encerra e None é retornado
            return self.maior and self.maior.remover(chave)
        else:
            if self.menor and self.maior:
                # tem ambos filhos
                return self._remover_pai_de_dois_filhos()
            if self.menor or self.maior:
                # tem ou filho menor ou filho maior
                return self._remover_pai_de_um_filho()
            # nao tem filhos
            return self._remover_folha()

    def imprimir_percurso_em_ordem(self):
        """
        Percorre a árvore em ordem simétrica (esquerda, vértice, direita)
        e imprime a chave do vértice
        :return: None
        """
        if self.menor:
            # recursividade: executa o mesmo atributo para seu filho esquerdo
            self.menor.imprimir_percurso_em_ordem()
        # imprime a chave do vértice
        print(self)
        if self.maior:
            # recursividade: executa o mesmo atributo para seu filho direito
            self.maior.imprimir_percurso_em_ordem()

    def imprimir_percurso_pre_ordem(self):
        """
        Percorre a árvore em pré ordem (vértice, esquerda, direita)
        e imprime a chave do vértice
        :return: None
        """
        # imprime a chave do vértice
        print(self)
        if self.menor:
            # recursividade: executa o mesmo atributo para seu filho esquerdo
            self.menor.imprimir_percurso_pre_ordem()
        if self.maior:
            # recursividade: executa o mesmo atributo para seu filho direito
            self.maior.imprimir_percurso_pre_ordem()

    def imprimir_percurso_pos_ordem(self):
        """
        Percorre a árvore em pré ordem (esquerda, direita, vértice)
        e imprime a chave do vértice
        :return: None
        """
        if self.menor:
            # recursividade: executa o mesmo atributo para seu filho esquerdo
            self.menor.imprimir_percurso_pos_ordem()
        if self.maior:
            # recursividade: executa o mesmo atributo para seu filho direito
            self.maior.imprimir_percurso_pos_ordem()
        # imprime a chave do vértice
        print(self)

    def buscar(self, chave_nova):
        print("")
        print("Procurando {}. Chave atual: {}".format(chave_nova, self.chave))
        if chave_nova < self.chave:
            return self.menor and self.menor.buscar(chave_nova)
        elif chave_nova > self.chave:
            return self.maior and self.maior.buscar(chave_nova)
        else:
            # encontrou, retorna o próprio
            return self

    def buscar_menor(self):
        """
        Procura o menor até que não encontra e
        retorna ele mesmo
        """
        print("Procurar menor {}".format(self))
        if self.menor:
            # recursividade
            return self.menor.buscar_menor()
        return self

    def imprimir(self):
        # 3 formas de apresentar a árvore como está neste momento
        print("_" * 20)
        print(self.representacao_com_parenteses())
        print("_" * 20)
        print(self.representacao_com_recuo())
        print("_" * 20)
        self.apresentar()
        print("_" * 20)


class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = Vertice(chave)
        else:
            self.raiz.inserir(chave)
        self.raiz.imprimir()

    def remover(self, chave):
        if self.raiz is not None:
            removido = self.raiz.remover(chave)
            if removido is self.raiz:
                self.raiz = None
        self.raiz.imprimir()


# Criação da árvore
arvore = ArvoreBinariaBusca()
arvore.inserir(14)

# Inserção de 4
arvore.inserir(4)

# Inserção de 18
arvore.inserir(18)

# Inserção de 0
arvore.inserir(0)

# Inserção de 21
arvore.inserir(21)

# Inserção de 17
arvore.inserir(17)

# Inserção de 1
arvore.inserir(1)

# Inserção de 8
arvore.inserir(8)

# Inserção de 13
arvore.inserir(13)

# Remoção de 13, vertice folha
arvore.remover(21)

# Remoção de zero, vertice pai de 1 filho
arvore.remover(0)

# Remoção de 14, vertice pai de 2 filhos e arvore
arvore.remover(14)

arvore.remover(99999)

