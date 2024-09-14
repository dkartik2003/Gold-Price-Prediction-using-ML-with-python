# Importing the Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

# Data Collection and Processing

# Loading the csv data to a Pandas DataFrame
gold_data = pd.read_csv(r'D:\ZMINEZ\ProjectsGit\Gold\goldprice.csv')  # Use raw string for the file path

# Print first 5 rows in the dataframe
print(gold_data.head())

# Print last 5 rows of the dataframe
print(gold_data.tail())

# Drop non-numeric columns for correlation calculation
numeric_data = gold_data.select_dtypes(include=[np.number])

# Calculate the correlation matrix
correlation = numeric_data.corr()

# Constructing a heatmap to understand the correlation
plt.figure(figsize=(8, 8))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size': 8}, cmap='Blues')
plt.show()  # Ensure the plot is shown

# Correlation values of GLD
print(correlation['GLD'])

# Checking the distribution of the GLD Price
sns.histplot(gold_data['GLD'], kde=True, color='green')  # Use histplot instead of distplot (deprecated)
plt.show()  # Ensure the plot is shown

# Prepare data for modeling
X = gold_data.drop(['Date', 'GLD'], axis=1)
Y = gold_data['GLD']

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Model Training: Random Forest Regressor
regressor = RandomForestRegressor(n_estimators=100)
# Training the model
regressor.fit(X_train, Y_train)

# Model Evaluation
# Prediction on Test Data
test_data_prediction = regressor.predict(X_test)
print(test_data_prediction)

# R squared error
error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared error : ", error_score)

# Compare the Actual Values and Predicted Values in a Plot
plt.figure(figsize=(10, 6))
plt.plot(Y_test.values, color='blue', label='Actual Value')
plt.plot(test_data_prediction, color='green', label='Predicted Value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('GLD Price')
plt.legend()
plt.show()  # Ensure the plot is shown
