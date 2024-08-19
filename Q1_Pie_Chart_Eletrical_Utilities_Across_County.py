import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset into a Pandas DataFrame
EVcar = pd.read_csv('Cleaned_Electric_Vehicle_Population_Data.csv', header=0)

#Remove the extraspace to get exact unique count for provider
EVcar['Electric Utility'] = EVcar['Electric Utility'].str.replace(' ', '')

# Group the data by county and electrical utility providers
grouped_providers = EVcar.groupby('County')['Electric Utility'].apply(lambda x: ','.join(x))

# Split the concatenated provider names by comma and convert them into sets to remove duplicates
unique_providers_by_county = grouped_providers.str.split(',').apply(set)

# Calculate the length of each set to find the count of unique providers for each county
unique_provider_counts_by_county = unique_providers_by_county.apply(len)

# Get the top counties with the highest number of unique electrical utility providers
top_counties_pie = unique_provider_counts_by_county.nlargest(4)

#define custome colors
colors = ['#0077c2', '#8dc6f7', '#b7d9f1', '#c9e3f6']

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 10))

# Plot pie chart for distribution of electrical utility providers
axes[0].pie(top_counties_pie, labels=top_counties_pie.index, autopct='%1.1f%%', startangle=140, colors= colors)
axes[0].set_title('Distribution of Electrical Utility Providers Across the County', fontweight='bold')
axes[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

#Get the Counts of Electric Vehicles per County groub by VIN number
county_vehicle_counts = EVcar.groupby('County')['VIN (1-10)'].count().reset_index().sort_values(by='VIN (1-10)',ascending=False).reset_index(drop=True)
county_vehicle_counts.columns = ['County','Count']

# Get the top 4 counties with the highest number of electric vehicles
county_vehicle_counts_top = county_vehicle_counts.head(4)

# Plot bar chart for number of electric vehicles per county
sns.barplot(ax=axes[1], data=county_vehicle_counts_top, y="County", x="Count")
axes[1].set_title('Number of Electric Vehicles Per County', fontweight='bold')
axes[1].set_ylabel('County')
axes[1].set_xlabel('Number of Electric Vehicles')
axes[1].tick_params(axis='x', rotation=45)

# Add counts on the bars
for index, value in enumerate(county_vehicle_counts_top['Count']):
    axes[1].text(value, index, str(value), va='center', ha='left', color='black')

plt.tight_layout()
plt.show()




