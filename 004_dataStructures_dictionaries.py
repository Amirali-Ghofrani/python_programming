# how to define a dictionary:
score = {"math" : 90, "programming" : 100, "science" : 80}
print(score)
print(score["math"])             # prints 90

# a dictionary can be defined into another dictionary as well:

score_total = {
           
           "score_sara" :{
               "math" : 90, 
               "programming" : 100, 
               "science" : 80
           },

           "score_amirali":{
               "math" : 100,
               "programming": 95,
               "physics": 80
           }
}

print(score_total["score_sara"]["math"])
print (score_total["score_amirali"]["programming"])

# how to return keys in a dictionary:
keys = score.keys()
print(keys, type(keys)) 

# how to return values in a dictionary:
values = score.values()
print(values, type(values)) 

# how to return keys and values:
items = score.items()
print(items, type(items))


# how to get values for a key without causing error for a missing key:
print (score.get("math"), -1)         # prints 90(math score) and -1
print(score.get("chemistery"), -1)    # prints only -1, doesnt cause errors!

# nested lists in a dictionary:
school_class = {
    "first" : ["mike", "robbert", "sara"],
    "second" : ["joe", "alphred","antonio"]
}

print(school_class["first"][1])    # prints robbert

