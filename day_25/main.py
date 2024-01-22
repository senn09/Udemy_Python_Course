import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240105.csv")
fur_colour_data = data["Primary Fur Color"]
print(fur_colour_data)

fur_data = {
    "Fur Colour":[],
    "Count":[]
            }
for fur_colour in fur_colour_data:
    if fur_colour not in fur_data["Fur Colour"]:
        fur_data["Fur Colour"].append(fur_colour)
        fur_data["Count"].append(1)
    else:
        index = fur_data["Fur Colour"].index(fur_colour)
        fur_data["Count"][index] += 1

print(fur_data)
df_fur_data = pandas.DataFrame(fur_data)
print(df_fur_data)
df_fur_data.to_csv("squirel_count.csv")




