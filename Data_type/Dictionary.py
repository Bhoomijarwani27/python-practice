chai_types = {"masala": "spicy", "ginger": "zesty", "green": "mild"}
print(chai_types)
#print(chai_types[0]) # give error because in this we made key to get value instead of index
print(chai_types["ginger"])  

#print(chai_types["gingery"]) # give error because 'gingery' key is not present in dictionary in this methos give error but with get method it will not give error

print(chai_types.get("gingery")) 
# None because 'gingery' key is not present in dictionary but it will not give error 

chai_types["green"] = "fresh" # changing value of existing key
print(chai_types)

for chai in chai_types:
    print(chai) # it will print all keys of dictionary 

    # it use mostly to get keys of dictionary you can also get values by mention  like this chai_types[chai] 

for chai in chai_types:
        print(chai, chai_types[chai]) # it will print all keys with their values

# items() method always give both key and value even you mention only key 
for key , value in chai_types.items():
    print(key, value)  # it will print all keys with their values using items() method 

if "masala" in chai_types:
    print("I have  masala chai ") # print only when it exist in dictionary 

if "herbal" in chai_types:
    print("I have  herbal chai ")

print(len(chai_types)) # it will print total number of key value pairs in dictionary

chai_types["herbal"] = "fragrant" # adding new key value pair in dictionary
print(chai_types) # add the new in last 

chai_types.pop("ginger") # removing key value pair using key name
print(chai_types) # print after removing key value pair

chai_types.popitem() # removing last key value pair
print(chai_types) # print after removing last key value pair

del chai_types["green"] # removing key value pair using del keyword
print(chai_types) 

chai_types_copy = chai_types.copy()
print(chai_types_copy)

# dictionary inside dictionary
tea_shop = {
     "chai": {"masala": "spicy", "ginger": "zesty"},
     "snacks": {"samosa": "savory", "pakora": "crispy"},
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["snacks"]["samosa"]) # acessing the specific value inside nested dictionary

print(len(tea_shop)) # it will give total number of dictionary inside main dictionary

square_dict = {x: x**2 for x in range(6)}
print(square_dict)
square_dict.clear() # removing all key value pairs from dictionary
print(square_dict) # it will print empty dictionary{}

keys = ["masala", "ginger", "green"]
default_value = "tasty"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # it will create new dictionary with all keys having same default value

key = ["cold", "hot", "iced"]
value = ["refreshing", "warming", "chilling"]
tea_dict = dict.fromkeys(key, value)
print(tea_dict)  # it will print all values in list for each key

key = ["cold", "hot", "iced"]
value = ["refreshing", "warming", "chilling"]
tea_dict = dict(zip(key, value))
print(tea_dict)  # it will print each key with its corresponding value from two lists
