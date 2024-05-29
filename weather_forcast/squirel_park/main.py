import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squ = len(data["Primary Fur Color"] == "Gray")
Cinn_squ = len(data["Primary Fur Color"] == "Cinnamon")
Black_squ = data["Primary Fur Color"] == "Black"
print(gray_squ)
print(Cinn_squ)
print(Black_squ)
