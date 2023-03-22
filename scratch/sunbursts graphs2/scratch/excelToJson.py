import pandas as pd
import json

# Read the Excel file into a pandas dataframe
df = pd.read_excel('exceldata.xlsx', usecols=[0, 1, 2, 3])

# Convert the dataframe to a dictionary
data = df.to_dict('records')

# Create a dictionary to hold the hierarchy
hierarchy = {}

# Iterate over the data and build the hierarchy
for row in data:
    node = hierarchy
    for level in row['Level 1':'Level 4']:
        if level not in node:
            node[level] = {}
        node = node[level]
    node['value'] = row['Value']

# Convert the hierarchy dictionary to JSON
json_data = json.dumps(hierarchy)

print(json_data)
