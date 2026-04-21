#https://leetcode.com/problems/car-fleet/description/
import heapq
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        if len(position) == 1:
            return 1
        def willMeet (c1, c2):
            #the car behind is ALWAYS c1, other is c2. Can make these assumptions because local function
            if (c1[0] < c2[0]) and (c1[1] > c2[1]):
                time_to_target = (target - c2[0]) / c2[1]
                time_to_meet = (c1[0]-c2[0]) / (c2[1]-c1[1])
                return time_to_meet <= time_to_target
            return False
        ##NOTE: zip does not directly return list
        s_and_p = list (zip (position, speed))
        ##NOTE: consider the tuple (x,y) as a list. See the lambda function
        ##NOTE: * -1 to sort by descending
        s_and_p.sort(key = lambda x: x[0] * -1)
        n = len(position)
        marked_positions = [0] * n
        clusters = 0

        for i in range(n):
            if marked_positions[i] == 0:
                clusters = clusters + 1
                marked_positions[i] = 1
                for j in range (i+1, n):
                    if willMeet (s_and_p[j], s_and_p[i]) and marked_positions[j] == 0:
                        marked_positions[j] = 1
        return clusters

s = Solution()

assert s.carFleet(target = 10, position = [6,8], speed = [3,2]) == 2
assert s.carFleet(target = 100, position = [0,20,90,40,70], speed = [50,30,10,60,30]) == 2
assert s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]) == 3
assert s.carFleet(target = 10, position = [3], speed = [3]) == 1
assert s.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]) == 1
assert s.carFleet(target = 100, position = [1,2,3,4,5], speed = [1,2,3,4,5]) == 5
assert s.carFleet(target = 100, position = [0,20,3,4,40], speed = [50,30,3,4,10]) == 3

