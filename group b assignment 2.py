#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as nm


# In[3]:


df=pd.read_csv(r"C:\Users\dubey\OneDrive\Desktop\TE-IT\dsbd\Datasets\heartdisease.csv")
df.head()


# In[24]:


df.isnull().sum()


# In[4]:


#data cleaning
mean=df['Ca'].mean()
df['Ca'].fillna(value=mean,inplace=True)


# In[5]:


#data integration
df1=df[['Age','Sex','ChestPain','RestBP','Chol','Fbs']].loc[0:5]
df2=df[['Age','Sex','ChestPain','RestBP','Chol','Fbs']].loc[6:11]
df_new=pd.concat([df1,df2])#you make mistakes here
df_new


# In[6]:


df['ChestPain'].unique()


# In[7]:


#data Transformation
df['ChestPain']=df['ChestPain'].replace('typical',0)
df['ChestPain']=df['ChestPain'].replace('asymptomatic',1)
df['ChestPain']=df['ChestPain'].replace('nonanginal',2)
df['ChestPain']=df['ChestPain'].replace('nontypical',3)


# In[8]:


df['AHD']=df['AHD'].replace('No',0)
df['AHD']=df['AHD'].replace('Yes',1)


# In[9]:


for i in range(len(df[['Chol']])):
    if i>200:
        df['Chol']=df['Chol'].replace(i,'high')
    else:
        df['Chol']=df['Chol'].replace(i,'low')


# In[30]:


df['Thal']=df['Thal'].replace('nan','irreversible')


# In[31]:


df['Thal'].unique()


# df['Ca'].unique()

# df['Ca'].replace(0.6722408,None)

# df['Ca'].unique()

# df['Thal'].unique()

# In[55]:


df


# In[20]:


#error correction
df['ChestPain']=df['ChestPain'].replace('asymptomatic','NaN')
df


# In[22]:


df['ChestPain'].unique()


# In[21]:


df['ChestPain']=df['ChestPain'].replace('asymptomatic','1')
df


# In[23]:


#model creation
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


# In[58]:


feature_cols = ['Age','ChestPain','RestBP',"Fbs",'RestECG','MaxHR','Slope']
X = df[feature_cols] # Features
y = df.AHD # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))
print("F1 score:",metrics.f1_score(y_test, y_pred))
print("Precesion:",metrics.precision_score(y_test, y_pred))


# In[35]:


#error correction
df=df.dropna(axis=0,how='any')
df


# In[ ]:




