import pandas as pd
import matplotlib.pyplot as plt

allDataSet = pd.read_csv(r"Simster_A\Pre fine tuning DB\Train_Test_Data\combined_data.csv")
trainSet = pd.read_csv(r"Simster_A\Pre fine tuning DB\Train_Test_Data\train_data.csv")
testSet = pd.read_csv(r"Simster_A\Pre fine tuning DB\Train_Test_Data\test_data.csv")


##### ALL DATA #####
counterAll = allDataSet['MITRE Technique ID'].value_counts().to_dict()
print(f"len all data: {len(counterAll)}")
print(f"sum rows: {sum(counterAll.values())}")
print(f"All dataset:{counterAll}\n")

##### TRAIN #####
counterTrain = trainSet['technique ids'].value_counts().to_dict()
print(f"len train data: {len(counterTrain)}")
print(f"sum rows: {sum(counterTrain.values())}")
print(f"Train set:{counterTrain}\n")

# ##### TEST #####
counterTest = testSet['technique ids'].value_counts().to_dict()
print(f"len test data: {len(counterTest)}")
print(f"sum rows: {sum(counterTest.values())}")
print(f"Test set:{counterTest}\n")



# # Extracting the counts and labels
# counts = list(counterAll.values())
# labels = list(counterAll.keys())

# # Plotting the histogram
# plt.figure(figsize=(10, 6))
# plt.barh(labels, counts, color='skyblue')
# plt.xlabel('Count')
# plt.ylabel('Technique')
# plt.title('Histogram of Techniques')
# plt.tight_layout()
# plt.show()
