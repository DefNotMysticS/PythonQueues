# test_queue.py
from structures import Node
from structures import Queue  # supongamos que tu Queue está en queue_module.py

def main():
    q = Queue()

    # Probamos push
    q.push(10)
    q.push(20)
    q.push(30)

    # Probamos peek
    print("Peek:", q.peek())  # → 10

    # Probamos pull
    print("Pull:", q.pull())  # → 10
    print("Peek después de pull:", q.peek())  # → 20

    # Probamos isEmpty
    print("Está vacía?", q.isEmpty())  

    # Vaciamos la cola
    q.pull()
    q.pull()
    print("Está vacía después de vaciarla?", q.isEmpty())  # → True

if __name__ == "__main__":
    main()
