class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        sum = [1] * n
        for i in range(m-1):
            for j in range(n):
                if j > 0:
                    sum[j] += sum[j-1]
        return sum[-1]

m = 3
n = 2
solution = Solution()
print(solution.uniquePaths(m, n))