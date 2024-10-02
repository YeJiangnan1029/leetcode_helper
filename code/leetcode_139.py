from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i:int):
            if i > len(s)-1:
                return True
            ans = False
            for w in wordDict:
                if s[i:].startswith(w):
                    ans = ans or dp(i+len(w))
            return ans
        return dp(0)


s = "leetcode"
wordDict = ["leet","code"]
solution = Solution()
print(solution.wordBreak(s, wordDict))