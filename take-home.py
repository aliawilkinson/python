class Solution:
    def stockSpa(firstDate, lastDate):
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
#             For firstDate = "1-January-2000" and lastDate = "11-January-2000", the output should be

# solution(firstDate, lastDate) = [
#     "5-January-2000 5265.09 5357.00",
#     "6-January-2000 5424.21 5421.53",
#     "7-January-2000 5358.28 5414.48",
#     "11-January-2000 5513.04 5296.30"
# ]
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



# In this challenge, you will write an HTTP GET method to retrieve information from a database containing information about stocks. You will be given two strings firstDate and lastDate which represent valid date range, your task is to return the opening and closing prices for each stock within the given date range.

# You can query for the stock information using one of the following queries:

# GET https://testapi.codesignal.com/stocks: This query returns all available stock information. The response is paginated, so you may need to query GET https://testapi.codesignal.com/stocks?page=<pageNumber>, where <pageNumber> is an integer that represents the page number to view (e.g., 1, 2, etc.).
# GET https://testapi.codesignal.com/stocks?<key>=<value>: This query returns all the results where the searched <key> is an exact match to <value>. The response is paginated, so you may need to query GET https://testapi.codesignal.com/stocks?<key>=<value>&page=<pageNumber>, where <pageNumber> is an integer that represents the page number you would like to view (e.g., 1, 2, etc.).
# GET https://testapi.codesignal.com/stocks/search?<key>=<value>: This query returns all results where the searched <key> has value that contains <value> as a substring. The response is paginated, so you may need to query GET https://testapi.codesignal.com/stocks/search?<key>=<value>&page=<pageNumber>, where <pageNumber> is an integer that represents the page number to view (e.g., 1, 2, etc.).
# All the queries return a JSON response with the following five fields:

# page: The current page.
# per_page: The maximum number of results per page.
# total: The total number of records found.
# total_pages: The total number of pages which must be queried to get all the results.
# data: An array of JSON objects that contain the stock information. The JSON contains the following five fields, each of which can be used as the key to query:
# date: A string that describes the date on which the stock information is provided. The date format is d-mmm-yyyy, where d represents a valid day of the month, mmm represents the complete name of the month (e.g. , January, February, March, etc.), and yyyy represents the year. The date is in the range 5-January-2000 to 1-January-2014 inclusive. There may not be information for some dates, and the information is available for Monday through Friday only.
# open: A float value that represents the stock's open price on the given date.
# close: A float value that represents the stock's close price on the given date.
# high: A float value that represents the stock's highest price on the given date.
# low: A float value that represents the stock's lowest price on the given date.
# After retrieving information from the database, the output should be represented by an array of strings, with each string containing values that represent the date, the open price, and the close price of each stock. Please, round all float values in the output to exactly 2 digits after the decimal point.

# Example

# For firstDate = "1-January-2000" and lastDate = "11-January-2000", the output should be

# solution(firstDate, lastDate) = [
#     "5-January-2000 5265.09 5357.00",
#     "6-January-2000 5424.21 5421.53",
#     "7-January-2000 5358.28 5414.48",
#     "11-January-2000 5513.04 5296.30"
# ]
# Note that as all float numbers should be returned with 2 digits after the decimal point, 5357 or 5357.0 won't be considered as a valid answer.

# If using Golang, the json and log package is already imported.

# Please optimize your solution for execution speed, something to especially consider if any tests are timing out.

# Input/Output

# [execution time limit] 12 seconds (py3)

# [input] string firstDate

# A string that denotes the beginning of the period to report.

# [input] string lastDate

# A string that denotes the end of the period to report.

# [output] array.string

# An array of strings, where each string contains three space-separated values that represent the date, the open price, and the close price respectively.

# All float values in the output should be rounded to exactly 2 digits after the decimal point.

