class Solution:
    """ 46
    给定一个没有重复数字的序列，返回其所有可能的全排列。
    """
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = [[]]
        for num in nums:
            tmps = []
            for result in results:
                for i in range(len(result)+1):
                    tmps.append(result[:i] + [num] + result[i:])
            results = tmps
        return results
