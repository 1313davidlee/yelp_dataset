import json
import pandas as pd
import numpy as np
import sys


# print('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))


if len(sys.argv) != 2:
    error('Invalid Number of Arguments')
else:
    path = sys.argv[1]
    
# print("path:", path)


# path = "/Users/David/Desktop/"
data2 = []
for l in open(path+"tip.json").readlines():
    data = json.loads(l) #from json string to python dictionary
    data2.append(data)


# Part 1
print(f"Q1:{len(data2)}")


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
# print(dictionary[max_len])
print(f"Q2:{dictionary[max_len]}")



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

# print(avg, std)

excellent_cutoff = avg + 6*std

num_excellent_users = 0
for key in users_dictionary:
    if users_dictionary[key] > excellent_cutoff:
        num_excellent_users += 1

# print("num_excellent_users", num_excellent_users)
print(f"Q3:{num_excellent_users}")

# Part 4
businesses_dictionary = {}
for tip in data2:
    business = tip['business_id']
    if business in businesses_dictionary:
        businesses_dictionary[business] += 1
    else:
        businesses_dictionary[business] = 1

max_business = max(businesses_dictionary, key=businesses_dictionary.get) 

# path = "/Users/David/Desktop/"
business_data = []
for l in open(path+"business.json").readlines():
    data = json.loads(l) #from json string to python dictionary
    business_data.append(data)

for rest in business_data:
    if max_business == rest['business_id']:
        business_name = rest['name']
        print(f"Q4:{business_name}")

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

