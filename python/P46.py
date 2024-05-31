def singleNumber(nums):
    result = 0
    for i in nums:
        result ^= i
    return result

num = [1,4,2,1,3,2,3]
res = singleNumber(num)
print(res)