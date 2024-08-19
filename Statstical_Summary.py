import pandas as pd
import numpy as np
from IPython.display import display

# Reading the csv file into dataframe
EVcar = pd.read_csv('Cleaned_Electric_Vehicle_Population_Data.csv', header=0)

# Getting the total rows & columns
print("Total Rows & Columns")
print(EVcar.shape)

# Some General info about the dataframe
print("General info")
print(EVcar.info())

#set the display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Some basic statistical characteristics of each numerical columns

# Compute the descriptive statistics
print("Statistics on Numerical datatypes\n")
stats_num = EVcar[['Base MSRP', 'Electric Range']].describe() # Compute the descriptive statistics
print(stats_num)

#-------------- Summary Statistic of Base MSRP column ----------------
print("Summary Statistic of Base MSRP column")
#describe the Base MSRP column
print(EVcar['Base MSRP'].describe())

print("Individual Statistics for Base MSRP Column\n")
print(f"Mean of the Base MSRP: {EVcar['Base MSRP'].mean():.2f}\n") #Calculate mean value
print(f"Standard deviation value of the Base MSRP: {EVcar['Base MSRP'].std():.2f}\n")  #Find the Standard deviation 
print(f"Min value of the Base MSRP: {EVcar['Base MSRP'].min():.2f}\n")  #Find the minimum value
print(f"25th percentile of the Base MSRP: {EVcar['Base MSRP'].quantile(0.25):.2f}\n") #Calculate the 25th Percentile
print(f"Median of the Base MSRP: {EVcar['Base MSRP'].median():.2f}\n") #Calculate median value
print(f"75th percentile of the Base MSRP: {EVcar['Base MSRP'].quantile(0.75):.2f}\n") #Calculate the 75th Percentile
print(f"Max value of the Base MSRP: {EVcar['Base MSRP'].max():.2f}\n")  #Find the maximum value

mode_value = EVcar['Base MSRP'].mode().iloc[0]  #Calculate mode value
print(f"Mode of the Base MSRP: {mode_value:.2f}\n") 


#-------------- Summary Statistic of Electric Range column ----------------
print("Summary Statistic of Electric Range column")
#describe the Electric Range column
print(EVcar['Electric Range'].describe())

print("Individual Statistics for Electric Range\n")
print(f"Mean of the Electric Range: {EVcar['Electric Range'].mean():.2f}\n") #Calculate mean value 
print(f"Standard deviation value of the Electric Range: {EVcar['Electric Range'].std():.2f}\n")  #Find the Standard deviation 
print(f"Min value of the Electric Range: {EVcar['Electric Range'].min():.2f}\n")  #Find the minimum value
print(f"25th percentile of the Electric Range: {EVcar['Electric Range'].quantile(0.25):.2f}\n") #Calculate the 25th Percentile
print(f"Median of the Electric Range: {EVcar['Electric Range'].median():.2f}\n") #Calculate median value
print(f"75th percentile of the Electric Range: {EVcar['Electric Range'].quantile(0.75):.2f}\n") #Calculate the 75th Percentile
print(f"Max value of the Electric Range: {EVcar['Electric Range'].max():.2f}\n")  #Find the maximum value

mode_value = EVcar['Electric Range'].mode().iloc[0]  #Calculate mode value
print(f"Mode of the Electric Range: {mode_value:.2f}\n")

#--------------Ensure that ther is no missing values-------------

print("Number of null values")
null_values = EVcar.isnull().sum()
print(null_values)

#--------------Statistics on non-numerical datatypes-----------------
print("Statistics on Non-Numerical datatypes")
stats_obj = EVcar[['Model', 'Make', 'Electric Vehicle Type', 'County', 'City', 'State']].describe(include=["object"]) # Compute the descriptive statistics
print(stats_obj) # Display the statistics

#-----------------Statistic Summary of Total Vehicle Counts Column------------------------------

# Reading the csv file into dataframe
df = pd.read_csv('Electric_Vehicle_Population_Size_History_By_County_.csv', header=0)

# Filter the dataset for the state of WA and the year 2023
df['Date'] = pd.to_datetime(df['Date'])
filtered_df = df[(df['State'] == 'WA') & (df['Date'].dt.year == 2023)]

# Convert the 'Total Vehicles' column to numeric, removing commas
filtered_df['Total Vehicles'] = filtered_df['Total Vehicles'].str.replace(',', '').astype(float)

#drop the null values rows
filtered_df.dropna()

#set the display formate 
pd.options.display.float_format = '{:.2f}'.format

#print the describe function
print("Summary Statistic of total vehicle counts column")
print(filtered_df['Total Vehicles'].describe(),"\n")

# Calculate the required statistics
mean_total_vehicles = filtered_df['Total Vehicles'].mean()
std_total_vehicles = filtered_df['Total Vehicles'].std()
min_total_vehicles = filtered_df['Total Vehicles'].min()
median_total_vehicles = filtered_df['Total Vehicles'].median()
max_total_vehicles = filtered_df['Total Vehicles'].max()

# Print the Statistic Summary 
print(f"Individual statistic summary for total vehicle counts:\n")
print(f"Mean value of total vehicle counts: {mean_total_vehicles:.2f}\n")
print(f"Standard Deviation value of total vehicle counts: {std_total_vehicles:,.2f}\n")
print(f"Minimum value of  total vehicle counts: {min_total_vehicles:,.2f}\n")
print(f"Median value of total vehicle counts: {median_total_vehicles:,.2f}\n")
print(f"Maximum of total vehicle counts: {max_total_vehicles:.2f}\n")








