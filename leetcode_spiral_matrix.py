##https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix):
        m, n = len (matrix), len(matrix[0])
        ##NOTE: Be very clear about the definitions here. The indexes are ones we "end at".
        ## The index adjustment will be greatly affected by these
        left, right, top, bottom = 0, n-1, 0, m-1
        result = []
        while top <= bottom or left <= right:
            ##move right
            if top <= bottom:
                for c in range (left, right+1):
                    result.append(matrix[top][c])
                top = top + 1
            ##move down
            if left <= right:
                for r in range (top, bottom+1):
                    result.append(matrix[r][right])
                right = right-1
            #move left
            ##NOTE: In range, the iterator doesn't automatically infer -1 if arg1 > arg2. Need to mention it.
            if top <= bottom:
                for c in range(right, left-1, -1):
                    result.append(matrix[bottom][c])
                bottom = bottom - 1
            #move upward
            if left <= right:
                for r in range(bottom, top-1, -1):
                    result.append(matrix[r][left])
                left = left + 1
        return result


s = Solution()
t1 = [[1,2,3],[4,5,6],[7,8,9]]
t2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
t3 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
t4 = [[13]]
t5 = [[6,9,7]]
t6 = [[6],[7],[8]]

assert s.spiralOrder(t6) == [6,7,8]
assert s.spiralOrder(t5) == [6,9,7]
assert s.spiralOrder(t4) == [13]
assert s.spiralOrder(t1) == [1,2,3,6,9,8,7,4,5]
assert s.spiralOrder(t2) == [1,2,3,4,8,12,11,10,9,5,6,7]
assert s.spiralOrder(t3) == [1,2,3,4,5,10,15,20,25,24,23,22,21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]

print ('All test cases passed')