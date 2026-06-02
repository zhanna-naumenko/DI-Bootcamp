import random
import json

# Exercise 1: Random Sentence Generator

def get_words_from_file(filename):
    with open(filename, "r") as f:
        file_content = f.read()
        return file_content.split()

def get_random_sentence(length):
    words_list = get_words_from_file("words.txt")
    random_str = " ".join((random.choice(words_list)).lower() for _ in range(length))
    return random_str

def main():
    """Print the sentence of random words from the file"""
    try:
        user_input = int(input("Enter the number (between 1 and 20) of words you want to generate in the sentence: "))
        if 2 <= user_input <= 20:
            print(get_random_sentence(user_input))
        else:
            print("Please enter an integer between 1 and 20.")
    except ValueError:
        print("Please enter an integer.")

main()

# Exercise 2: Working with JSON
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

json_data = json.loads(sampleJson)
print(json_data["company"]["employee"]["payable"]["salary"])    # Access the “salary” key and print it
json_data["company"]["employee"]["birth_date"] = "1990-05-15"   # Add a new key-value pair
print(json_data)

# Save the JSON to a file
# with open("employee.json", "w") as f:
#     json.dump(json_data,f,indent=4)

# read and check saved JSON file
with open("employee.json", "r") as f:
    employee = json.load(f)

print(employee["company"]["employee"]["birth_date"])
