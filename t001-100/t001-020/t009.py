class Solution:
    """ 9
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    """
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x % 10 == 0:
            return False
        else:
            i = 0
            j = len(str(x)) - 1
            while i < j:
                if (x//10**i) % 10 != (x//10**j) % 10:
                    return False
                i += 1
                j -= 1
            return True


if __name__ == "__main__":
    func = Solution().isPalindrome
    assert not func(-1)
    assert func(7)
    assert not func(10)
    assert not func(12)
    assert not func(123)
    assert func(323)
    assert func(1221)
    assert func(12321)
    assert func(123321)
