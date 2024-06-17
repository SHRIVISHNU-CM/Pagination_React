def rightRotate(arr,num):
    output = []

    for i in range(len(arr)-num,len(arr)):
        output.append(arr[i])
    for item in range(0,len(arr)-num):
        output.append(arr[item])

    return output

rotate = 3
arr = [1,2,3,4,5,6]

print(rightRotate(arr,rotate))