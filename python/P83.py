def findMissing(arr,n):
    total = (n*(n+1))//2
    arrsum = sum(arr)

    return total-arrsum

print(findMissing([1,2,3,5],5))