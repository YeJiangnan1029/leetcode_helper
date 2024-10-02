from functools import cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        max_l = 1
        max_i = 0
        for j in range(len(s)):
            dp[j][j] = 1
        for i in range(2, len(s)+1):
            for j in range(len(s)-i+1):
                if s[j] == s[j+i-1] and dp[j+1][j+i-2] == i-2:
                    dp[j][j+i-1] = i
                    if dp[j][j+i-1] > max_l:
                        max_l = dp[j][j+i-1]
                        max_i = j
                elif dp[j+1][j+i-1] > dp[j][j+i-2]:
                    dp[j][j+i-1] = dp[j+1][j+i-1]
                else:
                    dp[j][j+i-1] = dp[j][j+i-2]
                    
                if dp[j][j+i-1]>max_l:
                    max_l = dp[j][j+i-1]
                    max_i = j+1
        return s[max_i:max_i+max_l]

s = "cbabc"
solution = Solution()
print(solution.longestPalindrome(s))