def binary_Search(arr,t):
    left,right = 0 , len(arr) -1

    while (left <= right):
        mid = (left+right) //2

        if (arr[mid] == t ):
            return mid
        elif (arr[mid] <t):
            left = mid+1
        else:
            right = mid+1
    return -1



arr = [1,3,5,7,9,11,13]
t = 9
res = binary_Search(arr,t)

print("elemet is" , res)