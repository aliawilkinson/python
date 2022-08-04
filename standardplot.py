class Solution(object):
    def runningSum(self, nums):
        """
        Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
        Return the running sum of nums.

        Example 1:
        Input: nums = [1,2,3,4]
        Output: [1,3,6,10]
        Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
        :type nums: List[int]
        :rtype: List[int]
        """
        new_nums = []
        for i in range(len(nums)):
            if (i == 0):
                new_nums.insert(i,nums[i])  
                continue
            else:
                # add previous number to current number
                new_nums.insert(i,nums[i] + new_nums[i-1])  
                
        return new_nums
                
        
        """       
        for num in reversed(len(nums)) :
            print(num)
        """
   