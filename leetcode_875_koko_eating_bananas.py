#https://leetcode.com/problems/koko-eating-bananas/description/
import math
class Solution:
    def minEatingSpeed(self, apples: list[int], h: int) -> int:
        low, high = 1, max(apples)
        rate = 1
        while low <= high:
            mid = (low+high)//2
            total_hours = 0
            for a in apples:
                total_hours += math.ceil(a/mid)
            #If the total hours are more than max, then increase the rate. Reset the low end of the range
            if total_hours > h:
                low = mid+1
            #If the total hours are equal or lesser, there is chance to reduce the work per hour. So, look in the lower range. Set the rate to the current rate, because it will be better than the existing one anyways
            else:
                high = mid-1
                rate = mid
        return rate
#test cases
s = Solution()
assert s.minEatingSpeed([3,6,7,11],8) == 4
assert s.minEatingSpeed([30,11,23,4,20], 5) == 30
assert s.minEatingSpeed([30,11,23,4,20], 6) == 23
