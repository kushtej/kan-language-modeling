import json 
from collections import Counter 

f = open('data/dataset.json',) 
data = json.load(f) 

txt=input()

data_dict={}

for key, value in data.items(): 
        if key.startswith(txt):
                data_dict[key]=value


k = Counter(data_dict) 
high = k.most_common(3) 

print("Initial Dictionary:") 
print(data_dict, "\n") 


print("Dictionary with 3 highest values:") 
print("Keys: Values") 

for i in high: 
	print(i[0]," :",i[1]," ") 
