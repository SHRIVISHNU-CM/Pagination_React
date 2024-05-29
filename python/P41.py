def decimalBin(num):
    binary = ""

    while num>0:
        remainder = num%2
        binary =str(remainder) +binary
        num = num//2

    return binary

nums = 7
res= decimalBin(nums)
print(res)