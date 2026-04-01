#https://leetcode.com/problems/find-duplicate-file-in-system/description/
class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        contents = {}

        def getFileContents(path: str) -> (str, str):
            index = path.find('(')
            return (path[0:index], path[index + 1: len(path) - 1])

        for p in paths:
            space_separated = p.split(' ')
            # TODO: if file contains spaces this will not work
            directory, files = space_separated[0], space_separated[1:]
            for f in files:
                (path, content) = getFileContents(f)
                if content not in contents:
                    contents[content] = [f'{directory}/{path}']
                else:
                    contents[content].append(f'{directory}/{path}')

        result = []
        for k, v in contents.items():
            if len(v) >= 2:
                result.append(v)

        return result
#test cases
s = Solution()
assert s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]) == [["root/a/1.txt","root/c/3.txt"],["root/a/2.txt","root/c/d/4.txt","root/4.txt"]]
assert s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]) == [["root/a/1.txt","root/c/3.txt"],["root/a/2.txt","root/c/d/4.txt"]]