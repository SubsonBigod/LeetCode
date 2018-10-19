class Solution:
    """ 121
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
    注意你不能在买入股票前卖出股票。
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        i, in_price = 1, prices[0]
        result = 0
        while i < len(prices):
            while i < len(prices):
                if prices[i] <= in_price:
                    in_price = prices[i]
                else:
                    break
                i += 1
            j = i
            while j < len(prices):
                if prices[j] > in_price and result < prices[j] - in_price:
                    result = prices[j] - in_price
                j += 1
            while i < len(prices):
                if prices[i] <= in_price:
                    in_price = prices[i]
                    i += 1
                    break
                i += 1
        return result


if __name__ == '__main__':
    func = Solution().maxProfit
    print(func([7, 1, 5, 3, 6, 4]))
