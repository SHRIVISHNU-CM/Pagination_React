string1 = input("enter 1st string")
string2 = input("enter 2nd string")

if len(string1) != len(string2):
    print("string not anagram")
else:
    string1 = sorted(string1)
    string2 = sorted(string2)

if string1 == string2:
    print("string are anagram")
else:
    print("strings are not anagram")