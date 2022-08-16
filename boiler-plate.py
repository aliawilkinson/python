from typing import List


class Solution:
    def task(self, nums: List[int], target_sum: int) -> bool:
        """
        Task: 
            <Task>

        Examples:
            <Examples>
        """

    def testTask(self, nums=List[int], answer=[int]) -> bool:
        test_cases = {
        }
        passed = 0
        failed = 0
        for i in test_cases:
            code_answer = self.task(test_cases[i], i)
            if test_cases[i] == code_answer:
                passed += 1
                print("Success!, code answer was: ", code_answer,
                      " right answer was: ", test_cases[i])
            else:
                failed += 1
                print("Failed, code answer was: ", code_answer,
                      " right answer was ", test_cases[i])
        print("Passed ", passed, " tests, Failed ", failed,
              " tests, success rate: ", (passed/(passed+failed))*100, "%")


task = Solution()
answer = task.testTask()
