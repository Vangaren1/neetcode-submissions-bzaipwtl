class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])

        def dfs(pos, word):
            if len(word) == 0:
                return True

            y, x = pos
            ch = board[y][x]
            if ch != word[0]:
                return False
            if len(word[1:]) == 0:
                return True

            board[y][x] = "#"

            diff = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for dy, dx in diff:
                ny = dy + y
                nx = dx + x
                if 0 <= ny < height and 0 <= nx < width:
                    check = dfs((ny, nx), word[1:])
                    if check:
                        board[y][x] = ch
                        return True
            board[y][x] = ch
            return False

        for y in range(height):
            for x in range(width):
                check = dfs((y, x), word)
                if check:
                    return True
        return False