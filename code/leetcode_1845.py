class SeatManager:

    def __init__(self, n: int):
        self.N = n
        self.sum = [0] * (4*n)

    def add(self, o, l, r, i, val):
        if l==r:
            self.sum[o] += val
            return
        mid = (l+r)//2
        if i<=mid:
            self.add(o*2, l, mid, i, val)
        else:
            self.add(o*2+1, mid+1, r, i, val)
        self.sum[o] = self.sum[o*2] + self.sum[o*2+1]
    
    def query_sum(self, o, l, r, L, R):
        if L<=l and r<=R:
            return self.sum[o]
        mid = (l+r)//2
        _sum = 0
        if mid >= L:
            _sum += self.query_sum(o*2, l, mid, L, R)
        if mid < R:
            _sum += self.query_sum(o*2+1, mid+1, r, L, R)
        return _sum

    def reserve(self) -> int:
        # 查询第一个sum下小于区间长度的下标
        l, r = 1, self.N
        while l<=r:
            mid = (l+r)//2
            if self.query_sum(1, 1, self.N, 1, mid) == mid:
                l = mid+1
            else:
                r = mid-1
        self.add(1, 1, self.N, l, 1)
        return l


    def unreserve(self, seatNumber: int) -> None:
        self.add(1, 1, self.N, seatNumber, -1)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

seatManager = SeatManager(5)
seatManager.reserve()
seatManager.reserve()
seatManager.unreserve(2)
seatManager.reserve()
seatManager.reserve()
seatManager.reserve()
seatManager.reserve()
seatManager.unreserve(5)