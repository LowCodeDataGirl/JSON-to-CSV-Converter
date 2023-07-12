import json
import pandas as pd

# Specify the path of your JSON file
json_file = r"C:\Users\Peace\Path\data.json"

# Load the json file
with open(json_file) as f:
    data = json.load(f)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Write the data to a CSV file
df.to_csv(r"C:\Users\Peace\data.csv", index=False)
