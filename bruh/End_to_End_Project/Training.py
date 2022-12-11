import streamlit as st

def display(model):
    if model == "Linear Regression":
        LinearRegression()
    elif model == "Decision tree Regression":
        DecisionTreeRegression()
    elif model == "Random forest Regression":
        RandomForestRegression()
    elif model == "Random forest Regression - Grid search":
        GridSearch()
    elif model == "Random forest Regression - Random search":
        RandomSearch()

def LinearRegression():
    st.markdown("""## `Linear Regression`

```python
import os

import numpy as np
import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import cross_val_score

rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):  # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

def display_scores(scores):
    print("Mean: %.2f" % (scores.mean()))
    print("Standard deviation: %.2f" % (scores.std()))

def training():
    housing = pd.read_csv("../Data/housing.csv")
    # Them column income_cat dung de chia Data
    housing["income_cat"] = pd.cut(housing["median_income"],
                                   bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                   labels=[1, 2, 3, 4, 5])

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    # Chia xong thi delete column income_cat
    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)

    housing = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set["median_house_value"].copy()

    housing_num = housing.drop("ocean_proximity", axis=1)

    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ])

    num_attribs = list(housing_num)
    cat_attribs = ["ocean_proximity"]
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

    housing_prepared = full_pipeline.fit_transform(housing)

    # Training
    lin_reg = LinearRegression()
    lin_reg.fit(housing_prepared, housing_labels)

    # Save model lin_reg
    # save model
    if os.path.exists("../Model/model_lin_reg.pkl"):
        os.remove("../Model/model_lin_reg.pkl")
    joblib.dump(lin_reg, "../Model/model_lin_reg.pkl")

    # Prediction
    some_data = housing.iloc[:5]
    some_labels = housing_labels.iloc[:5]
    some_data_prepared = full_pipeline.transform(some_data)
    # Prediction 5 samples
    print("Predictions:", lin_reg.predict(some_data_prepared))
    print("Labels:", list(some_labels))
    print('\n')

    # Tính sai số bình phương trung bình trên tập dữ liệu huấn luyện
    housing_predictions = lin_reg.predict(housing_prepared)
    mse_train = mean_squared_error(housing_labels, housing_predictions)
    rmse_train = np.sqrt(mse_train)
    print('Sai so binh phuong trung binh - train:')
    print('%.2f' % rmse_train)

    # Tính sai số bình phương trung bình trên tập dữ liệu kiểm định chéo (cross-validation)
    scores = cross_val_score(lin_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)

    print('Sai so binh phuong trung binh - cross-validation:')
    rmse_cross_validation = np.sqrt(-scores)
    display_scores(rmse_cross_validation)

    # Tính sai số bình phương trung bình trên tập dữ liệu kiểm tra (test)
    X_test = strat_test_set.drop("median_house_value", axis=1)
    y_test = strat_test_set["median_house_value"].copy()
    X_test_prepared = full_pipeline.transform(X_test)
    y_predictions = lin_reg.predict(X_test_prepared)

    mse_test = mean_squared_error(y_test, y_predictions)
    rmse_test = np.sqrt(mse_test)
    print('Sai so binh phuong trung binh - test:')
    print('%.2f' % rmse_test)
```""")

def DecisionTreeRegression():
    st.markdown("""## `Decision tree Regression`

```python
import os

import numpy as np
import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import mean_squared_error

from sklearn.model_selection import cross_val_score

rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):  # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

def display_scores(scores):
    print("Mean: %.2f" % (scores.mean()))
    print("Standard deviation: %.2f" % (scores.std()))

def training():
    housing = pd.read_csv("../Data/housing.csv")
    # Them column income_cat dung de chia Data
    housing["income_cat"] = pd.cut(housing["median_income"],
                                   bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                   labels=[1, 2, 3, 4, 5])

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    # Chia xong thi delete column income_cat
    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)

    housing = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set["median_house_value"].copy()

    housing_num = housing.drop("ocean_proximity", axis=1)

    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ])

    num_attribs = list(housing_num)
    cat_attribs = ["ocean_proximity"]
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

    housing_prepared = full_pipeline.fit_transform(housing)

    # Training
    tree_reg = DecisionTreeRegressor()
    tree_reg.fit(housing_prepared, housing_labels)

    # save model
    if os.path.exists("../Model/deci_tree_reg.pkl"):
        os.remove("../Model/deci_tree_reg.pkl")
    joblib.dump(tree_reg, "../Model/deci_tree_reg.pkl")

    # Prediction
    some_data = housing.iloc[:5]
    some_labels = housing_labels.iloc[:5]
    some_data_prepared = full_pipeline.transform(some_data)
    # Prediction 5 samples
    print("Predictions:", tree_reg.predict(some_data_prepared))
    print("Labels:", list(some_labels))
    print('\n')

    # Tính sai số bình phương trung bình trên tập dữ liệu huấn luyện
    housing_predictions = tree_reg.predict(housing_prepared)
    mse_train = mean_squared_error(housing_labels, housing_predictions)
    rmse_train = np.sqrt(mse_train)
    print('Sai so binh phuong trung binh - train:')
    print('%.2f' % rmse_train)

    # Tính sai số bình phương trung bình trên tập dữ liệu kiểm định chéo (cross-validation)
    scores = cross_val_score(tree_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)

    print('Sai so binh phuong trung binh - cross-validation:')
    rmse_cross_validation = np.sqrt(-scores)
    display_scores(rmse_cross_validation)

    # Tính sai số bình phương trung bình trên tập dữ liệu kiểm tra (test)
    X_test = strat_test_set.drop("median_house_value", axis=1)
    y_test = strat_test_set["median_house_value"].copy()
    X_test_prepared = full_pipeline.transform(X_test)
    y_predictions = tree_reg.predict(X_test_prepared)

    mse_test = mean_squared_error(y_test, y_predictions)
    rmse_test = np.sqrt(mse_test)
    print('Sai so binh phuong trung binh - test:')
    print('%.2f' % rmse_test)
```""")

def RandomForestRegression():
    st.markdown("""## `Random forest Regression`

```python
import os

import numpy as np
import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error

from sklearn.model_selection import cross_val_score

rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self # nothing else to do
    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

def display_scores(scores):
    print("Mean: %.2f" % (scores.mean()))
    print("Standard deviation: %.2f" % (scores.std()))

def training():
    housing = pd.read_csv("../Data/housing.csv")
    # Them column income_cat dung de chia Data
    housing["income_cat"] = pd.cut(housing["median_income"],
                                   bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                   labels=[1, 2, 3, 4, 5])

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    # Chia xong thi delete column income_cat
    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)

    housing = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set["median_house_value"].copy()

    housing_num = housing.drop("ocean_proximity", axis=1)

    num_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy="median")),
            ('attribs_adder', CombinedAttributesAdder()),
            ('std_scaler', StandardScaler()),
        ])

    num_attribs = list(housing_num)
    cat_attribs = ["ocean_proximity"]
    full_pipeline = ColumnTransformer([
            ("num", num_pipeline, num_attribs),
            ("cat", OneHotEncoder(), cat_attribs),
        ])

    housing_prepared = full_pipeline.fit_transform(housing)

    # Training
    forest_reg = RandomForestRegressor()
    forest_reg.fit(housing_prepared, housing_labels)

    # save model
    if os.path.exists("../Model/rand_forest_reg.pkl"):
        os.remove("../Model/rand_forest_reg.pkl")
    joblib.dump(forest_reg , "../Model/rand_forest_reg.pkl")

    # Prediction
    some_data = housing.iloc[:5]
    some_labels = housing_labels.iloc[:5]
    some_data_prepared = full_pipeline.transform(some_data)
    # Prediction 5 samples
    print("Predictions:", forest_reg.predict(some_data_prepared))
    print("Labels:", list(some_labels))
    print('\n')

    # Tính sai số bình phương trung bình trên tập dữ liệu huấn luyện
    housing_predictions = forest_reg.predict(housing_prepared)
    mse_train = mean_squared_error(housing_labels, housing_predictions)
    rmse_train = np.sqrt(mse_train)
    print('Sai so binh phuong trung binh - train:')
    print('%.2f' % rmse_train)

    # Tính sai số bình phương trung bình trên tập dữ liệu kiểm định chéo (cross-validation)
    scores = cross_val_score(forest_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)

    print('Sai so binh phuong trung binh - cross-validation:')
    rmse_cross_validation = np.sqrt(-scores)
    display_scores(rmse_cross_validation)

    # Tính sai số bình phương trung bình trên tập dữ liệu kiểm tra (test)
    X_test = strat_test_set.drop("median_house_value", axis=1)
    y_test = strat_test_set["median_house_value"].copy()
    X_test_prepared = full_pipeline.transform(X_test)
    y_predictions = forest_reg.predict(X_test_prepared)

    mse_test = mean_squared_error(y_test, y_predictions)
    rmse_test = np.sqrt(mse_test)
    print('Sai so binh phuong trung binh - test:')
    print('%.2f' % rmse_test)
```""")

def GridSearch():
    st.markdown("""## `Random forest Regression - Grid search`

```python
import numpy as np
import pandas as pd
import joblib
import os

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error

from sklearn.model_selection import cross_val_score

from sklearn.model_selection import GridSearchCV

rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self # nothing else to do
    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

def display_scores(scores):
    print("Mean: %.2f" % (scores.mean()))
    print("Standard deviation: %.2f" % (scores.std()))

def training():
    housing = pd.read_csv("../Data/housing.csv")
    # Them column income_cat dung de chia Data
    housing["income_cat"] = pd.cut(housing["median_income"],
                                   bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                   labels=[1, 2, 3, 4, 5])

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    # Chia xong thi delete column income_cat
    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)

    housing = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set["median_house_value"].copy()

    housing_num = housing.drop("ocean_proximity", axis=1)

    num_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy="median")),
            ('attribs_adder', CombinedAttributesAdder()),
            ('std_scaler', StandardScaler()),
        ])

    num_attribs = list(housing_num)
    cat_attribs = ["ocean_proximity"]
    full_pipeline = ColumnTransformer([
            ("num", num_pipeline, num_attribs),
            ("cat", OneHotEncoder(), cat_attribs),
        ])

    housing_prepared = full_pipeline.fit_transform(housing)

    param_grid = [{'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
                  {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
                 ]
    # Training
    forest_reg = RandomForestRegressor(random_state=42)
    grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                               scoring='neg_mean_squared_error', return_train_score=True)
    grid_search.fit(housing_prepared, housing_labels)

    final_model = grid_search.best_estimator_

    # save model
    # save model
    if os.path.exists("../Model/forest_reg_rand_search.pkl"):
        os.remove("../Model/forest_reg_rand_search.pkl")
    joblib.dump(final_model , "../Model/forest_reg_rand_search.pkl")

    # Prediction
    some_data = housing.iloc[:5]
    some_labels = housing_labels.iloc[:5]
    some_data_prepared = full_pipeline.transform(some_data)
    # Prediction 5 samples
    print("Predictions:", final_model.predict(some_data_prepared))
    print("Labels:", list(some_labels))
    print('\n')

    # Tính sai số bình phương trung bình trên tập dữ liệu huấn luyện
    housing_predictions = final_model.predict(housing_prepared)
    mse_train = mean_squared_error(housing_labels, housing_predictions)
    rmse_train = np.sqrt(mse_train)
    print('Sai so binh phuong trung binh - train:')
    print('%.2f' % rmse_train)

    # Tính sai số bình phương trung bình trên tập dữ liệu kiểm định chéo (cross-validation)
    scores = cross_val_score(final_model, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)

    print('Sai so binh phuong trung binh - cross-validation:')
    rmse_cross_validation = np.sqrt(-scores)
    display_scores(rmse_cross_validation)

    # Tính sai số bình phương trung bình trên tập dữ liệu kiểm tra (test)
    X_test = strat_test_set.drop("median_house_value", axis=1)
    y_test = strat_test_set["median_house_value"].copy()
    X_test_prepared = full_pipeline.transform(X_test)
    y_predictions = final_model.predict(X_test_prepared)

    mse_test = mean_squared_error(y_test, y_predictions)
    rmse_test = np.sqrt(mse_test)
    print('Sai so binh phuong trung binh - test:')
    print('%.2f' % rmse_test)
```""")

def RandomSearch():
    st.markdown("""## `Random forest Regression - Random search`

```python
import numpy as np
import pandas as pd
import joblib
import os

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error

from sklearn.model_selection import cross_val_score

from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):  # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

def display_scores(scores):
    print("Mean: %.2f" % (scores.mean()))
    print("Standard deviation: %.2f" % (scores.std()))

def training():
    housing = pd.read_csv("../Data/housing.csv")
    # Them column income_cat dung de chia Data
    housing["income_cat"] = pd.cut(housing["median_income"],
                                   bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                   labels=[1, 2, 3, 4, 5])

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    # Chia xong thi delete column income_cat
    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)

    housing = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set["median_house_value"].copy()

    housing_num = housing.drop("ocean_proximity", axis=1)

    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ])

    num_attribs = list(housing_num)
    cat_attribs = ["ocean_proximity"]
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

    housing_prepared = full_pipeline.fit_transform(housing)

    param_distribs = {
        'n_estimators': randint(low=1, high=200),
        'max_features': randint(low=1, high=8),
    }

    # Training
    forest_reg = RandomForestRegressor(random_state=42)
    rnd_search = RandomizedSearchCV(forest_reg, param_distributions=param_distribs,
                                    n_iter=10, cv=5, scoring='neg_mean_squared_error', random_state=42)
    rnd_search.fit(housing_prepared, housing_labels)

    final_model = rnd_search.best_estimator_

    # save model
    if os.path.exists("../Model/forest_reg_grid_search.pkl"):
        os.remove("../Model/forest_reg_grid_search.pkl")
    joblib.dump(final_model, "../Model/forest_reg_grid_search.pkl")

    # Prediction
    some_data = housing.iloc[:5]
    some_labels = housing_labels.iloc[:5]
    some_data_prepared = full_pipeline.transform(some_data)
    # Prediction 5 samples
    print("Predictions:", final_model.predict(some_data_prepared))
    print("Labels:", list(some_labels))
    print('\n')

    # Tính sai số bình phương trung bình trên tập dữ liệu huấn luyện
    housing_predictions = final_model.predict(housing_prepared)
    mse_train = mean_squared_error(housing_labels, housing_predictions)
    rmse_train = np.sqrt(mse_train)
    print('Sai so binh phuong trung binh - train:')
    print('%.2f' % rmse_train)

    # Tính sai số bình phương trung bình trên tập dữ liệu kiểm định chéo (cross-validation)
    scores = cross_val_score(final_model, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)

    print('Sai so binh phuong trung binh - cross-validation:')
    rmse_cross_validation = np.sqrt(-scores)
    display_scores(rmse_cross_validation)

    # Tính sai số bình phương trung bình trên tập dữ liệu kiểm tra (test)
    X_test = strat_test_set.drop("median_house_value", axis=1)
    y_test = strat_test_set["median_house_value"].copy()
    X_test_prepared = full_pipeline.transform(X_test)
    y_predictions = final_model.predict(X_test_prepared)

    mse_test = mean_squared_error(y_test, y_predictions)
    rmse_test = np.sqrt(mse_test)
    print('Sai so binh phuong trung binh - test:')
    print('%.2f' % rmse_test)
```""")