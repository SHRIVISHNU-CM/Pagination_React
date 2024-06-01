def longestKSubStr (s,k):
    n = len(s)
    ans = -1

    for i in range(n):
        for j in range(i+1,n+1):
            dist = set(s[i:j])
            if len(dist) == k:
                ans = max(ans, j-i)

    return ans

s ="aabacbebebe"
k =3
print(longestKSubStr(s,k))