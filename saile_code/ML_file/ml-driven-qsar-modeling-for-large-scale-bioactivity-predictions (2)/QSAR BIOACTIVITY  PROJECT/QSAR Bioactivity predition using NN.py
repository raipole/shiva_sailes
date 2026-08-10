import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

#--------------------------------------------------
# Load your data
#--------------------------------------------------

# X = features (Morgan fingerprints + descriptors)
# y = target (IC50 or pIC50)

# Example:
# X = final_features
# y = data['pIC50']

#--------------------------------------------------
# Train-test split
#--------------------------------------------------


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
data_clean = data.drop_duplicates(subset='Smiles', keep='first')
print(data_clean.head())
print(data_clean.shape)
print('sum of duplicate:',data_clean.duplicated().sum())

X=data_clean[['Smiles']]
print('shape',X.shape)
y=data_clean['pChEMBL Value']
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


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
#--------------------------------------------------
# Feature Scaling
#--------------------------------------------------

# scaler = StandardScaler()
#
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

#--------------------------------------------------
# Feed Forward Neural Network
#--------------------------------------------------

model = Sequential()

model.add(Dense(512,
                activation='relu',
                input_shape=(X_train.shape[1],)))

model.add(Dropout(0.30))

model.add(Dense(256, activation='relu'))
model.add(Dropout(0.30))

model.add(Dense(128, activation='relu'))

model.add(Dense(64, activation='relu'))

model.add(Dense(1))

#--------------------------------------------------
# Compile
#--------------------------------------------------

model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

#--------------------------------------------------
# Early stopping
#--------------------------------------------------

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=20,
    restore_best_weights=True
)

#--------------------------------------------------
# Train
#--------------------------------------------------

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=300,
    batch_size=32,
    callbacks=[early_stop],
    verbose=1
)

#--------------------------------------------------
# Prediction
#--------------------------------------------------

train_pred = model.predict(X_train).flatten()
test_pred = model.predict(X_test).flatten()

#--------------------------------------------------
# Metrics
#--------------------------------------------------

train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))

train_r2 = r2_score(y_train, train_pred)
test_r2 = r2_score(y_test, test_pred)

print("="*50)
print("Training Results")
print("="*50)
print(f"Train RMSE : {train_rmse:.4f}")
print(f"Train R2   : {train_r2:.4f}")

print()

print("="*50)
print("Testing Results")
print("="*50)
print(f"Test RMSE  : {test_rmse:.4f}")
print(f"Test R2    : {test_r2:.4f}")

#--------------------------------------------------
# Train/Test Error
#--------------------------------------------------

train_loss, train_mae = model.evaluate(X_train, y_train, verbose=0)
test_loss, test_mae = model.evaluate(X_test, y_test, verbose=0)

print()
print("Model Errors")
print("--------------------------")
print("Train MSE :", train_loss)
print("Test MSE  :", test_loss)

print("Train MAE :", train_mae)
print("Test MAE  :", test_mae)

#--------------------------------------------------
# Learning Curve
#--------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("Training vs Validation Loss")
plt.legend()

plt.show()