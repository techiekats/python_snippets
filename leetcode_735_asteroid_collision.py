#https://leetcode.com/problems/asteroid-collision/description/
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [0] ##Adding an initial 0 to avoid unnecessary checks in the while loop
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                asteroid_destroyed = False
                while stack[-1] > 0 and not asteroid_destroyed:
                    if stack[-1] < a * -1:
                        stack.pop()
                    else:
                        asteroid_destroyed = True
                        if stack[-1] == -1 * a:
                            stack.pop()
                if not asteroid_destroyed:
                    stack.append(a)
        stack.pop (0) ##Remove the initial 0
        return stack

s = Solution ()
# assert s.asteroidCollision() ==
assert s.asteroidCollision([-1,1,-2,2,-3,3]) == [-1,-2,-3,3]
assert s.asteroidCollision([1,-1,2,-2,3,-3]) == []
assert s.asteroidCollision([-5]) == [-5]
assert s.asteroidCollision([-1,-2,-3,-4]) == [-1,-2,-3,-4]
assert s.asteroidCollision([1,2,4,5]) == [1,2,4,5]
assert s.asteroidCollision([5,10,-5]) == [5,10]
assert s.asteroidCollision([8,-8]) == []
assert s.asteroidCollision([10,2,-5]) == [10]
assert s.asteroidCollision([3,5,-6,2,-1,4]) == [-6,2,4]