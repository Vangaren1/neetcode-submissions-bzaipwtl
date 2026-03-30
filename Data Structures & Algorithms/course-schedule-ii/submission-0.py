class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        courses = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            courses[a].append(b)

        checking = set()
        seen = set()
        order = []

        def dfs(course):
            if course in checking:
                return False
            if course in seen:
                return True
            checking.add(course)

            for pre in courses[course]:
                check = dfs(pre)
                if not check:
                    return False

            checking.remove(course)
            seen.add(course)
            order.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
            else:
                courses[c] = []
        return order