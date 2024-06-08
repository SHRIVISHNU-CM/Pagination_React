def FindMaxArr(arr):
    if not  arr:
        print("the array is empty")

    max_num = max(arr)
    max_index = arr.index(max_num)

    print (max_num)
    print(max_index)

FindMaxArr([10, 15, 78, 96, 17, 20, 65, 14, 36, 18, 20])
