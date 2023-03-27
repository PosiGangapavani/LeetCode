class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_so_far = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                max_so_far = max(max_so_far,count)
            else:
                count = 0
        max_so_far = max(max_so_far,count)
        return max_so_far
        