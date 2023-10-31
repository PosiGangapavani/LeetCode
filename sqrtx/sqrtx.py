class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x 
        while low <= high:
            mid = (low + high) // 2
            if mid  == x // mid:
                return mid 
            elif mid  < x // mid:
                low = mid + 1
            elif mid > x // mid:
                high = mid - 1
        return high
        