class Solution:
    """ 59
    给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
    """
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        result = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        right, down, left, up = 0, n-1, n-1, 0
        while right <= left and up <= down:
            for idx in range(up, down+1):
                result[right][idx] = num
                num += 1
            right += 1
            if right > left:
                break
            for idx in range(right, left+1):
                result[idx][down] = num
                num += 1
            down -= 1
            if down < up:
                break
            for idx in range(down, up-1, -1):
                result[left][idx] = num
                num += 1
            left -= 1
            if right > left:
                break
            for idx in range(left, right-1, -1):
                result[idx][up] = num
                num += 1
            up += 1
            if down < up:
                break
        return result
