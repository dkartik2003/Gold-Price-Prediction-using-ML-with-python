This was a project which i wrote for a project  during my college.
Overview:-
This project aims to predict gold prices using machine learning techniques. The dataset contains historical gold price data along with various economic indicators. A Random Forest Regressor model is employed to forecast future gold prices based on these features.

Data:-
The dataset used for this project is a CSV file containing the following columns:

Date: Date of the record
Open: Opening price
High: Highest price of the day
Low: Lowest price of the day
Close: Closing price
Adj Close: Adjusted closing price
Volume: Trading volume
SP_open, SP_high, SP_low, SP_close, SP_Ajclose, SP_volume: Economic indicators from S&P
DJ_open, DJ_high, DJ_low, DJ_close, DJ_Ajclose, DJ_volume: Economic indicators from Dow Jones
EG_open, EG_high, EG_low, EG_close, EG_Ajclose, EG_volume: Economic indicators from EG
EU_Price, EU_open, EU_high, EU_low, EU_Trend: European market indicators
OF_Price, OF_Open, OF_High, OF_Low, OF_Volume, OF_Trend: Indicators from OF
OS_Price, OS_Open, OS_High, OS_Low, OS_Trend: Indicators from OS
SF_Price, SF_Open, SF_High, SF_Low, SF_Volume, SF_Trend: Indicators from SF
USB_Price, USB_Open, USB_High, USB_Low, USB_Trend: Indicators from USB
PLT_Price, PLT_Open, PLT_High, PLT_Low, PLT_Trend: Indicators from PLT
PLD_Price, PLD_Open, PLD_High, PLD_Low, PLD_Trend: Indicators from PLD
RHO_PRICE: Rho Price
USDI_Price, USDI_Open, USDI_High, USDI_Low, USDI_Volume, USDI_Trend: USDI indicators
GDX_Open, GDX_High, GDX_Low, GDX_Close, GDX_Adj Close, GDX_Volume: Indicators from GDX
USO_Open, USO_High, USO_Low, USO_Close, USO_Adj Close, USO_Volume: Indicators from USO


Methodology:-
Data Preprocessing: Loaded and explored the dataset to understand its structure and content. Removed non-numeric columns for correlation analysis.
Exploratory Data Analysis (EDA):
Calculated and visualized the correlation matrix.
Plotted the distribution of gold prices.
Feature Selection: Dropped non-relevant columns and prepared data for modeling.
Model Training: Used the Random Forest Regressor algorithm to train the model on the prepared dataset.
Model Evaluation: Evaluated the model's performance using the R-squared metric and visualized the predictions compared to actual values.



Installation:-
numpy
pandas
matplotlib
seaborn
scikit-learn
Install the required libraries using pip:


Results
The Random Forest Regressor model provides predictions for gold prices. The model's performance is evaluated using R-squared error, and results are visualized to compare actual vs. predicted prices.

