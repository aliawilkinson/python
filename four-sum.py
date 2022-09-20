class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

        0 <= a, b, c, d < n
        a, b, c, and d are distinct.
        nums[a] + nums[b] + nums[c] + nums[d] == target
        You may return the answer in any order.



        Example 1:

        Input: nums = [1,0,-1,0,-2,2], target = 0
        Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        Example 2:

        Input: nums = [2,2,2,2,2], target = 8
        Output: [[2,2,2,2]]
        """
        

    def testTask(self):
        test_cases = {
            0: {
                "Input": "",
                "Output": ""
            },
            1: {
                "Input": "",
                "Output": ""
            },
        }
        passed = 0
        failed = 0
        for i in test_cases:
            code_answer = self.fourSum(test_cases[i]["Input"])
            if test_cases[i] == code_answer:
                passed += 1
                print("Success!, code answer was: ", code_answer,
                      " right answer was: ", test_cases[i]["Output"])
            else:
                failed += 1
                print("Failed, code answer was: ", code_answer,
                      " right answer was ", test_cases[i]["Output"])
        print("Passed ", passed, " tests, Failed ", failed,
              " tests, success rate: ", (passed/(passed+failed))*100, "%")


task = Solution()
answer = task.testTask()
