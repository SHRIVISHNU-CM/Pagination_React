# missing and repeating number

def CheckElement(arr):
    n = len(arr)
    temp = [0] *n
    repeatNumber = -1
    missingNUmber = -1

    for i in range(n):
        temp[arr[i] - 1] +=1
        if temp[arr[i] - 1] >1:
            repeatNumber = arr[i]
    for i in range(n):
        if temp[i] == 0:
            missingNUmber = i+1
            break
    
    print("repeatNumber", repeatNumber)
    print("misssing" , missingNUmber)


arr = [7,3,4,5,6,6,2,1]
CheckElement(arr)