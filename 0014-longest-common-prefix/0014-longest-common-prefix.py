class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(reverse = True)
        index = 0
        first_word = strs[0]
        last_word = strs[-1]
        while index < len(first_word) and index < len(last_word):
            if first_word[index] != last_word[index]:
                break
            index += 1
        return first_word[:index]
                    
                