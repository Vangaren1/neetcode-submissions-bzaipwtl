class StockSpanner:

    def __init__(self):
        self.stk = []
        pass

    def next(self, price: int) -> int:
        self.stk.append(price)

        count = 0
        for index in range(len(self.stk) - 1, -1, -1):
            if self.stk[index] > price:
                break
            count += 1
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)