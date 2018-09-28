class Solution:
    """ 33
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。你的算法时间复杂度必须是 O(log n) 级别。
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif len(nums) == 1 and nums[0] != target:
            return -1
        if nums[0] < target:
            idx = 1
            while idx < len(nums) and nums[idx-1] <= nums[idx] < target:
                idx += 1
            if nums[idx % len(nums)] == target:
                return idx
            else:
                return -1
        elif nums[0] > target:
            idx = len(nums) - 1
            while idx > 0 and nums[(idx+1) % len(nums)] >= nums[idx] > target:
                idx -= 1
            if nums[idx % len(nums)] == target:
                return idx
            else:
                return -1
        else:
            return 0
