def sortNumber(nums):
    low = 0 
    mid = 0
    high = len(nums) -1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid] , nums[low] = nums[low] , nums[mid]
            low +=1
            mid +=1
        elif nums[mid] ==1:
            mid +=1
        else:
            nums[mid], nums[high] = nums[high] , nums[mid]
            high -=1
    
    return nums

num = [1,0,2,1,0]
res = sortNumber(num)
print(res)
