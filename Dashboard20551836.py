import pandas as pd
import folium
import matplotlib.pyplot as plt
# (((Putting Airports Coordinates On A Map)))

# Read CSV file containing latitude and longitude values
df = pd.read_csv('airports.csv')

# Create map object centered at the mean of the latitude and longitude values
airportmap = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)

# Add markers to map for each location in CSV file
for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Name']).add_to(map)

# Save map to HTML file
airportmap.save('map.html')
#////////////////

#(((Creating A Histogram with Using the Database Time zones as the category/bins)))
# Read the CSV file into a pandas DataFrame
TZdata = pd.read_csv('airports.csv')

# Separate the categorical data into a list
categories = TZdata['DB Time Zone'].unique().tolist()

# Create histogram
fig, ax = plt.subplots()
ax.hist(TZdata['DB Time Zone'], bins=len(categories))
ax.set_xlabel('DB Time Zone')
ax.set_ylabel('Airport Frequency')
ax.set_title('Histogram of Time zone frequency of Airports')

# Add category labels to the histogram
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories)

plt.show()
#///////////////
# (((Showing The percentages of different plane types on a pie chart)))
# Read the CSV file into a pandas DataFrame
planedata = pd.read_csv('planes.csv')

# Extract the first word from the column 'Column_name' and create a new column 'Category'
planedata['Category'] = planedata['Name'].str.split().str[0]

# Group the data by 'Category' and count the number of occurrences
grouped_data = planedata.groupby('Category').size().reset_index(name='Counts')

# Calculate the percentage for each category
grouped_data['Percentages'] = grouped_data['Counts'] / grouped_data['Counts'].sum() * 100

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(grouped_data['Percentages'], labels=grouped_data['Category'], autopct='%1.1f%%')
ax.set_title('Pie Chart of Categories')

plt.show()

# (((Showing The number of active airlines)))
# Read the CSV file into a pandas DataFrame
airlinedata = pd.read_csv('data.csv')

# Filter the data based on 'yes' values in the 'Yes/No' column
yes_count = airlinedata[airlinedata['Active'] == 'Y'].shape[0]

# Print the count of 'yes' occurrences
print("The number of active airlines is", yes_count)

