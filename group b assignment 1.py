#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
#import numpy as nm#numerical python


# In[31]:


df=pd.read_csv(r"C:\Users\dubey\OneDrive\Desktop\TE-IT\dsbd\Datasets\facebook.csv", sep=";")
df


# In[32]:


#creating subsets
df1=df[['Page total likes','Post Month','Post Weekday','Lifetime Engaged Users']].loc[0:5]
df1


# In[33]:


df2=df[['Page total likes','Post Month','Post Weekday','Lifetime Engaged Users']].loc[6:11]
df2


# In[34]:


df3=df[['Lifetime Post Consumptions','Lifetime Post Impressions by people who have liked your Page','Lifetime Post reach by people who like your Page','Lifetime People who have liked your Page and engaged with your post']].loc[12:17]


# In[35]:


df3


# In[36]:


merge=pd.concat([df1,df2])#sq brac
merge


# In[37]:


a=pd.merge(df2,df1, on=['Post Month','Post Weekday'])
a


# In[38]:


#sorting
sort=df.sort_values("Page total likes", ascending=False) #Mind this
sort


# In[39]:


#transposing
transpose1=df.transpose() #Mind this
transpose1


# In[45]:


pivot_table=pd.pivot_table(df,index=['Type','Category'],values='Total Interactions')
pivot_table


# In[46]:


ans1=df.melt()
ans1


# In[43]:


s=df.shape
s


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




