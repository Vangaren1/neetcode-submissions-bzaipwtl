class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first = {}
        last = {}

        for index, ch in enumerate(s):
            if ch not in first:
                first[ch] = index
            last[ch] = index

        results = []

        ptr1 = 0

        while ptr1 < len(s):
            start = ptr1
            startCh = s[ptr1]
            end = last[startCh]
            while ptr1 < end:
                ptr1 += 1
                tmp = s[ptr1]
                end = max(last[tmp], end)
            results.append(end - start + 1)
            ptr1 += 1

        return results
