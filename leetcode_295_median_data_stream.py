#https://leetcode.com/problems/find-median-from-data-stream/description/
##NOTE: do not implement heap in actual. Just use Python heaps
import heapq
class MedianFinder:

    def __init__(self):
        self._lowest = []
        self._highest = []
        heapq.heapify(self._lowest)
        heapq.heapify(self._highest)

    def addNum(self, num: int) -> None:

        if len (self._lowest) == 0:
            heapq.heappush(self._lowest, num * -1)
        else:
            left = self._lowest[0]
            ##NOTE: do not forget equals because there can be duplicates
            if num <= left * -1:
                heapq.heappush(self._lowest, num * -1)
            else:
                heapq.heappush(self._highest, num)
        ##rebalance
        len_lowest, len_highest = len(self._lowest), len(self._highest)
        while abs (len_lowest - len_highest) > 1:
            if len_highest > len_lowest:
                 x = heapq.heappop(self._highest)
                 heapq.heappush(self._lowest, x * -1)
                 len_highest -= 1
            else:
                x = heapq.heappop(self._lowest) * -1
                heapq.heappush(self._highest, x)
                len_lowest -= 1

    def findMedian(self) -> float:
        ##NOTE: heappop() removes the element. To peek use heap[0]
        ##NOTE: by default, heapq are min heaps. Hence the -1 for the lower elements to simulate max heap
        len_lowest, len_highest = len(self._lowest), len(self._highest)

        if len_lowest == len_highest:
            return (self._lowest[0] * -1 + self._highest[0]) / 2
        if len_lowest > len_highest: ##This also handles the case of just 1 element
            return self._lowest[0]* -1
        return self._highest[0] 

##smoke test
medianFinder = MedianFinder()
medianFinder.addNum(1)  # arr = [1]
medianFinder.addNum(2)  # arr = [1, 2]
assert medianFinder.findMedian() == 1.5 # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)  # arr[1, 2, 3]
assert medianFinder.findMedian() == 2.0 # return 2.0

##test for duplicates
medianFinder = MedianFinder()
medianFinder.addNum(2)
medianFinder.addNum(2)
##even number of entries
assert medianFinder.findMedian() == 2
#odd number of entries
medianFinder.addNum(2)
assert medianFinder.findMedian() == 2

#increasing numbers
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
medianFinder.addNum(3)
medianFinder.addNum(4)
medianFinder.addNum(5)
assert medianFinder.findMedian() == 3
medianFinder.addNum(6)
assert medianFinder.findMedian() == 3.5

#negative numbers
medianFinder = MedianFinder()
medianFinder.addNum(-1)
medianFinder.addNum(-2)
medianFinder.addNum(-3)
medianFinder.addNum(-4)
medianFinder.addNum(-5)
assert medianFinder.findMedian() == -3
medianFinder.addNum(-6)
assert medianFinder.findMedian() == -3.5