from collections import defaultdict
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        if tickets[k] == 1:
            return k+1
        fre = [0] * 101
        repeat = 0
        for i in range(len(tickets)):
            if i<=k and tickets[i] >= tickets[k]:
                repeat += 1
            fre[tickets[i]] += 1
        # 后缀和 fre[i]表示大于等于i总共有多少人
        for i in range(1, len(fre)):
            fre[len(fre)-i-1] += fre[len(fre)-i]
        t = 0
        for i in range(1, tickets[k]):
            t += fre[i]
        t += repeat
        return t



tickets = [5,1,1,1]
k = 3
solution = Solution()
print(solution.timeRequiredToBuy(tickets, k))