import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt

West = ['SF Bay Area', 'Salt Lake City', 'Los Angeles', 'Seattle', 'Phoenix', 'Sacremento', 'San Diego', 'Denver', 'Portland']
Northeast = ['New York City', 'Boston', 'Dover', 'Pittsburg', 'Philadelphia', 'Stamford', 'Washington D.C'] 
Midwest = ['St. Louis', 'Detroit', 'Kansas City', 'Boulder', 'Chicago', 'Milwaukee', 'Lexington', 'Columbus', 'Cincinnati', 'Minneapolis']
South = ['Atlanta', 'Mexico City', 'Dallas', 'Austin', 'Miami', 'Nashville']

layoffs = pd.read_csv("layoffs.csv", header=0)

layoffs = layoffs[(layoffs['date'] > '2022-01-01') & (layoffs['date'] <= '2022-30-12')]
layoffs = layoffs[layoffs['country'] == 'United States']
layoffs = layoffs.drop(['total_laid_off', 'funds_raised', 'country', 'date'], axis=1)
layoffs['percentage_laid_off'] = layoffs['percentage_laid_off'] * 100 

layoffs = layoffs.dropna()

c1 = layoffs['location'].isin(West)
c2 = layoffs['location'].isin(Northeast)
c3 = layoffs['location'].isin(Midwest)
c4 = layoffs['location'].isin(South)

layoffs = layoffs.assign(region=np.select([c1, c2, c3, c4], ['West', 'Northeast', 'Midwest', 'South']))

layoffs = layoffs[layoffs.location != 'London']
layoffs.to_csv("layoffs_clean.csv")

q1 = layoffs['percentage_laid_off'].quantile(0.25)
q3 = layoffs['percentage_laid_off'].quantile(0.75)
IQR = q3-q1

lower_range = (q1-1.5)*IQR
upper_range = (q3+1.5)*IQR

print(lower_range)
print(upper_range)
print(layoffs.boxplot(column=['percentage_laid_off']))

layoffs['region'].value_counts()

layoffs['industry'].value_counts()

layoffs['stage'].value_counts()

sns.barplot(y = 'percentage_laid_off', x = 'region', data = layoffs)
plt.title("Scatterplot of layoffs per Region")
plt.xlabel("Region")
plt.ylabel("Layoff Percentage")
None;

sns.barplot(y = 'percentage_laid_off', x = 'industry', data = layoffs)
plt.title("Scatterplot of Percentage Laid Off per Industry")
plt.xlabel("Industry")
plt.ylabel("Percentage Laid Off")
plt.xticks(rotation=90)
None;

sns.barplot(y = 'percentage_laid_off', x = 'stage', data = layoffs)
plt.title("Scatterplot of Percentage Laid Off per Stage of Funding")
plt.xlabel("Stage")
plt.ylabel("Percentage Laid Off")
plt.xticks(rotation=90)
None;
