import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#Load WorldCupMatches.csv into a DataFrame called df
df = pd.read_csv('WorldCupMatches.csv')

#check out dataframe
#print(df.head())

#make a new column for the total goals in a match
df['Total_Goals'] = df["Home Team Goals"]+df["Away Team Goals"]

#create dataframe with goals per year in the world cup
goals_per_year = df.groupby('Year').Total_Goals.sum().reset_index()
#print(goals_per_year)

#seaborn the seaborn barplot
sns.set_style('whitegrid')
sns.set_context('poster',font_scale = 0.75)
f,ax = plt.subplots(figsize=(12,7))

ax = sns.barplot(data = goals_per_year,x = 'Year',y='Total_Goals')
ax.set_title('Total Goals per Year')
#display plt
#plt.show()

#load goals.csv into a dataframe

df_goals = pd.read_csv('goals.csv')

#print(df_goals.head())
sns.set_context('notebook',font_scale=1.15)
#create the new boxplot with average goals per year
f,ax2 = plt.subplots(figsize=(12,7))
ax2 = sns.boxplot(data= df_goals,x = 'year',y='goals',palette=sns.color_palette('Spectral'))
ax2.set_title('Average Goals per Year')
#display boxplot
plt.show()

