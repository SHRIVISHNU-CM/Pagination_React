def addNum(arr):
    if len(arr) <=2:
        return
    
    s = []
    count = 0
    for num in arr:
        count +=num
        s.append(count)
    return s 

arr = [1,2,3,4]
res = addNum(arr=arr)
print(res)
