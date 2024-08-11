import csv
import re

def remove_reference(rule):
    # Remove reference if exists
    return re.sub(r'\s*reference\s*:[^;]+;', '', rule)

# Read data from All data CSV file
with open(r"Pre fine tuning DB\Train_Test_Data\combined_data.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

# Create a dictionary to store rules by SID
for row in rows:
    row['Rule'] = remove_reference(row['Rule'])

# Write updated rows to a new CSV file
with open(r"Pre fine tuning DB\Train_Test_Data\combined_data_fix.csv", 'w', newline='') as csv_file:
    fieldnames = ['SID', 'URL', 'MITRE Technique ID', 'Rule']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)




# Read data from test CSV file
with open(r"Pre fine tuning DB\Train_Test_Data\test_data.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

# Create a dictionary to store rules by SID
for row in rows:
    row['Rule'] = remove_reference(row['Rule'])

# Write updated rows to a new CSV file
with open(r"Pre fine tuning DB\Train_Test_Data\test_data_fix.csv", 'w', newline='') as csv_file:
    fieldnames = ['Sid', 'URL', 'technique ids', 'Rule']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)


# Read data from train CSV file
with open(r"Pre fine tuning DB\Train_Test_Data\train_data.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

# Create a dictionary to store rules by SID
for row in rows:
    row['Rule'] = remove_reference(row['Rule'])

# Write updated rows to a new CSV file
with open(r"Pre fine tuning DB\Train_Test_Data\train_data_fix.csv", 'w', newline='') as csv_file:
    fieldnames = ['Sid', 'URL', 'technique ids', 'Rule']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("CSV file updated successfully.")