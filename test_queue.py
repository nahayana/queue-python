from queue import Queue

fila = Queue()

fila.enqueue(10)
fila.enqueue(20)

print(fila.size())

print(fila.peek())

print(fila.dequeue())

fila.clear()

print(fila.is_empty())

try:
    fila.dequeue()
except IndexError as erro:
    print(erro)

fila2 = Queue(max_size=2)

fila2.enqueue(1)
fila2.enqueue(2)

try:
    fila2.enqueue(3)
except OverflowError as erro:
    print(erro)

print("Testes finalizados.")
