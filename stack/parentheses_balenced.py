class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



def is_balanced_parentheses(parentheses):
    stack = Stack()
    
    if len(parentheses) == 0:
        return True
    
    stack.push(1)
    for char in parentheses:
        if char == "(":
            stack.push(char)
        elif char == ")":
            stack.pop()
            
    if stack.size() == 1 and stack.peek() == 1:
        return True
    else:
        return False
    
print(is_balanced_parentheses(")("))