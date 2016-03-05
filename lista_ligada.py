'''
Lista Ligada ou Lista encadeada (linked list)

---------------- next   ---------------- next   ---------------- next
|  LinkedList  | ---->  |  LinkedList  | -----> |  LinkedList  | ----->
----------------        ----------------        ----------------
        |                       |                       |
      "Hello"                 "Stack"                 "Overflow"
'''

class Node:

    def __init__(self, label):
        self.label = label
        self.next = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):
        if index >= 0:
            # cria um novo nó
            node = Node(label)
            # verifica se a lista está vazia
            if self.empty():
                self.first = node
                self.last = node
            else:
                if index == 0:
                    # inserção no início
                    node.setNext(self.first)
                    self.first = node
                elif index >= self.len_list:
                    # inserção no final
                    self.last.setNext(node)
                    self.last = node
                else:
                    # inserção no meio
                    prev_node = self.first
                    curr_node = self.first.getNext()
                    curr_index = 1

                    while curr_node != None:
                        if curr_index == index:
                            # seta o curr_node como o próximo nó
                            node.setNext(curr_node)
                            # seta o node como o próximo do prev_node
                            prev_node.setNext(node)
                            break
                        prev_node = curr_node
                        curr_node =curr_node.getNext()
                        curr_index += 1
            # atualiza o tamanho da lista
            self.len_list += 1

    def pop(self, index):
        if not self.empty() and index >= 0 and index < self.len_list:
            flag_remove = False
            if self.first.getNext() == None:
                # possui apenas um elemento
                self.first = None
                self.last = None
                flag_remove =True

            elif index == 0:
                # remove do inicio mas possui mais de  1 elemento
                self.first = self.first.getNext()
                flag_remove = True
            else:
                '''
                    Se chuegou aqui é porque a lista possui mais
                    de 1 elemento e a remoção não é no início.
                '''
                prev_node = self.first
                curr_node = self.first.getNext()
                curr_index = 1

                while curr_node != None:

                    if index == curr_index:
                        # o próximo do anterior aponta para o próximo do nó corrente
                        prev_node.setNext(curr_node.getNext())
                        curr_node.setNext(None)
                        flag_remove = True
                        break
                    prev_node = curr_node
                    curr_node = curr_node.getNext()
                    curr_index += 1

            if flag_remove:
                # atualiza o tamanho da lista
                self.len_list -= 1
    def empty(self):
        if self.first == None:
            return True
        return False

    def length(self):
        return self.len_list

    def show(self):
        print('-' * 80 )
        curr_node = self.first

        while curr_node != None:
            print(curr_node.getLabel(), end=" ")
            curr_node = curr_node.getNext()
            print("")

def main():
    lista = LinkedList()
    #teste de inserção

    lista.push('Marcos', 0)
    lista.show()
    lista.push('Maria', 1)
    lista.show()
    lista.push('Yankee', 0)
    lista.show()
    lista.push('Catarina', 2)
    lista.show()
    lista.push('Lilica', 4)
    lista.show()
    lista.push('Sara', 2)
    lista.show()
    print('Tamanho da lista: {}'.format(lista.length()))
    # teste de remoção

    lista.pop(0)
    lista.show()
    lista.pop(2)
    lista.show()
    lista.pop(3)
    lista.show()
    print('Tamanho da lista: {}'.format(lista.length()))
if __name__ == '__main__':
    main()
