from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start>destination:
            start, destination = destination, start
        
        dis1 = 0
        dis2 = 0
        for i, d in enumerate(distance):
            if i >= start and i < destination:
                dis1 += d
            else:
                dis2 += d
        return min(dis1, dis2)


s = Solution()
distance = [1,2,3,4]
start = 0
destination = 3

print(s.distanceBetweenBusStops(distance, start, destination))