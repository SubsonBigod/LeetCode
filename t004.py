class Solution:
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
