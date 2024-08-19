import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset into a Pandas DataFrame
EVcar = pd.read_csv('TESLA_DATA.csv', header=0)

# Replace 0 values in 'Electric Range' with NaN
EVcar['Electric Range'] = EVcar['Electric Range'].replace(0, float('nan'))

# Drop duplicates and rows with NaN values in 'Electric Range'
EVcar = EVcar.drop_duplicates()
EVcar = EVcar.dropna()


# Filter the data for three specific Tesla models
tesla_models = ['MODEL S', 'MODEL 3', 'MODEL X']
filtered_data = EVcar[EVcar['Model'].isin(tesla_models)]

# # Group the filtered data by model year and calculate the average electric range
average_range = filtered_data.groupby(['Model', 'Model Year'])['Electric Range'].mean().reset_index()

#print(average_range)

specific_years = [2016, 2017, 2018, 2019, 2020]  # Example: specify the years you want to include
avg_range_specific_years = average_range[average_range['Model Year'].isin(specific_years)]

# Pivot the table 
pivot_table = avg_range_specific_years.pivot(index='Model Year', columns='Model', values='Electric Range')

# Plot the line graph
plt.figure(figsize=(12, 6))
for model in pivot_table.columns:
    plt.plot(pivot_table.index, pivot_table[model], marker='o', label=model)
    for x, y in zip(pivot_table.index, pivot_table[model]):
        plt.text(x, y, f'{y:.2f}', ha='center', va='bottom')  # Add value directly on the line

plt.title('Yearly Electric Range Variation in Tesla Models', fontweight='bold')
plt.xlabel('Model Year')
plt.ylabel('Electric Range (miles)')
plt.legend(title='Tesla Models', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
