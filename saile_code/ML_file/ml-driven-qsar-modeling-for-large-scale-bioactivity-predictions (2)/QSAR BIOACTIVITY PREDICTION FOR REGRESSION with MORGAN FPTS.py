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
from matplotlib.pyplot import plot
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV


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

print('No of Duplicates:',duplicate_smiles)

# i am removing id column

data_new=data.drop(['Molecule ChEMBL ID'],axis=1)
print(data_new.head())



plt.figure(figsize=(8,5))
plt.hist(data['pChEMBL Value'], bins=30)
plt.xlabel("Target Value")
plt.ylabel("Frequency")
plt.title("Distribution of Target")
plt.show()





# df = pd.read_csv("train.csv")

duplicates = data[data.duplicated(subset=["Smiles"], keep=False)]

print(duplicates)
print('sum of duplicate:',data.duplicated().sum())


####################### Data preprocessing #########################


# Removing duplicate occurrences
data_clean = data.drop_duplicates(subset='Smiles', keep=FIRST)
print(data_clean.head())
print(data_clean.shape)
print('sum of duplicate:',data_clean.duplicated().sum())

X=data_clean[['Smiles']]
print('shape',X.shape)
y=data_clean['pChEMBL Value']


#################### splitting data into train and test #######################


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=7)



def smile_to_morganprint(smiles,radius=2,n_Bits=1024):
    finger_prints=[]

    for  i in smiles:
        try:
            count=+1


            # i am going to convert string  smile to chemical object
            if i is not None :


                molecule=Chem.MolFromSmiles(str(i))

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



# converting smiles strings into morganfinger prints x_train and x_test

X_train=smile_to_morganprint(X_train['Smiles'],radius=2,n_Bits=1024)
X_test=smile_to_morganprint(X_test['Smiles'],radius=2,n_Bits=1024)
x_features=smile_to_morganprint(data_clean['Smiles'],radius=2,n_Bits=1024)
# x_features = pd.concat([x_features, descriptor_scaled], axis=1)



#################################### Model building ########################################



print(X.shape)

print('X_train morganfeatures prints:',X_train.shape)
print('X_test morganfinger prints',X_test.shape)

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


################## KFold cross validation for generalization of model and model selection ######################

# initialization of 10-kfold cross validation

kfold=KFold(n_splits=10,shuffle=True)

Kfold_result={}

result=[]

for name,model in models.items():



    cv_score=cross_validate(model,x_features,y,cv=kfold,scoring={'r2': 'r2','mse': 'neg_mean_squared_error'})

    r2_score=cv_score['test_r2']
    r2_mean=np.mean(cv_score['test_r2'])
    r2_std=np.std(cv_score['test_r2'])
    print(f'r_cores of moedl{name}:',r2_score)
    print(f'mean of r_score of {name}:',r2_mean)
    print(f'std of r_score of {name}:',r2_std)


    neg_score=-cv_score['test_mse']
    mean_rmse = np.sqrt(neg_score)
    mean_rmse_mean = mean_rmse.mean()
    mean_rmse_std = mean_rmse.std()

    print(f'mse_cores of moedl{name}:',-cv_score['test_mse'])
    print(f'mean of mse_score of {name}:',(-cv_score['test_mse']).mean())
    print(f'std of mse_score of {name}:',(-cv_score['test_mse']).std())
    result.append({
        "Model": name,"R2 Score":   r2_mean,"RMSE":mean_rmse_mean,'std_r2': r2_std})

    results_df = pd.DataFrame(result)

    results_df = results_df.sort_values(by="R2 Score",ascending=False)
print(results_df)


# ####################### this code for finding shap values #################
#
#
# import shap
# import matplotlib.pyplot as plt

# # Example: Random Forest
# for name, model in models.items():
#
#     model.fit(X, y)
#
#     if name in linear_model:
#         shap_values = shap.LinearExplainer(model, X).shap_values(X)
#     else:
#         shap_values = shap.TreeExplainer(model).shap_values(X)
#         if isinstance(shap_values, list):
#             shap_values = shap_values[1]
#
#     shap.summary_plot(shap_values, X, show=False)
#
#     plt.title(name + " SHAP")
#     plt.savefig(name + "_SHAP.png", dpi=300, bbox_inches="tight")
#     plt.close()