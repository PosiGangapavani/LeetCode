class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp = nums
        #ans = -1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n :
                nums[i] = n + 100
        for i in range(n):
            ele = abs(nums[i])
            if ele == n + 100 or nums[ele - 1] < 0:
                continue
            nums[ele-1] = -1 * abs(nums[ele-1])
        #print(nums)
        for i in range(n):
            if nums[i] >= 0:
                return  i + 1
                
        return n + 1
            