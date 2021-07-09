class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[j] == target - nums[i]):
                    return i,j
        print("no solutions found")'''
        
    #hashmap

        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
