class Solution:
    """ 4
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
    请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
    你可以假设 nums1 和 nums2 不同时为空。
    """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = sorted(nums1 + nums2)
        if len(arr) % 2 == 1:
            return arr[len(arr) // 2] * 1.0
        else:
            return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2


if __name__ == "__main__":
    func = Solution().findMedianSortedArrays
    assert 3 == func([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    assert 3 == func([1, 2, 3, 4], [1, 2, 3, 4, 5])
    assert 2.5 == func([1, 2, 3], [1, 2, 3, 4, 5])
    assert 2.0 == func([1, 3], [2])
    assert 3.0 == func([1, 2, 3, 4, 5], [])
