
# https://leetcode.com/problems/find-pivot-index/
# slice notation: [ <first element to include> : <first element to exclude> : <step> ]

class Solution(object):
    def pivotIndex(self, nums):
        all_num_sum = sum(nums)
        leftsum = 0
        for i, currentvalue in enumerate(nums):
            print(x)
            if leftsum == (all_num_sum - leftsum - currentvalue):
                return i
            leftsum += currentvalue
        return -1