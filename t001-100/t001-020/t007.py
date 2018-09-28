class Solution:
    """ 7
    给定一个 32 位有符号整数，将整数中的数字进行反转。
    """
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x) < 10:
            return x
        y = x
        x = abs(x)
        while x % 10 == 0:
            x //= 10
        result = 0
        while x != 0:
            result *= 10
            result += x % 10
            x //= 10
        if result > 2**31 or result < -2**31:
            return 0
        return result * y // abs(y)


if __name__ == "__main__":
    func = Solution().reverse
    assert 321 == func(123)
    assert -21 == func(-12)
    assert 21 == func(12)
    assert -102 == func(-2010)
    assert 102 == func(2010)
    assert 0 == func(-2147483648)
    assert 0 == func(1534236469)
    assert 0 == func(2147483647)
    assert 1 == func(1)
