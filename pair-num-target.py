from typing import List


class Solution:
    def task(self, nums: List[int], target_sum: int) -> bool:
        """
        Task: 
            Given an array of integers and a value, determine if there are any 
            two integers in the array whose sum is equal to the given value. 
            Return true if the sum exists and return false if it does not. 

        Examples:
            Input: [5,7,1,2,8,4,3], target_sum = 10
            Output: True
            Why: 7,3 and 2,8 equal 10
        """
        # look at ea. num in the array
        # subtract the target sum
        # get the pair for the number
        # if the number is in the array, return the pair
        pairs = {}
        answer = False
        for i in range(len(nums)-1):
            if (nums[i] < target_sum):
                paired_num = target_sum-nums[i]
                if paired_num in nums:
                    answer = True
                    break
        return answer

    def testTask(self, nums=List[int], answer=[int]) -> bool:
        test_cases = {
            10: [[5, 7, 1, 2, 8, 4, 3], True],
            5: [[2, 3, 0], True],
            4: [[0, 1], False]
        }
        passed = 0
        failed = 0
        for i in test_cases:
            code_answer = self.task(test_cases[i][0], i)
            if test_cases[i][1] == code_answer:
                passed += 1
                print("Success!, code answer was: ", code_answer,
                      " right answer was: ", test_cases[i][1])
            else:
                failed += 1
                print("Failed, code answer was: ", code_answer,
                      " right answer was ", test_cases[i][1])
        print("Passed ", passed, " tests, Failed ", failed,
              " tests, success rate: ", (passed/(passed+failed))*100, "%")


task = Solution()
answer = task.testTask()
