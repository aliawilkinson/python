from typing import List


class Solution:
    def task(self, nums: List[int]) -> int:
        """
        Task: <Task>
        Examples: <Examples>
        """
    def testTask(self, nums=List[int], answer=[int]) -> bool:
        test_cases = {
        }
        passed = 0
        failed = 0
        for right_answer in test_cases:
            code_answer = self.task(test_cases[right_answer])
            if right_answer == code_answer:
                passed+=1
                print("Success!, code answer was: ", code_answer,
                      " right answer was: ", right_answer)
            else:
                failed+=1
                print("Failed, code answer was: ", code_answer,
                      " right answer was ", right_answer)
        print("Passed ", passed , " tests, Failed ", failed, " tests, success rate: ", (passed/(passed+failed))*100, "%" )


task = Solution()
answer = task()
