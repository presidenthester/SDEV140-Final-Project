from logging.config import dictConfig
from msilib.schema import ComboBox
from multiprocessing import BufferTooShort
from os import popen
from select import select
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter.ttk import *
from turtle import title, width
from PIL import ImageTk, Image
from tkinter import messagebox
from anky_sheet import *
from bronto_sheet import *
from carno_sheet import *
from daeodon import *
from giga_sheet import *
from megatherium_sheet import *
from raptor_sheet import *
from rex_sheet import *
from spino_sheet import *
from theri_sheet import *
from yuty_sheet import *

# Full documentaion for the individual dino sheets can be found in anky_sheet.py and applies to all dino sheets.  The other dino sheets have abridged documentation


#  This is a list for the combo box.  T
#  These are also used as a check in the later function calls


dinoComboBox = [
    "Ankylosaurus", 
    "Brontosaurus", 
    "Carnotaurus", 
    "Daeodon", 
    "Giganotosaurus", 
    "Megatherium", 
    "Raptor", 
    "Rex", 
    "Spino", 
    "Therizinosaurus", 
    "Yutyrannus"
]



# Window setup
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
    infoExitButton = Button(infoPage, text="BACK",width=12, command=infoPage.destroy)
    infoExit = infoCanvas.create_window(400, 975, anchor="s", window=infoExitButton)
    
    infoCanvas.create_text(400, 25, text="Ark Wild Stat Calculator", font= ("Copperplate Gothic Bold", "18"))
    infoCanvas.create_text(400, 45, text="Version 1.0", font= ("Copperplate Gothic Bold", "12"))

    # Create text window
    infoCanvas.create_text(400, 150, fill="black", justify="left", font=("Helvetica", "14"), text=
    "Future app instructions. \nThis is a test.")


# Define Info Button
infoButton = Button(root, text= "Info", command= openInfo)

# Insert button on canvas
canInfoButton = myCanvas.create_window(25, 975, anchor= "sw", width=100, window= infoButton)


# Create combo box and place in canvas

options = dinoComboBox
comboText = "Select Dino"
dinoSelectBox = ttk.Combobox(root, value= options)
dinoSelectBox["state"] = "readonly"
dinoSelectBox.set(comboText)
myCanvas.create_window(850,500, anchor="center", width=250, window=dinoSelectBox)

# Error pop ups for dino selection and level entry
def badDinoPop():
    response = messagebox.showerror("ERROR", "You must select a dino from the drop down menu.")
    if response == "ok":
        mainloop()

def badLevelPop():
    response = messagebox.showerror("ERROR", "You must enter a number for the dinos level")
    if response == "ok":
        mainloop()

def badDinoandLevelPop():
    response = messagebox.showerror("ERROR", "You must select a dino from the drop down menu. \nYou must enter a number for the dinos level")
    if response == "ok":
        mainloop()


# Get dino slection from combo box
def getDino():
    global dinoVal
    dinoVal = dinoSelectBox.get()

    if dinoVal == "Select Dino":
        badDinoPop()
    elif dinoVal == "Ankylosaurus":
        ankyPage()
    elif dinoVal == "Brontosaurus":
        brontopage()
    elif dinoVal == "Carnotaurus":
        carnoPage()
    elif dinoVal == "Daeodon":
        daeodonPage()
    elif dinoVal == "Giganotosaurus":
        gigaPage()
    elif dinoVal == "Megatherium":
        megatheriumPage()
    elif dinoVal == "Raptor":
        raptorPage()
    elif dinoVal == "Rex":
        rexPage()
    elif dinoVal == "Spino":
        spinoPage()
    elif dinoVal == "Therizinosaurus":
        theriPage()
    elif dinoVal == "Yutyrannus":
        yutyPage()
    else:
        print(dinoVal)
        return dinoVal




def getSelection():
    getDino()
    
    
    
    

        
       

    
        
# Create button to take user to calculator
calcButton = Button(root, width=25, text="Calculate Stats", command=getSelection)
myCanvas.create_window(850, 750, anchor= "center", window= calcButton)




mainloop()