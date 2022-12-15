import pandas as pd
import numpy as np
import re

West = ['SF Bay Area', 'Salt Lake City', 'Los Angeles', 'Seattle', 'Phoenix', 'Sacremento', 'San Diego', 'Denver', 'Portland']
Northeast = ['New York City', 'Boston', 'Dover', 'Pittsburg', 'Philadelphia', 'Stamford', 'Washington D.C'] 
Midwest = ['St. Louis', 'Detroit', 'Kansas City', 'Boulder', 'Chicago', 'Milwaukee', 'Lexington', 'Columbus', 'Cincinnati', 'Minneapolis']
South = ['Atlanta', 'Mexico City', 'Dallas', 'Austin', 'Miami', 'Nashville']

layoffs = pd.read_csv("layoffs.csv", header=0)

layoffs = layoffs[(layoffs['date'] > '2022-01-01') & (layoffs['date'] <= '2022-30-12')]
layoffs = layoffs[layoffs['country'] == 'United States']
layoffs = layoffs[layoffs.location != 'London']
layoffs = layoffs.drop(['total_laid_off', 'funds_raised', 'country', 'date'], axis=1)
layoffs['percentage_laid_off'] = layoffs['percentage_laid_off'] * 100 
layoffs = layoffs.dropna()

c1 = layoffs['location'].isin(West)
c2 = layoffs['location'].isin(Northeast)
c3 = layoffs['location'].isin(Midwest)
c4 = layoffs['location'].isin(South)

layoffs = layoffs.assign(region=np.select([c1, c2, c3, c4], ['West', 'Northeast', 'Midwest', 'South']))
layoffs = layoffs.drop(['location'], axis=1)

layoffs.to_csv("layoffs_clean.csv")
