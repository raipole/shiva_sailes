
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
import os
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import shap
from rdkit.Chem.Draw import DrawMorganBit
#

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

bitInfo = {}
def smile_to_morganprint(smiles,radius=2,n_Bits=1024,bitInfo=bitInfo):
    finger_prints=[]

    for  i in smiles:
        try:
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


X_train=smile_to_morganprint(X_train['Smiles'],radius=2,n_Bits=1024,bitInfo=bitInfo)
X_test=smile_to_morganprint(X_test['Smiles'],radius=2,n_Bits=1024,bitInfo=bitInfo)
x_features=smile_to_morganprint(data_clean['Smiles'],radius=2,n_Bits=1024,bitInfo=bitInfo)



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
# ################## KFold cross validation for generalization of model and model selection ######################
#
#
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
# from rdkit import Chem
# from rdkit.Chem import AllChem
# from rdkit.Chem.Draw import DrawMorganBit
# import os
#
# #=====================================================
# # Input SMILES
# #=====================================================
#
# smiles = 'O=C(NC1CCN(CC2CC2)C1)c1cc(Cn2c(=O)[nH]c(=O)c3ccccc32)ccc1F'
#
# mol = Chem.MolFromSmiles(smiles)
#
# #=====================================================
# # Generate Morgan Fingerprint with bitInfo
# #=====================================================
#
#
# #
# fp = AllChem.GetMorganFingerprintAsBitVect(
#     mol,
#     radius=2,
#     nBits=1024,
#     bitInfo=bitInfo
# )
#
# #=====================================================
# # Print all fingerprint bits present
# #=====================================================
#
# print("Fingerprint Bits Present:\n")
# print(sorted(bitInfo.keys()))
#
# #=====================================================
# # Select SHAP Important Bit
# #=====================================================
#
# bit = 935      # Replace with your SHAP-important fingerprint bit
#
# #=====================================================
# # Check whether the bit exists
# #=====================================================
#
# if bit in bitInfo:
#
#     print(f"\nFingerprint Bit: {bit}")
#
#     print("Atom Index and Radius:")
#
#     print(bitInfo[bit])
#
#     #---------------------------------------------
#     # Draw Fragment
#     #---------------------------------------------
#
#     img = DrawMorganBit(
#         mol,
#         bit,
#         bitInfo
#     )
#
#     # Display image
#     img.show()
#
#     #---------------------------------------------
#     # Save Image
#     #---------------------------------------------
#
#     output_folder = "Morgan_Bit_Images"
#
#     os.makedirs(output_folder, exist_ok=True)
#
#     img.save(os.path.join(output_folder,
#                           f"FP_{bit}.png"))
#
#     print(f"\nImage saved as Morgan_Bit_Images/FP_{bit}.png")
#
# else:
#
#     print(f"Fingerprint bit {bit} not present in this molecule.")
#



from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import DrawMorganBit
from matplotlib import pyplot as plt

smiles = 'O=C(NC1CCN(CC2CC2)C1)c1cc(Cn2c(=O)[nH]c(=O)c3ccccc32)ccc1F'  # Replace with your SMILES
mol = Chem.MolFromSmiles(smiles)

bitInfo = {}

fp = AllChem.GetMorganFingerprintAsBitVect(
    mol,
    radius=2,
    nBits=1024,
    bitInfo=bitInfo
)

bit = 935   # Replace with a bit that exists in fp.GetOnBits()

print(fp.GetOnBits())

if bit in bitInfo:
    # img = DrawMorganBit(mol, bit, bitInfo)
    #
    # plt.imshow(img)
    # plt.axis("off")
    # plt.show()
    img = DrawMorganBit(mol, bit, bitInfo)

    print(type(img))
    print(img)

    # img.save("bit80.png")
else:
    print("Bit not present.")

import cairosvg
from rdkit.Chem.Draw import DrawMorganBit

bit = 935

svg = DrawMorganBit(mol, bit, bitInfo)

# Save SVG
with open("FP_935.svg", "w") as f:
    f.write(svg)

# Convert SVG to PNG
cairosvg.svg2png(
    bytestring=svg.encode("utf-8"),
    write_to="FP_935.png"
)

print("Saved FP_935.png")