#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        start = 0
        state = {}
        result = 0 # 3,
        # REMEMBER enumerate(s)
        for end, char in enumerate(s): #0 1 2 3 4
            if char in state and state[char] >= start:
                start = state[char] + 1 # 1
            state[char] = end # {'s': 3}
            result = max(result, end - start+1) # max(0, 3)
        return result

#test cases
s = Solution()
assert s.lengthOfLongestSubstring("abcadefgh") == 8
assert s.lengthOfLongestSubstring("abcabcbb") == 3