'''
Fila (=queue)

FIFO (=First_In-First_Out) significa primeiro a entrar, primeiro a sair.
É uma estrura de dados implementada para gerar fila de espera. Em uma fila
do tipo FIFO os elementos vão sendo colocadosna fila e retirados (ou processados)
por ordem de chegada. A idéia fundamental da fila é que só podemos inserir um
novo elemento no final da fila e só podemos retirar o elemento do início.

Como exemplo de aplicação para filas, pode-se citar a fila de processos de um
sistema operacional. Nela, é estabelecido um tempo t a ser usado por cada um
dos processos. Se durante a execução de um processo o tempo passa de 0 a t,
este é posto na fila e o processo seguinte é executado. Se o processo seguinte
não terminar de ser executado no tempo t, ele é posto na fila e o processo
subsequente é executado, e assim por diante até todos os processos serem
executados.

'''


class Queue:
    
    def __init__(self):
        '''
        Inicializa uma lista e uma variavel que
        controla o tamanho da fila.
        '''
        self.queue = []
        self.len_queue = 0

    def push(self, e):
        '''
        Insere um elemento no fim da fila
        '''
        self.queue.append(e)
        self.len_queue += 1

    def pop(self):
        '''
        Remove um elemento do inicio da fila
        '''
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1

    def empty(self):
        '''
        Verifica se a fila não é vazia
        '''
        if self.len_queue == 0:
            return True
        return False

    def length(self):
        '''
        Retorna o tamanho da fila
        '''
        return self.len_queue

    def front(self):
        '''
        Retorna o primeiro elemento da fila se não for vazia
        '''
        if not self.empty():
            return self.queue[0]
        return None

if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.front())
