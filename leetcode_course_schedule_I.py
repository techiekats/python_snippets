##https://leetcode.com/problems/course-schedule/
##NOTE: In Python, deque from collections is used because queue operations at both ends are efficient. A normal list is fine for appending, but removing from the front is slow.
from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        ## calculate indegrees
        ## NOTE: how an array of size n is created
        indegree = [0] * numCourses
        adj_list = {}
        for u,v in prerequisites:
            indegree[v] = indegree[v] + 1
            if u not in adj_list:
                adj_list[u] = [v]
            else:
                adj_list[u].append(v)
        ## create queue. a queue is necessary to detect cycles
        queue = deque([u for u in range(numCourses) if indegree[u] == 0])

        while queue:
            x = queue.popleft()
            if x in adj_list:
                for v in adj_list[x]:
                    indegree[v] = indegree[v] - 1
                    if indegree[v] == 0:
                        queue.append(v)
        return not any(x > 0 for x in indegree)

## Test cases
t1 = [2, [[1, 0]]]
t2 = [2, [[1, 0], [0, 1]]]
t3 = [3, [[1,0], [1,2]]]
t4 = [4, [[1,0], [1,2]]]
t5 = [5, [[0,1], [1,2], [2,3], [3,4], [4,1]]]
t6 = [1,[[0,0]]]
t7 = [1,[]]
t8 = [7, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,3],[2,6],[6,1]]]
s = Solution ()
assert s.canFinish(t5[0], t5[1]) == False
assert s.canFinish(t1[0], t1[1]) == True
assert s.canFinish(t2[0], t2[1]) == False
assert s.canFinish(t3[0], t3[1]) == True
assert s.canFinish(t4[0], t4[1]) == True
assert s.canFinish(t6[0], t6[1]) == False
assert s.canFinish(t7[0], t7[1]) == True
assert s.canFinish(t8[0], t8[1]) == False