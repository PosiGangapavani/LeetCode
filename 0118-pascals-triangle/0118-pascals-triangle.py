class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(1,numRows):
            rows = [1]
            for j in range(1,i):
                rows.append(triangle[i-1][j]+triangle[i-1][j-1])
            rows.append(1)
            triangle.append(rows)
        return triangle