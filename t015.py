class Solution:
    """ 15
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 
    找出所有满足条件且不重复的三元组。
    """
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        for idx in range(len(nums)-2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            i, j = idx+1, len(nums)-1
            while i < j:
                curr_sum = nums[idx]+nums[i]+nums[j]
                if curr_sum < 0:
                    i += 1
                elif curr_sum > 0:
                    j -= 1
                elif curr_sum == 0:
                    results.append([nums[idx], nums[i], nums[j]])
                    while nums[i] == nums[i+1] and i+1 < j:
                        i += 1
                    while nums[j] == nums[j-1] and i < j-1:
                        j -= 1
                    i += 1
                    j -= 1
        return results
