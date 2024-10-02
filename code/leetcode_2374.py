from typing import List

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score = [0] * len(edges)
        for i in range(len(edges)):
            score[edges[i]] += i
        max_score = -1
        max_i = -1
        for i in range(len(edges)):
            if score[i] > max_score:
                max_score = score[i]
                max_i = i
        return max_i

edges = [1,0,0,0,0,7,7,5]
solution = Solution()
print(solution.edgeScore(edges))