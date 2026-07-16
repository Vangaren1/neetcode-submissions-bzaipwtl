import string

class Solution:
    def decodeString(self, s: str) -> str:
        if "[" not in s:
            return s

        # find the start of the number
        start = 0
        while not s[start].isdigit():
            start += 1

        # find the end of the first number
        end = start
        while s[end].isdigit():
            end += 1

        front = s[:start]
        num = int(s[start:end])

        # find the matching ] character
        ptr = end + 1
        count = 1
        while count:
            if s[ptr] == "[":
                count += 1
            elif s[ptr] == "]":
                count -= 1
            ptr += 1

        mid = s[end + 1 : ptr - 1]
        back = s[ptr:]
        # print(f"{front} {num} {mid} {back}")
        return front + num * self.decodeString(mid) + self.decodeString(back)