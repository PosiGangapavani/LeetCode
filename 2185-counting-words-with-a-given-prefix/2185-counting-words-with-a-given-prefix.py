class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in words:
            if pref in i[:len(pref)]:
                count += 1
        return count
        