class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j or i + j == len(mat) - 1 :
                    sums += mat[i][j]
        return sums
        