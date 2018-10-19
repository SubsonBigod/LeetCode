class Solution:
    """ 121
    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pass


if __name__ == '__main__':
    func = Solution().maxProfit
    assert 1 == func([1, 2])
    assert 7 == func([7, 1, 5, 3, 6, 4])
    assert 7 == func([7, 1, 5, 4, 3, 6, 4])
    assert 7 == func([7, 3, 1, 5, 4, 3, 6, 4])
    assert 6 == func([3, 3, 5, 0, 0, 3, 1, 4])
    assert 4 == func([1, 2, 3, 4, 5])
    assert 12 == func([1, 2, 4, 2, 5, 7, 2, 4, 9, 0])
