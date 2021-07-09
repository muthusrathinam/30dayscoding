'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []
        nums.sort()
        result_arr = []
        
        for i in range(len(nums)):
            if(nums[i] > 0):
                break;
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            
            left, right = i+1, len(nums)-1
            
            
            while(left < right):
                sum = nums[left] + nums[i] + nums[right]
                if(sum == 0):
                    result_arr.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1

                    left += 1
                    right -=1
                elif(sum>0):
                    right-=1
                else:
                    left += 1
        return result_arr
            
#[-4,-1,-1,0,1,2] after sorting
