Machine Learning Project 

For many seniors in college and recent new graduates finding a job with little to no experience on your resume, can be a difficult task. On top of this as interest rates increase and the looming threat of recession comes closer, many companies have annouced significant layoffs such as Google, Amazon, Meta, Snap, gopuff, Wells Fargo, and Credit Suisse according to investopedia. These layoffs are only making it more difficlt for seniors and new graduates to get offers, as companies cant afford to hire more employees.  This report aims to analyze factors such as industry, stage of funding, and region with regard to the percentage of employyes laid off. This could allow for new gradiates to focus their job searches where the most oppertuntity is present. 

A companies location, industry, percentage laif off, date of layoff, stage of funding, and country will be used to answer the question:

Is there a trend in companies across the United States in 2022, where certain industries, stages of funding, and regions have less of a percentage of layoffs than others? By knowing how well these factors influence a companies layoff percentages new graduates can tailor their job search to find the most oppertunity. 

Results from the report suggests that there is not a trend and that the region, industry, and stage of funding of a company cannot be used to determine a company’s layoff percentages. This report will describe the data that was used, explain the methods and analysis, describe the results that were found, and conclude on the findings.


Data

Description of Data
The dependent variable for the analysis is percentage laid off. This is the percentage laid off of each U.S company on the Layoffs dataset. These percentages were gathered from Bloomberg, San Fransico Business Times, TechCrunch. and The New York Times as according to kaggles website. The independent variables are composed of location, industry, stage of funding, and funding. 

Location
This variable is the location (city) of the layoff. In order to analyze this, the variable was changed into only U.S cities and regions, where a value or state would be assigned to the following then encoded for machine learning.  

West = ['SF Bay Area', 'Salt Lake City', 'Los Angeles', 'Seattle', 'Phoenix', 'Sacremento', 'San Diego', 'Denver', 'Portland']
Northeast = ['New York City', 'Boston', 'Dover', 'Pittsburg', 'Philadelphia', 'Stamford', 'Washington D.C'] 
Midwest = ['St. Louis', 'Detroit', 'Kansas City', 'Boulder', 'Chicago', 'Milwaukee', 'Lexington', 'Columbus', 'Cincinnati', 'Minneapolis']
South = ['Atlanta', 'Mexico City', 'Dallas', 'Austin', 'Miami', 'Nashville']

Industry
This variable is the industry of the company. This values include finance, education, product, realestate, healrhcare, consumer, sales, crypto, trabsaportation, marketing, scurity, and more. encoded for use in machine leaning. 

Percentage Laid Off
This variable is the percentage of employees that were laid off at each company. 

Stage of Funding
This variable represents the current stage of funding that the company is in such as unknown, series b, ipo, series d, and series c. 

Method
The data was dowloaded as a csv file from Kaggles database. Then, in a python notebook with the pandas, numpy, and re libaraies a script was run. This script read the file showing a total of 1801 rows (companies) and 9 columns (company, location, industry, total laid off, percentage laid off, date, stage, country, funds raised. The data was cleaned by adjusting the dates to only layoffs during 2022. After that, the country column was adjusted to just layoffs in the United States. To clean the dataframe up I then dropped the total laid off, funds raised, country, and date columns. Also to make the percentage laid off column more readable multipled the values by 100 so they were in percent form. Next, to ensure there were only companies in the daatframe with present values, all na values were dropped. In order to be able to look at companies by region I created a new column that seperated the U.S cities into the Northeast, West, South, and Midwest. Lastly, the oriinal location column was dropped. The resulting dataframe was 482 rows and 5 columns representing individual companies. 

Analysis
Before running the random forrest regressor on the data, the industries, stage of funding, and region variables had to be numerically encoded using cat codes. The dataset was then split into a training set and a test set, where 20% of the data would be for testing, and 80% would be for training. The Random Forest Regression algorithm was then used on the dataset to produce a model that would predict a companies percentage of layoffs. 

Results
The model had a variance score of about 27%, which means that the predictor variables can explain 27% of the change that is happening with the company layoff percentages. This suggests that region, stage of funding, and industry will not be able to likely predict how many people a company laysoff. The model also had a mean absolute error of about 14.57%, which is acceptable.

Conclusion
The purpose of this report was to answer the question: Is there a trend in companies across the United States in 2022, where certain industries, stages of funding, and regions have less of a percentage of layoffs than others? From the analysis, it was found that there is not trend, as the model was not able to explain a high percentage of the change in layoffs. Therefore, it cannot predict how many layoofs a company would have if it were for example a companies located in the northeast region, ipo stage of funding, and in the finance industry. In order for more robust model, it is recommended that a dataset with more records of at least 10,000 and more variables such as the amount of employees at the companu and the age of the company could be used to train the model and produce more accurate results.

Appendix:

Machine learning script: https://github.com/brandonleer/Leer_INST414_Project-/blob/ef430c80683c62482969437479e034e092f7623c/layoffs_ml.py

Data Cleaing script: https://github.com/brandonleer/Leer_INST414_Project-/blob/ef430c80683c62482969437479e034e092f7623c/layoffs_clean.py

Data Set: https://github.com/brandonleer/Leer_INST414_Project-/blob/ef430c80683c62482969437479e034e092f7623c/layoffs.csv

Cleaned data set: https://github.com/brandonleer/Leer_INST414_Project-/blob/ef430c80683c62482969437479e034e092f7623c/layoffs_clean.csv




