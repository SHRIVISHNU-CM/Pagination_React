##Kth smallest element

def find_kth_smallest_number(arr, k):
    unique_nums = set(arr)

    num =1
    while k>0:
        if num in unique_nums:
            num +=1
        else:
            k -=1
            num +=1

    return num -1


if __name__ == "__main__":
    arr = [1,3]
    k =4

    kth_smallest = find_kth_smallest_number(arr,k)
    print(kth_smallest)