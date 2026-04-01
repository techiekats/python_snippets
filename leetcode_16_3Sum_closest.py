#https://leetcode.com/problems/3sum-closest/description/
import sys
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = nums[:]
        sorted_nums.sort()
        distance = sys.maxsize
        result = -1
        #[-1,2,1,-4]
        for i in range (len(sorted_nums)): #0
            left = i + 1 #1
            right = len(sorted_nums) - 1 # 3
            while left < right: #True
                current_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right] #-2
                difference = target-current_sum
                current_distance = abs(difference)
                if current_distance == 0:
                    return current_sum
                if current_distance < distance:
                    result = current_sum #-2
                    distance = current_distance #3
                # This is the main part where baseline 2 sum needs to be edited
                if difference < 0:
                    right -= 1
                else:
                    left += 1
        return result
#test cases
s = Solution()
assert s.threeSumClosest ([-1,2,1,-4], 1) == 2
assert s.threeSumClosest ([0,0,0], 1) == 0