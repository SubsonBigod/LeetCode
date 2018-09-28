class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        length = 1
        st = 0
        for i in range(1, len(s)):
            if s[i] not in s[st:i]:
                if length < i - st + 1:
                    length = i - st + 1
            else:
                st += s[st:i].index(s[i]) + 1
        return length


if __name__ == "__main__":
    func = Solution().lengthOfLongestSubstring
    assert 3 == func("abcabcbb")
    assert 1 == func("bbbbb")
    assert 3 == func("pwwkew")
    assert 0 == func("")
    assert 1 == func("a")
    assert 2 == func("au")
    assert 6 == func("bbtablud")
    assert 2 == func("aab")
