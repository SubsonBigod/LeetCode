class Solution:
    """ 53
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 1
        while idx < len(nums):
            if nums[idx-1] > 0:
                nums[idx] += nums[idx-1]
            idx += 1
        return max(nums)
