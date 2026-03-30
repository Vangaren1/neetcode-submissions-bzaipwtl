class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        routes = defaultdict(list)
        tickets.sort(reverse=True)

        for src, dst in tickets:
            routes[src].append(dst)

        path = []

        def dfs(src):
            while routes[src]:
                dst = routes[src].pop()
                dfs(dst)
            path.append(src)

        dfs("JFK")

        return path[::-1]