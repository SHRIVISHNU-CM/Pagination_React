def maxSubarr(nums):
    max_so_far = nums[0]
    max_ending = nums[0]

    for i in range(1,len(nums)):
        max_ending = max(nums[i], max_ending + nums[i])


        max_so_far = max(max_so_far,max_ending)

    return max_so_far

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarr(nums))