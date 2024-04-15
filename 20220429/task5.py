from linkedStack import LinkedStack

class TwoStackQueue:
    def __init__(self):
        self.__s = LinkedStack()
        self.__ts = LinkedStack()
    
    def enqueue(self, x):
        self.__s.push(x)

    def dequeue(self):
        if self.__ts.isEmpty():
            while not self.__s.isEmpty():
                self.__ts.push(self.__s.pop())

        return self.__ts.pop()

if __name__ == "__main__":
    st = TwoStackQueue()
    st.enqueue(1)
    st.enqueue(2)
    st.enqueue(3)
    print(st.dequeue())
    print(st.dequeue())
    print(st.dequeue())