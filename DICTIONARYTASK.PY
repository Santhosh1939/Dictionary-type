# Write Python code to add a new key-value pair to the following dictionary:
# my_dict = {'name': 'python', 'age': 25}
# my_dict["city"] = "west godavari"
# print(my_dict)
# Your code here
# Output: {'name': 'python', 'age': 25, 'city': 'west godavari'}

# Write Python code to access and print the value associated with the key 'price' in the following dictionary:
# product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': '1200'}
# print(product_info.get("price"))
# Output: 1200

# Write Python code to remove the key-value pair with the key 'city' from the following dictionary:
# my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
# my_dict.pop("city")
# print(my_dict)
# Output :{'name': 'python', 'age': 30}

# Write Python code to print all the keys present in the following dictionary:

# my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
# mydict_2 = my_dict.keys()
# print(mydict_2)
# Output should be: ['name', 'age', 'city']

# Write Python code to print all the values present in the following dictionary:
# my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
# mydict_2 = my_dict.values()
# print(mydict_2)
# Output : ['python', 25, 'tanuku']


###########################################################################################
Dictionary_1 ={
    "Name1" : "KSK",
    "Name2" : "GSK",
    "Name3" : "ASG",
    "Name4" : "ARR",
    }

# Exercise 1: Dictionary Update
# Write a Python script that updates a dictionary with a new key-value pair.
Dictionary_1["Name5"]= "RRR"
print(Dictionary_1)
# OUTPUT: {'Name1': 'KSK', 'Name2': 'GSK', 'Name3': 'ASG', 'Name4': 'ARR', 'Name5': 'RRR'}

# Exercise 2: Dictionary Access
# Write a Python script that accesses and prints the value associated with a specific key in a dictionary.
print(Dictionary_1.get("Name4"))
# output:ARR

# Exercise 3: Dictionary Removal
# Write a Python script that removes a key-value pair from a dictionary.
key_value=Dictionary_1.pop("Name3")
print(Dictionary_1)
# output:{'Name1': 'KSK', 'Name2': 'GSK', 'Name4': 'ARR'}

# Exercise 4: Dictionary Keys
# Write a Python script that prints all the keys present in a dictionary.
# print(Dictionary_1.keys())
# output:
# dict_keys(['Name1', 'Name2', 'Name3', 'Name4'])

# Exercise 5: Dictionary Values
# Write a Python script that prints all the values present in a dictionary.
# print(Dictionary_1.values())
# output:
# dict_values(['KSK', 'GSK', 'ASG', 'ARR'])
