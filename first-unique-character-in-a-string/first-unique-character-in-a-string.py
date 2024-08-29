class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = {}
        for i in s:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        for i in ans.keys():
            if ans[i] == 1:
                index = s.find(i)
                return  index
        return -1
        