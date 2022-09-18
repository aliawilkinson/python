class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Task: 
            Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

            Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

            Return k after placing the final result in the first k slots of nums.

            Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

        Examples:
            <Examples>
        """
        # can only modify input array
        count = 0
        for i in range(len(nums)):
            if (nums[i] == val):
                nums[i] = -1
            else:
                count += 1
        nums.sort(reverse=True)
        return [count, nums]

    # def testRemove(self):
    #     nums = [...]; # Input array
    #     val = ...; # Value to remove
    #     expectedNums = [...]; # The expected answer with correct length.
    #                                 # It is sorted with no values equaling val.
        
    #     k = removeElement(nums, val); # Calls your implementation
        
    #     assert k == expectedNums.length;
    #     sort(nums, 0, k); # Sort the first k elements of nums
    #     for (int i = 0; i < actualLength; i++) {
    #         assert nums[i] == expectedNums[i];
    #     }

    def testTask(self):
        test_cases = {
            # 0: {
            #     "Input": [[3,2,2,3], 3],
            #     "Output": [2, [2,2]]
            # },
            1: {
                "Input": [[0,1,2,2,3,0,4,2], 2],
                "Output": [5, [0,1,4,0,3]]
            },
        }
        passed = 0
        failed = 0
        for i in test_cases:
            input = test_cases[i]["Input"]
            code_answer = self.removeElement(input[0],input[1])
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
