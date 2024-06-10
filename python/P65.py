num = int(input("enter number"))
temp = num

rev = 0
while num>0:
    remainder = num%10
    rev = (rev * 10) + remainder
    num = num //10

print("the given {} and reverse is {}" .format(temp,rev))