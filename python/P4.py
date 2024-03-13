def rotationArray(arr,d):
    temp = []
    n = len(arr)
    for i in range(d,n):
        temp.append(arr[i])
    i = 0
    for i in range(0,d):
        temp.append(arr[i])
    return temp

arr = [1,2,3,4,5,6,7,8]
print("rotated array is")
res = rotationArray(arr,5)
print(res)
print(len(arr))