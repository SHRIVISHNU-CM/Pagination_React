def productex(arr,n):
    result = [1] *n
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= arr[i]

    right_product = 1
    for i in range(n-1,-1,-1):
        result[i] *= right_product
        right_product *= arr[i]

    return result

nums1 = [10, 3, 5, 6, 2]
n1 = 5
print(productex(nums1,n1))