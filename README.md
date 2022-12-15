# Leer_INST414_Project- 

Currently many seniors in college and recent new graduates struggle to find jobs in the times after they graduate. In 2022 as interest rates increase and 
the looming threat of recession comes closer, many companies have annouced significant layoffs. According to investopedia, many big name companies such as Google, Amazon, Meta, Snap, gopuff, Wells Fargo, and Credit Suisse are all undergoing signigicant layoffs in 2022. These layoffs are only making it more difficlt for seniors and new graduates to get offers, and can be caused by factors such as location, industry, and funding stage. This report aims to analyze these factors and predict the percetage of employyes laid off so applicants can focus their attention to the companies with the most opperuntity. A companies location, industry, percentage laif off, date of layoff, stage of funding, and country will be used to answer the question:

Is there a trend in companies across the United States, where some industries have less of a percentage of layoffs than others? By knowing which industries in the United States have more have a smaller amount of layoffs, new graduates can then look there for more available oppertunieies. 

Results:



Data

Description of Data
The dependent variable for the analysis is percentage laid off. This is the percentage laid off of each U.S company on the Layoffs dataset. These percentages were gathered from Bloomberg, San Fransico Business Times, TechCrunch. and The New York Times. The independent variables are composed of name, location, industry, stage of funding, layoff date, country, and funding. 

Location
This variable is the location (city) of the layoff. In order to analyze this, the variable was changed into only U.S cities and levels, where a value or state would be assigned to either

West = ['SF Bay Area', 'Salt Lake City', 'Los Angeles', 'Seattle', 'Phoenix', 'Sacremento', 'San Diego', 'Denver', 'Portland']
Northeast = ['New York City', 'Boston', 'Dover', 'Pittsburg', 'Philadelphia', 'Stamford', 'Washington D.C'] 
Midwest = ['St. Louis', 'Detroit', 'Kansas City', 'Boulder', 'Chicago', 'Milwaukee', 'Lexington', 'Columbus', 'Cincinnati', 'Minneapolis']
South = ['Atlanta', 'Mexico City', 'Dallas', 'Austin', 'Miami', 'Nashville']

Industry
This variable is the industry of the company. This values include finance, education, product, realestate, healrhcare, consumer, sales, crypto, trabsaportation, marketing, scurity, and more

Percentage Laid Off
This variable is the percentage of employees that were laid off at each company. 

Stage of Funding
This variable represents the current stage of funding that the company is in such as unknown, series b, ipo, series d, and series c. 

Method
The data was dowloaded as a csv file from Kaggles database. Then, in a python notebook with the pandas, numpy, and re libaraies a script was run. This script read the file showing a total of 1801 rows (companies) and 9 columns (company, location, industry, total laid off, percentage laid off, date, stage, country, funds raised. The data was cleaned by adjusting the dates to only layoffs during 2022. After that, the country column was adjusted to just layoffs in the United States. To clean the dataframe up I then dropped the total laid off, funds raised, country, and date columns. Also to make the percentage laid off column more readable multipled the values by 100 so they were in percent form. Next, to ensure there were only companies in the daatframe with present values, all na values were dropped. In order to be able to look at companies by region I created a new column that seperated the U.S cities into the Northeast, West, South, and Midwest. Lastly, the oriinal location column was dropped. The resulting dataframe was 482 rows and 5 columns representing individual companies. 

Analysis
Before running machine algorithms on the data, the industries variable had to be numerically encoded. Midwest was encoded as 1, Northeast as 2, South as 3, and West as 4. Big was encoded as 1, Medium as 2, and Small as 3. The dataset was split into a training set and a test set, where 20% of the data would be for testing, and 80% would be for training. The Random Forest Regression algorithm was then used on the dataset to produce a model that would predict company ratings.





