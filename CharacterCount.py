"""2. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor 
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}"""

def character_count(str1):
    dict = {}

    for char in str1:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

print(character_count("AKASH"))