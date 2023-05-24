# day 25

# challenge 1

# weather_set = []
# with open('weather_data.csv') as weather:
#     for l in weather.readlines():
#         weather_set.append(l)

# print(weather_set)

# challenage 2

# import csv

# def get_temp():
#   with open("weather_data.csv") as data_file:
#       data = csv.reader(data_file)
#       next(data)
#       temperatures = []
#       for row in data:
#           temperatures.append(int(row[1]))
#       return temperatures
#         # create a new temperatures list, contains all temps inside weather data
#         # int

# temperatures = get_temp()
# print(temperatures)

# challenge 3

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print("temp_list",temp_list)

# average temp in temp list
average = sum(temp_list) / len(temp_list)
print("average temp",average)

print("temp mean", data["temp"].mean())

# use data series method to find the max temp

print("temp max", data["temp"].max())
