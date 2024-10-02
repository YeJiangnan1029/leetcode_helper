from collections import defaultdict


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        dp = defaultdict(int)
        ret = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    j = stack.pop()
                    dp[len(stack)] += i-j+1
                    ret = max(ret, dp[len(stack)])
                    dp[len(stack)+1] = 0
                else:
                    dp[0] = 0
        return ret


s = "(()))())"
solution = Solution()
print(solution.longestValidParentheses(s))