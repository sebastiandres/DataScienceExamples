import pandas as pd
from matplotlib import pyplot as plt

filename = "SchoolLifeExpectancy.csv"
df = pd.DataFrame.from_csv(filename)

"""
As we have with the previous assignments, look at the distribution of values for each attribute. 
Anything in particular stand out at you? 
What's the median age and the mean age for each gender? 
Which do you think is more appropriate for this dataset?
"""
# The describe method returns a new pandas dataframe
df_subset = df[["men","women"]]
d = df_subset.describe()
print("Principal statistics for the School Life Expectancy by gender:")
print(d)

# A histogram
df_subset.hist(alpha=0.5, sharex=True, sharey=True)
plt.suptitle("School Life Expectancy years by gender")
plt.show()

# What country has the longest school life expectancy
print("")
genders = ["men", "women"]
for gender in genders: 
    print("{0} has the shortest school life expectancy for {1}".format(df[gender].argmin(), gender))
    print("{0} has the longest school life expectancy for {1}".format(df[gender].argmax(), gender))

# What elso could be important?
