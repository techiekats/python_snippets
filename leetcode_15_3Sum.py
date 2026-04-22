#https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        left, mid, right = 0, 1, len(nums) - 1
        result = []
        for left in range(len(nums) - 2):
            # for mid and right, needed additional loops. For left, reuse the main loop
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            target = nums[left] * -1
            mid = left + 1
            right = len(nums) - 1
            ##Simplified chain comparison, vs: mid < right and left < mid
            while right > mid > left:
                current_sum = nums[mid] + nums[right]
                if current_sum == target:
                    # In the initial version had this line to check uniqueness before inserting. Its not needed and also adds O(n) to each running resulting in O(n^2)
                    # if not any(map (lambda x: x[0] == nums[left] and x[1] == nums[mid], result)):
                    result.append([nums[left], nums[mid], nums[right]])
                    # Because numbers are not unique, decrement right and increment left
                    while (right - 1) > mid and nums[right] == nums[right - 1]:
                        right -= 1
                    while (mid + 1) < right and nums[mid] == nums[mid + 1]:
                        mid += 1

                if current_sum < target:
                    mid += 1
                else:
                    right -= 1
        return result
#test cases
s = Solution()
assert s.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert s.threeSum([0,1,1]) == []
assert s.threeSum([0,0,0]) == [[0,0,0]]
