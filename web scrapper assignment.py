#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests #for sending http request
import bs4 #beautiful soup library for pulling out html and xml files


# In[13]:


request1 = requests.get('https://www.flipkart.com/redmi-10-midnight-black-64-gb/p/itmd93641e4ebb47?pid=MOBGC9GYEBH3GZ4E&lid=LSTMOBGC9GYEBH3GZ4E44YY0L&marketplace=FLIPKART&fm=productRecommendation%2Fsimilar&iid=R%3As%3Bp%3AMOBG73E7GKQK4KZP%3Bpt%3App%3Buid%3Aac8a3859-f4de-11ed-aa73-955faf22b2d0%3B.MOBGC9GYEBH3GZ4E&ppt=pp&ppn=pp&ssid=smh40m1g000000001684347262906&otracker=pp_reco_Similar%2BProducts_3_35.productCard.PMU_HORIZONTAL_REDMI%2B10%2B%2528Midnight%2BBlack%252C%2B64%2BGB%2529_MOBGC9GYEBH3GZ4E_productRecommendation%2Fsimilar_2&otracker1=pp_reco_PINNED_productRecommendation%2Fsimilar_Similar%2BProducts_GRID_productCard_cc_3_NA_view-all&cid=MOBGC9GYEBH3GZ4E')
request1


# In[22]:


soup = bs4.BeautifulSoup(request1.text)
soup


# In[33]:


#real time comments
reviews = soup.findAll('div',{'class' : 't-ZTKy'});
for review in reviews:
  print(review.get_text() + "\n\n")


# In[24]:


#ratings
rating=soup.find('div',{'class':'_3LWZlK'}).get_text()
print(rating)


# In[25]:


individual_rate=soup.findAll('div',{'class':'_3LWZlK _1BLPMq'});
for individual_rate in individual_rate:
    print(individual_rate.get_text()+"\n")


# In[26]:


#comment tags
tag=soup.find('span',{'class':'yhB1nd GXgmTe'}).get_text()
print(tag)


# In[27]:


#customer name
cust_name=soup.find('p',{'class':'_2sc7ZR _2V5EHH'}).get_text()
print(cust_name)


# In[28]:


#price
price=soup.find('div',{'class':'_30jeq3 _16Jk6d'}).get_text()
print(price)


# In[34]:


#questions
q=soup.findAll('soan',{'class':'_3PSmm0'});
for q in q:
   print(q.get_text())


# In[ ]:




