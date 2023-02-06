class Solution:
    def digitCount(self, num: str) -> bool:
        count = 0
        for i in range(0 , len(num)):
            if int(num[i]) == num.count(str(i)):
                count += 1
        if count == len(num):
            return True
        return False
        