# Dictionary is a collection of keys-value pairs. Like hashmap in JAVA or object in JAVASCRIPT

profile = {
    "Name" : "Sayan Shil",
    "UID" : 85576535,
    "Level" : 40,
    "RP Level" : 139
}

print(profile)                                    # Direct print will give a dictionary with key-value as item



for x in profile :
    print(x)                                     # x represents all keys here
for x in profile :                             
    print(profile[x])                            # x represents all values here                         




# All Dictionary Methods --> 



#Adding and Updating Items
profile.update({ "Experience": "1 Month"})
print(profile)

#Removing Items
profile.popitem()                                    # remove last key-value
print(profile)

profile.pop("RP Level" , 139)                       # remove key-value or give error if not found
print(profile)

#profile.clear()                                     # clear entire dict


#Accessing Items

#.get(key[, default])
print(profile.get("Name", "Not Found"))              # get() returns  Value corresponsing to Key , return Default or "None" if not found   

#setdefault(key[, default])
print(profile.setdefault("Rank", "Crown III"))         # setdefault() returns Value corresponsing to Key , insert Default or "None" if not found   
print(profile.setdefault("Name", "NoName")) 
print(profile)


#Findind

print(profile.keys())               # Outputs all keys
print(profile.values())             # Outputs all values corresponding keys
print(profile.items())              # Outputs all Key-value pairs

