import json
import pandas as pd

# Specify the path of your json file
json_file = r"C:\Users\Peace Paix\Documents\Web Scraping\Amazon Web Scraping\Pages Snapshots\all_data.json"

# Load the json file
with open(json_file) as f:
    data = json.load(f)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Write the data to a CSV file
df.to_csv(r"C:\Users\Peace Paix\Documents\Web Scraping\all_data.csv", index=False)
