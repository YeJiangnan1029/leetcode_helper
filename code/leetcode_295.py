import heapq


class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.big):
            # 插入到small
            if not self.small or num <= self.big[0]:
                heapq.heappush(self.small, -num)
            else:
                x = heapq.heappop(self.big)
                heapq.heappush(self.small, -x)
                heapq.heappush(self.big, num)
        else:
            # 插入到big
            if num >= -self.small[0]:
                heapq.heappush(self.big, num)
            else:
                x = -heapq.heappop(self.small)
                heapq.heappush(self.big, x)
                heapq.heappush(self.small, -num)
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.big):
            return (-self.small[0]+self.big[0])/2
        else:
            return -self.small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
mf = MedianFinder()
print(mf.addNum(40))
print(mf.findMedian())
print(mf.addNum(12))
print(mf.findMedian())
print(mf.addNum(16))
print(mf.findMedian())
print(mf.addNum(14))
print(mf.findMedian())
print(mf.addNum(35))
print(mf.findMedian())
