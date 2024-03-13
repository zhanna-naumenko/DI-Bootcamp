import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

json_file = 'family.json'
#create a json file adding on it a python dictionary
with open(dir_path + '\\family.json', 'w') as file_json_object:
    json.dump(my_family, file_json_object, indent=2, sort_keys=True)

#convert dict to a kson string

# json_str = json.dumps(my_family)
# print(json_str)

#printing the json obj nucely add to json.dump the: indent=2, sort_keys=True


#retrieve json file
with open(dir_path +'\\family.json', 'r') as file_json_object:
    my_family1 = json.load(file_json_object)

