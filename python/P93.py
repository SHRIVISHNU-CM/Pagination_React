def operationBinaryString(string):
    a = int(string[0])
    i=1
    while i <len(string):
        if string[i] == "A":
            a &= int(string[i+1])
        elif string[i] == 'B':
            a |= int(string[i+1])
        else:
            a ^= int(string[i+1])
        i +=2

    return a

string = "1C0C1C1A0B1"
print(operationBinaryString(string))