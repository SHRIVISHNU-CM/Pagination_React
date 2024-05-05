def find_lower_index(arr, x):
    low,high = 0 , len(arr) -1
    while low<=high:
        mid = (low+high) //2
        if(arr[mid] >=x):
            high = mid -1
        else:
            low = mid-1
    return low

def find_upper_index(arr,y):
    low, high  =0,len(arr) -1
    while low<=high:
        mid = (low+high) //2
        if(arr[mid] <=y):
            low = mid+1
        else:
            high = mid+1
    return high

def count_ele_in_range(arr,x,y):
    arr.sort()
    lower_index = find_lower_index(arr,x)
    upper_index = find_upper_index(arr, y )
    count = upper_index - lower_index +1
    return count



arr = [ 1,4,4,9,10,3]

lower_range = 1
upper_ramge = 4

print(count_ele_in_range(arr, lower_range, upper_ramge))

lower_range = 9
upper_ramge = 12
print(count_ele_in_range(arr,lower_range,upper_ramge))