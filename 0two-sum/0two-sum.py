class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in ans:
                res.append(ans[target-nums[i]])
                res.append(i)
            ans[nums[i]] = i 
        if len(res) == 0:
            return [-1,-1]
        return res
        
        