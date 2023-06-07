#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
import seaborn as sns


# In[27]:


df=pd.read_csv(r"C:\Users\dubey\OneDrive\Desktop\TE-IT\dsbd\Datasets\Iris.csv")
df.head()


# In[17]:


df


# # Seaborn 

# In[10]:


sns.boxplot(x="Species",y="SepalWidthCm",data=df)


# In[11]:


sns.stripplot(x="Species",y="SepalWidthCm",data=df)


# In[12]:


sns.violinplot(x="Species",y="SepalWidthCm",data=df)


# In[13]:


sns.pairplot(df,hue="Species")#allows us to plot pairwse relationship between variables within a dataset


# # matplot

# In[14]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
KS = {'color': ['blue', 'red', 'yellow']}
sns.FacetGrid(df,hue='Species',hue_kws=KS,size=5).map(plt.scatter,'SepalLengthCm','SepalWidthCm').add_legend()


# In[15]:


x="Species"
y="SepalLengthCm"
x1="Species"
y1="PetalLengthCm"
plt.plot(x,y,data=df)
plt.plot(x1,y1,data=df)
plt.legend()
plt.show()


# In[34]:


x="Species"
y="SepalLengthCm"
plt.plot(x,y,'--',data=df)
plt.title("Line Chart")


# In[32]:


x=df["Species"]
y=df["SepalLengthCm"]
plt.bar(x,y)
plt.title("BAR GRAPH")


# In[30]:


x=df["Species"]
y=df["PetalLengthCm"]
plt.scatter(x,y)
plt.show()


# In[31]:


x=df["Species"]
plt.hist(x)


# In[ ]:




