import polyline
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString
import contextily as ctx

df = pd.read_csv('strava-api\data\Running Data Final.csv')

print(df.head())

# Function to plot a map from a polyline
def plot_map(polyline_str):
    # Decode the polyline string
    coordinates = polyline.decode(polyline_str)
    
    coordinates = [(lon, lat) for lat, lon in coordinates]

    # Create a GeoDataFrame from the coordinates
    gdf = gpd.GeoDataFrame(geometry=[LineString(coordinates)], crs="EPSG:4326")

    # Transform the GeoDataFrame to EPSG:3857
    gdf = gdf.to_crs(epsg=3857)

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot the polyline on the map
    gdf.plot(ax=ax, linestyle='-', color='#fc4c02', linewidth=4)

    # Add the basemap
    ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)

    # Remove the axis markers and labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Set the bounding box to ensure proper display
    xmin, ymin, xmax, ymax = gdf.total_bounds
    if not any(map(lambda v: pd.isna(v) or pd.isnull(v), [xmin, ymin, xmax, ymax])):
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)

    # Display the plot
    plt.show()

# Plot the map for the first polyline in the dataset
plot_map(df['map.summary_polyline'].iloc[0])