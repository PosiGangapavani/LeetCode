class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans1 = {}
        for i in list1:
            if i not in ans1:
                ans1[i] = 1
            else:
                ans1[i] += 1
        for i in list2:
            if i not in ans1:
                ans1[i] = 1
            else:
                ans1[i] += 1
        maxi = float('inf')
        res = []
        store = []
        for i in ans1.keys():
            if ans1[i] == 2:
                start = list1.index(i)
                end = list2.index(i)
                if start + end < maxi:
                    res.append(i)
                    store.append(start + end)
        res1 = []
        mini = min(store)
        for i in range(len(store)):
            if store[i] == mini:
                res1.append(res[i])
        return res1
            

                    
                    
                    
        
                    
                    
                    
                    
        