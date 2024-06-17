def findMax(arr):
    max_ele = arr[0]
    for num in arr:
        if num >max_ele:
            max_ele = num
    return max_ele

arr = [5,3,9,1,98]

print(findMax(arr=arr))