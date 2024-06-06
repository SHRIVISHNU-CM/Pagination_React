def findElements(arr,n):
    for i in range(n):
        count = 0
        for j in range(0,n):
            if arr[j] > arr[i]:
                count = count+1

        if count >= 2:
            print(arr[i], end=" ")

arr = [2,-6,3,5,1,4,6]
n  =  len(arr)

findElements(arr , n)

