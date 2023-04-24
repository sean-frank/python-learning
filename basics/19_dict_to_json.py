"""
Exercise 1: Convert the following dictionary into JSON format

data = {"key1" : "value1", "key2" : "value2"}
Expected Output:

data = {"key1" : "value1", "key2" : "value2"}
"""
# Code goes here
import json
data = {"key1" : "value1", "key2" : "value2"}

json_object = json.dumps(data)
print(json_object)

