from cgitb import text
from email.mime import image

from tkinter import *
from tkinter import ttk
import tkinter as tk
from turtle import width
from PIL import ImageTk, Image

'''This script contains all of the information for the dino window and its stat and base values.'''


# Variables for the ammount to increase or decrease a stat (actual values in funtion) 

health = 700
stam = 175
oxy = 150
food = 3000
weight = 250
melee = 100.0
speed = 0
torpor = 420


# Variables for the stat point number.  For every increment in a stat the stat point will be increased by 1
healthStatPoint = 0
stamStatPoint = 0
oxyStatPoint = 0
foodStatPoint = 0
weightStatPoint = 0
meleeStatPoint = 0
speedStatPoint = 0
torporStatPoint = 0

dinoLevel = healthStatPoint + stamStatPoint + oxyStatPoint + foodStatPoint + weightStatPoint + meleeStatPoint + speedStatPoint + torporStatPoint + 1

# Defines function that takes user to dino calculator
def ankyPage():

    # Window setup and position
    ankyCalc= Toplevel()

    # Variables for the size of the window
    width = 960
    height = 1080
    
    # Variables to get the sreen width and height
    screen_width = ankyCalc.winfo_screenwidth()  # Width of the screen
    screen_height = ankyCalc.winfo_screenheight() # Height of the screen

    # variables to set the formula to center the window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    # Initial window values and attributes
    ankyCalc.title("Ark Wild Dino Stat Calculator -- Ankylosaurus")
    ankyCalc.iconbitmap("C:\\FinalProject\\ArkStatCalculator\\Icons\\Nibby.ico")
    ankyCalc.geometry('%dx%d+%d+%d' % (width, height, x, y))
    ankyCalc.resizable(False, False)

    

    
    # Image for selected dino different on subsequent pages
    
    ankImg = ImageTk.PhotoImage(file="C:\\FinalProject\\ArkStatCalculator\\Images\\ankylosaurus.png")

    # Canvas setup

    ankCanvas = Canvas(ankyCalc, width=480, height=540, bg="#439BEB")
    ankCanvas.pack(fill="both", expand=True)
    ankCanvas.create_image(480,10, anchor="n", image=ankImg)
    ankCanvas.create_text(480, 325, text="Ankylosaurus", font= ("Copperplate Gothic Bold", "40") ,fill="#EB9443")
    
    

    # Text indicating the current dinos level
    ankCanvas.create_text(480, 375, text="LVL:", font= ("Copperplate Gothic Bold", "18") ,fill="#EB9443")

    # Label to display dinos level
    dinoLevelLabel = Label(ankyCalc, width=6,bd=1, text=1, font=("Copperplate Gothic Bold", "32"))
    
    # Labels containing base stat values 

    healthEntry = Label(ankyCalc, width=6,bd=1, text=700, font=("Copperplate Gothic Bold", "24"))
     
    stamEntry = Label(ankyCalc, width=6,bd=1, text=175, font=("Copperplate Gothic Bold", "24"))
   
    oxyEntry = Label(ankyCalc, width=6,bd=1, text=150, font=("Copperplate Gothic Bold", "24"))
    
    foodEntry = Label(ankyCalc, width=6,bd=1,text=3000, font=("Copperplate Gothic Bold", "24"))
     
    weightEntry = Label(ankyCalc, width=6,bd=1,text=250, font=("Copperplate Gothic Bold", "24"))
    
    meleeEntry = Label(ankyCalc, width=6,bd=1,text=100.0, font=("Copperplate Gothic Bold", "24"))
    
    speedEntry = Label(ankyCalc, width=6,bd=1,text=100.0, font=("Copperplate Gothic Bold", "24"))
    
    torporEntry = Label(ankyCalc, width=6,bd=1,text=420.0, font=("Copperplate Gothic Bold", "24"))
   

    # Labels identifying stats

    healthLab = Label(ankyCalc, width=13,anchor="e",   bd=1, text="Health", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    stamLab = Label(ankyCalc, width=13,anchor="e",  bd=1,text="Stamina", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    oxyLab = Label(ankyCalc, width=13,anchor="e",  bd=1,text="Oxygen", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    foodLab = Label(ankyCalc, width=13,anchor="e",  bd=1,text="Food", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    weightLab = Label(ankyCalc, width=13,anchor="e",  bd=1,text="Weight", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    meleeLab = Label(ankyCalc, width=13,anchor="e",  bd=1,text="Melee Damage", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    speedLab = Label(ankyCalc, width=13,anchor="e",  bd=1,text="Movement Speed", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    torporLab = Label(ankyCalc, width=13,anchor="e", bd=1,text="Torpor", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    # Lablels showing the amount of stat points are in a certain stat

    healthStatLab = Label(ankyCalc, width=2,anchor="center",   bd=1, text="0", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    stamStatLab = Label(ankyCalc, width=2,anchor="center",  bd=1,text="0", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    oxyStatLab = Label(ankyCalc, width=2,anchor="center",  bd=1,text="0", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    foodStatLab = Label(ankyCalc, width=2,anchor="center",  bd=1,text="0", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    weightStatLab = Label(ankyCalc, width=2,anchor="center",  bd=1,text="0", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    meleeStatLab = Label(ankyCalc, width=2,anchor="center",  bd=1,text="0", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    speedStatLab = Label(ankyCalc, width=2,anchor="center",  bd=1,text="0", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    torporStatLab = Label(ankyCalc, width=2,anchor="center", bd=1,text="0", font=("Copperplate Gothic Bold", "24"),fg="#CB2C16")

    


    # Windows to display labels on canvas
    ankCanvas.create_window(480, 425, anchor="center", window=dinoLevelLabel)


    ankCanvas.create_window(350, 600, anchor="nw", window=healthEntry)
    ankCanvas.create_window(350, 640, anchor="nw", window=stamEntry) 
    ankCanvas.create_window(350, 680, anchor="nw", window=oxyEntry) 
    ankCanvas.create_window(350, 720, anchor="nw", window=foodEntry) 
    ankCanvas.create_window(350, 760, anchor="nw", window=weightEntry) 
    ankCanvas.create_window(350, 800, anchor="nw", window=meleeEntry) 
    ankCanvas.create_window(350, 840, anchor="nw", window=speedEntry) 
    ankCanvas.create_window(350, 880, anchor="nw", window=torporEntry)

    ankCanvas.create_window(20, 600, anchor="nw", window=healthLab)
    ankCanvas.create_window(20, 640, anchor="nw", window=stamLab) 
    ankCanvas.create_window(20, 680, anchor="nw", window=oxyLab) 
    ankCanvas.create_window(20, 720, anchor="nw", window=foodLab) 
    ankCanvas.create_window(20, 760, anchor="nw", window=weightLab) 
    ankCanvas.create_window(20, 800, anchor="nw", window=meleeLab) 
    ankCanvas.create_window(20, 840, anchor="nw", window=speedLab) 
    ankCanvas.create_window(20, 880, anchor="nw", window=torporLab)

    ankCanvas.create_window(518, 600, anchor="nw", window=healthStatLab)
    ankCanvas.create_window(518, 640, anchor="nw", window=stamStatLab) 
    ankCanvas.create_window(518, 680, anchor="nw", window=oxyStatLab) 
    ankCanvas.create_window(518, 720, anchor="nw", window=foodStatLab) 
    ankCanvas.create_window(518, 760, anchor="nw", window=weightStatLab) 
    ankCanvas.create_window(518, 800, anchor="nw", window=meleeStatLab) 
    ankCanvas.create_window(518, 840, anchor="nw", window=speedStatLab) 
    ankCanvas.create_window(518, 880, anchor="nw", window=torporStatLab)
    
     

    # Functions to increase and decrease stat value, levels and stat points.  Documentaion in upHealth() 
    # applies to all functions
    def up_health():
        # gets global variable for base value
        global health, healthStatPoint, dinoLevel

        # stat is incremented by specific amount.  These are different per dino
        health += 140
        healthStatPoint += 1
        dinoLevel += 1

        # Updates the entry text when incremented
        healthEntry.config(text=health)
        healthStatLab.config(text=healthStatPoint)
        dinoLevelLabel.config(text=dinoLevel)
        
        # A check to not value to go below base value
        if health < 700:
            health = 700
            health += 140
        if healthStatPoint < 0:
            healthStatPoint = 0
            healthStatPoint += 1
        if dinoLevel < 1:
            dinoLevel = dinoLevel
            dinoLevel += 1
    
    def down_health():
        global health, healthStatPoint, dinoLevel
        # Decrements 
        health -= 140
        healthStatPoint -= 1
        dinoLevel -= 1
        dinoLevelLabel.config(text=dinoLevel)
        healthEntry.config(text=health)
        healthStatLab.config(text=healthStatPoint)
        # Value check
        if health < 700:
            health = 700
            # resets text in field to base value
            healthEntry.config(text=health)
        if healthStatPoint < 0:
            healthStatPoint = 0
            healthStatLab.config(text=healthStatPoint)
        if dinoLevel < 1:
            dinoLevel = 1
            dinoLevelLabel.config(text=dinoLevel)

    
    def up_stam():
        global stam, stamStatPoint, dinoLevel
        stam += 17.5
        stamStatPoint += 1
        dinoLevel += 1
        stamEntry.config(text=float(stam))
        stamStatLab.config(text=stamStatPoint)
        dinoLevelLabel.config(text=dinoLevel)
        if stam < 175:
            stam = 175
            stam+= 140
        if stamStatPoint < 0:
            stamStatPoint = 0
            stamStatPoint += 1
        if dinoLevel < 1:
            dinoLevel = dinoLevel
            dinoLevel += 1
    
    def down_stam():
        global stam, stamStatPoint, dinoLevel
        stam -= 17.5
        stamStatPoint -= 1
        dinoLevel -= 1
        dinoLevelLabel.config(text=dinoLevel)
        stamEntry.config(text=float(stam))
        stamStatLab.config(text=stamStatPoint)
        if stam < 175:
            stam = 175
            stamEntry.config(text=stam)
        if stamStatPoint < 0:
            stamStatPoint = 0
            stamStatLab.config(text=stamStatPoint)
        if dinoLevel < 1:
            dinoLevel = 1
            dinoLevelLabel.config(text=dinoLevel)

    def up_oxy():
        global oxy, oxyStatPoint, dinoLevel
        oxy += 15
        oxyStatPoint += 1
        dinoLevel += 1
        oxyEntry.config(text=oxy)
        oxyStatLab.config(text=oxyStatPoint)
        dinoLevelLabel.config(text=dinoLevel)
        if oxy < 150:
            oxy = 150
            oxy += 15
        if oxyStatPoint < 0:
            oxyStatPoint = 0
            oxyStatPoint += 1
        if dinoLevel < 1:
            dinoLevel = dinoLevel
            dinoLevel += 1
    
    def down_oxy():
        global oxy, oxyStatPoint, dinoLevel
        oxy -= 15
        oxyStatPoint -= 1
        dinoLevel -= 1
        dinoLevelLabel.config(text=dinoLevel)
        oxyEntry.config(text=oxy)
        oxyStatLab.config(text=oxyStatPoint)
        if oxy < 150:
            oxy = 150
            oxyEntry.config(text=oxy)
        if oxyStatPoint < 0:
            oxyStatPoint = 0
            oxyStatLab.config(text=oxyStatPoint)
        if dinoLevel < 1:
            dinoLevel = 1
            dinoLevelLabel.config(text=dinoLevel)

    def up_food():
        global food, foodStatPoint, dinoLevel
        food += 300
        foodStatPoint += 1
        dinoLevel += 1
        foodEntry.config(text=food)
        foodStatLab.config(text=foodStatPoint)
        dinoLevelLabel.config(text=dinoLevel)
        if food < 3000:
            food = 3000
            food += 300
        if foodStatPoint < 0:
            foodStatPoint = 0
            foodStatPoint += 1
        if dinoLevel < 1:
            dinoLevel = dinoLevel
            dinoLevel += 1
    
    def down_food():
        global food, foodStatPoint, dinoLevel
        food -= 300
        foodStatPoint -= 1
        dinoLevel -= 1
        dinoLevelLabel.config(text=dinoLevel)
        foodEntry.config(text=food)
        foodStatLab.config(text=foodStatPoint)
        if food < 3000:
            food = 3000
            foodEntry.config(text=food)
        if foodStatPoint < 0:
            foodStatPoint = 0
            foodStatLab.config(text=foodStatPoint)
        if dinoLevel < 1:
            dinoLevel = 1
            dinoLevelLabel.config(text=dinoLevel)

    def up_weight():
        global weight, weightStatPoint, dinoLevel
        weight += 5
        weightStatPoint += 1
        dinoLevel += 1
        weightEntry.config(text=weight)
        weightStatLab.config(text=weightStatPoint)
        dinoLevelLabel.config(text=dinoLevel)
        if weight < 250:
            weight = 250
            weight += 5
        if weightStatPoint < 0:
            weightStatPoint = 0
            weightStatPoint += 1
        if dinoLevel < 1:
            dinoLevel = dinoLevel
            dinoLevel += 1
    
    def down_weight():
        global weight, weightStatPoint, dinoLevel
        weight -= 5
        weightStatPoint -= 1
        dinoLevel -= 1
        dinoLevelLabel.config(text=dinoLevel)
        weightEntry.config(text=weight)
        weightStatLab.config(text=weightStatPoint)
        if weight < 250:
            weight = 250
            weightEntry.config(text=weight)
        if weightStatPoint < 0:
            weightStatPoint = 0
            weightStatLab.config(text=weightStatPoint)
        if dinoLevel < 1:
            dinoLevel = 1
            dinoLevelLabel.config(text=dinoLevel)

    def up_melee():
        global melee, meleeStatPoint, dinoLevel
        melee += (melee * 5/100)
        meleeStatPoint += 1
        dinoLevel += 1
        meleeEntry.config(text="{:.2f}".format(melee)) # Formatted to contain value to 2 decimal places
        meleeStatLab.config(text=meleeStatPoint)
        dinoLevelLabel.config(text=dinoLevel)
        if melee < 100:
            melee = 100
            melee += (melee * 5/100)
        if meleeStatPoint < 0:
            meleeStatPoint = 0
            meleeStatPoint += 1
        if dinoLevel < 1:
            dinoLevel = dinoLevel
            dinoLevel += 1
    
    def down_melee():
        global melee, meleeStatPoint, dinoLevel
        melee -= (melee * 5/100)
        meleeStatPoint -= 1
        dinoLevel -= 1
        dinoLevelLabel.config(text=dinoLevel)
        meleeEntry.config(text="{:.2f}".format(melee))
        meleeStatLab.config(text=meleeStatPoint)
        if melee < 100:
            melee = 100
            meleeEntry.config(text="{:.2f}".format(melee))
        if meleeStatPoint < 0:
            meleeStatPoint = 0
            meleeStatLab.config(text=meleeStatPoint)
        if dinoLevel < 1:
            dinoLevel = 1
            dinoLevelLabel.config(text=dinoLevel)

    def up_speed():
        global speedStatPoint, dinoLevel
        speedStatPoint += 1
        dinoLevel += 1
        speedStatLab.config(text=speedStatPoint)
        dinoLevelLabel.config(text=dinoLevel)
        if speedStatPoint < 0:
            speedStatPoint = 0
            speedStatPoint += 1
        if dinoLevel < 1:
            dinoLevel = dinoLevel
            dinoLevel += 1
    
    def down_speed():
        global speedStatPoint, dinoLevel
        speedStatPoint -= 1
        dinoLevel -= 1
        dinoLevelLabel.config(text=dinoLevel)
        speedStatLab.config(text=speedStatPoint)
        if speedStatPoint < 0:
            speedStatPoint = 0
            speedStatLab.config(text=speedStatPoint)
        if dinoLevel < 1:
            dinoLevel = 1
            dinoLevelLabel.config(text=dinoLevel)

    def up_torpor():
        global torpor, torporStatPoint, dinoLevel
        torpor += 25.2
        torporStatPoint += 1
        dinoLevel += 1
        torporEntry.config(text=float("{:.2f}".format(torpor)))
        torporStatLab.config(text=torporStatPoint)
        dinoLevelLabel.config(text=dinoLevel)
        if torpor < 420:
            torpor = 420
            torpor += 25.2
        if torporStatPoint < 0:
            torporStatPoint = 0
            torporStatPoint += 1
        if dinoLevel < 1:
            dinoLevel = dinoLevel
            dinoLevel += 1
    
    
    def down_torpor():
        global torpor, torporStatPoint, dinoLevel
        torpor -= 25.2
        torporStatPoint -= 1
        dinoLevel -= 1
        dinoLevelLabel.config(text=dinoLevel)
        torporEntry.config(text=float("{:.2f}".format(torpor)))
        torporStatLab.config(text=torporStatPoint)
        if torpor < 420:
            torpor = 420
            torporEntry.config(text=float("{:.2f}".format(torpor)))
        if torporStatPoint < 0:
            torporStatPoint = 0
            torporStatLab.config(text=torporStatPoint)
        if dinoLevel < 1:
            dinoLevel = 1
            dinoLevelLabel.config(text=dinoLevel)




    # Buttons to increase and decrease each stat by its game value
    
    health_up = Button(ankyCalc, text="+", width=2, font="16", command= up_health)
    health_down = Button(ankyCalc, text="-", width=2, font="16", command= down_health)

    stam_up = Button(ankyCalc, text="+", width=2, font="16", command= up_stam)
    stam_down = Button(ankyCalc, text="-", width=2, font="16", command= down_stam)

    oxy_up = Button(ankyCalc, text="+", width=2, font="16", command= up_oxy)
    oxy_down = Button(ankyCalc, text="-", width=2, font="16", command= down_oxy)

    food_up = Button(ankyCalc, text="+", width=2, font="16", command= up_food)
    food_down = Button(ankyCalc, text="-", width=2, font="16", command= down_food)

    weight_up = Button(ankyCalc, text="+", width=2, font="16", command= up_weight)
    weight_down = Button(ankyCalc, text="-", width=2, font="16", command= down_weight)

    melee_up = Button(ankyCalc, text="+", width=2, font="16", command= up_melee)
    melee_down = Button(ankyCalc, text="-", width=2, font="16", command= down_melee)

    speed_up = Button(ankyCalc, text="+", width=2, font="16", command= up_speed)
    speed_down = Button(ankyCalc, text="-", width=2, font="16", command= down_speed)

    torpor_up = Button(ankyCalc, text="+", width=2, font="16", command= up_torpor)
    torpor_down = Button(ankyCalc, text="-", width=2, font="16", command= down_torpor)

   
    
    
    # Windows to place buttons in canvas
  
    ankCanvas.create_window(588, 604, anchor="nw", window=health_up)
    ankCanvas.create_window(628, 604, anchor="nw", window=health_down)

    ankCanvas.create_window(588, 644, anchor="nw", window=stam_up)
    ankCanvas.create_window(628, 644, anchor="nw", window=stam_down)

    ankCanvas.create_window(588, 684, anchor="nw", window=oxy_up)
    ankCanvas.create_window(628, 684, anchor="nw", window=oxy_down)

    ankCanvas.create_window(588, 724, anchor="nw", window=food_up)
    ankCanvas.create_window(628, 724, anchor="nw", window=food_down)

    ankCanvas.create_window(588, 764, anchor="nw", window=weight_up)
    ankCanvas.create_window(628, 764, anchor="nw", window=weight_down)

    ankCanvas.create_window(588, 804, anchor="nw", window=melee_up)
    ankCanvas.create_window(628, 804, anchor="nw", window=melee_down)

    ankCanvas.create_window(588, 844, anchor="nw", window=speed_up)
    ankCanvas.create_window(628, 844, anchor="nw", window=speed_down)

    ankCanvas.create_window(588, 884, anchor="nw", window=torpor_up)
    ankCanvas.create_window(628, 884, anchor="nw", window=torpor_down)

 
    


    mainloop()



 