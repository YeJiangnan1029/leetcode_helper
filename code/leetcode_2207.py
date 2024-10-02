class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        _sum1 = 0
        _sum2 = 0
        cnt1 = 0
        cnt2 = 0
        for i in range(len(text)):
            if text[len(text)-i-1] == pattern[0]:
                _sum1 += cnt1
            if text[len(text)-i-1] == pattern[1]:
                cnt1 += 1
            if text[i] == pattern[1]:
                _sum2 += cnt2
            if text[i] == pattern[0]:
                cnt2 += 1
            
        return max(_sum1+cnt1, _sum2+cnt2)

text = "tttctt"
pattern = "tc"
solution = Solution()
print(solution.maximumSubsequenceCount(text, pattern))