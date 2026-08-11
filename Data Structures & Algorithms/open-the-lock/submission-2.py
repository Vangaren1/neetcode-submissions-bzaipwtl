class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        upDown = {
            "0": ("9", "1"),
            "1": ("0", "2"),
            "2": ("1", "3"),
            "3": ("2", "4"),
            "4": ("3", "5"),
            "5": ("4", "6"),
            "6": ("5", "7"),
            "7": ("6", "8"),
            "8": ("7", "9"),
            "9": ("8", "0"),
        }
        visited = set(["0000"])
        dead = set(deadends)
        queue = deque()
        if "0000" not in dead:
            queue.append(("0000", 0))

        while queue:

            curr, dist = queue.popleft()
            curr = [ch for ch in curr]

            for i in range(4):
                original = curr[i]
                pair = upDown[original]
                curr[i] = pair[0]
                up = "".join(curr)
                if up == target:
                    return dist + 1
                curr[i] = pair[1]
                down = "".join(curr)
                if down == target:
                    return dist + 1
                curr[i] = original
                if up not in dead and up not in visited:
                    visited.add(up)
                    queue.append((up, dist + 1))
                if down not in dead and down not in visited:
                    visited.add(down)
                    queue.append((down, dist + 1))

        return -1