with open("../../Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)

with open("../../Desktop/new_file.txt", "a") as file:
    contents = file.write("\nNew text.")
    print(contents)