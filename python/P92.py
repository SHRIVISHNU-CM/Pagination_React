def count(arr,n):
    visted = [False for i in range(n)]

    for i in range(n):
        if (visted[i] == True):
            continue

        count = 1

        for j in range(i+1,n):
            if arr[i]== arr[j]:
                visted[j] = True
                count +=1
        if count == 1:
            print(arr[i])
arr = [10, 30, 40, 20, 10, 20, 50, 10]
n = len(arr)
count(arr, n)