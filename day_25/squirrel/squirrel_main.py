import pandas as pd

squirrel_df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_df = squirrel_df.groupby("Primary Fur Color").size().reset_index(name="Count")
print(squirrel_df)
# squirrel_df.to_csv("all_the_squirrels.csv", index=False)

