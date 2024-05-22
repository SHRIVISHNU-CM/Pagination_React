def twoSum(nums,target):
    complement_dict = {}

    for i, num in enumerate(nums):
        if target - num in complement_dict:

            return[complement_dict[target-num],i]
        
        complement_dict[num] = i

    return []

arr = [3,3]
target = 6

res = twoSum(arr,target)

print(res)