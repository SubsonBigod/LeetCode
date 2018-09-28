
import sys


class Solution:
    """ 16
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
    使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
    """
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = sys.maxsize
        nums.sort()
        for idx in range(len(nums)-2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            i, j = idx+1, len(nums)-1
            while i < j:
                curr_sum = nums[idx]+nums[i]+nums[j]-target
                if curr_sum < 0:
                    i += 1
                elif curr_sum > 0:
                    j -= 1
                elif curr_sum == 0:
                    return target
                if abs(curr_sum) < abs(result):
                    result = curr_sum
        return result+target
