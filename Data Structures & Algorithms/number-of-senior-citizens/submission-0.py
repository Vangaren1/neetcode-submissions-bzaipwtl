class Solution:
    def countSeniors(self, details: List[str]) -> int:
        total = 0

        for detail in details:
            age = detail[11:13]
            if int(age)>60:
                total += 1
        return total 