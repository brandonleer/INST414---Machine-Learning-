import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# load cleaned dataset
layoffs_ml = pd.read_csv("layoffs_clean.csv", header=0)
layoffs_ml.reset_index(drop=True, inplace=True)

stage = layoffs_ml.stage.astype('category').cat.codes
industry = layoffs_ml.industry.astype('category').cat.codes
region = layoffs_ml.region.astype('category').cat.codes

layoffs_features = ['stage', 'industry', 'region']

layoffs_ml["stage"] = layoffs_ml["stage"].astype('category')
layoffs_ml['stage'].astype('category').cat.codes

layoffs_ml["industry"] = layoffs_ml["industry"].astype('category')
layoffs_ml['industry'].astype('category').cat.codes

layoffs_ml["region"] = layoffs_ml["region"].astype('category')
layoffs_ml['region'].astype('category').cat.codes

X = layoff_features.values 
y = layoffs_ml.percentage_laid_off #target dataset

X = X.reshape(-1, 1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


from sklearn.metrics import explained_variance_score,mean_absolute_error

from sklearn.ensemble import RandomForestRegressor
#Creating an instance of random forest regressor
rf_regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
rf_regressor.fit(X, y)
y_pred_rf=rf_regressor.predict(X_test)
print('Variance score: %.2f', explained_variance_score(y_test, y_pred_rf))
print('MAE score: %.2f', mean_absolute_error(y_test, y_pred_rf))
