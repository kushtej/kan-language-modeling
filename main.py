import json 
from collections import Counter 

f = open('data/dataset.json',) 
data = json.load(f) 

txt=input()

data_dict={}

for key, value in data.items(): 
        if key.startswith(txt):
                data_dict[key]=value


print("Dictionary with 5 highest values:") 
print("Keys: Values") 

for i in range(4):
        print(list(data_dict.keys())[i]+" : "+list(data_dict.values())[i])
