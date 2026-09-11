class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        results = [[1]]

        if numRows == 1:
            return results

        results.append([1, 1])
        if numRows == 2:
            return results

        for i in range(3, numRows + 1):
            last = results[-1]
            tmp = [1]
            ptr = 0
            while ptr < len(last) - 1:
                tmp.append(last[ptr] + last[ptr + 1])
                ptr += 1
            tmp.append(1)
            results.append(tmp)
        return results