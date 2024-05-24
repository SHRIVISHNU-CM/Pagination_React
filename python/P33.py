def word_break(s,wordDict):
    n = len(s)
    dp = [False] *(n+1)
    dp[0] = True

    for i in range(1,n+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[n]

s ="leetcode"

wordDict= ["leet", "code"]
print(word_break(s,wordDict))

s = "applepenapple"
wordDict = ["apple", "pen"]
print(word_break(s, wordDict)) 