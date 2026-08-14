
class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(list)

        # store the direct edges and their weights
        for index, (a, b) in enumerate(equations):
            graph[a].append((b, values[index]))
            graph[b].append((a, 1.0 / values[index]))

        def find_value(start, target):
            visited = set()

            def dfs(node, product):
                if node == target:
                    return product

                visited.add(node)

                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        result = dfs(neighbor, product * weight)

                        if result != -1.0:
                            return result

                return -1.0

            return dfs(start, 1.0)

        # calculate the query results
        results = []

        for first, second in queries:
            if first not in graph or second not in graph:
                results.append(-1.0)
                continue
            # dfs or bfs or dijsktra's here?
            results.append(find_value(first, second))

        return results