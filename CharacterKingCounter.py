import ast
# I wanted to use a dictionary so I could have the characters and kings associated directly, but I couldn't find another way that works to read a dictionary
# from a text file. The problem with this method is it is obscure, and I couldn't figure out how to make it update the file.
with open('CharacterKings.txt') as f:
    data = f.read()
characters = ast.literal_eval(data)

keepLoop = True

# This whole loop works well as a way to update and view the dictionary while the program is running, but it doesn't apply the updates to the text file.
while keepLoop == True:
    modeSelect = input("Type VIEW MODE to view kings,\ntype CHANGE MODE to update kingships,\ntype XXX to quit: ")
    if modeSelect == "CHANGE MODE":
        charSelect = input("Type in the character you would like to change the king of: ")
        characters[charSelect] = input("Enter new king for " + charSelect + ": ")
    elif modeSelect == "VIEW MODE":
        viewSelect = input("Enter the character you would like to look at, or enter SEE ALL to see whole list: ")
        if viewSelect == "SEE ALL":
            print(characters)
        else:
            print(characters[viewSelect])
    elif modeSelect == "XXX":
        keepLoop = False
        print("Powering down, good to see you")
    else:
        print("INCORRECT SPELLING, TRY AGAIN")
            
f.close()
