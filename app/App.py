# test_queue.py
from structures.Node import Node
from structures.Queue import Queue  # supongamos que tu Queue está en queue_module.py

def main():

    q = Queue()
    q.push(10)
    q.push(20)
    q.push(30)
    print("Peek:" + str(q.peek()))  # Debe mostrar 10
    print("Pull:" + str(q.pull()))  # Debe mostrar 10
    print("Peek:" + str(q.peek()))  # Debe mostrar 20
    print(q.isEmpty())
    while q.top is not None:
        q.pull()
    print(q.isEmpty())

if __name__ == "__main__":
    main()
