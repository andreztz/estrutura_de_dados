'''
Deque (pronuncia-se "deck")

Deque é um acrônimo de double-ended queue. Trata-se de uma fila
onde você pode inserir e remover das duas pontas.

'''



class Deque:
    def __init__(self):
        '''
        Inicializa o deque com uma fila
        Inicializa uma variável para o controle do tamanho do deque
        '''
        self.deque = []        
        self.len = 0

    def empty(self):
        '''
        Retorna o tamanho do deque
        '''
        if self.len == 0:
            return True
        return False

    def push_front(self, e):
        '''
        Inserir o elemento no inicio
        '''
        self.deque.insert(0, e)
        self.len += 1

    def push_back(self, e):
        '''
        Insere o elemento no final
        '''
        self.deque.insert(self.len, e)
        self.len += 1

    def pop_front(self):
        '''
        Remove o elemento do inicio
        '''
        if not self.empty():
            self.deque.pop(0)
            self.len -= 1

    def pop_back(self):
        '''
        Remove o elemento do final
        '''
        if not self.empty():
            self.deque.pop(self.len - 1)
            self.len -= 1
    def front(self):
        '''
        Retorna o primeiro elemento
        '''
        if not self.empty():
            return self.deque[0]
    def back(self):
        '''
        Retorna o ultimo elemento
        '''
        if not self.empty():
            return self.deque[-1]
    def show(self):
        for i in self.deque:
            print(i, end=' ')
        
if __name__ == '__main__':
    d = Deque()
    print(d.empty())
    # teste inserção
    d.push_front(10)
    d.push_front(5)
    d.push_back(20)
    d.push_front(7)
    d.push_back(40)
    d.show()
    print('\nfront: {}'.format(d.front()))
    print('back: {}'.format(d.back()))
    print(d.empty())
    # teste remoção
    d.pop_back() 
    d.pop_front()
    d.show()
