import csv
import re

def remove_reference(rule):
    # Remove reference if exists
    return re.sub(r'\s*reference\s*:[^;]+;', '', rule)

def extract_rule_id(rule):
    # Extract SID from the rule
    match = re.search(r'sid:(\d+);', rule)
    if match:
        return match.group(1)
    else:
        return None

# Read the rules from rules.txt
with open('rules.txt', 'r') as f:
    rules = f.readlines()

# Create a dictionary to store rules by SID
rule_dict = {}
for rule in rules:
    sid = extract_rule_id(rule)
    if sid:
        rule_dict[sid] = remove_reference(rule)

# Read the CSV file and update rules for SIDs with "nan"
with open('sorted_ground_truth.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

for row in rows:
    if row['Rule'] == 'nan':
        sid = row['SID']
        if sid in rule_dict:
            row['Rule'] = rule_dict[sid]

# Write updated rows to a new CSV file
with open('sorted_ground_truth.csv', 'w', newline='') as csv_file:
    fieldnames = ['SID', 'URL', 'MITRE Technique ID', 'Rule']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("CSV file updated successfully.")
