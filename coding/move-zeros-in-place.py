# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution():
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        isContiguousZeroes = True
        lastZeroPos = len(nums) - 1
        i = 0
        for i in range (len(nums)-1, -1, -1):
            if nums[i] == 0 and isContiguousZeroes == False:
                j = i
                while j < lastZeroPos:
                    nums[j] = nums[j+1]
                    j += 1
                nums[lastZeroPos] = 0
                lastZeroPos -= 1
            elif nums[i] != 0 and isContiguousZeroes == True:
                isContiguousZeroes = False
            elif nums[i] == 0:
                lastZeroPos -= 1
            else:
                pass


    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonZeroIndex = 0
        i = 0
        numsLen = len(nums)
        for i in range (0, numsLen):
            if nums[i] != 0:
                nums[nonZeroIndex] = nums[i]
                nonZeroIndex += 1
        while nonZeroIndex < numsLen:
            nums[nonZeroIndex] = 0
            nonZeroIndex += 1