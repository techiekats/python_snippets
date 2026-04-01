#https://leetcode.com/problems/distance-between-bus-stops/
class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        total = sum(distance)
        patch = 0
        ##NOTE: the summing of a sub array
        if start < destination:
            patch = sum(distance[start:destination])
        else:
            patch = sum(distance[destination:start])
        return min(patch, total-patch)

#Test cases
s= Solution()
assert s.distanceBetweenBusStops([1,2,3,4], 0, 1) == 1
assert s.distanceBetweenBusStops([1,2,3,4], 0, 2) == 3
assert s.distanceBetweenBusStops([1,2,3,4], 0, 3) == 4
assert s.distanceBetweenBusStops([1,2,3,4,3,2,1], 4, 3) == 4
assert s.distanceBetweenBusStops([6], 0, 0) == 0
