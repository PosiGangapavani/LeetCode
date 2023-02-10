class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = [str(x) for x in str(num)]
        maximum_so_far = 0
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = '9'
            if int("".join(nums)) > maximum_so_far:
                maximum_so_far = int("".join(nums))
            nums[i] = temp
                
        #print(ans)
        return maximum_so_far
        