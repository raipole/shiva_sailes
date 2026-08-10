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
from sklearn.svm import LinearSVC
from xgboost import XGBRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold, cross_validate
from sklearn.feature_selection import VarianceThreshold
from rdkit.Chem import Descriptors
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import shap

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



def molecular_descriptors(smiles_list):

    descriptor_list = []

    for smi in smiles_list:

        mol = Chem.MolFromSmiles(str(smi))

        if mol is None:
            continue

        desc = [
            Descriptors.MolWt(mol),
            Descriptors.MolLogP(mol),
            Descriptors.TPSA(mol),
            Descriptors.NumHDonors(mol),
            Descriptors.NumHAcceptors(mol),
            Descriptors.NumRotatableBonds(mol),
            Descriptors.RingCount(mol),
            Descriptors.HeavyAtomCount(mol),
            Descriptors.FractionCSP3(mol)
        ]

        descriptor_list.append(desc)

    return np.array(descriptor_list)



# i am getting training features

X_feature_morgan=smile_to_morganprint(data_clean['Smiles'],radius=2,n_Bits=1024)
X_feature_mdescriptor = molecular_descriptors(data_clean["Smiles"])
features = np.concatenate((X_feature_morgan, X_feature_mdescriptor), axis=1)
print(features.shape)


feature_selection=VarianceThreshold(threshold=0.0)

X_selected_features =feature_selection.fit_transform(features)

X_train,X_test,y_train,y_test=train_test_split(X_selected_features,y,test_size=0.3,random_state=7)

print('x test shape:',X_test.shape)
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
    # "Bagging": BaggingRegressor(random_state=42),
    "XGBoost": XGBRegressor(random_state=42)}

tree_based_model=[models["RandomForest"],models["GradientBoosting"],models['XGBoost']]

linear_model=[models['LinearRegression'],models['Ridge'],models['Lasso']]

# def model_selection():
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# X_test_df=pd.DataFrame(X_test_scaled,columns=feature)

# lasso={'lasso':Lasso(alpha=0.1, max_iter=10000)}
# lasso['lasso'].fit(X_train_scaled,y_train)
# selector = SelectFromModel(lasso['lasso'],prefit=True)
# X_train_selected = selector.transform(X_train_scaled)
#
# X_test_selected = selector.transform(X_test_scaled)

# PCA feature selection
# pca = PCA(n_components=200)
#
# X_train_pca = pca.fit_transform(X_train_scaled)
# X_test_pca = pca.transform(X_test_scaled)
#

model_result={}
model_co={}
#
for name,mod in models.items():

        # diveding x_train in train data val_data
        # X_train_val,X_test_val,y_train_val,y_test_val=train_test_split(X_train,y_train,test_size=0.2,random_state=7)

        mod.fit(X_train_scaled,y_train)
        y_pred=mod.predict(X_test_scaled)
        # rmse=mean_squared_error(y_test,y_pred)

        r_score=r2_score(y_test,y_pred)
        print(f'r2_score of {name}:',r_score)

        mse=mean_squared_error(y_test,y_pred)

        RMSE=np.sqrt(mse)
        print(f'RMSE score of {name}:',RMSE)
        model_result[name]=[r_score,mse,RMSE]

        # if mod in tree_based_model:
        #     explainer_tree = shap.TreeExplainer(mod,feature_perturbation="tree_path_dependent")
        #     shap_values = explainer_tree(X_test_val)
        #
        #
        #     shap.summary_plot(shap_values, X_test_val,show=False)
        #     # plt.savefig(f'/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/shap_summary_plot{name}with threshold_0.0.png',dpi=300,bbox_inches="tight",)
        #     #
        #     # plt.close()
        #
        #     shap_df = pd.DataFrame(shap_values.values,)
        #     # Mean absolute SHAP value for each feature
        #     shap_importance = np.abs(shap_values.values).mean(axis=0)
        #
        #     top100_idx = np.argsort(shap_importance)[::-1][:350]
        #
        #     print(top100_idx)
        #
        #     # feature_names = [f"Bit_{i}" for i in range(X_train.shape[1])]
        #     # # Create importance DataFrame
        #     # feature_importance = pd.DataFrame({"Feature": feature_names,"Importance": shap_importance})
        #     #
        #     # # Sort by importance
        #     # feature_importance = feature_importance.sort_values(by="Importance",ascending=False)
        #     #
        #     # # Top 100 features
        #     # top100_features = feature_importance["Feature"].head(100).tolist()
        #
        #     # print(top100_features)
        #     mod.fit(X_train[: ,top100_idx] ,y_train)
        #
        #     y_pred=mod.predict(X_test[: ,top100_idx] )
        #
        #     r_score=r2_score(y_test,y_pred)
        #     print(f'r2_score of of top 100 {name}:',r_score)
        #
        #     mse=mean_squared_error(y_test,y_pred)
        #
        #     RMSE=np.sqrt(mse)
        #     print(f'RMSE score of of top 100 {name}:',RMSE)
        #     model_result[name]=[r_score,mse,RMSE]
        #
        #     shap_df.to_csv(f"/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/{name}_SHAP_threshold_0.0.csv")
        # if mod in linear_model:
        #     explainer_lin = shap.LinearExplainer(mod, X_train_val)
        #     shap_values = explainer_lin(X_test_val)
        #
        #     # shap.summary_plot(shap_values, X_test,show=False)
        #     # plt.savefig(f'/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/shap_summary_plot{name}_threshold_0.0.png',dpi=300,bbox_inches="tight")
        #
        #     # plt.close()
        #     # shap_df = pd.DataFrame(
        #     #     shap_values.values,
        #     #
        #     # )
        #     # shap_df = pd.DataFrame(shap_values.values,)
        #     # # Mean absolute SHAP value for each feature
        #     shap_importance = np.abs(shap_values.values).mean(axis=0)
        #     #
        #     # feature_names = [f"Bit_{i}" for i in range(X_train.shape[1])]
        #
        #     top100_idx = np.argsort(shap_importance)[::-1][:350]
        #
        #     print(top100_idx)
        #     #
        #     # # Create importance DataFrame
        #     # feature_importance = pd.DataFrame({"Feature": feature_names,"Importance": shap_importance})
        #     #
        #     # # Sort by importance
        #     # feature_importance = feature_importance.sort_values(by="Importance",ascending=False)
        #     #
        #     # # Top 100 features
        #     # top100_features = feature_importance["Feature"].head(100).tolist()
        #
        #     # print(top100_features)
        #     mod.fit(X_train[:,top100_idx] ,y_train)
        #
        #     y_pred=mod.predict(X_test[: , top100_idx] )
        #
        #     r_score=r2_score(y_test,y_pred)
        #     print(f'r2_score of of top 100 {name}:',r_score)
        #
        #     mse=mean_squared_error(y_test,y_pred)
        #
        #     RMSE=np.sqrt(mse)
        #     print(f'RMSE score of of top 100 {name}:',RMSE)
        #     model_result[name]=[r_score,mse,RMSE]




            # shap_df.to_csv(f'/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/{name}_SHAP_threshold_0.0.csv')
    # if mob in linear_model:
    #     explainer = shap.LinearExplainer(mod, X_train)
    #
    # else:
    #     explainer = shap.Explainer(mod, X_train)



model_result=pd.DataFrame(model_result,index=['r_score','mse','rmse'])
print(model_result)

model_result.to_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/model_resul_1024_before_cv_with m_dicriptorswith_standard_scaler_test size 30%.csv')
