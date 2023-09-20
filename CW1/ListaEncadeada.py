#1º Processo da ListaEncadeada. Inicializa o sistema dos Nós (Info / Next)
class ItemLista: # Representa cada item de uma lista encadeada (Os dados[data] e o endereço do proximo item.)

    def __init__(self, data = 0, nextItem = None): # O método __init__ instancia / inicia a classe e determina dois
                                                   # atributos necessários: data (que armazena o dado que irá ser
                                                   # adicionado à lista) e nextItem (que armazena o próximo item na
                                                   # lista encadeada)
        self.data = data
        self.nextItem = nextItem

    def __repr__(self):                            # retorna uma string a cada objeto criado apresentando o item
                                                   # adicionado e o próximo item.

        return '%s => %s' % (self.data, self.nextItem)

class ListaEncadeada:   # Essa classe tem como função de criar o cabeçalho[endereço] da lista presente no nó.

    def __init__(self):
        self.head = None    # indica o primeiro item da lista. Cabeçalho está nulo.

    def __repr__(self):
        return "%s" % (self.head)

    def insere(lista, data):

        item = ItemLista(data)      # Cria um objeto para armazenar um novo item da lista
        item.nextItem = lista.head  # O head é apontado como próximo item
        lista.head = item           # O item atual se torna o head

        '''Observe que esse método chama a classe ItemLista enviando o dado como argumento e salvando os resultados 
        em uma variável denominada item. A seguir, o atributo nextItem receberá o valor contido no cabeçalho da lista 
        (head) e o cabeçalho da lista recebe o objeto atual. Isso indica que o objeto atual passa a ser o primeiro item 
        da lista.'''

    def busca(lista, valor):

        navegar = lista.head

        while navegar and navegar.data != valor:
            navegar = navegar.nextItem

        return navegar

    '''Aqui, a função recebe a lista e um valor que será usado na busca. Aqui coletaa o cabeçalho atual do arquivo e
        armazena na variável navegar. Essa variável é percorrida até se obter o valor None ou enquanto o valor presente 
        em data seja diferente do valor buscado. Se essas condições forem atendidas o objeto é retornado.'''

    def remove(self, valor):    # Remove o valor da lista encadeada.

        if self.head.data == valor:     # Verifica se o item se trata do Head.
            self.head = self.head.nextItem

        else:   # encontre a posição do elemento

            before = None
            navegar = self.head

            # Navegando pelo cabeçalho atual
            while navegar and navegar.data != valor:
                before = navegar
                navegar = navegar.nextItem

            if navegar:
                before.nextItem = navegar.nextItem

            else:
                before.nextItem = None

    '''O método recebe o valor que será removido e navega por toda a lista em busca do valor. Inicialmente, deve-se
       verificar se o valor buscado corresponde ao item do cabeçalho (remoção mais simples). Se não for o método deve 
       buscar o anterior e o próximo (baseado no head). Observe que o valor correspondente ao próximo item é alterado, 
       não sendo necessário assim alterar toda a lista, e sim apenas os itens anterior e posterior diretamente 
       envolvidos'''
