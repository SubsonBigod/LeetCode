class Solution:
    """ 54
    给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
    """
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if len(matrix) == 0:
            return result
        m, n = len(matrix), len(matrix[0])
        right, down, left, up = 0, n-1, m-1, 0
        while right <= left and up <= down:
            for idx in range(up, down+1):
                result.append(matrix[right][idx])
            right += 1
            if right > left:
                break
            for idx in range(right, left+1):
                result.append(matrix[idx][down])
            down -= 1
            if down < up:
                break
            for idx in range(down, up-1, -1):
                result.append(matrix[left][idx])
            left -= 1
            if right > left:
                break
            for idx in range(left, right-1, -1):
                result.append(matrix[idx][up])
            up += 1
            if down < up:
                break
        return result
