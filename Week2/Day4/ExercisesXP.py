import os
import random
import json


#Exercise 1
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + "\sowpods.txt", "r+") as file_sowpods:
    def get_words_from_file():
        '''Reads the file’s content and return the words as a list'''
        text = file_sowpods.readlines()
        print(text)
    # get_words_from_file()
    def get_random_sentence(length_sent):
        '''Gets the length parameter and create a sentence with random words from the list'''
        file_sowpods.seek(0)
        list_of_words = file_sowpods.readlines()
        user_sent = []
        for _ in range(length_sent):
            user_sent.append((random.choice(list_of_words).strip()).lower())
        print(" ".join(user_sent))

    # get_random_sentence(3)

    def main():
        print('''The function asks the user how long they want the sentence
        to be and if an integer between 2 and 20 it prints the sentence,
        and if it not than it print an error message and end the program''')
        file_sowpods.seek(0)
        list_of_words = file_sowpods.readlines()
        user_sent = []
        length_sent = int(input("Please write how many words should be in the sentence: "))
        if length_sent >= 2 and length_sent <= 20:
            for _ in range(length_sent):
                user_sent.append((random.choice(list_of_words).strip()))
            print(" ".join(user_sent))
        else:
            raise ValueError("Please enter the correct number between 2 and 20.")
    # main()

#Exercise 2

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_object = json.loads(sampleJson)
# print(type(json_object))

print(json_object["company"]["employee"]["payable"]["salary"])
json_object["company"]["employee"]["birth_date"] = "12/05/1987"
print(json_object)


with open(dir_path + "\\sampleJson.json", 'w') as file_obj:
    json.dump(json_object, file_obj)


with open(dir_path + "\\sampleJson.json", 'r') as file_obj:
    json_object = json.load(file_obj)
    print(json_object)




