def find_pair(nums,k):
    left = 0
    right = len(nums) -1

    while left<right:
        current_sum = nums[left] +nums[right]

        if current_sum == k:
            return [left ,right]
        elif current_sum <k:
            left +=1
        else:
            right -=1
    
    return[-1,-1]


arr = [1,2,3,4,6]
target = 9

res =find_pair(arr,target)
print(res)