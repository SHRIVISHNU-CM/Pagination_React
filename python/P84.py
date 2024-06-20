def max_subarray(arr):
    max_sum = float("-inf")
    current_Sum = 0

    for num in arr:
        current_Sum = max(num,current_Sum+num)

        max_sum = max(max_sum,current_Sum)

    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]

print(max_subarray(arr))