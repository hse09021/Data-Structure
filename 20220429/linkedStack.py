from circularDoublyLinkedList import CircularDoublyLinkedList

class LinkedStack:
    def __init__(self):
        self.__stack = CircularDoublyLinkedList()
    
    def push(self, x):
        self.__stack.append(x)
    
    def pop(self):
        return self.__stack.pop(0)

    def top(self):
        if self.isEmpty():
            print("No element in stack")
            return None
        else:
            return self.__stack.get(0)
    
    def isEmpty(self) -> bool:
        return self.__stack.isEmpty()

    def popAll(self):
        self.__stack.clear()
    
    def printStack(self):
        print("Stack from top: ", end = ' ')
        for i in range(self.__stack.size()):
            print(self.__stack.get(i), end = ' ')
        print()