import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
 
# Load your CSV file into a DataFrame
data = pd.read_csv('Cleaned_Electric_Vehicle_Population_Data.csv')
 
# Assuming the columns are named 'latitude' and 'longitude'
data = data.dropna(subset=['latitude', 'longitude'])
 
# Convert the DataFrame to a GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.longitude, data.latitude))
 
# Set the coordinate reference system (CRS) to WGS84 (lat/lon)
gdf.set_crs(epsg=4326, inplace=True)
 
# Convert to Web Mercator for compatibility with contextily basemaps
gdf = gdf.to_crs(epsg=3857)
 
# Plotting
fig, ax = plt.subplots(figsize=(10, 10))
# Adjust alpha to 0.3 for more transparency
gdf.plot(ax=ax, alpha=0.3, color='red', markersize=10)  # More transparent
 
# Add a basemap
ctx.add_basemap(ax)
 
# Adjust the axis to the limits of the data
ax.set_xlim([gdf.total_bounds[0], gdf.total_bounds[2]])
ax.set_ylim([gdf.total_bounds[1], gdf.total_bounds[3]])
ax.axis('off')  # Turn off the axis
 
plt.title('Electric Vehicle Population Heatmap')
plt.show()



