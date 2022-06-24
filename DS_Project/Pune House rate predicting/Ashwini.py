#!/usr/bin/env python
# coding: utf-8

# PROBLEM STATEMENTS 

# In[ ]:





#  IMPORT ALL LIBRARIES: 

# In[88]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_log_error
from sklearn.model_selection import train_test_split
from category_encoders import MEstimateEncoder
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sklearn.feature_selection import mutual_info_regression
from sklearn.linear_model import ElasticNet, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV


# LOAD DATA

# In[89]:


df= pd.read_csv("Pune_House_Data.csv")
df


# In[90]:


for columns in df.columns:
    print (columns)
    print()
    print (df[columns].value_counts())
    print("*"*60)


# #The Curse of Dimensionality
# 
# Here is a simple summarization:
# 
# As the number of features grows, the amount of data we need to accurately be able to distinguish between these features (in order to give us a prediction) and generalize our model (learned function) grows EXPONENTIALLY.

# In[91]:


df_num = df.select_dtypes(exclude=['object'])
df_cat =df.select_dtypes(include=['object'])


# In[92]:


df_num.head(3)


# In[93]:


df_cat.head(3)


# HANDLING MISSING VALUES:

# In[94]:


df.isnull().sum()


# In[95]:


# Get the percentages of null value
null_percent = df.isnull().sum()/df.shape[0]*100
null_percent


# In[96]:


# Show the null values using heatmap
plt.figure(figsize=(10,5))
sns.heatmap(df.isnull())


# In[97]:


df["BHK"]=df["BHK"].fillna(df["BHK"].median())
df["bath"]=df["bath"].fillna(df["bath"].median())
df["balcony"]=df["balcony"].fillna(df["balcony"].median())
df["site_location"]=df["site_location"].fillna("Alandi Road")


# In[98]:


df.isnull().sum()


# In[99]:


df.nunique()


# ENCODING OF CATEGORIAL FEATURES:

# In[100]:


df_cat.head(3)


# In[101]:


df.replace({'area_type':{'Plot  Area':[3],'Super built-up  Area':[2],'Built-up  Area':[1], 'Carpet  Area':[0]}},inplace=True)
df


# In[102]:


df.info()


# In[103]:


def range_to_mid_value(x):
    temp=x.split('-')
    if len(temp)==2:
        return (float(temp[0])+float(temp[1]))/2
    try:
        return float(x)
    except:
        return None
df['total_sqft']=df['total_sqft'].apply(range_to_mid_value) 


# In[104]:


df.info()


# In[105]:


df['price_per_sqft']=df['price']*100000/df['total_sqft']


# In[106]:


df= df.drop(["availability"], axis=1)
df.head(3)


# In[107]:


df


# Here availalibility not making impact on price. 

# SPLITING: 

# In[108]:


Y = df["price"]
X = df.drop(["price"], axis=1)
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=42)


# In[109]:


x_train.shape , x_test.shape, y_train.shape, y_test.shape 


# In[110]:


# concatenating the DataFrames
train_data = pd.concat([x_train, y_train], join = 'outer', axis = 1)
test_data = pd.concat([x_test, y_test], join = 'outer', axis = 1)
train_data.shape, test_data.shape


# In[111]:


ordinal_Encoder = OrdinalEncoder()
df['site_location'] = ordinal_Encoder.fit_transform(df[['site_location']])# Print sample of dataset
df.head()


# In[112]:


for features in df.columns:
    print("hist_kde_plot:",features,'\n',sns.histplot(df[features],kde=True))
    print(plt.show())


# HANDLING OF OUTLIERS :

# In[114]:


df.describe()


# In[115]:


df["BHK"].mode()


# In[116]:


df[df["price"]>400].value_counts().tail()


# In[117]:


for features in df_num:
    plt.figure()
    print("boxplot:,features",'\n',df_num[[features]].boxplot())
    print(plt.show())


# In[120]:


q3=df['BHK'].quantile(0.75)
q1=df['BHK'].quantile(0.25)
median= df['BHK'].quantile(0.50)
iqr=q3-q1
upper_limit=q3+3*iqr
lower_limit=q1-1.5*iqr
df['BHK']=np.where(df['BHK']>upper_limit,upper_limit,df['bath'])
#*******************************************************
plt.figure()
print("boxplot:,features",'\n',df[['BHK']].boxplot())
print(plt.show())


# In[121]:


q3=df['bath'].quantile(0.75)
q1=df['bath'].quantile(0.25)
median= df['bath'].quantile(0.50)
iqr=q3-q1
upper_limit=q3+1.5*iqr
lower_limit=q1-1.5*iqr
df['bath']=np.where(df['bath']>upper_limit,median,df['bath'])
#*******************************************************
plt.figure()
print("boxplot:,features",'\n',df[['bath']].boxplot())
print(plt.show())


# DATA VISUALIZATION:

# In[ ]:


sns.pairplot(train_data, kind="reg")


# In[66]:


# Plot the distplot of target
plt.figure(figsize=(6,5))
bar = sns.distplot(train_data["price"])
bar.legend(["Skewness: {:.2f}".format(train_data['price'].skew())])


# In[67]:


log_Price = np.log1p(train_data['price'])
sns.displot(log_Price)


# In[69]:


# correlation heatmap
plt.figure(figsize=(5,5))
x = sns.heatmap(train_data.corr(), cmap = "coolwarm", annot=True, linewidth=2)
# # to fix the bug "first and last row cut in half of heatmap plot"
# bottom, top = ax.get_ylim()
# ax.set_ylim(bottom + 0.5, top - 0.5)


# ##### here in BHK and bath there is colinearity issue as they are strongly correlated with each other. 

# In[ ]:


# correlation heatmap of higly correlated features with SalePrice
hig_corr = train_data.corr()
hig_corr_features = hig_corr.index[abs(hig_corr["price"]) >= 0.4]
hig_corr_features


# plt.figure(figsize=(10,8))
# ax = sns.heatmap(train_data[hig_corr_features].corr(), cmap = "coolwarm", annot=True, linewidth=3)
# *to fix the bug "first and last row cut in half of heatmap plot"
# bottom, top = ax.get_ylim()
# ax.set_ylim(bottom + 0.5, top - 0.5)

# In[ ]:


# Plot regplot to get the nature of highly correlated data
plt.figure(figsize=(16,9))
for i in range(len(x_train)):
    if i <= 9:
        plt.subplot(3,4,i+1)
        plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
        sns.regplot(data=train_data, x = x_train[i], y = 'price')


# In[ ]:


SCALING:

log_Price = np.log1p(train_data['price'])
sns.displot(log_Price)
