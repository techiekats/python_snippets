#https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals):
        #Note: initializing to [[]] instead of [] will change the empty check
        result = []
        intervals.sort(key = lambda x: x[0])
        for i in intervals:
            if not result:
                result.append(i)
            else:
                top = result[-1]
                if i[0] <= top[1]:
                    result[-1][1] = max(i[1], top[1])
                else:
                    result.append(i)

        return result
    
##Tests
s = Solution()
assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert s.merge([[1,4],[4,5]]) == [[1,5]]
assert s.merge([[4,7],[1,4]]) == [[1,7]]
assert s.merge([[1,2], [2,3], [3,4]]) == [[1,4]]
assert s.merge([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]]
assert s.merge([[2,3],[4,5],[7,9],[1,10]]) == [[1,10]]