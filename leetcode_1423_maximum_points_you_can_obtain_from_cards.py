#https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
class Solution:
    def maxScore(self, cards: list[int], k: int) -> int:
        if k > len(cards):
            return 0
        current_score = max_score = sum(cards[:k])
        for i in range(1, k+1):
            current_score = current_score + cards[-i] - cards[k-i]
            max_score = max(max_score, current_score)
        return max_score
#test cases
s = Solution()
assert s.maxScore([1,2,3,4,5,6,1],3) == 12
assert s.maxScore([2,2,2],2) == 4
assert s.maxScore([9,7,7,9,7,7,9], 7) == 55