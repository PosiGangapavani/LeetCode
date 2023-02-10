class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = {}
        for i in nums:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        #print(ans)
        for i in ans:
            if ans[i] > (len(nums)//2):
                return i
            
                
        