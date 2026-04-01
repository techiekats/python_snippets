#https://leetcode.com/problems/kth-largest-element-in-an-array/description/
from typing import List
import sys
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # [3,2,1,5,6,4]
        max_heap = []
        for h in nums:  # 3 2
            max_heap.append(h)  # [3 2 1 5] [5,3,1,2,6] [6,5,1,2,3,4]
            current_index = len(max_heap) - 1  # 0 1 2 3 4 5
            parent = (current_index - 1) // 2  # 0 0 0 1 1 2

            while max_heap[current_index] > max_heap[parent] and parent >= 0:
                max_heap[parent], max_heap[current_index] = max_heap[current_index], max_heap[
                    parent]  # [3,5,1,2] [5,3,1,2], [5,6,1,2,3] [6,5,1,2,3], [6,5,4,2,3,1]
                current_index = parent  # 1 1 1 2
                parent = (current_index - 1) // 2  # 0 0 0 0 0

        # [6, 5, 4, 2, 3, 1]
        min_int = -sys.maxsize - 1
        for i in range(k):  # 0
            h = max_heap[0]  # 6
            if i == k - 1:
                return h
            # forgot the adjustment operation
            max_heap[0] = max_heap.pop()  # 6, [1, 5, 4, 2, 3]
            parent = 0
            left_child = right_child = min_int
            if parent * 2 + 2 < len(max_heap):
                right_child = max_heap[2]  # 4
            if parent * 2 + 1 < len(max_heap):
                left_child = max_heap[1]  # 5

            while max_heap[parent] < left_child or max_heap[parent] < right_child:
                if left_child > right_child:
                    max_heap[parent], max_heap[parent * 2 + 1] = max_heap[parent * 2 + 1], max_heap[
                        parent]  # [5, 1, 4, 2, 3]
                    parent = parent * 2 + 1  # 1
                else:
                    max_heap[parent], max_heap[parent * 2 + 2] = max_heap[parent * 2 + 2], max_heap[
                        parent]  # [5, 3, 4, 2, 1]
                    parent = parent * 2 + 2

                if parent * 2 + 1 >= len(max_heap):
                    left_child = min_int
                else:
                    left_child = max_heap[parent * 2 + 1]  # 2
                if parent * 2 + 2 >= len(max_heap):
                    right_child = min_int
                else:
                    right_child = max_heap[parent * 2 + 2]  # 3

        return -1
#test cases
s = Solution()
assert s.findKthLargest([3,2,1,5,6,4], 2) == 5
assert s.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

