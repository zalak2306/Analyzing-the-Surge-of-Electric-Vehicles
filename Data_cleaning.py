
import pandas as pd
import numpy as np
import re


# Reading the csv file into dataframe
EVcar = pd.read_csv('Electric_Vehicle_Population_Data.csv', header=0)

# Check whether the data gets loaded properly.

# print(EVcar.head())
# print(EVcar.describe())
# print(EVcar.info())
# print(len(EVcar.columns))
# print(EVcar.shape)


# -----------------------------------Data Cleaning -----------------------------------------------------

# ------------------------Cleaning Electric Vehicle Type Column------------------------

# Replace the EV type value ( BEV and PHEV )

EVcar['Electric Vehicle Type'] = EVcar['Electric Vehicle Type'].str.replace('Battery Electric Vehicle \(BEV\)', 'BEV', regex=True, case=False)
EVcar['Electric Vehicle Type'] = EVcar['Electric Vehicle Type'].str.replace('Plug-in Hybrid Electric Vehicle \(PHEV\)', 'PHEV', regex=True, case=False)
#print(EVcar['Electric Vehicle Type'].head(10))

# # #-----------------------Cleaning Base Price Column-----------------------------------

# Filter the DataFrame for rows where 'Base MSRP' is not 0
nonzero_baseprice_range = EVcar[EVcar['Base MSRP'] != 0]

# Calculate average electric range for each combination of 'model year' and 'Model'
avg_baseprice_range = nonzero_baseprice_range.groupby(['Model Year', 'Model'])['Base MSRP'].mean()

# Replace 0 values in 'Base MSRP' column with NaN
EVcar['Base MSRP'] = EVcar['Base MSRP'].replace(0, np.nan)

# Fill NaN values in 'Base MSRP' column with average baseprice range for each combination of 'Model Year' and 'Model'
EVcar['Base MSRP'] = EVcar.apply(lambda row: avg_baseprice_range.get((row['Model Year'], row['Model']), row['Base MSRP']), axis=1) 


#print(EVcar['Base MSRP'].head(10))


#-------------------------Cleaning Electric Range Column------------------------------

# Filter the DataFrame for rows where 'Electric Range' is not 0
nonzero_electric_range = EVcar[EVcar['Electric Range'] != 0]

# # Calculate average electric range for each combination of 'EV Type' and 'Model'
avg_electric_range = nonzero_electric_range.groupby(['Electric Vehicle Type', 'Model'])['Electric Range'].mean()

# Replace 0 values in 'Electric Range' column with NaN
EVcar['Electric Range'] = EVcar['Electric Range'].replace(0, np.nan)

# Fill NaN values in Electric Range column with average electric range for each combination of 'EV Type' and 'Model'
EVcar['Electric Range'] = EVcar.apply(lambda row: avg_electric_range.get((row['Electric Vehicle Type'], row['Model']), row['Electric Range']), axis=1)

#print(EVcar['Electric Range'].head(10))


# #------------------Check that Base MSRP and Electric Range has non-zero values-----------

# Check if all values in a column are non-zero
columns_to_check = ['Electric Range', 'Base MSRP']
no_zero_values = EVcar[columns_to_check].ne(0).all()

# #print("Columns with no zero values:", no_zero_values[no_zero_values].index.tolist())


# #------------Cleaning Clean Alternative Fuel Vehicle (CAFV) Eligibility column------------

#Replace the Clean Alternative Fuel Vehicle (CAFV) Eligibility column value according to eligibility

EVcar.rename(columns={'Clean Alternative Fuel Vehicle (CAFV) Eligibility' : 'CAFV Eligibility'}, inplace=True)
EVcar['CAFV Eligibility'] = EVcar['CAFV Eligibility'].str.replace('Clean Alternative Fuel Vehicle Eligible', 'Eligible', regex=False, case=False)
EVcar['CAFV Eligibility'] = EVcar['CAFV Eligibility'].str.replace('Eligibility unknown as battery range has not been researched', 'Unknown Eligibility', regex=False, case=False)
EVcar['CAFV Eligibility'] = EVcar['CAFV Eligibility'].str.replace('Not eligible due to low battery range', 'Not Eligible', regex=False, case=False)
#print(EVcar['CAFV Eligibility'])

#print(EVcar['CAFV Eligibility'].head(10))


# #-----------------------Cleaning Vehicle Location column--------------------

# Define a function to extract coordinates 

def extract_coordinates(point): 

    # Ensure point is a string before applying regex 

    if isinstance(point, str): 

        match = re.search(r'POINT \((-?\d+\.\d+) (-?\d+\.\d+)\)', point) 

        if match: 

            # Return the extracted latitude and longitude as floats 

            return float(match.group(2)), float(match.group(1)) 

    # In case of invalid or missing data, return None for both latitude and longitude 

    return None, None 
# Apply the extraction function to each value in 'vehicle location' 
EVcar['latitude'], EVcar['longitude'] = zip(*EVcar['Vehicle Location'].apply(extract_coordinates)) 

# Check if the new columns are created properly 
#print(EVcar[['latitude', 'longitude']].head(10))

# #---------------------Cleaning Electric Utility Column-----------------------------

# Convert Electric Utility column values to lowercase
EVcar['Electric Utility'] = EVcar['Electric Utility'].str.lower()

# Replace '|' with ',' in 'Electric Utility' column then replace ',,' with ','
EVcar['Electric Utility'] = EVcar['Electric Utility'].str.replace('|', ',').str.replace(',,', ',')

#Remove ' - (wa)' in Electric Utility column
EVcar['Electric Utility'] = EVcar['Electric Utility'].str.replace(' - \(wa\)', '', regex=True, case=False)

print(EVcar['Electric Utility'].head(10))

# #---------------------Drop duplicate rows------------------------

EVcar = EVcar.drop_duplicates()

# #--------------------Drop rows with null values------------------

EVcar = EVcar.dropna()

# print(EVcar['Electric Range'].head(10))

#--------------Ensure that ther is no missing values-------------

null_values = EVcar.isnull().sum()
# print(null_values)


#----------Convert the Postal Code datatype from float to int---------
EVcar['Postal Code'] = EVcar['Postal Code'].round().astype(int)

#------------------Cleaning Model Year Column-------------------

EVcar['Model Year'] = pd.to_datetime(EVcar['Model Year'], format='%Y').dt.year

# print(EVcar['Electric Utility'].head(10))


#------------------Create new cleaned file--------------------------


EVcar.to_csv('Cleaned_Electric_Vehicle_Population_Data.csv', index=False)






