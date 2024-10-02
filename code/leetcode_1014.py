from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # 遍历得到 max(max_[0, k)_{v+i} + max_[k, n)_{v-j})
        max_vp = values[0]
        max_score = -1
        for i in range(1, len(values)):
            if max_vp + values[i]-i > max_score:
                max_score = max_vp + values[i]-i
            if values[i]+i > max_vp:
                max_vp = values[i]+i
        return max_score



values = [2,7,7,2,1,7,10,4,3,3]
solution = Solution()
print(solution.maxScoreSightseeingPair(values))