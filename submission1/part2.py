#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import pandas as pd

path = "/Users/David/Desktop/"
data2 = []
for l in open(path+"tip.json").readlines():
    data = json.loads(l) #from json string to python dictionary
    data2.append(data)


# In[ ]:


# Part 1
print(len(data2))


# In[ ]:


# Part 2
dictionary = {}
for tip in data2:
    text = tip['text']
    length = len(text)
    if length in dictionary:
        dictionary[length] += 1
    else:
        dictionary[length] = 1

max_len = max(dictionary.keys())
print(dictionary[max_len])


# In[ ]:


print(data2[0])


# In[ ]:


import numpy as np

# Part 3

users_dictionary = {}
for tip in data2:
    user = tip['user_id']
    if user in users_dictionary:
        users_dictionary[user] += 1
    else:
        users_dictionary[user] = 1

counts = list(users_dictionary.values())
avg = np.mean(counts)
std = np.std(counts)

print(avg, std)

excellent_cutoff = avg + 6*std

num_excellent_users = 0
for key in users_dictionary:
    if users_dictionary[key] > excellent_cutoff:
        num_excellent_users += 1

print("num_excellent_users", num_excellent_users)


# In[ ]:


# Part 4
businesses_dictionary = {}
for tip in data2:
    business = tip['business_id']
    if business in businesses_dictionary:
        businesses_dictionary[business] += 1
    else:
        businesses_dictionary[business] = 1

max_business = max(businesses_dictionary, key=businesses_dictionary.get) 
print(max_business)


# In[ ]:


path = "/Users/David/Desktop/"
business_data = []
for l in open(path+"business.json").readlines():
    data = json.loads(l) #from json string to python dictionary
    business_data.append(data)


# In[ ]:


for rest in business_data:
    if max_business == rest['business_id']:
        business_name = rest['name']
        print(business_name)


# In[ ]:


# Part 5
review_hours = {}
for review in data2:
    if review['business_id'] == max_business:
        hour = review['date'][-8:-6]
        if hour in review_hours:
            review_hours[hour] += 1
        else:
            review_hours[hour] = 1
            
min_reviews = min(review_hours, key=review_hours.get) 
print(f"Q5: {int(min_reviews)}")


# In[ ]:


print(data2[9]['date'])
print(data2[9]['date'][-8:-6])


# In[ ]:





# In[ ]:





# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


path = "/Users/David/Desktop/"
states={}
for l in open(path+"business.json").readlines():
    data = json.loads(l) #from json string to python dictionary
    if data["state"] in states.keys():
        states[data["state"]] = states[data["state"]]+1
    else:
        states[data["state"]] = 1
print(states)
print(sum(states.values()))


# In[ ]:


len(states)


# In[ ]:


azbus = []
for l in open(path+"business.json").readlines():
    data = json.loads(l)
    if data["state"] == "AZ":
        azbus.append(data)
print(len(azbus))


# In[ ]:


cities = {}
for d in azbus:
    if d["city"] in cities.keys():
        cities[d["city"]] = 1 + cities[d["city"]]
    else:
        cities[d["city"]] = 1
for k in cities.keys():
    print(k, cities[k])


# In[ ]:





# In[1]:


# PART 2

import pandas as pd
import json


# In[42]:


path = "/Users/David/Desktop/"
d=[]
for l in open(path+"business.json").readlines():
    d.append(json.loads(l))
df = pd.DataFrame.from_records(d)

df = df[df['state'] == 'AZ']


# In[ ]:





# In[50]:


df['city'] = df['city'].str.lower()
df = df[df.city != '']
df = df[df.city != 'arizona']
df = df[df.city != 'az']
df['city'] = df['city'].str.replace(',', '')
df['city'] = df['city'].str.replace('.', '')
df['city'] = df['city'].str.replace('az', '')
df['city'] = df['city'].str.replace('  ', ' ')
df['city'] = df['city'].str[0:-1] + df['city'].str[-1].replace(' ', '')


df['city'] = df['city'].str.replace('phx', 'phoenix')
df['city'] = df['city'].str.replace('north phoenix', 'phoenix')
df['city'] = df['city'].str.replace('phoeniix', 'phoenix')
df['city'] = df['city'].str.replace('metro phoenix', 'phoenix')
df['city'] = df['city'].str.replace('phoenix metro area', 'phoenix')
df['city'] = df['city'].str.replace('phoenix valley', 'phoenix')
df['city'] = df['city'].str.replace('central', 'phoenix')
df['city'] = df['city'].str.replace('central city', 'phoenix')
df['city'] = df['city'].str.replace('phoneix', 'phoenix')
df['city'] = df['city'].str.replace('phoniex', 'phoenix')
df['city'] = df['city'].str.replace('phoenix city', 'phoenix')
df['city'] = df['city'].str.replace('phoenx', 'phoenix')
df['city'] = df['city'].str.replace('pheonix', 'phoenix')
df['city'] = df['city'].str.replace('phoenix city', 'phoenix')
df['city'] = df['city'].str.replace('phoenix city village', 'phoenix')
df['city'] = df['city'].str.replace('phoenix village', 'phoenix')
df['city'] = df['city'].str.replace('phoenix foothills village', 'phoenix')
df['city'] = df['city'].str.replace('ahwahtukee', 'phoenix')
df['city'] = df['city'].str.replace('ahwatukee', 'phoenix')
df['city'] = df['city'].str.replace('ahwatukee foothills village', 'phoenix')

df['city'] = df['city'].str.replace('old town scottsdale', 'scottsdale')
df['city'] = df['city'].str.replace('scottsale', 'scottsdale')
df['city'] = df['city'].str.replace('old scottsdale', 'scottsdale')
df['city'] = df['city'].str.replace('north scottsdale', 'scottsdale')
df['city'] = df['city'].str.replace('westworld scottsdale', 'scottsdale')
df['city'] = df['city'].str.replace('scottdale', 'scottsdale')
df['city'] = df['city'].str.replace('scotesdale', 'scottsdale')
df['city'] = df['city'].str.replace('scotsdale', 'scottsdale')
df['city'] = df['city'].str.replace('schottsdale', 'scottsdale')

df['city'] = df['city'].str.replace('chandler-gilbert', 'chandler')
df['city'] = df['city'].str.replace('chander', 'chandler')
df['city'] = df['city'].str.replace('\u200bchandler', 'chandler')

df['city'] = df['city'].str.replace('mesa arizona', 'mesa')
df['city'] = df['city'].str.replace('east mesa', 'mesa')

df['city'] = df['city'].str.replace('litchfield', 'litchfield park')
df['city'] = df['city'].str.replace('park park', 'park')

df['city'] = df['city'].str.replace('suprise', 'surprise')
df['city'] = df['city'].str.replace('surprise crossing', 'surprise')

df['city'] = df['city'].str.replace('cave creek road', 'cave creek')

df['city'] = df['city'].str.replace('suncity', 'sun city')
df['city'] = df['city'].str.replace('sun city west', 'sun city')

df['city'] = df['city'].str.replace('fountain hls', 'fountain hills')

df['city'] = df['city'].str.replace('laveen village', 'laveen')
df['city'] = df['city'].str.replace('san tan', 'san tan valley')
df['city'] = df['city'].str.replace('valley valley', 'valley')
df['city'] = df['city'].str.replace('valley valley', 'valley')

df['city'] = df['city'].str.replace('glbert', 'gilbert')
df['city'] = df['city'].str.replace('gelndale', 'glendale')

df['city'] = df['city'].str.replace('', '')
df['city'] = df['city'].str.replace('', '')
df['city'] = df['city'].str.replace('', '')
df['city'] = df['city'].str.replace('', '')


# In[ ]:





# In[53]:


lst = list(df['city'].unique())

print(lst)
print(len(lst))


# In[ ]:





# In[ ]:




