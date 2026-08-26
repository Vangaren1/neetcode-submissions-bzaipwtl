class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        roomCount = [0 for _ in range(n)]
        # (endtime, roomNum)
        available = [i for i in range(n)]
        heapq.heapify(available)
        occupied = []

        for start, end in meetings:
            duration = end - start

            while occupied and occupied[0][0] < start:
                freeTime, room = heapq.heappop(occupied)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
            else:
                freeTime, room = heapq.heappop(occupied)

                heapq.heappush(occupied, (freeTime + duration, room))

            roomCount[room] += 1

        return roomCount.index(max(roomCount))