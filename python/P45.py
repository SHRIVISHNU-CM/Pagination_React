def search_sorted_arr(arr,key):
    left = 0
    right = len(arr) -1

    is_ascending = arr[0] <arr[right]
    while left <=right :
        mid = (left+right) //2
        if arr[mid] == key:
            return mid
        if is_ascending:
            if arr[mid] <key:
                left = mid+1
            else:
                right = mid-1
        else:
            if arr[mid] <key:
                right = mid-1
            else:
                left= mid+1
    return -1

num = [4,6,10]
res = search_sorted_arr(num,10)
print(res)
