from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        #各行の内容と出現回数を保存する
        row_count = Counter()

        for row in grid:
            row_count[tuple(row)] += 1
        
        pairs = 0

        #各列を作成して、同じ行が何個あるか調べる
        for col in range(n):
            column = tuple(grid[row][col] for row in range(n))
            pairs += row_count[column]
        
        return pairs       