#https://leetcode.com/problems/01-matrix/description/
from typing import List
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m==n==1:
            return [[0]] #because it is a given that at least one element is 0
        #initialize result to -1 because unknown
        result = []
        for _m in range (m):
            result.append([])
            for _n in range (n):
                result[_m].append(-1)
        #set the zeros
        queue = deque([])
        for _m in range(m):
            for _n in range(n):
                if mat[_m][_n] == 0:
                    result[_m][_n] = 0
                    queue.append((_m, _n))
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue:
            (row,col) = queue.popleft()
            current_distance = result[row][col]
            for d in directions:
                _row = row + d[0]
                _col = col + d[1]
                # can't go wrong with this condition, else will end up visiting same node multiple times
                if _row < m and _col < n and _row >=0 and _col >=0 and result[_row][_col] == -1:
                    queue.append((_row,_col))
                    result[_row][_col] = current_distance + 1

        return result
#test cases
s = Solution()
assert s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
assert s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]