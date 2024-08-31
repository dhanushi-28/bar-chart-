import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from folium import Map, Circle, Marker
from folium.plugins import HeatMap

# Step 1: Data Collection
# Simulating a dataset for demonstration purposes
data = {
    'date_time': ['2024-08-25 14:30', '2024-08-26 09:15', '2024-08-26 18:45', '2024-08-27 22:30', '2024-08-28 07:00'],
    'location': ['Point A', 'Point B', 'Point A', 'Point C', 'Point B'],
    'latitude': [40.7128, 40.7138, 40.7128, 40.7148, 40.7138],
    'longitude': [-74.0060, -74.0070, -74.0060, -74.0080, -74.0070],
    'road_condition': ['Wet', 'Dry', 'Wet', 'Wet', 'Dry'],
    'weather': ['Rain', 'Clear', 'Rain', 'Rain', 'Clear'],
    'time_of_day': ['Afternoon', 'Morning', 'Evening', 'Night', 'Morning']
}
df = pd.DataFrame(data)

# Convert date_time to datetime format
df['date_time'] = pd.to_datetime(df['date_time'])

# Step 2: Preprocessing
# Extract day of the week and hour
df['day_of_week'] = df['date_time'].dt.day_name()
df['hour'] = df['date_time'].dt.hour

# Step 3: Exploratory Data Analysis (EDA)
# Analyze the distribution of accidents by road condition, weather, and time of day
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='road_condition', hue='weather', palette='coolwarm')
plt.title('Accidents by Road Condition and Weather')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='time_of_day', hue='weather', palette='coolwarm')
plt.title('Accidents by Time of Day and Weather')
plt.show()

# Step 4: Visualization - Accident Hotspots
# Create a base map
base_map = Map(location=[40.7128, -74.0060], zoom_start=12)

# Add accident data as points
for i, row in df.iterrows():
    Circle(
        location=(row['latitude'], row['longitude']),
        radius=50,
        color='red',
        fill=True,
        fill_color='red'
    ).add_to(base_map)

# Generate heatmap
heat_data = [[row['latitude'], row['longitude']] for index, row in df.iterrows()]
HeatMap(heat_data).add_to(base_map)

# Display the map
base_map.save('traffic_accident_hotspots.html')
