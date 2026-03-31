#https://leetcode.com/problems/car-fleet/description/
import heapq
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        if len(position) == 1:
            return 1

        # Per the caller, s1 is the lower of the speeds
        def willMeet(p1, s1, p2, s2):
            # conditions where catch up is not possible. Lower speed vehicle should not be behind
            if (p2 > p1) and s2 > s1:
                return False
            if s1 == s2:
                return p1 == p2
            d = p1 - p2
            s = s2 - s1
            t = d / s
            # because slower vehicle's speed doesn't change
            destination = s1 * t
            return destination <= target
        ##NOTE: zip does not directly return list
        s_and_p = list (zip (speed, position))
        ##NOTE: consider the tuple (x,y) as a list. See the lambda function
        s_and_p.sort(key = lambda x: x[0])
        s = []
        p = []
        for i in range (len(s_and_p)):
            x = s_and_p[i]
            s.append(x[0])
            p.append(x[1])
        for i in range (len(s)):
            if p[i] != -1:
                for j in range (i, len(s)):
                    if i!= j:
                        if willMeet (p[i], s[i],p[j], s[j]):
                            p[j] = -1
        result = 0
        for x in p:
            if x != -1:
                result += 1
        return result

#tests
s = Solution()
assert s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]) == 3
assert s.carFleet(target = 10, position = [3], speed = [3]) == 1
assert s.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]) == 1


