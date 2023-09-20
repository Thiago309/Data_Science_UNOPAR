# 2º Processo da Lista Encadeada. Verifica se nosso script possui problemas de codificação.

import ListaEncadeada as le     # Observe que a importação do arquivo ListaEncadeada.py (não é necessário
                                # informar a extensão “.py”) e apliquei um apelido (le) para facilitar a chamada de
                                # métodos e classes desse módulo.

lista = le.ListaEncadeada()         # Criando o objeto
print("Conteúdo da lista: ", lista) # Neste momento a lista se encontra vazia. imprimir o conteúdo da variável
                                    # criada, você obterá a seguinte mensagem: Conteúdo da lista: None. Isso indica
                                    # que a lista encadeada foi corretamente criada e se encontra atualmente vazia
                                    # (None).

#Criando a Lista

le.ListaEncadeada.insere(lista, "abacate")
le.ListaEncadeada.insere(lista, "bola")
le.ListaEncadeada.insere(lista, "cachorro")
le.ListaEncadeada.insere(lista, "dado")
le.ListaEncadeada.insere(lista, "elefante")

print(lista)
# elefante => dado => cachorro => bola => abacate => None

#Buscando um elemento especifico na lista.
query = "cenoura"

item_buscado = le.ListaEncadeada.busca(lista, query)

if item_buscado:
    print("Elemento encontrado")

else:
    print("Elemento NÃO encontrado")


#le.ListaEncadeada.remove(lista, "cenoura")
#print(lista)