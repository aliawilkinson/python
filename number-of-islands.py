class Solution:
    def number_of_islands(self, nums: List[int]) -> bool:
        """
        Task: 
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

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
