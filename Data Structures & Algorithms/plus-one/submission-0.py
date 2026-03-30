class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 0

        digits[-1] += 1
        for index in range(len(digits) - 1, -1, -1):
            tmp = digits[index] + carry

            carry = 1 if tmp >= 10 else 0
            digits[index] = tmp % 10

        if carry:
            digits.insert(0, 1)
        return digits