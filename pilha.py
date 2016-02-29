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

Lembrar de uma pilha de pratos sujos que serão lavados.

'''


class Stack:

    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, elem):
        self.stack.append(elem) # metodo append do objeto lista do python por padrão ja insere o elemento no final da lista.
        self.len_stack += 1

    def pop(self):
        if not self.empty():
            self.stack.pop(self.len_stack - 1) # o metodo pop do objeto lista do python ja remove o ultimo elemento por padrão (sem parametros).
            self.len_stack -= 1

    def top(self):
        if not self.empty():
            return self.stack[-1] # retorna o elemento do top
        return None

    def empty(self):
        if self.len_stack == 0:
            return True
        return False
 
    def length(self):
        return self.len_stack


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.length())
    s.pop()
    print(s.top())
