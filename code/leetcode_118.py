from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        if numRows==1:
            return ret
        last = [1]
        for _ in range(1, numRows):
            cur = []
            last.append(0)
            for j in range(len(last)):
                cur.append(last[j-1]+last[j])
            ret.append(cur)
            last = cur.copy()
        return ret

numRows = 5
solution = Solution()
print(solution.generate(numRows))