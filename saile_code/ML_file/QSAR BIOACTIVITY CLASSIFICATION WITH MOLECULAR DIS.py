
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from contourpy.util.data import random
from fontTools.merge.util import first
from pandas.core.interchange import column
from sklearn import linear_model
# from sklearn.externals.array_api_compat.cupy.linalg import pinv
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import RidgeClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem import rdFingerprintGenerator
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Lasso
from sklearn.linear_model import RidgeClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold, cross_validate
from sklearn.feature_selection import VarianceThreshold
from rdkit.Chem import Descriptors
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import log_loss
from sklearn.metrics import recall_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import StratifiedKFold, cross_validate

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


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

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=7)


print(X_train.shape)
print(y_train.shape)

# ==========================================================
# Generate RDKit Molecular Descriptors & Remove Constant Features
# ==========================================================

# import pandas as pd
# import numpy as np
# from rdkit import Chem
# from rdkit.Chem import Descriptors
# from sklearn.feature_selection import VarianceThreshold

# ---------------------------
# Load Dataset
# ---------------------------
# df = pd.read_csv("your_dataset.csv")      # Dataset containing a 'SMILES' column

# ---------------------------
# Generate Molecular Descriptors
# ---------------------------
descriptor_names = [name for name, func in Descriptors._descList]

descriptor_data = []

for smi in data_clean["Smiles"]:
    mol = Chem.MolFromSmiles(smi)

    if mol:
        values = []
        for name, func in Descriptors._descList:
            try:
                values.append(func(mol))
            except:
                values.append(np.nan)
        descriptor_data.append(values)
    else:
        descriptor_data.append([np.nan] * len(descriptor_names))

# Convert to DataFrame
descriptor_df = pd.DataFrame(descriptor_data, columns=descriptor_names)

# ---------------------------
# Remove Missing & Infinite Values
# ---------------------------
descriptor_df.replace([np.inf, -np.inf], np.nan, inplace=True)
descriptor_df.dropna(axis=1, inplace=True)

# ---------------------------
# Remove Constant Features
# ---------------------------
selector = VarianceThreshold(threshold=0.01)   # Remove zero-variance features

descriptor_filtered = selector.fit_transform(descriptor_df)

selected_features = descriptor_df.columns[selector.get_support()]

descriptor_filtered = pd.DataFrame(
    descriptor_filtered,
    columns=selected_features
)

print(descriptor_filtered.head())
# ---------------------------
# Results
# # ---------------------------
print("Original descriptors :", descriptor_df.shape[1])
print("Remaining descriptors:", descriptor_filtered.shape[1])

# ---------------------------
# Save Filtered Descriptors
# ---------------------------
descriptor_filtered.to_csv("Filtered_Molecular_Descriptors.csv", index=False)

print("Filtered descriptors saved successfully.")

# # converting smiles strings into morganfinger prints x_train and x_test
#
#
# X_train=smile_to_morganprint(X_train['Smiles'],radius=2,n_Bits=1024)
# X_test=smile_to_morganprint(X_test['Smiles'],radius=2,n_Bits=1024)
# x_features=smile_to_morganprint(data_clean['Smiles'],radius=2,n_Bits=1024)
#
# #
# models = {
#     "Logistic": LogisticRegression(max_iter=1000,random_state=42),
#     "Ridge": RidgeClassifier(),
#
#     "RandomForest":RandomForestClassifier(),
#     "Lightboot": LGBMClassifier(),
#     "Bagging":  BaggingClassifier(),
#     "XGBoost": XGBClassifier()}
# #
# # kfold=KFold(n_splits=10,shuffle=True)
# #
# # Kfold_result={}
# #
# #
# #
# results = []
# #
# # ################## KFold cross validation for generalization of model and model selection ######################
# #
# #
# for name, model in models.items():
#
#     # Train model
#     model.fit(X_train, y_train)
#
#     # Predictions
#     y_train_pred = model.predict(X_train)
#     y_test_pred = model.predict(X_test)
#
#     # Accuracy
#     trainaccuracy = accuracy_score(y_train, y_train_pred)
#     testaccuracy = accuracy_score(y_test, y_test_pred)
#
#     # Precision, Recall, F1
#     precision = precision_score(y_test, y_test_pred)
#     recall = recall_score(y_test, y_test_pred)
#     f1 = f1_score(y_test, y_test_pred)
#
#     # ROC-AUC (only if predict_proba is available)
#     if hasattr(model, "predict_proba"):
#         y_prob = model.predict_proba(X_test)[:, 1]
#         auc = roc_auc_score(y_test, y_prob)
#     else:
#         auc = None
#
#     # Store results
#     results.append({
#         "Model": name,
#         "Train Accuracy": trainaccuracy,
#         "Test Accuracy": testaccuracy,
#         "Precision": precision,
#         "Recall": recall,
#         "F1 Score": f1,
#         "ROC AUC": auc
#     })
#     cm=confusion_matrix(y_test, y_test_pred)
#     print(cm)
# # Create DataFrame
# results_df = pd.DataFrame(results)
#
# # Sort by Test Accuracy
# results_df = results_df.sort_values(by="Test Accuracy", ascending=False)
#
# print(results_df)
#
# # storing the results
#
# results_Clas=results_df.to_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/QSAR bioactivity classification results/model_resul_1024_binary_classification.csv')
#
# rf = RandomForestClassifier(random_state=42)
#
# param_dist = {
#     'n_estimators': [100, 200, 300, 500, 800],
#     'max_depth': [10, 20, 30, None],
#     'min_samples_split': [2, 5, 10],
#     'min_samples_leaf': [1, 2, 4],
#     'max_features': ['sqrt', 'log2'],
#     'bootstrap': [True, False]
# }
#
# random_search = RandomizedSearchCV(
#     estimator=rf,
#     param_distributions=param_dist,
#     n_iter=30,
#     cv=5,
#     scoring='accuracy',
#     random_state=42,
#     n_jobs=-1
# )
#
# random_search.fit(X_train, y_train)
#
# # results = pd.DataFrame([{"Best Score": grid.best_score_,**grid.best_params_}])
# #
# # print(results)
#
# print(random_search.best_params_)
#
#
