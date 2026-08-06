#     param_grid = {
#         'n_estimators': [100,300, 500, 700, 1000],
#         'max_depth': [10, 15, 20, 30, None],
#         'min_samples_split': [2, 5, 10, 15],
#         'min_samples_leaf': [1, 2, 4, 6, 8],
#         'max_features': ['sqrt', 'log2', 0.3, 0.5],
#         'bootstrap': [True]
#     }
#
#     rf = model
#     search = RandomizedSearchCV(
#         rf,
#         param_distributions=param_grid,
#         n_iter=50,
#         cv=10,
#         scoring='r2',
#         n_jobs=-1,
#         random_state=42)
#
#     search.fit(x_train, y_train)
#
#     print(search.best_params_)
#     print(search.best_score_)
#
# hypertunning_parameter(model=RandomForestRegressor(),x_train=X_train,y_train=y_train)

# results_kfold=results_df.to_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/model_resul_1024_After_cv_after data-preprocess_feature_selction.csv')

# model = RandomForestRegressor(n_estimators=500, min_samples_split=5, min_samples_leaf=2,max_features=0.5, max_depth=None, bootstrap= True)
#
# model.fit(X_train, y_train)
# y_pred_test = model.predict(X_test)
# y_pred_train = model.predict(X_train)
#
# r2_score_test=r2_score(y_test,y_pred_test)
# r2_score_train=r2_score(y_train,y_pred_train)
#
# print('train score',r2_score_train)
# print('test score',r2_score_test)
result=[]
import pandas as pd

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error
)
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    BaggingRegressor
)
from xgboost import XGBRegressor

models = {

    "Linear Regression": (
        LinearRegression(),
        {}
    ),

    "Lasso": (
        Lasso(random_state=42),
        {
            "alpha": [0.0001, 0.001, 0.01, 0.1, 1, 10]
        }
    ),

    "Random Forest": (
        RandomForestRegressor(random_state=42),
        {
            "n_estimators": [100, 200, 300],
            "max_depth": [10, 20, 30, None],
            "min_samples_split": [2, 5, 10],
            "min_samples_leaf": [1, 2, 4],
            "max_features": ["sqrt", "log2"]
        }
    ),

    "Gradient Boosting": (
        GradientBoostingRegressor(random_state=42),
        {
            "n_estimators": [100, 200, 300],
            "learning_rate": [0.01, 0.05, 0.1],
            "max_depth": [3, 5, 7],
            "subsample": [0.8, 1.0]
        }
    ),

    "Bagging": (
        BaggingRegressor(random_state=42),
        {
            "n_estimators": [10, 50, 100, 200],
            "max_samples": [0.5, 0.7, 1.0],
            "max_features": [0.5, 0.7, 1.0]
        }
    ),

    "XGBoost": (
        XGBRegressor(random_state=42),
        {
            "n_estimators": [100, 200, 300],
            "learning_rate": [0.01, 0.05, 0.1],
            "max_depth": [3, 5, 7],
            "subsample": [0.8, 1.0],
            "colsample_bytree": [0.8, 1.0]
        }
    )
}
results = []

for name, (model, params) in models.items():

    # Hyperparameter tuning with 10-fold CV
    grid = GridSearchCV(
        estimator=model,
        param_grid=params,
        cv=10,
        scoring='r2',
        n_jobs=-1
    )

    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_

    # Predictions
    y_train_pred = best_model.predict(X_train)
    y_test_pred = best_model.predict(X_test)

    # Metrics
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)

    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

    train_mae = mean_absolute_error(y_train, y_train_pred)
    test_mae = mean_absolute_error(y_test, y_test_pred)

    results.append({
        "Model": name,
        "Best CV R²": grid.best_score_,
        "Train R²": train_r2,
        "Test R²": test_r2,
        "Train RMSE": train_rmse,
        "Test RMSE": test_rmse,
        "Train MAE": train_mae,
        "Test MAE": test_mae,
        "Best Parameters": grid.best_params_
    })

results_df = pd.DataFrame(results)

print(results_df.head())
results=results_df.to_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/QSAR bioactivity classification results/model_resul_1024_After_cv_gridsearch_cv_for_best_parametes_data.csv')
