class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        ans = 0
        for i in range(len(piles) // 2):
            check = max(piles)
            ans += check
            piles.remove(check)
        if ans > (sum(piles) - ans):
            return True
        return False
        