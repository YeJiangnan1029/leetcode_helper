from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        cur_end = -1
        ret_list = []
        for l, r in intervals:
            if l > cur_end:
                ret_list.append([l, r])
                cur_end = r
            else:
                if r > ret_list[-1][1]:
                    ret_list[-1][1] = r
                    cur_end = r
        return ret_list


intervals = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
print(s.merge(intervals))