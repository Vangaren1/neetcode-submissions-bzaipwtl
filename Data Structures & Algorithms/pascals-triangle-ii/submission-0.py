class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        lastRow = self.getRow(rowIndex -1)
        newRow = [1]
        for index in range(len(lastRow)-1):
            newRow.append( lastRow[index] + lastRow[index + 1])
        newRow.append(1)
        return newRow