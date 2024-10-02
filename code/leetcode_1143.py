from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] 表示text1以i结尾和text2以j结尾的最长公共子序列长度
        @cache
        def dp(i, j):
            if i==0 or j==0:
                return 0
            if text1[i-1] == text2[j-1]:
                return dp(i-1, j-1)+1
            else:
                return max(dp(i-1, j), dp(i, j-1))
        return dp(len(text1), len(text2))

text1 = "abcde"
text2 = "ace"
solution = Solution()
print(solution.longestCommonSubsequence(text1, text2))