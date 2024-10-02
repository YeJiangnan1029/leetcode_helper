from functools import cache
import math


class Solution:
    def numSquares(self, n: int) -> int:
        sqr = [i**2 for i in range(0, 101)]
        @cache
        def dp(n:int):
            if n<=1:
                return n
            ret = 10000
            i = 1
            while i**2 <= n:
                ret = min(ret, dp(n-sqr[i])+1)
                i+=1
            return ret
        return dp(n)

n = 12
solution = Solution()
print(solution.numSquares(n))