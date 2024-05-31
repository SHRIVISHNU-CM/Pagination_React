def quich_select(nums,k):
    left = 0
    right =len(nums) -1

    def partition(l,r):
        pivot = nums[r]
        i = l-1
        for j in range(l,r):
            if nums[j] <= pivot:
                i +=1
                nums[i], nums[j] = nums[j] , nums[i]

        nums[i+1] , nums[r] = nums[r] , nums[i+1]
        return i+1
    
    while True:
        pivot_index = partition(left,right)

        if pivot_index == k -1:
            return nums[pivot_index]
        elif pivot_index < k-1:
            left = pivot_index +1

        else:
            right = pivot_index -1

num = [1,5,12,2,11,5]
k = 3
res = quich_select(num,k)
print(res)