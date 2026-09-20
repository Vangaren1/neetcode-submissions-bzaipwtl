class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        height = len(image)
        width = len(image[0])
        visited = set()
        originalColor = image[sr][sc]
        diff = ((0, 1), (0, -1), (1, 0), (-1, 0))

        dq = deque()
        visited.add((sr, sc))

        dq.append((sr, sc))

        while dq:

            y, x = dq.popleft()
            image[y][x] = color

            for dy, dx in diff:
                ny, nx = dy + y, dx + x
                if (
                    0 <= ny < height
                    and 0 <= nx < width
                    and image[ny][nx] == originalColor
                    and (ny, nx) not in visited
                ):
                    visited.add((ny, nx))
                    dq.append((ny, nx))

        return image