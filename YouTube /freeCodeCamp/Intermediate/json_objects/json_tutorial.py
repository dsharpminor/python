"""      conversion
Python              JSON
___________________________
dict                object
list, tuple         array
str                 string
int, long, float    number
True                true
False               false
None                null
"""

#  Python -> JSON (serialization, encoding)
import json

person = {"name": "Anastasia", "age": 23}
# personJSON = json.dumps(person)
personJSON = json.dumps(person, indent=4, separators=("; ", " = "), sort_keys=True)
print(personJSON)

# write to a file
with open("person.json", "w") as file:
    json.dump(person, file)
    print(person)