class Solution:
    """ 62
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    问总共有多少条不同的路径？
    """
    def uniquePaths(self, m, n):
        """
        方法一：动态规划，当前位置的不同路径数是上边位置和左边位置的不同路径数之和
        方法二：排列，m-1个下走、n-1个右走
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 1 or n <= 1:
            return 1
        else:
            return math.factorial(m+n-2)//(math.factorial(n-1)*math.factorial(m-1))
