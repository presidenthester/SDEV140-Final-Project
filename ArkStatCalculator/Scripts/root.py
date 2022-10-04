from msilib.schema import ComboBox
from multiprocessing import BufferTooShort
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter.ttk import *
from turtle import title, width
from PIL import ImageTk, Image

# Setup
root = Tk()
root.title("Ark Wild Dino Stat Calculator")
root.iconbitmap("C:\\FinalProject\\ArkStatCalculator\\Icons\\Nibby.ico")
root.geometry("1700x1000")
root.resizable(True, True)



# Backgorund Image
BG = ImageTk.PhotoImage(file= "C:\FinalProject\ArkStatCalculator\Images\mainBackground.png")


# Foreground Image
F1 = Image.open("C:\FinalProject\ArkStatCalculator\Images\ArkLogo2.png")
width, height = F1.size
newWidth = 300
newHeight = 250
F2 = F1.resize((newWidth, newHeight))
F2.save("Foreground.png")
FG = PhotoImage(file= "C:\FinalProject\ArkStatCalculator\Images\Foreground.png")


# Define Canvas
myCanvas = Canvas(root, width=1700, height=1000)
myCanvas.pack(fill="both", expand=True)


# Canvas Images
myCanvas.create_image(0, 0, image= BG, anchor= "nw")
myCanvas.create_image(850,30, image= FG, anchor= "n")


# Canvas app name with 3D effect
myCanvas.create_text(850,300, text= "ARK Wild Dino Stat Calculator", font= ("Copperplate Gothic Bold", "36"), fill="#2762de")
myCanvas.create_text(855,300, text= "ARK Wild Dino Stat Calculator", font= ("Copperplate Gothic Bold", "36"), fill="white")


# Define openInfo. Opens the info window 
def openInfo():
    # Setup top level window
    infoPage = Toplevel()
    infoPage.title("Ark Wild Dino Stat Calculator -- Info")
    infoPage.geometry("800x1000")
    infoPage.iconbitmap("C:\\FinalProject\\ArkStatCalculator\\Icons\\Nibby.ico")

    # Make window open in center of root 
    x = root.winfo_x()
    y= root.winfo_y()
    infoPage.geometry("+%d+%d" %(x+450,y+0))
    infoPage.wm_transient(root)

    # Create canvas for buttons and text
    infoCanvas = Canvas(infoPage, width=800, height=1000)
    infoCanvas.pack(fill="both", expand=True)
    infoExitButton = Button(infoPage, text="exit", command=infoPage.destroy)
    infoExit = infoCanvas.create_window(400, 975, anchor="se", window=infoExitButton)
    
    infoCanvas.create_text(400, 25, text="Ark Wild Stat Calculator", font= ("Copperplate Gothic Bold", "18"))
    infoCanvas.create_text(400, 45, text="Version 1.0", font= ("Copperplate Gothic Bold", "12"))

    # Create text window
    infoCanvas.create_text(400, 150, fill="black", justify="left", font=("Helvetica", "14"), text=
    "Future app instructions. \nThis is a test.")

       
# Define Info Button
infoButton = Button(root, text= "Info", command= openInfo)

# Insert button on canvas
canInfoButton = myCanvas.create_window(25, 975, anchor= "sw", width=100, window= infoButton)


# Create label for entry box in canvas
myCanvas.create_text(1025, 470, text= "Enter dino level", font= ("Copperplate Gothic Bold", "18"), fill="#2762de")
myCanvas.create_text(1030, 470, text= "Enter dino level", font= ("Copperplate Gothic Bold", "18"), fill="white")


# Create entry box and place in canvas
levelEntry = Entry(root, width=28)
myCanvas.create_window(1150,500, anchor= "e", width=250, window=levelEntry)


# Create combo box and place in canvas
from dicsAndLists import dinoComboBox
options = dinoComboBox
comboText = "Select Dino"
dinoSelectBox = ttk.Combobox(root, value= options)
dinoSelectBox["state"] = "readonly"
myCanvas.create_window(550,500, anchor="w", width=250, window=dinoSelectBox)

# Define funtion to get value Combo box AND entry box
def getSelection(dinoSelectBox, levelEntry):
        dinoVal = dinoSelectBox.get()
        levelVal = levelEntry.get()





mainloop()