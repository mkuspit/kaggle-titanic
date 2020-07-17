# Kaggle Competition
# Titanic: Machine Learning from Disaster
# https://www.kaggle.com/c/titanic/


#%% Import packages
import pandas as pd
import matplotlib.pyplot as plt

#%% Read data in
data_path = "./data/raw/"

# Read data
train = pd.read_csv(data_path + 'train.csv')
holdout = pd.read_csv(data_path + 'test.csv')

# Show summary
train.describe()

#%% Analyze data



#%% Engineer features



#%% Build models



#%% Finalize model



#%% Create final predictions



#%% Export solution