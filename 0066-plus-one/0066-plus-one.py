class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(x) for x in digits]
        check = int("".join(digits)) + 1
        return [int(x) for x in str(check)]
        