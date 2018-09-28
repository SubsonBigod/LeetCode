class Solution:
    """ 88
    给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
    说明:
        初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = 0, 0, 0
        nums1[m:] = []
        while k < m and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
                k += 1
            else:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
        if j < n:
            nums1.extend(nums2[j:n])
