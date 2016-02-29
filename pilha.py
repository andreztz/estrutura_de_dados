'''
Pilha (=stack).

Uma pilha é uma estrutura de dados que admite inserção e remoção de elementos.
Regra de operação: sempre que houver uma remoção,o elemento removido é o que
está no topo da estrutura.

Em outras palavras, o primeiro objeto a ser inserido na pilha é o último a ser
removido. Essa política é conhecida pela sigla LIFO (= Last-In-First-Out).

São exemplos de uso de pilha em um sistema:

Funções recursivas em compiladores;
Mecanismo de desfazer/refazer dos editores de texto;
Navegação entre páginas Web;
etc.


'''


class Stack:


    def __init__(self):
        '''
        Inicializa a pilha (self.stack) com um objeto list do python
        e inicializa a variável (self.len_stack) que controla o estado
        da pilha quanto ao seu tamanho.
        '''
        self.stack = []
        self.len_stack = 0

    def push(self, elem):
        '''
        Insere um elemento na pilha.

        O método append do objeto lista do python por
        padrão insere o novo elemento no final da lista.
        '''
        self.stack.append(elem) #
        self.len_stack += 1

    def pop(self):
        '''
        Remove um elemento da pilha.
        
        O método pop do objeto lista do python por padrão
        remove o último elemento da lista.
        '''
        if not self.empty():
            self.stack.pop(self.len_stack - 1)
            self.len_stack -= 1

    def top(self):
        '''
        Retorna o elemento do topo da pilha.
        
        '''
        if not self.empty():
            return self.stack[-1] # retorna o elemento do top
        return None

    def empty(self):
        '''
        Verifica o estado da pilha (vazia ou não vazia).  
        '''
        if self.len_stack == 0:
            return True
        return False
 
    def length(self):
        '''
        Retorna o tamanho da pilha.  
        '''        
        return self.len_stack


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.length())
    s.pop()
    print(s.top())
