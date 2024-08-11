import json
import os

# Directory containing the JSON files
json_directory = r'Semester_A\Extract data from MITRE ATTACK\techniques_split'

# List all JSON files in the directory
json_files = [f for f in os.listdir(json_directory) if f.endswith('.json')]

# Initialize an empty list to hold the combined data
combined_data = []

# Loop through each JSON file and append its data to the combined_data list
for json_file in json_files:
    with open(os.path.join(json_directory, json_file), 'r') as file:
        data = json.load(file)
        combined_data.append(data)

# Write the combined data to a new JSON file
output_file = r'Semester_A\Extract data from MITRE ATTACK\combined_techniques_split.json'  # Name of the output file
with open(output_file, 'w') as file:
    json.dump(combined_data, file, indent=4)

print(f"Combined JSON data has been written to {output_file}")
