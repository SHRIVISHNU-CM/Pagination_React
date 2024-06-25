def missing (arr):
    n = len(arr)
    s = n * (n+1) //2

    return s - sum(arr)

arr = [3,0,1]
b = [0,1,2,3,4,5,6,7,9]
print(missing(arr=arr))
print(missing(b))