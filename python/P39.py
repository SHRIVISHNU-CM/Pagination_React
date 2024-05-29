def four_sum(nums ,target):
    nums.sort()
    n = len(nums)
    result =[]

    for i in range(n -3):
        if i >0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1 , n-2):
            if j >i+1 and nums[j] == nums[j-1]:
                continue

            left = j+1
            right = n-1

            while left<right:
                total = nums[i] + nums[j] + nums[left] +nums[right]

                if left <target:
                    left +=1
                elif total > target:
                    right -=1
                else:
                    result.append([nums[i],nums[j],nums[left],nums[right]])

                    while left<right and nums[left] == nums[left+1]:
                        left +=1
                    while left <right and nums[right] == nums[right-1]:
                        right -=1
                    
                    left +=1
                    right -=1
    
    return result

num =[4,1,2,-1,1,-3]
k= 1
res = four_sum(num,k)
print(res)