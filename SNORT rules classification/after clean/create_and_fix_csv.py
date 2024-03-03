import pandas as pd
import re

# Read the CSV file
df = pd.read_csv("SNORT rules classification\\after clean\\ground_truth_new.csv")

# Remove the ,Unnamed: 4,Unnamed: 5
df = df.drop(columns=["Unnamed: 4", "Unnamed: 5"])

# Sort the "sid" column
df.sort_values("SID", inplace=True)

# # Change the "MITRE Technique ID" column value
# df["MITRE Technique ID"] = df["MITRE Technique ID"].apply(lambda x: f"['T{int(float(x)):04d}']" if pd.notnull(x) and any(part.replace('.','',1).isdigit() for part in x.split(',')) else x)

# Add square brackets to the "MITRE Technique ID" column values with commas
# df["MITRE Technique ID"] = df["MITRE Technique ID"].apply(lambda x: f"[{', '.join([f'T{int(float(part.strip())):04d}' for part in str(x).split(',') if part.replace('.','',1).strip().isdigit()])}]" if pd.notnull(x) else x)


# Function to extract and format values from the third column
def extract_mitre_values(row):
    values = row.split(",")
    formatted_values = [f'T{int(float(part.strip())):04d}' for part in values if part.replace('.','',1).strip().isdigit()]
    return formatted_values

# Applying the function to create the new column
df["MITRE Technique ID"] = df["MITRE Technique ID"].apply(extract_mitre_values)


# Remove "Rule" from the "reference" column
df["Rule"] = df["Rule"].astype(str).apply(lambda x: re.sub(r"reference:url,attack\.mitre\.org/techniques/", "", x))

# Save the modified dataframe to a new CSV file
df.to_csv("SNORT rules classification\\after clean\\sorted_ground_truth.csv", index=False)