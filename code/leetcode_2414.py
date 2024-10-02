from collections import deque


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        last_t = ""
        i = 0
        ret = 0
        streak = 0
        while i < len(s):
            t = s[i]
            if last_t and ord(t) - ord(last_t) == 1:
                last_t = t
                streak +=1               
            else:
                last_t = t
                streak = 1
            ret = max(ret, streak)
            i += 1
        return ret

                    






so = Solution()
s = "abacaba"
print(so.longestContinuousSubstring(s))
