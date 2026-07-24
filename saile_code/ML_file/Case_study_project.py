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

import matplotlib.pyplot as plt

plt.boxplot(data['pChEMBL Value'])

plt.title("Box Plot of pChEMBL Value")
plt.ylabel("pChEMBL Value")

plt.show()
Q1 = data['pChEMBL Value'].quantile(0.25)
Q3 = data['pChEMBL Value'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = data[(data['pChEMBL Value'] < lower) |
                (data['pChEMBL Value'] > upper)]

print(outliers)
print("Number of outliers:", len(outliers))



#
# df = pd.read_csv("train.csv")

duplicates = data[data.duplicated(subset=["Smiles"], keep=False)]

print(duplicates)
print('sum of duplicate:',data.duplicated().sum())

# Removing duplicate occurrences

data_clean = data.drop_duplicates(subset='Smiles', keep=FIRST)
print(data_clean.head())
print(data_clean.shape)
print('sum of duplicate:',data_clean.duplicated().sum())

X=data_clean[['Smiles']]
print('shape',X.shape)
y=data_clean['pChEMBL Value']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=7)

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




# i am getting training features

X_train=smile_to_morganprint(X_train['Smiles'],radius=2,n_Bits=1024)
X_test=smile_to_morganprint(X_test['Smiles'],radius=2,n_Bits=1024)
x_features=smile_to_morganprint(data_clean['Smiles'],radius=2,n_Bits=1024)



# X_train,X_test,y_train,y_test=train_test_split(x_features,y,test_size=0.2,random_state=7)

print('x',X_train.shape)
print('y',X_test.shape)

print('x_features_morganfingerprints:',x_features)
# rf = RandomForestRegressor(random_state=42)
#
# rf.fit(X_train, y_train)
#
# importance = rf.feature_importances_
# print(max(importance))
# top = np.argsort(importance)[::-1][:200]
#
# print(top)
#
# X_selected = X_train[:, top]
# rfd=XGBRegressor(random_state=42)
# x_test_selected = X_test[:, top]
# rfd.fit(X_selected,y_train)
# y_predict=rf.predict(x_test_selected)
#
# r_score=r2_score(y_test,y_predict)
# print(r_score)
#
#
# print(X_selected)
# print(x_features)
#
#
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=7)
#
# # # i am doing model building Linear regression
#
# # model evaluation
#
# # test_data=pd.read_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/test.csv')
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

# def model_selection():


#
# model_result={}
# model_co={}
# #
# for name,mod in models.items():

#         mod.fit(X_train,y_train)
#
#         y_pred=mod.predict(X_test)
#
#         r_score=r2_score(y_test,y_pred)
#         print(f'r2_score of {name}:',r_score)
#
#         mse=mean_squared_error(y_test,y_pred)
#
#         RMSE=np.sqrt(mse)
#         print(f'RMSE score of {name}:',RMSE)
#         model_result[name]=[r_score,mse,RMSE]
#
# # model_result=pd.DataFrame(model_result,index=['r_score','mse','rmse'])
# # print(model_result)
# # model_result.to_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/model_resul_2048_before_cv and after preprocess_feature_selction.csv')
#
# # KFold cross validation
#
# kfold=KFold(n_splits=10,shuffle=True)
#
# Kfold_result={}
# result=[]
# for name,model in models.items():
#
#
#
#     cv_score=cross_validate(model,x_features,y,cv=kfold,scoring={'r2': 'r2','mse': 'neg_mean_squared_error'})
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
#     "Model": name,"R2 Score":   r2_mean,"RMSE":mean_rmse_mean,"std_r2": r2_std})
#
#     results_df = pd.DataFrame(result)
#
#     results_df = results_df.sort_values(
#     by="R2 Score",
#     ascending=False
#     )
#
# results_kfold=results_df.to_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/model_resul_1024_After_cv_after data-preprocess_feature_selction.csv')
#
# # #     # print(f'mse_cores of moedl{i}:',cv_score['mean_squared_error'])
# # #     #
# # #     #
# # #     # print(f'mean of r_score of {i}:',np.mean(cv_score['mean_squared_error']))
# # #     # print(f'std of r_score of {i}:',np.std(cv_score['mean_squared_error']))
#
# # Feature engineering with threshold
#
# #For binary Morgan fingerprints :
#
# #threshold=0.0 → Remove only constant features (recommended as a starting point)
# #threshold=0.01 → Remove features with very low variance
# #threshold=0.05 → More aggressive filtering
#
# # feature_selection=VarianceThreshold(threshold=0.075)
# # X_selected_features =feature_selection.fit_transform(x_features)
# # X_test_selected = selector.transform(X_test)
#
# # print("Original features :", X_train.shape[1])
# # print("Selected features :", X_selected_features.shape)
# #
# #
# # kfold=KFold(n_splits=10,shuffle=True)
# # #
# # Kfold_result_slt={}
# # result=[]
# # for name,model in models.items():
# #
# #
# #
# #     cv_score=cross_validate(model,X_selected_features,y,cv=kfold,scoring={'r2': 'r2','mse': 'neg_mean_squared_error'})
# #
# #     r2_score=cv_score['test_r2']
# #     r2_mean=np.mean(cv_score['test_r2'])
# #     r2_std=np.std(cv_score['test_r2'])
# #     print(f'r_cores of moedl{name}:',r2_score)
# #     print(f'mean of r_score of {name}:',r2_mean)
# #     print(f'std of r_score of {name}:',r2_std)
# #
# #
# #     neg_score=-cv_score['test_mse']
# #     mean_rmse = np.sqrt(neg_score)
# #     mean_rmse_mean = mean_rmse.mean()
# #     mean_rmse_std = mean_rmse.std()
# #
# #     print(f'mse_cores of moedl{name}:',-cv_score['test_mse'])
# #     print(f'mean of mse_score of {name}:',(-cv_score['test_mse']).mean())
# #     print(f'std of mse_score of {name}:',(-cv_score['test_mse']).std())
# #     result.append({
# #     "Model": name,"R2 Score":   r2_mean,"RMSE":mean_rmse_mean})
# #
# #     results_df = pd.DataFrame(result)
# #
# #     results_df = results_df.sort_values(
# #     by="R2 Score",
# #     ascending=False
# #     )
# #
# # results_kfold=results_df.to_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/model_resul_1024_After_cv_afterfeature_selction_threshold_0.075.csv')
#
# #     # print(f'mse_cores of moedl{i}:',cv_score['mean_squared_error'])
# #     #
# #     #
# #     # print(f'mean of r_score of {i}:',np.mean(cv_score['mean_squared_error']))
# #     # print(f'std of r_score of {i}:',np.std(cv_score['mean_squared_error']))
#
#
