class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        st = 0
        ed = 1
        for i in range(1, len(s)):
            j = i - 1
            k = i
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    if k - j + 1 > ed - st or (k - j + 1 == ed - st and j < st):
                        st = j
                        ed = k + 1
                else:
                    break
                j -= 1
                k += 1

            j = i - 1
            k = i + 1
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    if k - j + 1 > ed - st or (k - j + 1 == ed - st and j < st):
                        st = j
                        ed = k + 1
                else:
                    break
                j -= 1
                k += 1
            if ed - st >= (len(s) - i) * 2 + 1:
                break
        return s[st:ed]


if __name__ == "__main__":
    func = Solution().longestPalindrome
    assert ("bab" == func("babad"))
    assert ("bb" == func("cbbd"))
    assert ("a" == func("a"))
    assert ("a" == func("ab"))
    assert ("bbb" == func("abbb"))
    assert ("" == func(""))
    str0 = "a" * 972
    assert str0 == func(str0)
    str1 = "0" * 1019
    assert (str1 == func(str1))
