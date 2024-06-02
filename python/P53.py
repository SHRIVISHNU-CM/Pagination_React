def longestConse(arr):
    s = set(arr)
    longest = 0
    for num in s:
        if num -1 not in s:
            curr =1
            while num +1 in s:
                curr +=1
                num +=1
            longest = max(longest,curr)
    return longest


arr = [100,4,200,1,3,2,5]

res = longestConse(arr)

print(res)
