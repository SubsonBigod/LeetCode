class Solution:
    """ 43
    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，
    它们的乘积也表示为字符串形式。
    """
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1)+len(num2))
        i = len(num1) - 1
        while i >= 0:
            j = len(num2) - 1
            while j >= 0:
                result[len(num1)+len(num2)-i-j-2] += int(num1[i])*int(num2[j])
                result[len(num1)+len(num2)-i-j-2+1] += result[len(num1)+len(num2)-i-j-2] // 10
                result[len(num1)+len(num2)-i-j-2] %= 10
                j -= 1
            i -= 1
        end = len(result) - 1
        while result[end] == 0 and end > 0:
            end -= 1
        return ''.join(map(str, result[end::-1]))
