def sum_diff (m,n):
    sum_divisible = sum(i for i in range(1,n+1) if i %m == 0)
    sum_not_divisible = sum(i for i in range(1,n+1) if i%m != 0)
    print(sum_divisible)
    diff = sum_not_divisible - sum_divisible
    return diff

print(sum_diff(6,30))
