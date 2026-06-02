
user_info = []
for _ in range(5):
    user_name = input("Please enter your name: ")
    user_age = int(input("Please enter your age: "))
    user_score = int(input("Please enter your score: "))
    user_tuple = (user_name, user_age, user_score)
    user_info.append(user_tuple)

sorted_by_name = sorted(user_info, key=lambda x: (x[0], x[1], x[2]))
print(sorted_by_name)

