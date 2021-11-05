import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

# Taking a look at the dataset
print(london_data.head())
# Looking through rows 100 to 199
print(london_data.iloc[100:200])

# Taking a look at the number of data points we have
print(len(london_data))

# Looking at the temperature column
temp = london_data['TemperatureC']

# Computing the average temperature in 2015
average_temp = np.mean(temp)

# Computing the variance of the temperature column
temperature_var = np.var(temp)
print(temperature_var)

# Computing the standard deviation of the temperature column
temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)

# Analysing for columns that will help us group by months
print(london_data.head())
print(london_data.tail())

# Selecting temperature rows from the month of June '6'
june = london_data.loc[london_data['month']==6]['TemperatureC']

# Selecting temperature rows from the month of July '7'
july = london_data.loc[london_data['month']==7]['TemperatureC']

# Calculating the mean temperature in London for both June and July
june_mean = np.mean(june)
july_mean = np.mean(july)

# Computing standard deviation for both june and july based on temperature
june_std = np.std(june)
print('Standard Deviation for June is ', june_std)

july_std = np.std(july)
print('Standard Deviation for June is ', july_std)

# Calculating the mean and standard deviation for every month.
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")


# The rainiest month is 8 (August)
rainiest_month = london_data.loc[london_data['dailyrainMM'] == london_data.dailyrainMM.max()]['month']
print('The rainiest month is :',rainiest_month.head(1), "'August'")
