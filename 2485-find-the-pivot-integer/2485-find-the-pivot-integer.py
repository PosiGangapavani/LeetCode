class Solution:
    def pivotInteger(self, n: int) -> int:
        k = n * ( n + 1) // 2
        ans = int(math.sqrt(k))
        if ans * ans == k:
            return ans
        return -1