class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > prev:
                prev = nums[i]
        for i in range(len(nums)):
            if nums[i] == prev:
                return i
            
        