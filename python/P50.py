def two_sum(nums , target):
    num_dict ={}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        
        num_dict[num] = i


arr = [3,2,4]
k = 6
res = two_sum(arr,k)
print(res)