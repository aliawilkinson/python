#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
start = open("./Input/Letters/starting_letter.txt", "r")
letter_cont = start.read()

names = open("./Input/Names/invited_names.txt", "r")
names = names.readlines()

for n in names:
    n = n.strip()
    new_letter = letter_cont.replace("[name]",n)
    f = open(f"./Output/{n}.txt", "w")
    f.write(new_letter)
    f.close()
