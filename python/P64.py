def groupAnagram(strs):
    ans ={}

    for s in strs:
        s_sorted = sorted(s)
        kry = tuple(s_sorted)

        if kry not in ans:
            ans[kry] = [s]
        else:
            ans[kry].append(s)

    return ans.values()

strs = ["eat","tan","ate","nat","bat"]

res=groupAnagram(strs)
print(res)