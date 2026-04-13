class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # map each course to prereq list
        prevMap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            prevMap[crs].append(pre)

        visited = set() # track nodes along dfs path

        def dfs(crs):
            if crs in visited:
                return False
            if prevMap[crs] == []:
                return True

            visited.add(crs)

            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            prevMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



