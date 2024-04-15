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

str = 'abcd$dcba'
str2 = 'abca$abca'

def checker(str):
    st = LinkedStack()
    idx = 0

    ## push all elements before '$'
    for ch in str:
        if ch == '$':
            break
        
        st.push(ch)
        idx += 1

    if idx != (len(str) - 1) / 2:
        return False

    for i in range(idx + 1, len(str)):

        if st.pop() != str[i]:
            return False
    
    return st.isEmpty()

print(checker(str))
print(checker(str2))