class Solution:
    """ 121
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if len(prices) < 2:
            return result
        i = 1
        in_idx = 0
        while i < len(prices) and prices[in_idx] >= prices[i]:
            in_idx = i
            i += 1
        if i >= len(prices):
            return result
        out_idx = i
        while i < len(prices) and prices[out_idx] <= prices[i]:
            out_idx = i
            i += 1
        if i >= len(prices):
            return prices[out_idx] - prices[in_idx]
        while i < len(prices):
            curr_in_idx = out_idx + 1
            while i < len(prices) and prices[i] <= prices[curr_in_idx]:
                curr_in_idx = i
                i += 1
            if prices[out_idx] >= prices[curr_in_idx]:
                result += prices[out_idx] - prices[in_idx]
                in_idx = curr_in_idx
            if i >= len(prices):
                break
            out_idx = i
            while i < len(prices) and prices[i] >= prices[out_idx]:
                out_idx = i
                i += 1
            if i >= len(prices):
                result += prices[out_idx] - prices[in_idx]
                break
        return result


if __name__ == '__main__':
    func = Solution().maxProfit
    print(func([1, 2]))
    print(func([7, 1, 5, 3, 6, 4]))
    print(func([7, 1, 5, 4, 3, 6, 4]))
    print(func([7, 3, 1, 5, 4, 3, 6, 4]))
