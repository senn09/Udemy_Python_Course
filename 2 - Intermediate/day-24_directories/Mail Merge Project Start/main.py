#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
    print(names)


with open("./Input/Letters/starting_letter.txt", 'r') as starting_letter:
    letter_template = starting_letter.read()

for name in names:
    with open(f"./Output/ReadyToSend/{name}.txt", 'w') as sending_letter:
        new_letter = letter_template.replace("[name]", f"{name}")
        sending_letter.write(new_letter)




#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp