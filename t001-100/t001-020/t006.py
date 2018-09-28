class Solution:
    """ 6
    将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：
        P   A   H   N
        A P L S I I G
        Y   I   R
    之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"
    """
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = ""
        for i in range(0, numRows):
            j = i
            step = i * 2
            while j < len(s):
                if i == 0 or i == numRows - 1:
                    step = (numRows - 1) * 2
                else:
                    step = (numRows - 1) * 2 - step
                result += s[j]
                j += step
        return result


if __name__ == "__main__":
    func = Solution().convert
    assert "0123456789" == func("0123456789", 1)
    assert "0246813579" == func("0123456789", 2)
    assert "0481357926" == func("0123456789", 3)
    assert "0615724839" == func("0123456789", 4)
    assert "0817926354" == func("0123456789", 5)
    assert "0192837465" == func("0123456789", 6)
    assert "0123948576" == func("0123456789", 7)
    assert "0123459687" == func("0123456789", 8)
    assert "0123456798" == func("0123456789", 9)
