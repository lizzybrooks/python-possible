# Dictionaries collaborative learning exercise

List = collection of items ordered numerically
Dictionary = no order, the items are indexed by another variable (usually a String)



On the terminal
Make a new file and open it with your text editor. 

MAC
    $ touch dicts.py
  
WINDOWS
   type nul > dicts.py

**Dictionaries are Key and Value pairs**
They’re used to represent structures of data

1. Create a dictionary with the names and ages of everyone at your table. 

In python, you define dictionaries with curly brackets { }

    
    person = { } # empty dictionary
    
    person = { "first_name": "Karl, "last_name": "Marx", "age": 235 }
    
    # An easier way to look at it:
    person = { 
      "first_name": "Karl, 
      "last_name": "Marx", 
      "age": 235 
    }
  

“first_name” is the **Key**, “Karl” is the **value**

the values can be of any type: int, float, boolean, Strings, or even other dictionaries

**Dictionaries can contain any type, including dictionaries and lists**

2. Add additional information about each person in your dictionary (you will have to talk with each other). 
    
    person = { 
      "first_name": "Karl", 
      "last_name": "Marx", 
      "age": 235,
      "pet": {
        "name": "Proleterry",
        "species": "parrot",
        "age": 12
      },
      "favorite_books": ["Ethics", "Twilight"]
    }
    


You’ll want to do things with values in the dictionary


## Getting values

3. Use the techniques below to extract the information from your dictionary.

**You can get a value from a dictionary using brackets and accessing the key**
The key has to be exactly the name of the key, e.g. first_name
If it doesn’t exist, an error halts the program

    
    # 1. access the value using brackets by referencing the key
    print( person["first_name!"] ) #Outputs: KeyError, there is no key names first_name!
    
    print( person["first_name"] ) #Outputs: Karl
    

**A safer way is to use the get method,**
Returns None without an error if the key isn’t present

    
    name = person.get("first_name")
    

Sometimes dictionaries will have nested values, like a list and dictionaries, so you’ll **iterate** through the values

    
    for book in person["favorite_books"]:
      print(book)
      


## You can iterate through a dictionary 

and get all its properties

    
    for key in person:
      print(key) # prints all the keys
      print(person[key]) # prints all the values
      


## Adding and modifying the dictionary

4. Remove someone from your dictionary and add someone from another table. 

Accessing a key and modifying its value will override the value for that key:

    
    # replaces the value for first_name
    person["first_name"] = "Lenin"
    

If the key doesn’t exist, you can create it and assign a value

    
    person["middle_name"] = "Terry"
    # now there's a new key middle_name with value Terry
    


