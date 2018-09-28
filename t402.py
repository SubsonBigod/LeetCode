class Solution:
    """ 402
    非0开头的数字字符串num，去除k个字符串，是的该数字字符串最小
    """
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        idx = 0
        while k > 0 and idx < len(num):
            curr = num[idx]
            if len(stack) == 0:
                if curr != '0':
                    stack.append(curr)
                idx += 1
            else:
                if curr < stack[-1]:
                    stack.pop()
                    k -= 1
                else:
                    if not (len(stack) == 0 and curr == '0'):
                        stack.append(curr)
                    idx += 1
        while len(stack) >= k > 0:
            tail = stack.pop()
            if len(stack) <= 0:
                break
            if tail < stack[-1]:
                stack.pop()
                stack.append(tail)
            k -= 1
        while idx < len(num):
            curr = num[idx]
            idx += 1
            if len(stack) == 0 and curr == '0':
                continue
            stack.append(curr)
        if len(stack) == 0:
            return '0'
        else:
            return ''.join(stack)
