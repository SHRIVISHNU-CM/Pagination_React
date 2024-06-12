def ChangeArr(input1):
    newArr = input1.copy()
    newArr.sort()

    for i in range(len(input1)):
        for j in range(len(newArr)):
            if input1[i] == newArr[j]:
                input1[i] = j +1
                break
    
arr = [100, 2, 70, 12 , 90]
ChangeArr(arr)
print(arr)
