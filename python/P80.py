def prefixToInfix(pre):
    stack = []
    i = len(pre) - 1
    while i >= 0:
        if not isOperator(pre[i]):
            stack.append(pre[i])
            i -=1
        else:
            str = "(" + stack.pop() + pre[i] + stack.pop() +")"
            stack.append(str)
            i -=1
    return stack.pop()
def isOperator(c):
    if c =="*" or c =="+" or c =="-" or c =="/" or c == "^" or c =="(" or c ==")":
        return True
    else:
        return False
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))
    
