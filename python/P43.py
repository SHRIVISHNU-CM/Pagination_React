def sortStack(stack):
    aux_stack = []

    while stack:
        temp = stack.pop()

        while aux_stack and aux_stack[-1] <temp:
            stack.append(aux_stack.pop())

        aux_stack.append(temp)

    
    while aux_stack:
        stack.append(aux_stack.pop())

    return stack


num = [34,3,31,98,92,23]

res= sortStack(num)
print(res)