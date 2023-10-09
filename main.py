# Import the pandas library as pd for data manipulation
import pandas as pd

# Import the matplotlib.pyplot module for data visualization
import matplotlib.pyplot as plt

# Read a CSV file named "Mobile phone price.csv" into a DataFrame named 'phone_csv'
phone_csv = pd.read_csv("Mobile phone price.csv")

# Get data types of columns
data_types = phone_csv.dtypes

# Get column names
columns = phone_csv.columns

# Get index information
index = phone_csv.index

# Get descriptive statistics of the DataFrame
description = phone_csv.describe()

# Get general information about the DataFrame
information = phone_csv.info()

# Calculate the mean of 'Battery Capacity (mAh)'
Mean_battery = phone_csv['Battery Capacity (mAh)'].mean()

# Display the first few rows of the DataFrame
head = phone_csv.head()

# Display the last few rows of the DataFrame
tail = phone_csv.tail()

# Create a Series 'birds' with custom index values
birds = pd.Series(['crow', 'pigeon', 'parrot', 'winged donkey', 'eagle'], index=[0, 3, 9, 8, 3])

# Access elements using label-based and position-based indexing
print(birds.loc[8])
print(birds.iloc[3])

# Filter phones with 'Battery Capacity (mAh)' equal to 4000
mah_4000 = phone_csv[phone_csv['Battery Capacity (mAh)'] == 4000]

# Create a cross-tabulation between 'RAM' and 'Price'
crosstab = pd.crosstab(phone_csv['RAM '], phone_csv['Price ($)'])

# Group by 'Brand' and calculate the mean of 'Battery Capacity (mAh)'
comparison = phone_csv.groupby('Brand')['Battery Capacity (mAh)'].mean()

# Create a figure and plot 'Battery Capacity (mAh)'
fig1 = plt.figure('Figure 1')
phone_csv['Battery Capacity (mAh)'].plot()

# Create another figure and plot a histogram of 'Battery Capacity (mAh)'
fig2 = plt.figure('Figure 2')
phone_csv['Battery Capacity (mAh)'].hist()

# Clean 'Price ($)' column by removing $ and converting to integer
phone_csv['Price ($)'] = phone_csv['Price ($)'].str.replace('$', '')
phone_csv['Price ($)'] = phone_csv['Price ($)'].str.replace(',', '').astype(int)

# Create a third figure and plot 'Price ($)'
fig3 = plt.figure('Figure 3')
phone_csv['Price ($)'].plot()
