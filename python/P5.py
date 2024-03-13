def rotatearr(arr,k):
    n = len(arr)
    rotated_arr = [0] *N
    for i in range(n):
        rotated_arr[(i+k)%n] = arr[i]
    return rotated_arr


a = int(input())
N,K = map(int,input().split())
arr = list(map(int,input().split()))

for _ in range(K):
    arr  = rotatearr(arr,a)

print(arr)