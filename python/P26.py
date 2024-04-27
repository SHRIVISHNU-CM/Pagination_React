def IsPalindrome(x):
    strx = str(x)

    return strx == strx[::-1]

print(IsPalindrome(121))
print(IsPalindrome(-121))
print(IsPalindrome(10))
