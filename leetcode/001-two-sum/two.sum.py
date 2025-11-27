class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list = []
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    list.append(i)
                    list.append(j)
                    break
        return list
    
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i


solution = Solution()
print(solution.twoSum2([2, 7, 11, 15], 9))
print(solution.twoSum2([3, 2, 4], 6))
print(solution.twoSum2([3,3], 6))
print(solution.twoSum2([2,5,5,11], 10))