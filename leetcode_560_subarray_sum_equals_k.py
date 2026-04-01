#https://leetcode.com/problems/subarray-sum-equals-k/description/
#NOTE: cannot use 2-sum it would need sorted arrays
class Solution:
    def subarraySum(self, nums, k):
        n = len(nums) #[1,1,1]
        if n == 0:
            return 0
        partial_sum_indices = {} ## This is not needed in the sliding window version
        result = 0
        partial_sum_indices[nums[0]] = 1
        for i in range(1, n):
            nums[i] = nums[i-1] + nums[i]
            if nums[i] in partial_sum_indices:
                partial_sum_indices[nums[i]] += 1
            else:
                partial_sum_indices[nums[i]] = 1

        if k in partial_sum_indices:
            result += partial_sum_indices[k]
        for key in partial_sum_indices:
            target = k + key
            if target in partial_sum_indices:
                if key < target: ## to avoid duplicates
                    result += partial_sum_indices[target]
                else:
                    if key == target:
                        result += partial_sum_indices[target] - 1

        ##NOTE: Implement sliding window. This solution is correct but has n^2 complexity
        # for i in range (n):
        #     for j in range(i+1, n+1):
        #         if (partial_sum[j] - partial_sum[i]) == k:
        #             result+=1


        return result


s = Solution()
assert s.subarraySum([-1,-1,1], 1) == 1
assert s.subarraySum([-1, -2, -3, 3, 2, 1], 0) == 3
assert s.subarraySum([-1,-1,1], 0) == 1
assert s.subarraySum([1,1,1], 2) == 2
assert s.subarraySum([1,2,3], 3) == 2
assert s.subarraySum([1,2,3], 300) == 0
assert s.subarraySum([1], 1) == 1
assert s.subarraySum([1], 100) == 0
assert s.subarraySum([1,2,3,3,2,1], 6) == 3
assert s.subarraySum([1,2,3,3,2,1], 5) == 2
