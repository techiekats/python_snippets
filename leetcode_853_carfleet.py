#https://leetcode.com/problems/car-fleet/description/
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        if len(position) == 1:
            return 1
        n = len(position)
        ##NOTE: Here we cannot simply sort the position array because each element is coupled with one in the speed array.
        ## We can create a joint tuple structure but that's additional memory
        ## instead just stored the indices of the array if the sorting were to happen
        sorted_idx = sorted (range(n), key= lambda i: position[i])

        clusters = 0
        prev_blocking_time = 0
        ## We need to access in descending order, closest to target to furthest. See the pattern [::1] start from end and step ny -1
        for i in sorted_idx[::-1]:
            t = (target - position[i]) / speed[i]
            if t > prev_blocking_time:
                clusters += 1
                prev_blocking_time = t

        return clusters

s = Solution()

assert s.carFleet(target = 10, position = [6,8], speed = [3,2]) == 2
assert s.carFleet(target = 100, position = [0,20,90,40,70], speed = [50,30,10,60,30]) == 2
assert s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]) == 3
assert s.carFleet(target = 10, position = [3], speed = [3]) == 1
assert s.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]) == 1
assert s.carFleet(target = 100, position = [1,2,3,4,5], speed = [1,2,3,4,5]) == 5
assert s.carFleet(target = 100, position = [0,20,3,4,40], speed = [50,30,3,4,10]) == 3

