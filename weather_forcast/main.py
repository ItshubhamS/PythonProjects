# import csv
#
# with open("weather_data.csv") as deta_file:
#     weather_data = csv.reader(deta_file)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
import pandas

total = 0
data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# average = data["temp"].mean()
# print(round(average, 2))
# print(data["temp"].max())
print(data[data.temp == data.temp.max()])
