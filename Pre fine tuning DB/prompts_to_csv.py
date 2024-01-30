import csv
import pandas as pd

input_file_path = 'mitre_attack_enterprise_full.csv'
output_file_path = 'train.csv'
output_folder = "Pre fine tuning DB"

# Read the original CSV and transform the data
with open(f"{output_folder}/{input_file_path}", mode='r', encoding='utf-8') as infile, \
     open(f"{output_folder}/{output_file_path}", mode='w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['instruction', 'output']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        transformed_row = {
            'instruction': f"what is technique {row['ID']}?",
            'output': f"the name of the technique is '{row['Technique Name']}', and the description is {row['Description']}"
        }
        writer.writerow(transformed_row)



df = pd.read_csv(f"{output_folder}/{output_file_path}")
df = df.fillna("")
text_col = []

for _, row in df.iterrows():
    prompt = "Below is an instruction that describes a technique ID from MITRE ATT&CK. Write a query that returns the name of the technique and its description.\n"
    instruction = str(row["instruction"])
    response = str(row["output"])

    text = f"{prompt} \n### Instructions:\n{instruction} \n### Response:\n{response}"

    text_col.append(text)

df.loc[:, "text"] = text_col

df.to_csv(f"{output_folder}/{output_file_path}", index=False)