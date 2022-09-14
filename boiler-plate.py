class Solution:
    def task(self, nums: List[int]) -> bool:
        """
        Task: 
            <Task>

        Examples:
            <Examples>
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
            code_answer = self.task(test_cases[i]["Input"])
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
