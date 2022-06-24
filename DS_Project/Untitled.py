#!/usr/bin/env python
# coding: utf-8

# PROBLEM STATEMENTS 

# In[ ]:





#  IMPORT ALL LIBRARIES: 

# In[127]:


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

# In[105]:


df= pd.read_csv("Pune_House_Data.csv")
df


# In[106]:


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

# In[107]:


df_num = df.select_dtypes(exclude=['object'])
df_cat =df.select_dtypes(include=['object'])


# In[108]:


df_num.head(3)


# In[109]:


df_cat.head(3)


# HANDLING MISSING VALUES:

# In[110]:


df.isnull().sum()


# In[132]:


# Get the percentages of null value
null_percent = df.isnull().sum()/df.shape[0]*100
null_percent


# In[112]:


# Show the null values using heatmap
plt.figure(figsize=(10,5))
sns.heatmap(df.isnull())


# In[113]:


df["BHK"]=df["BHK"].fillna(df["BHK"].median())
df["bath"]=df["bath"].fillna(df["bath"].median())
df["balcony"]=df["balcony"].fillna(df["balcony"].median())
df["site_location"]=df["site_location"].fillna("Alandi Road")


# In[114]:


df.isnull().sum()


# In[115]:


df.nunique()


# ENCODING OF CATEGORIAL FEATURES:

# In[116]:


df_cat.head(3)


# In[117]:


df.replace({'area_type':{'Plot  Area':[3],'Super built-up  Area':[2],'Built-up  Area':[1], 'Carpet  Area':[0]}},inplace=True)
df


# In[128]:


# df.to_array.reshape(1,-1)
Label_Encoder = LabelEncoder()
df['site_location'] = Label_Encoder.fit_transform(df['site_location'])# Print sample of dataset
df.head()


# In[133]:


df= df.drop(["availability"], axis=1)
df.head(3)


# Here availalibility not making impact on price. 

# #********************************Reducing categories *************************************************
# from collections import Counter
# def cumulatively_categorise(column,threshold=0.75,return_categories_list=True):
#   #Find the threshold value using the percentage and number of instances in the column
#   threshold_value=int(threshold*len(column))
#   #Initialise an empty list for our new minimised categories
#   categories_list=[]
#   #Initialise a variable to calculate the sum of frequencies
#   s=0
#   #Create a counter dictionary of the form unique_value: frequency
#   counts=Counter(column)
# 
#   #Loop through the category name and its corresponding frequency after sorting the categories by descending order of frequency
#   for i,j in counts.most_common():
#     #Add the frequency to the global sum
#     s+=dict(counts)[i]
#     #Append the category name to the list
#     categories_list.append(i)
#     #Check if the global sum has reached the threshold value, if so break the loop
#     if s>=threshold_value:
#       break
#   #Append the category Other to the list
#   categories_list.append('Other')
# 
#   #Replace all instances not in our new categories by Other  
#   new_column=column.apply(lambda x: x if x in categories_list else 'Other')
# 
#   #Return transformed column and unique values if return_categories=True
#   if(return_categories_list):
#     return new_column,categories_list
#   #Return only the transformed column if return_categories=False
#   else:
#     return new_column
# 
# 
# #Call the function with a default threshold of 75%
# transformed_column,new_category_list=cumulatively_categorise(df['site_location'],return_categories_list=True)
# transformed_column.describe()

# In[ ]:


SPLITING: 


# In[138]:


x = df["price"]
y = df.drop(["price"], axis=1)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)


# In[ ]:





# In[142]:


sns.displot(df["price"])
plt.show()


# In[143]:


log_SalePrice = np.log1p(df['price'])
sns.displot(log_SalePrice)


# In[ ]:


# correlation heatmap
plt.figure(figsize=(25,25))
ax = sns.heatmap(train.corr(), cmap = "coolwarm", annot=True, linewidth=2)

# to fix the bug "first and last row cut in half of heatmap plot"
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)


# In[ ]:


# correlation heatmap of higly correlated features with SalePrice
hig_corr = train.corr()
hig_corr_features = hig_corr.index[abs(hig_corr["SalePrice"]) >= 0.5]
hig_corr_features


# In[ ]:


plt.figure(figsize=(10,8))
ax = sns.heatmap(train[hig_corr_features].corr(), cmap = "coolwarm", annot=True, linewidth=3)
# to fix the bug "first and last row cut in half of heatmap plot"
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)


# In[ ]:


# Plot regplot to get the nature of highly correlated data
plt.figure(figsize=(16,9))
for i in range(len(hig_corr_features)):
    if i <= 9:
        plt.subplot(3,4,i+1)
        plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
        sns.regplot(data=train, x = hig_corr_features[i], y = 'SalePrice')


# In[ ]:





# In[ ]:





# In[ ]:





# In[139]:


x = df['area_type', 'availability', 'size', 'society', 'total_sqft', 'bath',
       'balcony', 'site_location']
y = df["price"]
sns.pairplot(df,x_vars=x, y_vars=y,height=5,aspect=.8, kind="reg")
plt.show()


# In[26]:


df.columns 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




