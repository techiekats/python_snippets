#https://leetcode.com/problems/word-search/description/
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # intuition for backtracking: need to explore all paths
        m, n = len(board), len(board[0])

        def dfs(path: str, index: (int, int)):
            # BUG 1: these 4 lines after base case len(path) == len(word): introduced bug wherein last cell along a path was never visited
            (_m, _n) = index
            temp = board[_m][_n]
            board[_m][_n] = '#'
            path = f'{path}{temp}'

            if len(path) == len(word):
                # not setting back to temp caused bugs when False was returned
                board[_m][_n] = temp
                return path == word

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in directions:
                (next_m, next_n) = (_m + d[0], _n + d[1])
                if next_m >= 0 and next_m < m and next_n >= 0 and next_n < n:
                    if board[next_m][next_n] != '#':
                        exists = dfs(path, (next_m, next_n))
                        if exists:
                            return True
            # reset here, very important
            board[_m][_n] = temp

        for _m in range(m):
            for _n in range(n):
                # very important to tecnique: REDUCE SEARCH SPACE. In recursion, even for 3x3 grids, there are exponential combinations
                if board[_m][_n] == word[0]:
                    if dfs('', (_m, _n)):
                        return True
        return False

#test cases
s = Solution()
assert s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True
assert s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE") == True
assert s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") == False