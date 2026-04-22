#https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            current_area = height * width

            if current_area > max_area:
                max_area = current_area
            if heights[left] > heights[right]:
                right = right - 1
            else:
                left = left + 1
        return max_area

#test cases
s = Solution()
assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert s.maxArea([1,1]) == 1