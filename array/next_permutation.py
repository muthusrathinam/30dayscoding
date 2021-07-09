'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:
    Input: nums = [1,2,3]
    Output: [1,3,2]
'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                j = i
                while j < n and nums[j] > nums[i-1]:
                    idx = j
                    j += 1
                nums[idx], nums[i-1] = nums[i-1], nums[idx]
                for k in range((n-i)//2):
                    nums[i+k], nums[n-1-k] = nums[n-1-k], nums[i+k]
                break
        else:
            nums.reverse()
