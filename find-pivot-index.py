class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_index = len(nums)-1
        right_sum = 0
        left_sum = 0
        for left_index in range(len(nums)):
            # get first index
            # get last index
            right_index = right_index - 1 
            print("woo")
            
        
        """
        Input: nums = [1,7,3,6,5,6]
        Input: nums = [1,7,3
        ,6,
        5,6]
        
        8
        11
        Input: nums = [1,7,3,
        6,7,8
        5,6]
        no?
        8+3 = 11
            do we have 11?
            if yes? return index next to last index calc'd
            else
            keep going

        Output: 3
        Explanation:
        The pivot index is 3.
        Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
        Right sum = nums[4] + nums[5] = 5 + 6 = 11
        
        pivot index position value is 6 
        11 to the left
        11 (but would have been 15 including the pivot index)
        
        
        """
        
        
        hashmap
        key = index
        left_val = 
        right_val = 