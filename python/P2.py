def wordCheck(n):
    count_zs = n.count('z')
    count_os = n.count('o')

    if count_zs * 2 == count_os:
        return "yes"
    else:
        return "no"



n =  input().strip().lower()
res = wordCheck(n)
print(res) 