class Vertice:
    """
    Vertice de Arvore Binária de Busca
    """

    def __init__(self, chave, dado, pai=None):
        # será usada na busca
        self.chave = chave
        self.dado = dado
        # vértice pai
        self.pai = pai
        # filho menor (à esquerda) e maior (à direita)
        self.menor = None
        self.maior = None

    def __str__(self):
        return str(self.chave)

    def inserir(self, chave_nova, dado):
        """
        Executa a inserção
        :param chave_nova: chave da chave a ser inserido
        :return: vértice inserido
        """
        if chave_nova < self.chave:
            # é menor, procura no lado esquerdo
            if self.menor:
                print("Inserir {} no lado menor".format(chave_nova))
                return self.menor.inserir(chave_nova, dado)

            # cria Vertice no lado menor
            self.menor = Vertice(chave_nova, dado, self)
            # retorna vertice criado
            return self.menor
        elif chave_nova > self.chave:
            # é maior, procura no lado direito
            if self.maior:
                print("Inserir {} no lado maior".format(chave_nova))
                return self.maior.inserir(chave_nova, dado)

            # cria Vertice no lado maior e o retorna
            self.maior = Vertice(chave_nova, dado, self)
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
        # sou pai de dois filhos

        # obter o menor do lado menor
        menor = self.maior.buscar_menor()

        # troca valor da chave entre o nó atual e o menor
        self.chave, menor.chave = menor.chave, self.chave

        # remover o menor / recursividade
        return menor.remover(menor.chave)

    def remover(self, chave):
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
        if self.menor:
            self.menor.imprimir()
        print(" {}|\t{}".format(self.chave, self.dado))
        if self.maior:
            self.maior.imprimir()


class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None

    def inserir(self, chave, dado):
        if self.raiz is None:
            self.raiz = Vertice(chave, dado)
        else:
            self.raiz.inserir(chave, dado)

    def remover(self, chave):
        if self.raiz:
            removido = self.raiz.remover(chave)
            if removido is self.raiz:
                self.raiz = None

    def imprimir(self):
        if self.raiz:
            self.raiz.imprimir()


class ListaDeAfazeres:

    def __init__(self):
        self.arvore = ArvoreBinariaBusca()

    def inserir(self, ordem, atividade):
        self.arvore.inserir(ordem, atividade)

    def remover(self, ordem):
        self.arvore.remover(ordem)

    def listar(self):
        print("_" * 20)
        print("Seus afazeres são:")
        self.arvore.imprimir()
        print("_" * 20)


# Criação da lista de afazeres
lista_de_afazeres = ListaDeAfazeres()

while True:

    try:
        lista_de_afazeres.listar()
        # op = input("Digite I para Inserir ou R para Remover atividade: ")
        op = input(
            """
            Digite I para Inserir atividade
            Digite R para Remover atividade
            Digite x para Sair
            """
        )
        print(op)
        if op == "x":
            print("Saiu do programa")
            break

        if op == "I":
            atividade = input("Entre com a atividade: ")
            ordem = int(input("Entre com a ordem (número): "))
            lista_de_afazeres.inserir(ordem, atividade)
            continue

        if op == "R":
            ordem = int(input("Entre com a ordem (número): "))
            lista_de_afazeres.remover(ordem)
            continue
    except Exception:
        print("Terminado pelo usuário")
        break

