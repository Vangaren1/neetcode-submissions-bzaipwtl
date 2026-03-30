class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            courses[a].append(b)

        checking = set()

        def dfs(course):
            if course in checking:
                return False

            checking.add(course)

            for pre in courses[course]:
                check = dfs(pre)
                if not check:
                    return False

            checking.remove(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True        