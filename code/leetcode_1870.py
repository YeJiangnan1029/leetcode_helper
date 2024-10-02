from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist)-1:
            return -1

        l, r = 1, int(1e7)
        while l<=r:
            k = (l+r)//2
            s = 0
            for d in dist[:-1]:
                s += (d+k-1)//k
            s += dist[-1]/k
            if s <= hour:
                r = k-1
                ans = k
            else:
                l = k+1
        return ans

dist = [1,3,2]
hour = 6
solution = Solution()
print(solution.minSpeedOnTime(dist, hour))