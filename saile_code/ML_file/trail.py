from tkinter.constants import FIRST

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from contourpy.util.data import random
from fontTools.merge.util import first
from pandas.core.interchange import column
from sklearn import linear_model
# from sklearn.externals.array_api_compat.cupy.linalg import pinv
from sklearn.linear_model import LinearRegression
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from xgboost import XGBRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold, cross_validate
from sklearn.feature_selection import VarianceThreshold
from rdkit.Chem import Descriptors
from sklearn.preprocessing import StandardScaler

# i am loading data


data=pd.read_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/train.csv')

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



#
# df = pd.read_csv("train.csv")

duplicates = data[data.duplicated(subset=["Smiles"], keep=False)]

print(duplicates)
print('sum of duplicate:',data.duplicated().sum())

# Removing duplicate occurrences

data_clean = data.drop_duplicates(subset='Smiles', keep=FIRST)
data_more_than_5 = data_clean[data_clean["pChEMBL Value"] > 5]
print(data_clean.head())
print(data_clean.shape)
print('sum of duplicate:',data_clean.duplicated().sum())

X=data_more_than_5[['Smiles']]
print('shape',X.shape)
y=data_more_than_5['pChEMBL Value']
print(y)

# y_bins = pd.qcut(y, q=5, labels=False)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=7)
# X_train, X_test, y_train, y_test = train_test_split(  X,y,test_size=0.2,random_state=42,stratify=y_bins)

# print(X_train.shape)
# print(y_train.shape)

# return X_train,X_test,y_train,y_test


def smile_to_morganprint(smiles,radius=2,n_Bits=1024):
    finger_prints=[]

    for  i in smiles:
        try:
            count=+1


            # i am going to convert string  smile to chemical object
            if i is not None :


                molecule=Chem.MolFromSmiles(str(i))

                # i am going to save each chemical object to structure show in a file named called molicule.png
                # file_name=f'structi_{count}.png'
                # Draw.MolToFile(molecule,'/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)file_name',size=(300,300))


                # print(f"Saved: {file_name}")
                # i am going to convert each molecule morganfingerprints

                morgan_finger=AllChem.GetMorganFingerprintAsBitVect(molecule,radius,n_Bits)

                # i am creating a emtpy arr

                empty_arr=np.zeros((0,),np.int8)

                # i am going to convert morganfingerprint to array


                Chem.DataStructs.ConvertToNumpyArray(morgan_finger,empty_arr)


                # now i am taking storing these values in  finger_prints


                finger_prints.append(empty_arr)

            else:
                arr=np.zeros((n_Bits,),np.int8)
                finger_prints.append(arr)

        except:
            arr=np.zeros((n_Bits,),np.int8)
            finger_prints.append(arr)

    print(np.array(finger_prints).shape)

    return np.array(finger_prints)
x_train_mor=smile_to_morganprint(X_train['Smiles'],radius=2,n_Bits=1024)
x_test_mor=smile_to_morganprint(X_test['Smiles'],radius=2,n_Bits=1024)
#
# descriptor_list = [desc[0] for desc in Descriptors._descList]
#
# descriptor_values = []
#
# for smile in data_clean['Smiles']:
#     mol = Chem.MolFromSmiles(smile)
#
#     values = []
#     for name, func in Descriptors._descList:
#         values.append(func(mol))
#
#     descriptor_values.append(values)
#
# descriptor_df = pd.DataFrame(
#     descriptor_values,
#     columns=descriptor_list
# )
#
# descriptor_df = descriptor_df.dropna(axis=1)
#
#
# selector = VarianceThreshold(threshold=0.05)
#
# descriptor_filtered = selector.fit_transform(descriptor_df)
#
# descriptor_filtered = pd.DataFrame(
#     descriptor_filtered,
#     columns=descriptor_df.columns[selector.get_support()],
#     index=descriptor_df.index
# )
#
# print(descriptor_filtered.head())
# print(descriptor_filtered.shape)
#
# corr_matrix = descriptor_filtered.corr().abs()
#
# upper = corr_matrix.where(
#     np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
# )
#
# to_drop = [column for column in upper.columns if any(upper[column] > 0.90)]
#
# descriptor_filtered = descriptor_filtered.drop(columns=to_drop)
#
# print(descriptor_filtered.shape)
# print(descriptor_filtered.head())
#
#
# # # i am getting training features
# # #
# # # X_train=smile_to_morganprint(X_train['Smiles'],radius=2,n_Bits=1024)
# # # X_test=smile_to_morganprint(X_test['Smiles'],radius=2,n_Bits=1024)
# # # x_features=smile_to_morganprint(data_clean['Smiles'],radius=2,n_Bits=1024)
# # # x_features = pd.concat([x_features, descriptor_scaled], axis=1)
# #
# # scaler = StandardScaler()
# #
# # descriptor_scaled = scaler.fit_transform(descriptor_filtered)
#
# descriptor_scaled = pd.DataFrame(
#     descriptor_scaleded,
#     columns=descriptor_df.columns,
#     index=descriptor_df.index
# )
# print(descriptor_scaled.head())
# #
# x_features = np.concatenate([x_features, descriptor_scaled], axis=1)

print(X.shape)

print('x',X_train.shape)
print('y',X_test.shape)

models = {
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(),
    "Lasso": Lasso(),
    "RandomForest": RandomForestRegressor(random_state=42),
    "GradientBoosting": GradientBoostingRegressor(random_state=42),
    "Bagging": BaggingRegressor(random_state=42),
    "XGBoost": XGBRegressor(random_state=42)}

tree_based_model=[models["RandomForest"],models["GradientBoosting"],models['XGBoost'],models['GradientBoosting']]

linear_model=[models['LinearRegression'],models['Ridge'],models['Lasso']]


# KFold cross validation
#
# kfold=KFold(n_splits=10,shuffle=True)
#
# Kfold_result={}
# result=[]
# for name,model in models.items():
#
#
#
#     cv_score=cross_validate(model,descriptor_scaled ,y,cv=kfold,scoring={'r2': 'r2','mse': 'neg_mean_squared_error'})
#
#     r2_score=cv_score['test_r2']
#     r2_mean=np.mean(cv_score['test_r2'])
#     r2_std=np.std(cv_score['test_r2'])
#     print(f'r_cores of moedl{name}:',r2_score)
#     print(f'mean of r_score of {name}:',r2_mean)
#     print(f'std of r_score of {name}:',r2_std)
#
#
#     neg_score=-cv_score['test_mse']
#     mean_rmse = np.sqrt(neg_score)
#     mean_rmse_mean = mean_rmse.mean()
#     mean_rmse_std = mean_rmse.std()
#
#     print(f'mse_cores of moedl{name}:',-cv_score['test_mse'])
#     print(f'mean of mse_score of {name}:',(-cv_score['test_mse']).mean())
#     print(f'std of mse_score of {name}:',(-cv_score['test_mse']).std())
#     result.append({
#         "Model": name,"R2 Score":   r2_mean,"RMSE":mean_rmse_mean,'std_r2': r2_std})
#
#     results_df = pd.DataFrame(result)
#
#     results_df = results_df.sort_values(
#         by="R2 Score",
#         ascending=False
#     )
# # #
# # # results_kfold=results_df.to_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/model_resul_1024_After_cv_after data-preprocess_feature_selction.csv')
# from sklearn.model_selection import RandomizedSearchCV
# from sklearn.ensemble import RandomForestRegressor
#
# param_grid = {
#     'n_estimators': [100,300, 500, 700, 1000],
#     'max_depth': [10, 15, 20, 30, None],
#     'min_samples_split': [2, 5, 10, 15],
#     'min_samples_leaf': [1, 2, 4, 6, 8],
#     'max_features': ['sqrt', 'log2', 0.3, 0.5],
#     'bootstrap': [True]
# }
#
# rf = RandomForestRegressor(random_state=42)
#
# search = RandomizedSearchCV(
#     rf,
#     param_distributions=param_grid,
#     n_iter=50,
#     cv=10,
#     scoring='r2',
#     n_jobs=-1,
#     random_state=42
# )
#
# search.fit(x_train_mor, y_train)
#
# print(search.best_params_)
# print(search.best_score_)

results = []

for name, model in models.items():

    # Train the model
    model.fit(x_train_mor, y_train)

    # Predictions
    y_train_pred = model.predict(x_train_mor)
    y_test_pred = model.predict(x_test_mor)

    # Metrics
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)

    # train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    # test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
    #
    # train_mae = mean_absolute_error(y_train, y_train_pred)
    # test_mae = mean_absolute_error(y_test, y_test_pred)

    # Store results
    results.append({
        "Model": name,
        "Train R²": train_r2,
        "Test R²": test_r2,
        # "Train RMSE": train_rmse,
        # "Test RMSE": test_rmse,
        # "Train MAE": train_mae,
        # "Test MAE": test_mae
    })

# Create DataFrame
results_df = pd.DataFrame(results)

# Sort by Test R² (highest first)
results_df = results_df.sort_values(by="Test R²", ascending=False)

print(results_df)