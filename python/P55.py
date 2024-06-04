def find_missing_number(arr,n):
    sum_arr = sum(arr)
    
    total_summ = (n*(n+1))//2

    missing_number = total_summ - sum_arr
    
    

    return missing_number


arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
n = 10
res = find_missing_number(arr,n)
print(res)
