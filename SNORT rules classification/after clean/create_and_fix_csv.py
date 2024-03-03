import pandas as pd
import re

# Read the CSV file
df = pd.read_csv("SNORT rules classification\\after clean\\ground_truth_new.csv")

# Remove the ,Unnamed: 4,Unnamed: 5
df = df.drop(columns=["Unnamed: 4", "Unnamed: 5"])

# Sort the "sid" column
df.sort_values("SID", inplace=True)

# Change the "MITRE Technique ID" column value
df["MITRE Technique ID"] = df["MITRE Technique ID"].apply(lambda x: f"['T{int(float(x)):04d}']" if pd.notnull(x) and x.replace('.','',1).isdigit() else x)

# Remove "Rule" from the "reference" column
df["Rule"] = df["Rule"].astype(str).apply(lambda x: re.sub(r"reference:url,attack\.mitre\.org/techniques/", "", x))

# Save the modified dataframe to a new CSV file
df.to_csv("SNORT rules classification\\after clean\\sorted_ground_truth.csv", index=False)