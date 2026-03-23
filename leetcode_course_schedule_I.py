##https://leetcode.com/problems/course-schedule/
##NOTE: In Python, deque from collections is used because queue operations at both ends are efficient. A normal list is fine for appending, but removing from the front is slow.
from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        ## calculate indegrees
        ## NOTE: how an array of size n is created
        indegree = [0] * numCourses
        for u,v in prerequisites:
            indegree[v] = indegree[v] + 1
        ## create queue. a queue is necessary to detect cycles
        queue = deque([u for u in range(numCourses) if indegree[u] == 0])
        #while queue:

        return True

t1 = [2, [[1, 0]]]
t2 = [2, [[1, 0], [0, 1]]]
t3 = [3, [[1,0], [1,2]]]
t4 = [4, [[1,0], [1,2]]]
s = Solution ()

assert s.canFinish(t1[0], t1[1]) == True
assert s.canFinish(t2[0], t2[1]) == False
assert s.canFinish(t3[0], t3[1]) == True
assert s.canFinish(t4[0], t4[1]) == True