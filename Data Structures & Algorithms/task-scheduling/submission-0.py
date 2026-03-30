class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1

        taskCounts = [-i for i in count.values()]
        heapq.heapify(taskCounts)

        q = deque()
        time = 0

        while taskCounts or q:
            time += 1
            if taskCounts:
                c = 1 + heapq.heappop(taskCounts)
                if c:
                    q.append((c, time + n))
            if q and q[0][1] == time:
                heapq.heappush(taskCounts, q.popleft()[0])

        return time