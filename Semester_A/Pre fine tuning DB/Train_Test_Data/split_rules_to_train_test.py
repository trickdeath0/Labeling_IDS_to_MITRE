import pandas as pd
from sklearn.model_selection import train_test_split
import math

# # Read the rules.txt file
# with open("SNORT rules classification/after clean/rules.txt", "r") as file:
#     lines = file.readlines()

# # Extract the SID and Rule from each line
# data = []
# for line in lines:
#     sid = line.split("sid:")[1].split(";")[0]
#     rule = line.strip()
#     data.append([sid, rule])

# # Create a DataFrame from the extracted data
# df = pd.DataFrame(data, columns=["SID", "Rule"])

# # # Save the DataFrame to a CSV file
# # df.to_csv(r"Pre fine tuning DB\Train_Test_Data\rules.csv", index=False)


# # Read the sorted_ground_truth.csv file
# ground_truth = pd.read_csv("SNORT rules classification/after clean/sorted_ground_truth.csv") # TODO: Feautre change this to add new rule

# # # Replace rows with "nan" values with "sid:XXXX" from the data
# for index, row in ground_truth.iterrows():
#     if pd.isnull(row['Rule']):
#         sid = str(row['SID'])
#         for i,r in df.iterrows():
#             if r["SID"] == sid:
#                 ground_truth.at[index, 'Rule'] = r['Rule']
#                 break


# # Save the DataFrame to a CSV file
# ground_truth.to_csv(r"Pre fine tuning DB\Train_Test_Data\ground_truth_fullData.csv", index=False)
            

# # Split the data into train and test sets
# train_data = ground_truth.sample(frac=0.7, random_state=42)
# test_data = ground_truth.drop(train_data.index)

# # Save the train and test sets to separate CSV files
# train_data.to_csv(r"Pre fine tuning DB\Train_Test_Data\train_data.csv", index=False)
# test_data.to_csv(r"Pre fine tuning DB\Train_Test_Data\test_data.csv", index=False)





# # This code is to split the data into train and test sets based on the MITRE Technique ID counts

# ground_truth = pd.read_csv(r"Pre fine tuning DB\Train_Test_Data\combined_data.csv")

# # Function to split data while ensuring a maximum count for a specific key
# def split_data_with_max_count(data, max_count, test_size=0.3, random_state=None):
#     test_data = pd.DataFrame(columns=data.columns)
#     train_data = pd.DataFrame(columns=data.columns)
#     dict_distribution = {}

#     randomTrain = ground_truth.sample(frac=1, random_state=42)
#     for index, row in randomTrain.iterrows():
#         if row['MITRE Technique ID'] in dict_distribution:
#             if dict_distribution[row['MITRE Technique ID']] < max_count:
#                 test_data = test_data._append(row)
#                 dict_distribution[row['MITRE Technique ID']] += 1
#             else:
#                 train_data = train_data._append(row)
#         else:
#             test_data = test_data._append(row)
#             dict_distribution[row['MITRE Technique ID']] = 1

    
#     train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
#     return train_data, test_data

# # Split data into train and test sets
# train_data, test_data = split_data_with_max_count(ground_truth, max_count=40, test_size=0.3, random_state=42)

# # Save the train and test sets to separate CSV files
# train_data.to_csv(r"Pre fine tuning DB\Train_Test_Data\train_data.csv", index=False)
# test_data.to_csv(r"Pre fine tuning DB\Train_Test_Data\test_data.csv", index=False)



import pandas as pd
import random
import csv

df = pd.read_csv(r"Pre fine tuning DB\Train_Test_Data\combined_data.csv")

# Create empty sets for training and test data
training_set = []
test_set = []

# Dictionary to store the count of each technique
technique_count = {}

# # Function to update sets based on the count of techniques
# def update_sets(technique):
#     if technique_count[technique] > 40:
#         test_set.add(technique)
#     else:
#         training_set.add(technique)

# Iterate through the data and perform random extraction
while len(df) > 0:
    index = random.choice(df.index)
    row = df.loc[index]

    technique = row['MITRE Technique ID']  # Assuming the technique is stored in a list

    # if technique not in test_set:


    if technique not in technique_count:            
        technique_count[technique] = 1
    else:
        technique_count[technique] += 1
        

    # Check if we've already extracted 40 rows with the same technique
    if technique_count[technique] < 8 and len(test_set) < 300:
        test_set.append(row)
    else:
        training_set.append(row)

    # Drop the selected row from the DataFrame
    df = df.drop(index)


# Define headers for CSV files
headers = ['Sid', 'URL', 'technique ids', 'Rule']

# Save the train and test sets to separate CSV files
with open(r"Pre fine tuning DB\Train_Test_Data\train_data.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(training_set)

with open(r"Pre fine tuning DB\Train_Test_Data\test_data.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(test_set)
