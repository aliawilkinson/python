# day 25

# weather_set = []
# with open('weather_data.csv') as weather:
#     for l in weather.readlines():
#         weather_set.append(l)

# print(weather_set)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    next(data)
    for row in data:
        print(int(row[1]))

        # create a new temperatures list, contains all temps inside weather data
        # int