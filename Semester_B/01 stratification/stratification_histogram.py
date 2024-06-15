# Display statistics on the data set (distribution of rules).
# Step 1: Read in the dataset from the CSV file

import pandas as pd 
  
# read the dataset as csv file 
Nir_Data = pd.read_csv(r'Semester_B\01 stratification\ground_truth.csv') 
Our_Full_Data = pd.read_csv(r'Semester_B\01 stratification\combined_data_fix.csv')
Our_Test_Data_300 = pd.read_csv(r'Semester_B\01 stratification\test_data_fix.csv')
  
# # drop the name column as it is of no importance here 
Nir_Data.drop('Unnamed: 0', axis=1, inplace=True) 


# Step 2: Check the percentage of class
(Nir_Data['technique ids'].value_counts()) / len(Nir_Data) * 100
(Our_Full_Data['MITRE Technique ID'].value_counts()) / len(Our_Full_Data) * 100
(Our_Test_Data_300['technique ids'].value_counts()) / len(Our_Test_Data_300) * 100

# Step 3: Display the distribution of rules
import matplotlib.pyplot as plt
import seaborn as sns

def print_plot(data, miter):
    # Count the occurrences of each unique "Technique ID"
    technique_counts = data[miter].value_counts()

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    technique_counts.plot(kind='bar')

    # Set the labels and title
    plt.xlabel('Technique ID')
    plt.ylabel('Quantity')
    plt.title('Quantity of Each Technique ID')

    # Show the plot
    plt.show()


print_plot(Nir_Data, 'technique ids')
print_plot(Our_Full_Data, 'MITRE Technique ID')
print_plot(Our_Test_Data_300, 'technique ids')


import ast

technique_counts = (Our_Test_Data_300['technique ids'].value_counts())
# Converting the Series to a dictionary
technique_counts_dict = technique_counts.to_dict()
#print(technique_counts_dict)

# Initialize the new dictionary
new_data = {}
# Iterate through the original dictionary
for key, value in technique_counts_dict.items():
    # Convert the string key to a list
    techniques = ast.literal_eval(key)
    # Iterate through the techniques in the list
    for technique in techniques:
        # Add the technique to the new dictionary
        if technique in new_data:
            new_data[technique] += value
        else:
            new_data[technique] = value

sorted_data = dict(sorted(new_data.items(), key=lambda item: item[1], reverse=True))
print(sorted_data)