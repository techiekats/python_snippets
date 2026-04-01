#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binarySearch(start: int, end: int) -> list[int]:
            if end < start:
                return [-1, -1]
            if end == start:
                if nums[end] == target:
                    return [start, end]
                return [-1, -1]
            if nums[start] == target and nums[end] == target:
                return [start, end]
            mid = (start + end) // 2  # 2
            if nums[mid] > target:  # 7>8(False)
                return binarySearch(start, mid - 1)
            if nums[mid] < target:
                return binarySearch(mid + 1, end)  # f(3, 5)
            left_search_result = binarySearch(start, mid - 1)
            right_search_result = binarySearch(mid + 1, end)
            # Note the ternary operators in Python
            return [left_search_result[0] if left_search_result[0] != -1 else mid,
                    right_search_result[1] if right_search_result[1] != -1 else mid]

        return binarySearch(0, len(nums) - 1)

#test cases
s = Solution()
assert s.searchRange([5,7,7,8,8,10], 8) == [3,4]
assert s.searchRange([5,7,7,8,8,10], 6) == [-1, -1]
assert s.searchRange([], 0) == [-1,-1]