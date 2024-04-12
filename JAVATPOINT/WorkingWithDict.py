# Initializing a dictionary with some elements   
Dictionary = {1: 'Javatpoint', 2: 'Python', 3: 'Dictionary'}  
print("\nDictionary created using curly braces: ")  
print(Dictionary)  
# Creating a Dictionary with keys of different data types  
Dictionary = {'Website': 'Javatpoint', 3: [2, 3, 5, 'Dictionary']}  
print("\nDictionary with keys of multiple data type: ")  
print(Dictionary)  

Dictionary[4] = "GO LANG"
print(Dictionary)  
Dictionary[5] = {"nested_key":{"key":[1,23,4,]}}
print(Dictionary[5]['nested_key'])