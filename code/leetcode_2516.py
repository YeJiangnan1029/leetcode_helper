from collections import defaultdict


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        if 3*k > len(s):
            return -1
        N = len(s)
        fre = defaultdict(int)
        for t in s:
            fre[t] += 1
        def check(fre):
            for t in ['a', 'b', 'c']:
                if fre[t] < k:
                    return False
            return True
        if not check(fre):
            return -1
        fre = defaultdict(int)
        # find the most left j
        for j in range(N):
            t = s[N-j-1]
            fre[t] += 1
            if check(fre):
                break
        j = N-j-1
        ret = N - j
        i = 0
        while i <= j and j < N:
            fre[s[i]] += 1
            while j<N and fre[s[j]] > k:
                fre[s[j]] -= 1
                j += 1
            ret = min(ret, i+N-j+1)
            i+=1
        return ret

s = "bcca"
k = 1
solution = Solution()
print(solution.takeCharacters(s, k))