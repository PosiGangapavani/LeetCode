class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ans = "abcdefghijklmnopqrstuvwxyz"
        count = 0
        for i in list(set(sentence)):
            if i in ans:
                count += 1
        if count == len(ans):
            return True
        return False
            
        