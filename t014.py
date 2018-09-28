class Solution:
    """ 14
    编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。
    """
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ''
        elif len(strs) == 1:
            return strs[0]
        idx = 0
        base_str = strs[0]
        while True:
            brk = False
            if idx >= len(base_str):
                break
            for str_ in strs[1:]:
                if idx < len(str_):
                    if base_str[idx] != str_[idx]:
                        brk = True
                        break
                else:
                    brk = True
                    break
            if brk:
                break
            idx += 1
        return base_str[:idx]
