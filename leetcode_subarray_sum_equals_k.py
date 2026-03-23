#https://leetcode.com/problems/subarray-sum-equals-k/description/
#NOTE: cannot use 2-sum it would need sorted arrays
class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)
        partial_sum = [0] * (n + 1) #[0, 1, 2, 3]
        partial_sum_indices = {} ## This is not needed in the sliding window version
        index = 1
        result = 0
        for sas in nums:
            key = partial_sum[index] = partial_sum[index-1] + sas
            if key in partial_sum_indices:
                partial_sum_indices[key] += 1
            else:
                partial_sum_indices[key] = 1
            index+=1
        print (partial_sum_indices)
        for i in range (1, n+1):
            current = partial_sum[i]
            target = k - current
            # to avoid double counting

            if target in partial_sum_indices:
                result += partial_sum_indices[target]

        ## to handle the case of sum == k
        result += partial_sum_indices[k]
        ##NOTE: Implement sliding window. This solution is correct but has n^2 complexity
        # for i in range (n):
        #     for j in range(i+1, n+1):
        #         if (partial_sum[j] - partial_sum[i]) == k:
        #             result+=1


        return result


s = Solution()
print (s.subarraySum([1,1,1], 2))
assert s.subarraySum([1,1,1], 2) == 2
assert s.subarraySum([1,2,3], 3) == 2
assert s.subarraySum([1,2,3], 300) == 0
assert s.subarraySum([1], 1) == 1
assert s.subarraySum([1], 100) == 0
assert s.subarraySum([1,2,3,3,2,1], 6) == 3
assert s.subarraySum([1,2,3,3,2,1], 5) == 2
