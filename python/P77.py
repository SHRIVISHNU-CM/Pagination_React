def find_third(arr):
    if len(arr) < 3:
        return None
    
    first = max(arr[0] , arr[1])
    second = max(arr[0] , arr[1])

    for num in arr[2:]:
        if num >first:
            first, second , num= num,first,second
        elif num >second:
            second , num = num ,second
    
    if len(arr) == 2:
        return second
    else:
        return min(first,second)
    
my_arr = [10,5,8,20,15,12,3]
print(find_third(my_arr))