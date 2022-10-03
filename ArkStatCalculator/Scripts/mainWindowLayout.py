from tkinter import *
from tkinter import ttk

from setuptools import Command
import dicsAndLists


root = Tk()
root.geometry("1700x1000")
root.title("Ark Stat Simulator")

# Define clearEntry function
def clearEntry(e):
    if levelEntry.get() == "Enter dino level":
        levelEntry.delete(0, END)

# Define function to get value from combo box
def comboClick(event):
    selectedDino = dinoCombo.get()
    print(selectedDino)
    return selectedDino
    

# Define function to get value from entry box
def getEntry(event):
    enteredLevel = levelEntry.get()
    print(enteredLevel)
    return enteredLevel

    
    
    


    



#Background image


#Canvas
myCanvas = Canvas(root, width= 1700, height= 1000)
myCanvas.pack(fill= "both", expand= True)


#Canvas Buttons
simulate = Button(root, text= "Simulate", font= ("Helvetica", "30"), width= 14)


#Canvas combo box
dinoCombo = ttk.Combobox(root, font= ("Helvetica", "28"), width=14, value= dicsAndLists.dinoComboBox)
dinoCombo.current(0)
dinoCombo.bind("<<ComboboxSelected>>", comboClick)

#Canvas level entry
levelEntry = Entry(root, font= ("Helvetica", "30"), width=14, bd=0)
levelEntry.insert(0, "Enter dino level")
levelEntry.bind("<Return>", getEntry)

# Canvas windows
levelEntryWindow = myCanvas.create_window(1100,500, window= levelEntry)
simulateWindow = myCanvas.create_window(850,850, window= simulate)
comboWindow = myCanvas.create_window(600, 500, window= dinoCombo)






# Bind entry box
levelEntry.bind("<Button-1>", clearEntry)

















root.mainloop()