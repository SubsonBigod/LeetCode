class Solution:
    # modified from https://github.com/pezy/LeetCode
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                return [dic[num], index]
            dic[target - num] = index
        raise ValueError("No indices")


if __name__ == "__main__":
    func = Solution().twoSum
    nums0 = [2, 7, 11, 15]
    target0 = 9
    indices0 = [0, 1]
    assert func(nums0, target0) == indices0

    nums1 = [0, 4, 3, 0]
    target1 = 0
    indices1 = [0, 3]
    assert func(nums1, target1) == indices1

    nums2 = [-1, -2, -3, -4, -5]
    target2 = -8
    indices2 = [2, 4]
    assert func(nums2, target2) == indices2
