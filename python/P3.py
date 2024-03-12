


n = int(input())
data = [int(x) for x in input().split()]

for i in range(n):
    last = data[i]%10
    
    if (last % 10 == 0):
        print("Yes")
    else:
        print("No")