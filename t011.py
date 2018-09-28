class Solution:
    """ 11
    给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，
    垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
    使得它们与 x 轴共同构成的容器可以容纳最多的水。
    """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        elif len(height) == 2:
            return min(height)
        i, j = 0, len(height)-1
        curr_max = 0
        while i < j:
            if height[i] < height[j]:
                curr_area = (j-i)*height[i]
                i += 1
            else:
                curr_area = (j-i)*height[j]
                j -= 1
            if curr_area > curr_max:
                curr_max = curr_area
        return curr_max
