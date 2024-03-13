import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + "\\nameslist.txt", "r+") as file_names:
    for line in file_names:
        print(line, end="")
    file_names.seek(0)
    context = file_names.readlines()
    print(f"\nThe 5th line of the file is: {context[4]}", end="")
    file_names.seek(0)
    print(f"\nOnly the 5 first characters: {file_names.read(5)}", end="")
    file_names.seek(0)
    context_list = file_names.readlines()
    print(f"\nList of lines: {context_list}")
    file_names.seek(0)
    words = [[char for char in word.strip()] for word in context_list]
    print(words)
    # split_word = []
    # context_list_new = []
    # for item in context_list:
    #     context_list_new.append(list(item))
    # print(context_list_new)
    file_names.seek(0)
    darth = 0
    luke = 0
    lea = 0

    for name in context_list:
        if name.lower().strip("\n") == "luke":
            luke += 1
        elif name.lower().strip("\n") == "darth":
            darth += 1
        elif name.lower().strip("\n") == "lea":
            lea += 1
    print(darth, luke, lea)



