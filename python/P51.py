def perfect_square(num):
    left = 1
    right = num

    while left <= right:
        mid = left+(right-left) //2
        mid_square = mid*mid

        if mid_square == num:
            return True
        elif mid_square <num:
            left = mid +1
        else:
            right = mid -1
    return  False

print(perfect_square(49))