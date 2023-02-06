class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = {}
        for i in range(len(arr)):
            if arr[i] in ans:
                ans[arr[i]] += 1
            else:
                ans[arr[i]] = 1
        res = []
        #print(ans)
        for i in ans.keys():
            if ans[i] == 1:
                res.append(i)
        if len(res) > k -1:
            return res[k-1]
        return ""
               
            