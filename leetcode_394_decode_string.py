#https://leetcode.com/problems/decode-string/
class Solution:
    def isInteger(self, s:str) -> bool:
        try:
            int(s)
            return True
        except(ValueError, TypeError):
            return False

    def decodeString(self, s: str) -> str:
        if not s:
            return ''
        stack = []
        result = ''
        for c in s:
            if c == ']':
                temp = ''
                while stack[-1]!='[':
                    temp = stack.pop() + temp #d cd
                stack.pop() #removes the opening [
                multiplier = int(stack.pop()) #3
                stack.append(multiplier * temp)
            else:
                if self.isInteger(c):
                    #check if previous is integer as well
                    y = 0
                    if stack:
                        y = stack.pop()
                    if self.isInteger(y):
                        stack.append(int(y)*10 + int(c))
                    else:
                        stack.append(y)
                        stack.append(c)
                else:
                    stack.append(c)
        while stack:
            result = stack.pop() + result
        return result
#test cases
s = Solution()
assert s.decodeString("3[a]2[bc]") == "aaabcbc"
assert s.decodeString("3[a2[c]]") == "accaccacc"
assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"