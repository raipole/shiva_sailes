
import pandas as pd
import numpy as np
########################## i am loading the data ############################


data=pd.read_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/train.csv')


#################################### Explanatory data analysis ########################################


print(data.head())

print(data.describe())

print(data.info())
print('total number of null values:',data.isnull().sum())

print(data.shape)
print(data.columns)


duplicates = data[data.duplicated(subset='Smiles', keep=False)]

print('Duplicate:',duplicates)

print('sum of duplicate:',data.duplicated().sum())
duplicate_smiles = data[data.duplicated(subset=["Smiles"], keep=False)]

print('d',duplicate_smiles)
# i am removing id column

data_new=data.drop(['Molecule ChEMBL ID'],axis=1)
print(data_new.head())




duplicates = data[data.duplicated(subset=["Smiles"], keep=False)]

print(duplicates)
print('sum of duplicate:',data.duplicated().sum())

####################### Data preprocessing #########################


# Removing duplicate occurrences

data_clean = data.drop_duplicates(subset='Smiles', keep='first')
print(data_clean.head())
print(data_clean.shape)
print('sum of duplicate:',data_clean.duplicated().sum())

X=data_clean[['Smiles']]
print('shape',X.shape)
# y=data_clean['pChEMBL Value']

# converting continues values of target features into binary values to classification

data_clean["Activity"] = np.select([data_clean["pChEMBL Value"] < 5,(data_clean["pChEMBL Value"] >= 5)],[0, 1])

y=data_clean["Activity"]
print(y)
print(y.value_counts())

# splitting data into train and test



