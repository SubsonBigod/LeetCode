class Solution:
    """ 34
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。
    找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。
    如果数组中不存在目标值，返回 [-1, -1]。
    """
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        st, ed = 0, len(nums)-1
        while st < ed:
            mid = st + (ed-st)//2
            if nums[mid] < target:
                st = mid + 1
            else:
                ed = mid
        if nums[st] != target:
            return [-1, -1]
        final_st = st
        ed = len(nums)-1
        while st < ed:
            mid = st + (ed-st)//2 + 1
            if nums[mid] > target:
                ed = mid - 1
            else:
                st = mid
        return final_st, ed
