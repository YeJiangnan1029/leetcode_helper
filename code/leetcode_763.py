from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        fre = defaultdict(int)
        for t in s:
            fre[t] += 1
        
        seg = []
        ret = []
        cur_fre = defaultdict(int)
        for i in range(len(s)):
            cur_fre[s[i]] += 1
            complete = True
            for k in cur_fre:
                if cur_fre[k] != fre[k]:
                    complete = False
                    break
            if complete:
                seg.append(i)
                if len(seg)==1:
                    ret.append(i+1)
                else:
                    ret.append(i-seg[-2])
                cur_fre = defaultdict(int)
        
        return ret

s = "eccbbbbdec"
solution = Solution()
print(solution.partitionLabels(s))