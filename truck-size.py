class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        """
        Task: 
            You are assigned to put some amount of boxes onto one truck. 
            You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

            numberOfBoxesi is the number of boxes of type i.
            numberOfUnitsPerBoxi is the number of units in each box of the type i.
            You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. 
            You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

            Return the maximum total number of units that can be put on the truck.

        Example 1:

            Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize  = 4
            Output: 8
            Explanation: There are:
            - 1 box of the first type that contains 3 units. 
            - 2 boxes of the second type that contain 2 units each. 
            - 3 boxes of the third type that contain 1 unit each. 
            You can take all the boxes of the first and second types, and one box of the third type.
            The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
            [[[5,10],[3,9],[4,7],[2,5]], 10]
            truckSize, boxes_remaining = 10
            
            5 boxes
            
            is boxes_remaining(10) - boxes(5) gt 0 (5)
             boxes_remaining = boxes_remaining - truckSize(5)
             add 50 units to Answer
            is boxes_remaining(5) - boxes(3) gt 0 (2)
             boxes_remaining = boxes_remaining - truckSize(5)
             add 50 units to Answer
            3 boxes
            27 units
            boxes_remaining = 2

            4 boxes

        """
        # sort the list by the number of units
        boxTypes.sort(reverse=True,key=self.sortByUnits)
        units = 0
        boxes_remaining = truckSize
        i = 0
        while (not boxes_remaining == 0 and i <= len(boxTypes)-1):
            box = boxTypes[i]  
            box_num = box[0]
            unit_num = box[1]
            units += min(box_num,boxes_remaining)*unit_num
            boxes_remaining = boxes_remaining - min(box_num,boxes_remaining)
            i += 1
        return units

    def sortByUnits(self,ele):
        return ele[1]

    def testTask(self):
        test_cases = {
            0: {
                "Input": [[[1,3],[2,2],[3,1]], 4],
                "Output": 8
            },
            1: {
                "Input": [[[5,10],[2,5],[4,7],[3,9]], 10],
                "Output": 91
            },
        }
        passed = 0
        failed = 0
        for i in test_cases:
            code_answer = self.maximumUnits(test_cases[i]["Input"][0],test_cases[i]["Input"][1])
            if test_cases[i]["Output"] == code_answer:
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
