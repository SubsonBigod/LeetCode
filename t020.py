class Solution:
    """ 20
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    有效字符串需满足：
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = True
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    result = False
                    break
            elif c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    result = False
                    break
            elif c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    result = False
                    break
            else:
                result = False
                break
        if len(stack) != 0:
            result = False
        return result
