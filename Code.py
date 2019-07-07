from tkinter import *

master = Tk()
#extras
def Game():
    with open ('test.txt', 'a') as w:
        w.write('\n------------------------------------------------------------------------------------------------------------------------\nNEW GAME\n')
def Error():
    with open ('test.txt', 'a') as w:
        w.write('*<<<ERROR*')
#Maps
def Awoken():
    with open ('test.txt', 'a') as w:
        w.write('---------------------------\nCURRENT MAP\nAwoken\n---------------------------')
def BC():
    with open ('test.txt', 'a') as w:
        w.write('---------------------------\nCURRENT MAP\nBlood Covenant\n---------------------------')
def BR():
    with open ('test.txt', 'a') as w:
        w.write('---------------------------\nCURRENT MAP\nBlood Run\n---------------------------')
def CK():
    with open ('test.txt', 'a') as w:
        w.write('---------------------------\nCURRENT MAP\nCorrupted Keep\n---------------------------')
def MF():
    with open ('test.txt', 'a') as w:
        w.write('---------------------------\nCURRENT MAP\nMolten Falls\n---------------------------')
def Ruins():
    with open ('test.txt', 'a') as w:
        w.write('---------------------------\nCURRENT MAP\nRuins of Sarnath\n---------------------------')
def Vale():
    with open ('test.txt', 'a') as w:
        w.write('---------------------------\nCURRENT MAP\nVale of Pnath\n---------------------------')

#Champions
def Anarki():
    with open ('test.txt', 'a') as w:
        w.write('\nCURRENT CHAMPION\nPICKED ANARKI\n---------------------------\nGAME START\n')
def Athena():
    with open ('test.txt', 'a') as w:
        w.write('\nCURRENT CHAMPION\nPICKED ATHENA\n---------------------------\nGAME START\n')
def BJ():
    with open ('test.txt', 'a') as w:
        w.write('\nCURRENT CHAMPION\nPICKED B.J. Blazkowicz\n---------------------------\nGAME START\n')
def Clutch():
    with open ('test.txt', 'a') as w:
        w.write('\nCURRENT CHAMPION\nPICKED CLUTCH\n---------------------------\nGAME START\n')
def DK():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED DEATH KNIGHT\n---------------------------\nGAME START\n')
def DS():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED DOOM SLAYER\n---------------------------\nGAME START\n')
def Eisen():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED EISEN\n---------------------------\nGAME START\n')
def Galena():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED GALENA\n---------------------------\nGAME START\n')
def KEEL():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED KEEL\n---------------------------\nGAME START\n')
def Nyx():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED NYX\n---------------------------\nGAME START\n')
def Ranger():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED RANGER\n---------------------------\nGAME START\n')
def Scalebearer():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED SCALEBEARER\n---------------------------\nGAME START\n')
def Slash():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED SLASH\n---------------------------\nGAME START\n')
def Sorlag():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED SORLAG\n---------------------------\nGAME START\n')
def SP():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED STROGG & PEEKER\n---------------------------\nGAME START\n')
def Visor():
    with open ('test.txt', 'a') as w:
        w.write('\nPICKED VISOR\n---------------------------\nGAME START\n')
#Weapon Actions
def RL():
    with open ('test.txt', 'a') as w:
        w.write('\nHe got Rocket Launcher ')
def LG():
    with open ('test.txt', 'a') as w:
        w.write('\nHe got Lighting Gun ')
def RG():
    with open ('test.txt', 'a') as w:
        w.write('\nHe got Rail Gun ')
def MG():
    with open ('test.txt', 'a') as w:
        w.write('\nHe got Machine Gun ')
def SG():
    with open('test.txt', 'a') as w:
        w.write('\nHe got Shotgun ')
def NG():
    with open ('test.txt', 'a') as w:
        w.write('\nHe got Nailgun')
def Tribolt():
    with open ('test.txt', 'a') as w:
        w.write('\nHe got Tri-Bolt')
#Stacking Actions
def Mega():
    with open ('test.txt', 'a') as w:
        w.write('\nHe got Mega ')
def Heavy():
    with open ('test.txt', 'a') as w:
        w.write('\nHe got Heavy ')
def Health():
    with open ('test.txt', 'a') as w:
        w.write('\nHe got Health Bubble(s) ')
def Armor():
    with open ('test.txt', 'a') as w:
        w.write('\nHe got Small Armor ')
#Actions
def Found():
    with open ('test.txt', 'a') as w:
        w.write('\nHe found the enemy ')
def Chased():
    with open ('test.txt', 'a') as w:
        w.write('\nHe Chased the enemy ')
def Killed():
    with open ('test.txt', 'a') as w:
        w.write('\nHe Killed the enemy ')
def Died():
    with open ('test.txt', 'a') as w:
        w.write('\nHe Died \nRespawned\n ')
#Damage
def Pick29():
    with open ('test.txt', 'a') as w:
        w.write('\nHe did damage (29-) ')
def Pick30():
    with open ('test.txt', 'a') as w:
        w.write('\nHe did damage (30+) ')
def Pick90():
    with open ('test.txt', 'a') as w:
        w.write('\nHe did damage (90+) ')
def Pick150():
    with open ('test.txt', 'a') as w:
        w.write('\nHe did damage (150+) ')
def Pick200():
    with open ('test.txt', 'a') as w:
        w.write('\nHe did damage (200+) ')
def Pick250():
    with open ('test.txt', 'a') as w:
        w.write('\nHe did damage (250+) ')
#Damage Taken
def Took29():
    with open ('test.txt', 'a') as w:
        w.write('\nHe took 29- Damage ')
def Took30():
    with open ('test.txt', 'a') as w:
        w.write('\nHe took 30+ Damage ')
def Took90():
    with open ('test.txt', 'a') as w:
        w.write('\nHe took 90+ Damage ')
def Took150():
    with open ('test.txt', 'a') as w:
        w.write('\nHe took 150+ Damage ')
def Took200():
    with open ('test.txt', 'a') as w:
        w.write('\nHe took 200+ Damage ')
def Took250():
    with open ('test.txt', 'a') as w:
        w.write('\nHe took 250+ Damage ')
#Current Health/Armor
def Health49():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 49- health ')
def Health50():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 50+ health ')
def Health100():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 100+ health ')
def Health150():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 150+ health ')
def Health200():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 200+ health ')
def Health250():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 250+ health ')
def Health300():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 300+ health ')
def Armor0():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 0 Armor ')
def Armor49():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 49- Armor ')
def Armor50():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 50+ Armor ')
def Armor100():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 100+ Armor ')
def Armor150():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 150+ Armor ')
def Armor200():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 200+ Armor ')
def Armor250():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 250+ Armor ')
def Armor300():
    with open ('test.txt', 'a') as w:
        w.write('\nhas 300+ Armor ')
#Labels
def Extras():
    with open ('test.txt', 'a') as w:
        w.write('')
def Maps():
    with open ('test.txt', 'a') as w:
        w.write('')
def Champions():
    with open ('test.txt', 'a') as w:
        w.write('')
def Weapons():
    with open ('test.txt', 'a') as w:
        w.write('')
def Stacking():
    with open ('test.txt', 'a') as w:
        w.write('')
def Damage():
    with open ('test.txt', 'a') as w:
        w.write('')
def DamageT():
    with open ('test.txt', 'a') as w:
        w.write('')
def CurHealth():
    with open ('test.txt', 'a') as w:
        w.write('')
def CurArmor():
    with open ('test.txt', 'a') as w:
        w.write('')


#BUTTONS
#extra buttons
Extras = Button(master, text="Extras", command=Extras, bg="white")
Game = Button(master, text="New Game", command=Game, bg="white")
Error = Button(master, text="Error", command=Error, bg="white")
#map buttons
Maps = Button(master, text="Maps", command=Maps, bg="gray")
Awoken = Button(master, text="Awoken", command=Awoken, bg="gray",)
BC = Button(master, text="Blood Covenant", command=BC, bg="gray")
BR = Button(master, text="Blood Run", command=BR, bg="gray")
CK = Button(master, text="Corrupted Keep", command=CK, bg="gray")
MF = Button(master, text="Molten Falls", command=MF, bg="gray")
Ruins = Button(master, text="Ruins", command=Ruins, bg="gray")
Vale = Button(master, text="Vale of Pnath", command=Vale, bg="gray")
#champion butons
Anarki = Button(master, text="Anarki", command=Anarki, bg="orange")
Champions = Button(master, text="Champions", command=Champions, bg="orange")
Athena = Button(master, text="Athena", command=Athena, bg="orange")
BJ = Button(master, text="Blazkowicz", command=BJ, bg="orange")
Clutch = Button(master, text="Clutch", command=Clutch, bg="orange")
DK = Button(master, text="Death Knight", command=DK, bg="orange")
DS = Button(master, text="Doom Slayer", command=DS, bg="orange")
Eisen = Button(master, text="Eisen", command=Eisen, bg="orange")
Galena = Button(master, text="Galena", command=Galena, bg="orange")
KEEL = Button(master, text="Keel", command=KEEL, bg="orange")
Nyx = Button(master, text="Nyx", command=Nyx, bg="orange")
Ranger = Button(master, text="Ranger", command=Ranger, bg="orange")
Scalebearer = Button(master, text="ScaleBearer", command=Scalebearer, bg="orange")
Slash = Button(master, text="Slash", command=Slash, bg="orange")
Sorlag = Button(master, text="Sorlag", command=Sorlag, bg="orange")
SP = Button(master, text="Strogg & Peeker", command=SP, bg="orange")
Visor = Button(master, text="Visor", command=Visor, bg="orange")


#weapon buttons
Weapons = Button(master, text="Weapons", command=Weapons, bg="yellow")
RL = Button(master, text="Rocket Launcher", command=RL, bg="yellow")
LG = Button(master, text="Lightning Gun", command=LG, bg="yellow")
RG = Button(master, text="Rail Gun", command=RG, bg="yellow")
NG = Button(master, text="Nail Gun", command=NG, bg="yellow")
SG = Button(master, text="Shot Gun", command=SG, bg="yellow")
MG = Button(master, text="Machine Gun", command=MG, bg="yellow")
Tribolt = Button(master, text="Tri-Bolt", command=Tribolt, bg="yellow")
#stacking buttons
Stacking = Button(master, text="Stacking", command=Stacking, bg="#5D8AA8")
Mega = Button(master, text="Mega", command=Mega, bg="#5D8AA8")
Heavy = Button(master, text="Heavy", command=Heavy, bg="#5D8AA8")
Health = Button(master, text="Health", command=Health, bg="#5D8AA8")
Armor = Button(master, text="Armor", command=Armor, bg="#5D8AA8")
#damage buttons
Damage = Button(master, text="Damage", command=Damage, bg="#FA4047")
Pick29 = Button(master, text="Picked 29-", command=Pick29, bg="#FA4047")
Pick30 = Button(master, text="Picked 30+", command=Pick30, bg="#FA4047")
Pick90 = Button(master, text="Picked 90+", command=Pick90, bg="#FA4047")
Pick150 = Button(master, text="Picked 150+", command=Pick150, bg="#FA4047")
Pick200 = Button(master, text="Picked 200+", command=Pick200, bg="#FA4047")
Pick250 = Button(master, text="Picked 250+", command=Pick250, bg="#FA4047")
#damage taken buttons
DamageT = Button(master, text="Damage Taken", command=DamageT, bg="#800000")
Died = Button(master, text="He Died", command=Died, bg="#800000")
Took29 = Button(master, text="Took 29-", command=Took29, bg="#800000")
Took30 = Button(master, text="Took 30+", command=Took30, bg="#800000")
Took90 = Button(master, text="Took 90+", command=Took90, bg="#800000")
Took150 = Button(master, text="Took 150+", command=Took150, bg="#800000")
Took200 = Button(master, text="Took 200+", command=Took200, bg="#800000")
Took250 = Button(master, text="Took 250+", command=Took250, bg="#800000")
#health buttons
CurHealth = Button(master, text="Current Health", command=CurHealth, bg="#7A0CD2")
Health49 = Button(master, text="49-", command=Health49, bg="#7A0CD2")
Health50 = Button(master, text="50+", command=Health50, bg="#7A0CD2")
Health100 = Button(master, text="100+", command=Health100, bg="#7A0CD2")
Health150 = Button(master, text="150+", command=Health150, bg="#7A0CD2")
Health200 = Button(master, text="200+", command=Health200, bg="#7A0CD2")
Health250 = Button(master, text="250+", command=Health250, bg="#7A0CD2")
Health300 = Button(master, text="300+", command=Health300, bg="#7A0CD2")


#armor buttons
CurArmor = Button(master, text="Current Armor", command=CurArmor, bg="#008040")
Armor0 = Button(master, text="0", command=Armor0, bg="#008040")
Armor49 = Button(master, text="49-", command=Armor49, bg="#008040")
Armor50 = Button(master, text="50+", command=Armor50, bg="#008040")
Armor100 = Button(master, text="100+", command=Armor100, bg="#008040")
Armor150 = Button(master, text="150+", command=Armor150, bg="#008040")
Armor200 = Button(master, text="200+", command=Armor200, bg="#008040")
Armor250 = Button(master, text="250+", command=Armor250, bg="#008040")
Armor300 = Button(master, text="300+", command=Armor300, bg="#008040")

#Grid
#extras grids
Extras.grid(column=1, row=0, sticky="ew")
Game.grid(column=1, row=1, sticky="ew")
Error.grid(column=1, row=2, sticky="ew")
#map grids
Maps.grid(column=2, row=0, sticky="ew")
Awoken.grid(column=2, row=1, sticky="ew")
BC.grid(column=2, row=2, sticky="ew")
BR.grid(column=2, row=3, sticky="ew")
CK.grid(column=2, row=4, sticky="ew")
MF.grid(column=2, row=5, sticky="ew")
Ruins.grid(column=2, row=6, sticky="ew")
Vale.grid(column=2, row=7, sticky="ew")
#Champion Grids
Champions.grid(column=3, row=0, sticky="ew")
Anarki.grid(column=3, row=1, sticky="ew")
Athena.grid(column=3, row=2, sticky="ew")
BJ.grid(column=3, row=3, sticky="ew")
Clutch.grid(column=3, row=4, sticky="ew")
DK.grid(column=3, row=5, sticky="ew")
DS.grid(column=3, row=6, sticky="ew")
Eisen.grid(column=3, row=7, sticky="ew")
Galena.grid(column=3, row=8, sticky="ew")
KEEL.grid(column=3, row=9, sticky="ew")
Nyx.grid(column=3, row=10, sticky="ew")
Ranger.grid(column=3, row=11, sticky="ew")
Scalebearer.grid(column=3, row=12, sticky="ew")
Slash.grid(column=3, row=13, sticky="ew")
Sorlag.grid(column=3, row=14, sticky="ew")
SP.grid(column=3, row=15, sticky="ew")
Visor.grid(column=3, row=16, sticky="ew")
#weapon Grids
Weapons.grid(column=4, row=0, sticky="ew")
RL.grid(column=4, row=1, sticky="ew")
LG.grid(column=4, row=2, sticky="ew")
RG.grid(column=4, row=3, sticky="ew")
NG.grid(column=4, row=4, sticky="ew")
SG.grid(column=4, row=5, sticky="ew")
MG.grid(column=4, row=6, sticky="ew")
Tribolt.grid(column=4, row=7, sticky="ew")
#stacking Grids
Stacking.grid(column=5, row=0, sticky="ew")
Mega.grid(column=5, row=1, sticky="ew")
Heavy.grid(column=5, row=2, sticky="ew")
Health.grid(column=5, row=3, sticky="ew")
Armor.grid(column=5, row=4, sticky="ew")
#Damage Grids
Damage.grid(column=6, row=0, sticky="ew")
Pick29.grid(column=6, row=1, sticky="ew")
Pick30.grid(column=6, row=2, sticky="ew")
Pick90.grid(column=6, row=3, sticky="ew")
Pick150.grid(column=6, row=4, sticky="ew")
Pick200.grid(column=6, row=5, sticky="ew")
Pick250.grid(column=6, row=6, sticky="ew")
#Damage Taken Grids
DamageT.grid(column=7, row=0, sticky="ew")
Died.grid(column=7, row=1, sticky="ew")
Took29.grid(column=7, row=2, sticky="ew")
Took30.grid(column=7, row=3, sticky="ew")
Took90.grid(column=7, row=4, sticky="ew")
Took150.grid(column=7, row=5, sticky="ew")
Took200.grid(column=7, row=6, sticky="ew")
Took250.grid(column=7, row=7, sticky="ew")
#Health Grids
CurHealth.grid(column=8, row=0, sticky="ew")
Health49.grid(column=8, row=1, sticky="ew")
Health50.grid(column=8, row=2, sticky="ew")
Health100.grid(column=8, row=3, sticky="ew")
Health150.grid(column=8, row=4, sticky="ew")
Health200.grid(column=8, row=5, sticky="ew")
Health250.grid(column=8, row=6, sticky="ew")
Health300.grid(column=8, row=7, sticky="ew")
#Armor Grids
CurArmor.grid(column=9, row=0, sticky="ew")
Armor0.grid(column=9, row=1, sticky="ew")
Armor49.grid(column=9, row=2, sticky="ew")
Armor50.grid(column=9, row=3, sticky="ew")
Armor100.grid(column=9, row=4, sticky="ew")
Armor150.grid(column=9, row=5, sticky="ew")
Armor200.grid(column=9, row=6, sticky="ew")
Armor250.grid(column=9, row=7, sticky="ew")
Armor300.grid(column=9, row=8, sticky="ew")






#PACKING

#THE MAIN LOOP
mainloop()
