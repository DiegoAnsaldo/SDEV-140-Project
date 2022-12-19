# Program needs tkinter to function
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

# Loads ruler list
kings = open("KingList.txt", "r")
kingText = kings.read()
kingList = kingText.split(",")
kings.close()

# Loads character list
characters = open("CharacterList.txt", "r")
charText = characters.read()
charList = charText.split(",")
characters.close()

# Allows the program to crown one player champion
def most_frequent(List):
    return max(set(List), key = List.count)
 
champion = most_frequent(kingList)

# Opens main window
mainWindow = Tk()
mainWindow.title('Super Smash Bros. Ruler Counter')
mainWindow.geometry("400x600")

#Displays champion
champDisplay = tk.Label(text="The current champion is " + champion)
champDisplay.pack()

# Displays image of smash bros stage
canvas = Canvas(mainWindow, width = 253, height = 148)      
canvas.pack(pady=10)      
img = PhotoImage(file="mainWindowPPM.ppm")
canvas.create_image(0,30, anchor=W, image=img)

# Creates listbox from character list
charListbox = Listbox(mainWindow)
charListbox.pack(pady=15)

# Label to display current champion
charLabel = Label(mainWindow, text='')
charLabel.pack(pady=5)

# Generates lisbox of characters
for item in charList:
    charListbox.insert(END, item)


def Submit(kingName, selection):
    # Allows program to update rulers
    kingIndex = charList.index(selection)
    kingList[kingIndex] = kingName
    kings = open("KingList.txt", "w")
    for i in range(len(kingList)):
        kings.write(kingList[i])
        kings.write(",")
    kings.close()

def Select():
    # Displays current ruler
    kings = open("KingList.txt", "r")
    kingText = kings.read()
    kingList = kingText.split(",")
    kings.close()
    selection = charListbox.get(ANCHOR)
    kingIndex = charList.index(selection)
    charLabel.config(text="The current Ruler is " + kingList[kingIndex])

def SecondWindow():
    # Opens second window
    secondWindow = Toplevel(mainWindow)
    secondWindow.title("Edit Character Rulers")
    secondWindow.geometry("400x600")

    # This should display a different image with a different smash bros stage,
    # but for some unfathomable reason it doesn't work. Literally the same code
    # from the first image, but one works and the other doesn't. I tried
    # changing the variable names but no dice.
    canvas = Canvas(secondWindow, width = 241, height = 175)
    canvas.pack(pady=10)
    img = PhotoImage(file="secondWindowPPM.ppm")
    canvas.create_image(0,30, anchor=W, image=img)

    # Creates second listbox
    charListbox = Listbox(secondWindow)
    charListbox.pack(pady=15)

    # Displays new champion
    champLabel = Label(secondWindow, text='')
    champLabel.pack(pady=5)

    # Generates second lisbox
    for item in charList:
        charListbox.insert(END, item)

    # Allows player to enter name
    playerEntry = tk.Entry(secondWindow)
    playerEntry.pack()

    # Allows player to submit name
    playerSubmit = Button(secondWindow, text="Enter Player Name", command=lambda: [Submit(playerEntry.get(), charListbox.get(ANCHOR)), champLabel.config(text="New Ruler is " + playerEntry.get())])
    playerSubmit.pack(pady=10)

    # Closes second window
    exitWindow = Button(secondWindow, text="Exit This Window", command=secondWindow.destroy)
    exitWindow.pack()

# Allows user to select character to edit
pickCharacter = Button(mainWindow, text="Select Character", command=Select)
pickCharacter.pack(pady=10)

# Allows player to go to second window
changeWindow = Button(mainWindow, text="Change Characters", command=SecondWindow)
changeWindow.pack(pady=10)

# Lets player close application
exitTool = Button(mainWindow, text="Exit Application", command=mainWindow.destroy)
exitTool.pack(pady=10)




mainWindow.mainloop()

    
