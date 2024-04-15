class LinkedStack:
    def __init__(self):
        self.__stack = []
    
    def push(self, x):
        self.__stack.append(x)
    
    def pop(self):
        return self.__stack.pop()

    def top(self):
        if self.isEmpty():
            print("No element in stack")
            return None
        else:
            return self.__stack[-1]
    
    def isEmpty(self) -> bool:
        return not bool(self.__stack)
        #return len(self.__stack) == 0

    def popAll(self):
        self.__stack.clear()
    
    def printStack(self):
        print("Stack: ")
        for i in range(len(self.__stack)):
            print('stack[', i, ']', self.__stack[i])

str = '((hello))'
str2 = '(((hello))'

def parenBalance(str) -> bool:
    st = LinkedStack()
    idx = 0

    ## push all elements before '$'
    for ch in str:
        if ch == '(':
            st.push(ch)
        elif ch == ')':
            if st.isEmpty() == False:
                st.pop()
            else:
                return False
    
    return st.isEmpty()

print(parenBalance(str))
print(parenBalance(str2))