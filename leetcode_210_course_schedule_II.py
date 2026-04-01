#https://leetcode.com/problems/course-schedule-ii/description/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = {}
        indegree = [0] * numCourses
        for a,b in prerequisites:
            indegree[a] += 1
            if b not in adj_list:
                adj_list[b] = [a]
            else:
                adj_list[b].append(a)
        #NOTE: the keyword here is "range"
        stack = [x for x in range(numCourses) if indegree[x] == 0]
        courses = []
        ## dfs
        while stack != []:
            x = stack.pop()
            courses.append(x)
            ##NOTE: use get() method to avoid if key exists check
            for c in adj_list.get(x, []):
                indegree[c] = indegree[c] - 1
                if indegree[c] == 0:
                    stack.append(c)
        if len (courses) == numCourses:
            return courses
        return []

## test cases
s = Solution()
## Test cases
t1 = [2, [[1, 0]]]
t2 = [2, [[1, 0], [0,1]]]
t3 = [3, [[1,0], [1,2]]]
t4 = [4, [[1,0], [1,2]]]
t5 = [5, [[0,1], [1,2], [2,3], [3,4], [4,1]]]
t6 = [1,[[0,0]]]
t7 = [1,[]]
t8 = [7, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,3],[2,6],[6,1]]]

assert s.findOrder(t3[0], t3[1]) == [2,0,1]
assert s.findOrder(t5[0], t5[1]) == []
assert s.findOrder(t1[0], t1[1]) == [0,1]
assert s.findOrder(t2[0], t2[1]) == []
assert s.findOrder(t4[0], t4[1]) == [3,2,0,1]
assert s.findOrder(t6[0], t6[1]) == []
assert s.findOrder(t7[0], t7[1]) == [0]
assert s.findOrder(t8[0], t8[1]) == []