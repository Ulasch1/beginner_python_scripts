def create_stack():
    stack = list()
    return stack

def isEmpty(stack: list) -> bool:
    return len(stack) == 0

def push(stack: list, item):
    stack.append(item)
    
def pop(stack:list):
    return stack.pop()



