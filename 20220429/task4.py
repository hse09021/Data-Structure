from linkedQueue import LinkedQueue

class TwoQueueStack:
    def __init__(self):
        self.__q = LinkedQueue()
        self.__tq = LinkedQueue()
    
    def push(self, x):
        self.__tq.enqueue(x)
    
    def pop(self):
        front = None
        while not self.__tq.isEmpty():
            front = self.__tq.dequeue()
            if not self.__tq.isEmpty():
                self.__q.enqueue(front)
        self.__q, self.__tq = self.__tq, self.__q

        return front


if __name__ == "__main__":
    st = TwoQueueStack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop())
    print(st.pop())
    print(st.pop())