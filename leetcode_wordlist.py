#https://leetcode.com/problems/word-ladder/description/
import math
class Solution:
    ##assuming they are equal length
    def calculateDist(self, w1, w2):
        result = 0
        for i in range (self._n):
            if w1[i] != w2[i]:
                result += 1
        return result

    def getMinWordDistance(self, begin, end, visited):
        if begin == end:
            #print (f"Iteration: {begin} {end} {visited}")
            return len (visited)
        result = self._maxConst
        visited_copy = dict(visited)
        for i in range (self._wordListLength):
            if i not in visited_copy:
                w = self._wordList[i]
                x = self.calculateDist(begin, w)
                if x == 1:
                    visited_copy[i] = 1
                    result = min (result, self.getMinWordDistance(w, end, visited_copy))
                    del visited_copy[i]
        return result

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        #divide into distance-wise buckets. Intuition, you need at most n transformations to reach destination word, where n = length of word
        self._wordList = wordList
        self._wordListLength = len(wordList)
        visited = {}
        self._maxConst = math.inf
        self._n = len(beginWord)
       
        result = self.getMinWordDistance(beginWord, endWord, visited)
        if result == self._maxConst:
            return 0
        return result+1
    
#test cases
s = Solution()

assert s.ladderLength("a", "b", ["q", "r", "b"]) == 2
assert s.ladderLength("ab", "cd", ["ad", "cb", "ad", "cd"]) == 3
assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
