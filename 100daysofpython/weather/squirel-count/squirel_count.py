import pandas

# Primary Fur Color
# Figure out totals of each squirel color
df = pandas.read_csv("central-park-sq-2018.csv")
# put that into a new dataframe 
fur_df = df['Primary Fur Color'].value_counts(dropna=False)
# create a csv
fur_df.to_csv('primary_fur_color.csv')

