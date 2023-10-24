class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        for i in nums:
            if i in ans:
                
                return True 
            if i not in ans:
                ans.add(i)
            
        return False
            
        