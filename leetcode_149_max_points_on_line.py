#https://leetcode.com/problems/max-points-on-a-line/description/
from typing import List
from itertools import combinations
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <=2:
            return len(points) #technically speaking, we need minimum two points to form a line so this is not accurate but that's expected answer on leetcode for just one point

        combos = combinations (points, 2)
        slopes = {}
        ##REMEMBER: an edge case. there can be multiple lines parallel to y-axis. the design decision here is which key should be used? For each of lines, the x-coordinate is distinct
        infinite_slopes = {}
        for c in combos:
            #edge case : slope is infinite
            p1, p2 = c[0], c[1]
            if p1[0] == p2[0]:
                if p1[0] not in infinite_slopes:
                    infinite_slopes[p1[0]] = set()
                #NOTE: no need to add both x and y co-ordinates in this case
                infinite_slopes[p1[0]].add(p1[1])
                infinite_slopes[p1[0]].add(p2[1])
            else:
                ##TODO: the same edge case of infinite lines applies for regular slopes as well. in y = mx + c, if the c is different, the points are not collinear. Need a sub-key of y intercept
                slope = (p1[1] - p2[1]) / (p1[0] - p2[0])
                if slope not in slopes:
                    slopes[slope] = set()
                ##NOTE: need to convert to tuple before adding to set because list is not hashable
                slopes[slope].add((p1[0], p1[1]))
                slopes[slope].add((p2[0], p2[1]))

        max_points = 0
        for k in slopes:
            if len(slopes[k]) > max_points:
                max_points = len(slopes[k])
        for k in infinite_slopes:
            if len(infinite_slopes[k]) > max_points:
                max_points = len(infinite_slopes[k])
        return max_points

s = Solution()
assert s.maxPoints([[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]) == 5
assert s.maxPoints([[3,3],[1,4],[1,1],[2,1],[2,2]]) == 3
assert s.maxPoints([[1,1],[2,2],[3,3]]) == 3
assert s.maxPoints([[1,1],[2,2]]) == 2
assert s.maxPoints([[3,3]]) == 1
assert s.maxPoints ([[1,4], [3,8], [5,90]]) == 2
assert s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4
assert s.maxPoints([[1,1],[1,2],[1,3],[1,4],[2,3],[1,7]]) == 5
assert s.maxPoints([[1,1],[3,3],[5,3],[4,3],[2,3],[-1,3]]) == 5
