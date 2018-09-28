class Solution:
    """ 78
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        for num in nums:
            results.append([num])
            for l in results:
                if num not in l:
                    results.append(l + [num])
        results.append([])
        return results
