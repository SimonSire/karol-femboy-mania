    # hello welcome to the script of karolfemboymania where there are barely any femboys at the moment as i write this
# and no im not adding any rn
# dont worry im not gonna be adding any either

# atp im just adding pointless shit

init python:
    renpy.music.register_channel("karolChannel", mixer="sfx")

    def karolTalks(event, **kwargs):
        shit = 0
        while shit < 50:
            if karolTalkingShit:
                sound_dongus = renpy.random.randint(0,2)
                if event == "show":
                    if sound_dongus == 0:
                        renpy.sound.queue("karoltalk 1.mp3", channel="karolChannel", loop=False)
                    elif sound_dongus == 1:
                        renpy.sound.queue("karoltalk 2.mp3", channel="karolChannel", loop=False)
                    elif sound_dongus == 2:
                        renpy.sound.queue("karoltalk 3.mp3", channel="karolChannel", loop=False)
                elif event == "slow_done" or event == "end":
                    renpy.sound.stop(channel="karolChannel")
            shit += 1

define k = Character("Karol Mijas", color="#ffe864", callback=karolTalks)
define un = Character("???")
define d = Character("papa Mijas", color="#706316")
define do = Character("Domin", color="#a32d76")
define b = Character("Bartender", color="#264972")
define p1 = Character("Other Police Officer", color="#0c2644")
define p2 = Character("Police Officer", color="#1366c5")
define bb = Character("Floor manager", color="#d45130")
define w = Character("Proffessional Gambler", color="#14531d")
define wb = Character("Gambler", color="#091811")
define br = Character("Broke robux", color="#9f3db3")
define sx = Character("Sexy Gamemaster", color="#39b308")
define pl = Character("Undersized delinquent", color="#a87698")
define b2 = Character("Bartender 2", color="#120c63")

define j = Character("Judge", color="#186d45")
define t = Character("Trump", color="#614e12")
define ob = Character("Obama", color="#503528")

default isPathetic = True
default isZlinkDie = False
default isMatysiakAnger = False

default femboyChoices = 0
default casinoLovesYou = 0

#simon bar thingiesss
default hasbeenbar = 0
default barguybad = 0   #0 is neutral?, 1 is like happy, 2 is you told the truth

#courts
default didyankdoor = 0
default staysilent = 0

default shitcourt = 1
default judgepissedlevel = 0

#bors
default wrenchCasinoShingas = 0         #0 = never met robux, 1 = you made robux win, 2 = you made robux lose
default pielaCasinoShingas = 0          #0 = never met piela, 1 = is being ignored, 2 = told to fuck off, 3 = agreed to help
default wiktorCasinoShingas = 0
default sexyguyCasinoShingas = 0
default sexyguyMadnessLevel = 0

default casinoMajorHappens = 0

default shapeDraggable = None
default shapeDroppable = None
default doShapesMatch = False

default randomAssShit = 0 #when used value only from 1 to 100

#fnaf shit here
default starttime = 0
default lastCheckUpdate = 0
default audioCooldownStart = 0

default drywallLocation = 1
default dryPrevLocation = 1
default drywallRandom = 0
default timeDryMoved = 0

default matysiakLocation = 0
default matPrevLocation = 0
default matysiakRandom = 0
default timeMatMoved = 0

default cameraSelect = 5
default flashBright = False
default hoverTime = 0
default actionDoorLeft = 0
default actionDoorTop = 0
default actionDoorRight = 0
default flashBattery = 0
default drywallAttack = 0
default matysiakAttack = 0

default debugMode = False
default karolTalkingShit = True

#gambel machine
define interval = 0.1 
define rolltime = 1
define rollwheelradius = 500
define slotsnumber = 6
define gamble1didwin = False

init python: #PYTHON FUNCTIONS AND THINGIESS
    casinoRoomsTable = [
        [0,0,0,0,0,0,0,0],                  #room0 toilet stuck
        [2,2,3,3,3,3,3,3],                  #room1
        [3,5,5,5,5,5,6,6],                  #room2
        [1,2,4,4,4,5,5,5],                  #room3
        [3,5,5,5,7,7,7,7],                  #room4
        [2,3,4,4,6,6,8,8],                  #room5
        [2,5,5,10,10,10,10,10],             #room6
        [4,4,9,9,9,9,9,9],                  #room7
        [5,12,12,12,12,12,12,12],           #room8
        [7,11,11,11,11,11,11,11],           #room9
        [6,13,13,13,13,13,13,13],           #room10
        [11,11,11,11,11,11,11,11],          #room11 left office door
        [12,12,12,12,12,12,12,12],          #room12 hole in the office ceiling
        [13,13,13,13,13,13,13,13]           #room13 right office door
    ]
    casinoAudioCueTable = [
        [0,0,0,0],
        [2,2,3,3],          #room1
        [2,2,3,3],          #room2
        [2,2,3,3],          #room3
        [2,3,3,5],          #room4
        [2,3,3,5],          #room5
        [2,2,3,5],          #room6
        [3,4,4,5],          #room7
        [2,3,5,5],          #room8
        [3,4,4,7],          #room9
        [5,6,6,6],          #room10
        [11,11,11,11],
        [12,12,12,12],
        [13,13,13,13]
    ]
    slotstable = [
        Image("gambel0.png"),
        Image("gambel1.png"),
        Image("gambel2.png"),
        Image("gambel3.png"),
        Image("gambel4.png"),
        Image("gambel5.png"),
        Image("gambel6.png")
    ]

    casinoAudioCueFile = [
        "karolcue1.mp3",
        "karolcue2.mp3",
        "karolcue3.mp3",
        "karolcue4.mp3",
        "karolcue5.mp3"
    ]


    def drag_placed(drags, drop):
        global shapeDraggable, shapeDroppable, doShapesMatch
        if not drop:
            return
        shapeDraggable = drags[0].drag_name
        shapeDroppable = drop.drag_name
        doShapesMatch = (drags[0].drag_name == drop.drag_name)

        return True

    def make_slots_table():
        return [
            [renpy.random.randint(0, 6) for c in range(3)]
            for r in range(7)
        ]
    
    def makeMenMove():
        global randomAssShit, lastCheckUpdate, starttime, drywallRandom, matysiakRandom, drywallLocation, matysiakLocation, dryPrevLocation, matPrevLocation, timeDryMoved, timeMatMoved, drywallAttack, matysiakAttack
        
        randomAssShit = renpy.random.randint(1,100)
        
        if (lastCheckUpdate + 1) < renpy.get_game_runtime():
            lastCheckUpdate = renpy.get_game_runtime()

            if (renpy.get_game_runtime() - starttime) < 60:
                drywallRandom = renpy.random.randint(0, 7)
                matysiakRandom = renpy.random.randint(0, 11)

            elif (renpy.get_game_runtime() - starttime) > 180:
                drywallRandom = renpy.random.randint(0, 3)
                matysiakRandom = renpy.random.randint(0, 5)
            else:
                drywallRandom = renpy.random.randint(0, 5)
                matysiakRandom = renpy.random.randint(0, 7)

            if drywallRandom == 0 and (timeDryMoved + 4) < renpy.get_game_runtime():
                dryPrevLocation = drywallLocation
                timeDryMoved = renpy.get_game_runtime()
                drywallLocation = casinoRoomsTable[drywallLocation][renpy.random.randint(0,7)]

            if matysiakRandom == 0 and (timeMatMoved + 4) < renpy.get_game_runtime():
                matPrevLocation = matysiakLocation
                timeMatMoved = renpy.get_game_runtime()
                matysiakLocation = casinoRoomsTable[matysiakLocation][renpy.random.randint(0,7)]

            if drywallLocation > 10 and drywallAttack == 0:
                drywallAttack = renpy.get_game_runtime() + 5 + renpy.random.randint(0,5)

            if matysiakLocation > 10 and matysiakAttack == 0:
                matysiakAttack = renpy.get_game_runtime() + 5 + renpy.random.randint(0,5)


    def menGoToSound():
        global drywallLocation, matysiakLocation, timeDryMoved, timeMatMoved
        if renpy.random.randint(0, 2) < 2:
            timeDryMoved = renpy.get_game_runtime()
            drywallLocation = casinoAudioCueTable[drywallLocation][renpy.random.randint(0,3)]
        if renpy.random.randint(0, 2) < 2:
            timeMatMoved = renpy.get_game_runtime()
            matysiakLocation = casinoAudioCueTable[matysiakLocation][renpy.random.randint(0,3)]


#i have no idea what it does but im not touching it:
#DONT TOUCH OR CASINO GAMBLING WILL BREAK
transform size:
    zoom 8

#######################################################################
#SCREEENSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
#######################################################################

screen show_time:
    zorder 256
    if (renpy.get_game_runtime() - starttime) < 60:
        text "{size=*2}{color=#ffffff}[12]:[int((renpy.get_game_runtime() - starttime) % 60):02d] AM{/color}{/size}" xalign 0.9 yalign 0.15
    else:
        text "{size=*2}{color=#ffffff}[int((renpy.get_game_runtime() - starttime) // 60)]:[int((renpy.get_game_runtime() - starttime) % 60):02d] PM{/color}{/size}" xalign 0.9 yalign 0.15

    if (audioCooldownStart + 20) > renpy.get_game_runtime():
        text "{color=#ffffff}Cooldown = [int(audioCooldownStart + 20 - renpy.get_game_runtime())]{/color}" xalign 0.9 yalign 0.22

    key "x" action [Show("DEBUGmode"), SetVariable("debugMode", True)]
    key "c" action [Hide("DEBUGmode"), SetVariable("debugMode", False)]
    timer 0.1 action Function(makeMenMove) repeat True
    if drywallLocation == 9 and dryPrevLocation == 7:
        timer 0.001 action [SetVariable("dryPrevLocation",9)]
        if renpy.random.randint(0,9) < 6:
            timer 0.001 action Play("audio","stepsleft.mp3")
    #if drywallLocation == 8 and dryPrevLocation == 5:
    #    timer 0.001 action [SetVariable("dryPrevLocation",8),Play("audio","ventcrawl.mp3")]#change sound
    if drywallLocation == 12 and dryPrevLocation == 8:
        timer 0.001 action [SetVariable("dryPrevLocation",12)]
        if renpy.random.randint(0,9) < 6:
            timer 0.001 action Play("audio","ventcrawl.mp3")
    if drywallLocation == 10 and dryPrevLocation == 6:
        timer 0.001 action [SetVariable("dryPrevLocation",10)]
        if renpy.random.randint(0,9) < 6:
            timer 0.001 action Play("audio","stepsright.mp3")
    if matysiakLocation == 9 and matPrevLocation == 7:
        timer 0.001 action [SetVariable("matPrevLocation",9)]
        if renpy.random.randint(0,9) < 6:
            timer 0.001 action Play("audio","stepsfartleft.mp3")
    #if matysiakLocation == 8 and matPrevLocation == 5:
    #    timer 0.001 action [SetVariable("matPrevLocation",8),Play("audio","ventfartcrawl.mp3")]#change sound
    if matysiakLocation == 12 and matPrevLocation == 8:
        timer 0.001 action [SetVariable("matPrevLocation",12)]
        if renpy.random.randint(0,9) < 6:
            timer 0.001 action Play("audio","ventfartcrawl.mp3")
    if matysiakLocation == 10 and matPrevLocation == 6:
        timer 0.001 action [SetVariable("matPrevLocation",10)]
        if renpy.random.randint(0,9) < 6:
            timer 0.001 action Play("audio","stepsfartright.mp3")

screen door_buttons:
    zorder 128
    imagebutton:
        xalign 0.2 yalign 0.5
        idle "buttoleft.png"
        hover "buttolefthover.png"
        if flashBattery >= 0:
            hovered [Show("flashleft"), SetVariable("hoverTime", renpy.get_game_runtime() )]
        unhovered [Hide("flashleft"), SetVariable("hoverTime",0)]
        action [SetVariable("rolltime",1)] #this does nothing but DO NOT TOUCH

    imagebutton:
        xalign 0.8 yalign 0.5
        idle "buttoright.png"
        hover "buttorighthover.png"
        if flashBattery >= 0:
            hovered [Show("flashright"), SetVariable("hoverTime", renpy.get_game_runtime() )]
        unhovered [Hide("flashright"), SetVariable("hoverTime",0)]
        action [SetVariable("rolltime",1)] #this does nothing but DO NOT TOUCH

    imagebutton:
        xalign 0.5 yalign 0.1
        idle "buttotop.png"
        hover "buttotophover.png"
        if flashBattery >= 0:
            hovered [Show("flashtop"), SetVariable("hoverTime", renpy.get_game_runtime() )]
        unhovered [Hide("flashtop"), SetVariable("hoverTime",0)]
        action [SetVariable("rolltime",1)] #this does nothing but DO NOT TOUCH

    imagebutton:
        xalign 0.5 yalign 0.9
        idle "buttodown.png"
        hover "buttodownhover.png"
        if flashBattery >= 0:
            action [Hide("door_buttons"), Show("cameraview")]
        else:
            action [Play("audio", "jimdead.mp3")]
    imagebutton:
        xalign 0.2
        yalign 0.9
        idle "flashbutton.png"
        hover "flashbuttonhover.png"
        if flashBattery >= 0:
            if flashBright:
                action [ToggleVariable("flashBright"), Play("audio", "jimalt.mp3")]
            else:
                action [ToggleVariable("flashBright"), Play("audio", "jim.mp3")]
        else:
            action [SetVariable("flashBright",False), Play("audio", "jimdead.mp3")]

    fixed:
        xalign 0.1
        ypos 707
        if (hoverTime > 0) and flashBright:
            if flashBattery > 33:
                if renpy.random.randint(0,1) == 0:
                    image "batterypainbright" zoom 1.5
                else:
                    image "batterypainbright2" zoom 1.5
            else:
                if renpy.random.randint(0,1) == 0:
                    image "batterymorepainbright" zoom 1.5
                else:
                    image "batterymorepainbright2" zoom 1.5
        elif flashBattery < 0:
            image "batterydead" zoom 1.5
        else:
            if flashBattery >= 67:
                if flashBright:
                    image "batteryfatbright" zoom 1.5
                else:
                    image "batteryjoyfull" zoom 1.5
            elif flashBattery <= 33:
                if flashBright:
                    image "batteryalmostcrybright" zoom 1.5
                else:
                    image "batterytired" zoom 1.5
            else:
                if flashBright:
                    image "batteryworrybright" zoom 1.5
                else:
                    image "batterypickle" zoom 1.5

    fixed:
        if actionDoorLeft > 0:
            image "brightburnleft"
            timer 0.5 action [SetVariable("actionDoorLeft",0)]

        if actionDoorTop > 0:
            #text "{color=#ffffff}top act{/color}" xalign 0.5 yalign 0.3
            image "brightburnleft" xpos 470 ypos -510
            timer 0.5 action [SetVariable("actionDoorTop",0)]

        if actionDoorRight > 0:
            image "brightburnleft" xpos 930 ypos 0
            timer 0.5 action [SetVariable("actionDoorRight",0)]

screen flashleft:
    fixed:
        if flashBright:
            image "flashleftbright"
        else:
            image "flashleft"
        if drywallLocation == 11:
            if flashBright:
                image "drydoorleftbright"
            else:
                image "drydoorleft"
        if matysiakLocation == 11:
            if flashBright:
                image "matdoorleftbright"
            else:
                image "matdoorleft"
    if flashBright and (hoverTime + 2 < renpy.get_game_runtime()) and (actionDoorLeft == 0) and (drywallLocation == 11 or matysiakLocation == 11):
        if drywallLocation == 11:
            timer 0.001 action [SetVariable("actionDoorLeft", renpy.get_game_runtime()), SetVariable("drywallAttack",0), SetVariable("drywallLocation",renpy.random.randint(2, 5)), Play("audio", "hl2scream.mp3")]
        else:
            timer 0.001 action [SetVariable("actionDoorLeft", renpy.get_game_runtime()), SetVariable("matysiakAttack",0), SetVariable("matysiakLocation",renpy.random.randint(2, 5)), Play("audio", "hl2scream.mp3")]
    if flashBright:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.3)] repeat True
    else:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.03)] repeat True
    if flashBattery < 0:
        timer 0.001 action [Hide("flashleft"), SetVariable("hoverTime",0)]

screen flashtop:
    fixed:
        if flashBright:
            image "flashtopbright"
        else:
            image "flashtop"
        if drywallLocation == 12:
            if flashBright:
                image "drydoortopbright"
            else:
                image "drydoortop"
        if matysiakLocation == 12:
            if flashBright:
                image "matdoortopbright"
            else:
                image "matdoortop"
    if flashBright and (hoverTime + 2 < renpy.get_game_runtime()) and (actionDoorTop == 0) and (drywallLocation == 12 or matysiakLocation == 12):
        if drywallLocation == 12:
            timer 0.001 action [SetVariable("actionDoorTop", renpy.get_game_runtime()), SetVariable("drywallAttack",0), SetVariable("drywallLocation",renpy.random.randint(2, 5)), Play("audio", "hl2scream.mp3")]
        else:
            timer 0.001 action [SetVariable("actionDoorTop", renpy.get_game_runtime()), SetVariable("matysiakAttack",0), SetVariable("matysiakLocation",renpy.random.randint(2, 5)), Play("audio", "hl2scream.mp3")]
    if flashBright:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.3)] repeat True
    else:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.03)] repeat True
    if flashBattery < 0:
        timer 0.001 action [Hide("flashtop"), SetVariable("hoverTime",0)]

screen flashright:
    fixed:
        if flashBright:
            image "flashrightbright"
        else:
            image "flashright"
        if drywallLocation == 13:
            if flashBright:
                image "drydoorrightbright"
            else:
                image "drydoorright"
        if matysiakLocation == 13:
            if flashBright:
                image "matdoorrightbright"
            else:
                image "matdoorright"
    if flashBright and (hoverTime + 2 < renpy.get_game_runtime()) and (actionDoorRight == 0) and (drywallLocation == 13 or matysiakLocation == 13):
        if drywallLocation == 13:
            timer 0.001 action [SetVariable("actionDoorRight", renpy.get_game_runtime()), SetVariable("drywallAttack",0), SetVariable("drywallLocation",renpy.random.randint(2, 5)), Play("audio", "hl2scream.mp3")]
        else:
            timer 0.001 action [SetVariable("actionDoorRight", renpy.get_game_runtime()), SetVariable("matysiakAttack",0), SetVariable("matysiakLocation",renpy.random.randint(2, 5)), Play("audio", "hl2scream.mp3")]
    if flashBright:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.3)] repeat True
    else:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.03)] repeat True
    if flashBattery < 0:
        timer 0.001 action [Hide("flashright"), SetVariable("hoverTime",0)]

screen cameraview:
    timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.015)] repeat True
    if flashBattery < 0:
        timer 0.001 action [Hide("cameraview")]
    if cameraSelect == 1:
        fixed:
            if renpy.random.randint(0,2) == 0:
                image "cam cas1alt"
            else:
                image "cam cas1"
            if drywallLocation == 1:
                image "cam dry1"
            if matysiakLocation == 1:
                image "cam mat1"
    if cameraSelect == 2:
        fixed:
            image "cam cas2"
            if drywallLocation == 2:
                image "cam dry2"
            if matysiakLocation == 2:
                image "cam mat1" xpos 570 ypos 70
    if cameraSelect == 3:
        fixed:
            image "cam cas3"
            if drywallLocation == 3:
                image "cam dry3"
            if matysiakLocation == 3:
                image "cam mat3"
    if cameraSelect == 4:
        fixed:
            image "cam cas4"
            if drywallLocation == 4:
                image "cam dry1"
            if matysiakLocation == 4:
                image "cam mat4"
    if cameraSelect == 5:
        fixed:
            image "cam cas5"
            if drywallLocation == 5:
                image "cam dry1" xpos -200
            if matysiakLocation == 5:
                image "cam mat1" xpos -250 ypos 150
    if cameraSelect == 6:
        fixed:
            image "cam cas6"
            if drywallLocation == 6:
                image "cam dry1"
            if matysiakLocation == 6:
                image "cam mat6"
    if cameraSelect == 7:
        fixed:
            image "cam cas7"
            if drywallLocation == 7:
                image "cam dry1"
            if matysiakLocation == 7:
                image "cam matysiakright" xalign 0.5 yalign 0.5
    if cameraSelect == 8:
        fixed:
            image "cam cas8"
            if drywallLocation == 8:
                image "cam dry1"
            if matysiakLocation == 8:
                image "cam matysiakright" xalign 0.5 yalign 0.5
    if cameraSelect == 9:
        fixed:
            image "cam cas9"
            if drywallLocation == 9:
                image "cam dry1"
            if matysiakLocation == 9:
                image "cam matysiakright" xalign 0.5 yalign 0.5
    if cameraSelect == 10:
        fixed:
            image "cam cas10"
            if drywallLocation == 10:
                image "cam dry1"
            if matysiakLocation == 10:
                image "cam matysiakright" xalign 0.5 yalign 0.5

    fixed:
        image "cam overlay"
        image "cameralayout"

    imagebutton:
        xalign 0.5 yalign 0.9
        idle "buttodown.png"
        hover "buttodownhover.png"
        action [Show("door_buttons"), Hide("cameraview")]
    
    imagebutton:    #room1
        xpos 1480 ypos 463
        idle "camerabutton.png"
        hover "camerabuttonhover.png"
        action [SetVariable("cameraSelect",1)]
    imagebutton:    #room2
        xpos 1590 ypos 511
        idle "camerabutton.png"
        hover "camerabuttonhover.png"
        action [SetVariable("cameraSelect",2)]
    imagebutton:    #room3
        xpos 1405 ypos 543
        idle "camerabutton.png"
        hover "camerabuttonhover.png"
        action [SetVariable("cameraSelect",3)]
    imagebutton:    #room4
        xpos 1385 ypos 603
        idle "camerabutton.png"
        hover "camerabuttonhover.png"
        action [SetVariable("cameraSelect",4)]
    imagebutton:    #room5
        xpos 1528 ypos 605
        idle "camerabutton.png"
        hover "camerabuttonhover.png"
        action [SetVariable("cameraSelect",5)]
    imagebutton:    #room6
        xpos 1640 ypos 665
        idle "camerabutton.png"
        hover "camerabuttonhover.png"
        action [SetVariable("cameraSelect",6)]
    imagebutton:    #room7
        xpos 1400 ypos 805
        idle "camerabutton.png"
        hover "camerabuttonhover.png"
        action [SetVariable("cameraSelect",7)]
    imagebutton:    #room8
        xpos 1520 ypos 785
        idle "camerabutton.png"
        hover "camerabuttonhover.png"
        action [SetVariable("cameraSelect",8)]
    imagebutton:    #room9
        xpos 1440 ypos 900
        idle "camerabutton.png"
        hover "camerabuttonhover.png"
        action [SetVariable("cameraSelect",9)]
    imagebutton:    #room10
        xpos 1636 ypos 844
        idle "camerabutton.png"
        hover "camerabuttonhover.png"
        action [SetVariable("cameraSelect",10)]

    imagebutton:
        xpos 1520 ypos 521
        idle "audiobutton.png"
        hover "audiobuttonhover.png"
        if (audioCooldownStart + 20) < renpy.get_game_runtime():
            action [SetVariable("audioCooldownStart",renpy.get_game_runtime()), Function(menGoToSound),SetVariable("flashBattery", flashBattery - 2), Play("audio", casinoAudioCueFile[renpy.random.randint(0,4)])]

screen DEBUGmode:
    zorder 224
    text "{color=#ffffff}rywall [int(drywallAttack)]{/color}" xalign 0.1 yalign 0.05
    text "{color=#ffffff}atysiak [int(matysiakAttack)]{/color}" xalign 0.1 yalign 0.1
    text "{color=#ffffff}DEBUG dry in room [drywallLocation] [dryPrevLocation]{/color}" xalign 0.1 yalign 0.15
    text "{color=#ffffff}DEBUG mat in room [matysiakLocation] [matPrevLocation]{/color}" xalign 0.1 yalign 0.2
    text "{color=#ffffff}bater [int(flashBattery)]{/color}" xalign 0.1 yalign 0.25
    text "{color=#ffffff}randomshit [randomAssShit]{/color}" xalign 0.1 yalign 0.3

    hbox:
        xalign 0.95
        yalign 0.9
        spacing 20
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("starttime",min(starttime + 10, renpy.get_game_runtime()))]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("starttime",starttime - 10)]

    grid 4 5:
        xalign 0.05
        yalign 0.5
        spacing 20
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("drywallLocation",1)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("drywallLocation",2)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("matysiakLocation",1)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("matysiakLocation",2)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("drywallLocation",3)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("drywallLocation",4)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("matysiakLocation",3)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("matysiakLocation",4)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("drywallLocation",5)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("drywallLocation",6)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("matysiakLocation",5)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("matysiakLocation",6)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("drywallLocation",7)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("drywallLocation",8)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("matysiakLocation",7)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("matysiakLocation",8)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("drywallLocation",9)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("drywallLocation",10)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("matysiakLocation",9)]
        imagebutton:
            idle "camerabutton.png"
            hover "camerabuttonhover.png"
            action [SetVariable("matysiakLocation",10)]


# The game starts here.
######################################################################################################################################################
label _1ST_SECTION_ORIGINAL_GAME_HERE_________________________________________________________________________________________________________________:
    ##################################################################################################################################################
    label start:

        play music karoltheme_poor fadein 2.0 volume 0.2
        scene bg bed

        k "Ohh man I looove sitting here makking games in Godot and jerkind off"

        play sound knock

        "*knock knock*"

        play sound dad1
        un "Come out here, son."

        play sound door

        show livinroom

        show dad
        play sound dad2
        d "son."

        play sound dad3
        d "you have {color=#de1809}3 days to move out.{/color}"
        ##with vpunch
        ##extend "{color=#e34236}3 days to move out." ##simon u fucked this shit up it aint working unless u split the voice line

        play sound dad4

        d "we're tired of your nonsense"
        play sound dad5

        d "for your entire life, you've done nothing but make garrys mod maps and gooning on the bathroom floor (not comfy)"

        k "B-but dad.. "
        k "B-but dad.. My map got over 30 thousand downloads!"
        
        play sound dad6
        d "now start packing your things"

        hide dad with moveoutleft

        ".."

        play sound door
        scene bg bed

        k "oh mnnooo what am going to d9o9 now"

        k "i have to..."

        show phone with moveinbottom

        k "call my friends! maybe someone can take me"
        
        show phcall

        play sound callp

        $ renpy.pause(7.0, hard=True)
        
        

        show callzelazo

        $ renpy.pause(5.0, hard=True)

        k "hes busy"

        k "ill call someo ne else tgen"

        play sound horse

        hide callzelazo

        show phcall


        $ renpy.pause(4.5, hard=True)

        show callhorse

        $ renpy.pause(6.0, hard=True)

        hide callhorse
        hide phcall
        

        k "stupid fucker"

        k "okay, last try, i hope he will accept me"

        show phcall
        play sound calling
        $ renpy.pause(3.0, hard=True)
        show domnical
        play sound dom1
        do "Hello karol."

        play sound dom2
        menu:
            do "How are you doinmg?"
            "I'm so good doing right now":
                play sound dom3
                do "That;s so giiid!!"
                k "wait no... im not good at all"
            "I want you domin.":
                $ femboyChoices = femboyChoices + 1
                play sound dom4
                do "Woah.."
        
        k "domin.. my ass is kind of homeless.. and femboyless"
        k "i need yuo domin"

        play sound dom5
        
        do "Okay!!!"
        play sound dom6
        do "Here's my adress: "
        play sound dom7
        do "Here's my adress: Gdańska 129, Łódź"
        play sound dom8
        menu:
            do "Come to me!"
            "Wow, that's not even that far away!!":
                play sound dom9
                do "Really?? THat is such good news!"
                k "this is so good! i will be right there!"
            "I'm not sure where that is":
                play sound dom10
                do "well.. just put it in ur gps, okay?"
                k "Okay, I will!"
                k "I'll try my best"

        k "I gotta get to my car then"

        show gar
        play sound door

        k "here is my car"

        show mey with moveinbottom
        play sound appear

        k "here is my key for my csar"

        k "i guess its time to leave this crib behind"

        show black
        stop music fadeout 5.0

        play sound carstart

        $ renpy.pause(9.0, hard=True)

        show drive
        play music driving fadein 1.0

        k "finally im on the road"

        k "the car took ages to start"

        k "ill be at domins house sooon"

        show pickle with moveinright

        $ renpy.pause(0.5, hard=True)

        show drivecrash with vpunch
        play sound crash

        k ".."

        k "That was a weird speed bump"

        k "this ride is so nice"
        k "the wind is blowing into my head"
        k " i love this ride"
        stop music fadeout 0.5
        play sound stopcar
        show drivearrived
        k "it looks like imn hgere"   

        play sound getout
        $ renpy.pause(6.0, hard=True)
        show destination


        k  "i cant wait to see domin"
        jump house

    label house:
        play music karoltheme_poor fadein 5.0 volume 0.2
        play audio foot
        show house1
        k "this house looks pretty good so far"
        play audio foot
        show door1
        k "that's the front door right there!"
        play audio foot
        show door2
        play audio knock
        "*Karol Mijas knocks on the door*"
        
        play sound dom11
        do "Karol Mijas, is that you? Come in."

        show lv2
        play audio door

        show domin with moveinbottom

        play sound dom12
        do "Something reallly bad happened.."
        play sound dom13
        do "My toilet shattered.."
        play sound dom14
        menu:
            do "into a million pieces"

            "That is so horrible":
                play sound dom15
                do "Yeah.. I'm so unluckyu.."
                play sound dom16
                do "I will go have to fix it now"
            "I want you domin":
                play sound dom17
                do "But.. my toilet"
                play sound dom18
                do "I'm sorry but i gotta fix it now"

        k "Okay, I'm gonna go to the bar"
        k "Goodbye!"
        
        hide door2
        show door1
        hide domin
        play sound door
        hide lv2 

        k "I really need to drink right now"
        play sound foot
        hide door1
        show house1

        k "got to get to the bar nearby here"

        hide house1
        show destination
        play sound foot

        k "really need a drink right now so muchg"

        jump walking


    label walking:

        show walk1
        play music footsteps fadein 2.0
        k "What a lovely street"

        stop music
        play sound foot
        play music ambienace
        show bar1
        k "Here is the bar, yippee!!"

        play sound door
        show bar2
        stop music
        play music jazz fadein 1.5 volume 0.2
        play sound bar1
        un "Hello there."
        play sound bar2
        b "I'm the bartender here"
        play sound bar3
        b "Would you like something to drink, good sir?"

        menu:
            "Yes, PLEASE!":
                jump continued
            "No":
                play sound bar5
                b "Hey, think about it, I think you might want something to drink"

                menu:
                    "Okay fine":
                        jump continued
                    "No":
                        play sound bar6
                        b "Come ooon, it will be fun"

                        menu:
                            "Okay":
                                jump continued
                            "No":
                                play sound bar7
                                b "Just do it. Order some drinks."

                                menu:
                                    "Fine":
                                        jump continued
                                    "No":
                                        play sound bar8
                                        b "You can't leave"

                                        menu:
                                            "Yes":
                                                jump continued
                                            "No":
                                                play sound bar9
                                                b "Get something to drink man"

                                                menu:
                                                    "Sure":
                                                        jump continued
                                                    "No":
                                                        jump nuhuh

        label nuhuh:
            play sound bar10
            b "Nuh uh"

            menu:
                "Yeah":
                    jump continued
                "No":
                    play sound bar11
                    b "Can't do that"

                    menu:
                        "Yeah":
                            jump continued
                        "No":
                            play sound bar12
                            b "Think about the taste"

                            menu:
                                "Yeah":
                                    jump continued
                                "No":
                                    jump nuhuh

        label continued:
            play sound bar4
            b "Let me pour some of our finest wine in for you."

            "Karol Mijas takes a big gulp"

            k "Why.. do i feel so weird??"

            $ renpy.pause(2, hard=True)

            play sound bad
            show horse1 with vpunch
            play music horseishere volume 0.5
            k "You fucker!"
            k "Why the long face?"
            show fists with moveinbottom
            menu:
                "FIGHT":
                    hide fists
                    show horse1 with hpunch
                    show fists2
                    play sound bad
                    $ renpy.pause(0.5, hard=True)
                    hide fists2
                    show fists
            
            show fists
            hide fists2
            play sound hose1
            menu:
                "FIGHT":
                    hide fists
                    show horse1 with hpunch
                    show fists2
                    play sound bad
                    $ renpy.pause(0.5, hard=True)
                    hide fists2
                    show fists
            
            hide fists2
            show fists
            play sound hose2
            menu:
                "FIGHT":
                    hide fists
                    show horse1 with hpunch
                    show fists2
                    play sound bad
                    $ renpy.pause(0.5, hard=True)
                    hide fists2
                    show fists
            
            hide fists2
            show fists
            play sound hose3
            menu:
                "FIGHT":
                    hide fists
                    show horse1 with hpunch
                    show fists2
                    play sound bad
                    $ renpy.pause(0.5, hard=True)
                    hide fists2
                    show fists
            $ renpy.pause(1.0, hard=True)

            "The horse attacks"

            play sound hose2
            hide fists2
            show fists with vpunch

            $ renpy.pause(2.0, hard=True)

            jump drugged

######################################################################################################################################################
label _END_OFORIGINAL_PART_AND_NOW_ESCAPING_BAR_______________________________________________________________________________________________________:
    ##################################################################################################################################################
    label drugged:
        stop music fadeout 0.5

        scene black
        "The horses attack puts you to sleep"

        "Some time passes.."

        play music "karolthemeEVIL.mp3" volume 0.2 fadein 2.0

        scene barfloor1

        "You suddenly come back to consciousness"

        scene barfloor2

        

        play sound bardeads

        "You notice the bartender laying dead on the floor"


        k "huh thats pretty weird"

        k "why'd he collapse like that what happened to him"

        play sound police

        "Suddenly police sirens scream"

        play sound glassbreak

        "*glass breaking*"

        p2 "Ugghh"

        p1 "The front door was open you idiot"

        p2 "Shut uuup. Just let me do my thing man."

        p2 "Now let's take a look at what happaned here."

        play sound foots

        "*sounds of footsteps getting closer*"

        show dry with moveinright

        play sound cloth

        p2 "hey hey there.. yellow guy?"

        p2 "ehhhh, why'd you do this?"

        menu:
                "Yeah":
                    k "yeah"
                    p2 "uh huh"
                "I didn't do this!!":
                    k "You gotta believe me!! I didn't do this!"
                    p2 "sure pally-o broskiti-o whatever you say"
                    p2 "lil bro's dead on the floor and yo fists are{nw=0.0}"
                    play sound impact2
                    with vpunch
                    extend "{b} COVERED{/b} in {color=#de1809}blood"
                    p2 "Just look at you. What a sorry sight."
                    menu:
                            "It was not me man":
                                k "Beleive me pleasee it was not me"
                                k "I wouldnt do this to anybody.."
                                p2 "yeah im like, pretty sure you did it"
                                k "actually.."
                                k "yeah.."
                                k "yeah.. i would do this sort of thing"
                                p2 "you got like a.. screw loose or something?"
                                p2 "anyway.."
                            "Okay fine i did this, me":
                                k "Okay okay i did this, it was me, me!"
                                p2 "good, good.. a confession."
                                p2 "perfect, in fact"
                                p2 "unfortunately for you.."

        
        p2 "im afraid imma have to take you in, you're coming wth me brotisserie chicken"

        menu:
                "FIGHT":
                    jump fight
                "FLEE":
                    jump flee


    label fight:
        show bfists with moveinbottom
        k "I'm nOT GOING DOWN WITHOUT A FIGHT"
        $ renpy.pause(0.2, hard=True)
        hide bfists
        show bfists2
        show dry with hpunch
        play sound bad
        hide bfists2
        show bfists
        p2 "OOH"
        p2 "assault on a policer, lemme write that down, yup"
        menu:
                "FIGHT":
                    k "Taste THIS you fucke!1"
                    $ renpy.pause(0.5, hard=True)
                    hide bfists
                    show bfists2
                    show dry with hpunch
                    play sound bad
                    hide bfists2
                    show bfists
                    p2 "AAGHH"
                    p2 "stop resisting lil bro."
                    menu:
                            "FIGHT":
                                k "take this AND tTHIS!!"
                                $ renpy.pause(0.5, hard=True)
                                hide bfists
                                show bfists2
                                show dry with hpunch
                                play sound bad
                                hide bfists2
                                show bfists
                                $ renpy.pause(0.2, hard=True)
                                hide bfists
                                show bfists2
                                show dry with hpunch
                                play sound bad
                                hide bfists2
                                show bfists
                                p2 "UGHH"
                                p2 "THAT'S IT, ILL HANDLE IT MYSELF"
                                menu:
                                        "FIGHT":
                                            $ renpy.pause(0.2, hard=True)
                                            hide bfists
                                            show dry2 with vpunch
                                            play sound gun
                                            p2 "you are done"

                                            menu:
                                                    "FLEE":
                                                        $ isPathetic = False
                                                        jump flee
                                                    "FLEE":
                                                        $ isPathetic = False
                                                        jump flee
                                                    "FUCKING RUN AWAY":
                                                        $ isPathetic = False
                                                        jump flee
                                        "FLEE":
                                            jump flee
                            "FLEE":
                                jump flee
                "FLEE":
                    jump flee


    label flee:
        if isPathetic:
            "*you turn around and start flooring it like a pussy*"
            "your a fuckin pussy bro"
        else:
            "you turn around and start flooring it"
            "i'd say ur a pussy for runnin but tbf he did have a fun i mean gun"
        scene bar3
        "*you run trough the bar*"
        show zlink 1 with moveinbottom
        play sound cloth
        p1 "*sigh* that guy.."
        p1 "why did he let you go.."
        p1 "ughh.. what a drag"
        p1 "Look man, can we just not do this?"
        p1 "Just give up or something"
        p1 "There's nowhere for you to go anyway.."

        menu:
                "FIGHT":
                    jump fightzink
                    

                "PERSUADE":
                    k "hey man you know maybe you can just let me go man"
                    p1 "Cmon, we both know that i can't do that."
                    p1 "Now come along quietly. I mean it."
                    menu:
                            "FIGHT":
                                jump fightzink
                            "FLEE":
                                play sound cloth
                                hide zlink 1 with dissolve
                                "You push him aside and continue running. You hear yelling."
                                jump escape
        

        jump escape

    label fightzink:
        show bfists with moveinbottom
        $ renpy.pause(1.0, hard=True)
        play sound bloody
        hide bfists
        show bfists2
        show zlink 1 with hpunch
        
        hide bfists2
        show bfists


        $ renpy.pause(1.0, hard=True)
        hide bfists
        show bfists2
        show zlink 2 with vpunch
        
        hide bfists2
        show bfists

        $ renpy.pause(0.3, hard=True)
        hide bfists
        show bfists2
        show zlink 3 with vpunch
        
        hide bfists2
        show bfists

        $ renpy.pause(0.5, hard=True)
        hide bfists
        show bfists2
        show zlink 4 with vpunch
        
        hide bfists2
        show bfists

        $ renpy.pause(1.0, hard=True)
        hide bfists
        show bfists2
        show zlink 5 with vpunch
        
        hide bfists2
        show bfists

        $ renpy.pause(1.0, hard=True)
        hide bfists
        show bfists2
        show zlink 6 with vpunch
        
        hide bfists2
        show bfists

        $ renpy.pause(2.0, hard=True)
        play sound fall
        show zlink 7
        $ isZlinkDie = True
        "looks like that killed him"
        hide bfists with dissolve
        k "oh shit"
        "the officeer lies dead on the floor below you"
        p2 "HEY"
        k "I better get out of here now"
        "as you step over his lifeless body you start running to the backdoor"
        play sound door
        jump escape

######################################################################################################################################################
label _CASINO_ENTRY_HERE______________________________________________________________________________________________________________________________:
    ##################################################################################################################################################
    label escape:
        play sound door
        scene backdoor
        "you arrive at the backdoor"
        menu:
                "Open the door and GET THE FUCK OUUTA HERE BRO":
                    play sound door
        scene street1
        play sound run
        "you are running trough the street"
        "you see an alleyway so you turn to hide in there"
        scene alley1
        play sound run
        "you run trought the alley"
        scene alley2
        "there is a door here"
        menu:
                "Enter door":
                    play sound door
                    scene cas1
                    "it looks like you enter a casino"
                    play music casmusic fadein 1.5 volume 0.2
                    show bobis 1 with moveinbottom
                    play sound cloth
                    un "oh hey there fella"
                    un "i haven't seen you around here, you must be new herer"
                    bb "i am the floor manager"
                    show bobis 3
                    bb "Welcome to the casino!!"
                    bb "make sure you behave or ill have to"
                    play sound bad
                    show bobis 2 with vpunch
                    bb "KICK{nw=0.5}"
                    show bobis 3
                    extend " {nw=0.5}"
                    play sound bad
                    show bobis 2 at vpunch
                    extend "YOU{nw=0.5}"
                    show bobis 3
                    extend " {nw=0.5}"
                    play sound bad
                    show bobis 2 at vpunch
                    extend "OUT"
                    show bobis 3

                    bb "would you like to see the main *fun* area?"
                    menu:
                            "Yeah":
                                bb "oh"
                                "*he takes your hand and leads you to another room*"
                                play sound door
                                jump gocasino
                            "I wanna piss right now, where are the toilets at":
                                #$ shitcourt = 1
                                bb "Right this way sir"
                                play sound door
                                scene bath0
                                play music casmusic2 fadein 1.5 volume 0.2
                                $ renpy.pause(1.5, hard=True)
                                scene bath1
                                "You enter the bathroom"
                                menu:
                                        "Enter stall":
                                            play sound door
                                            scene bath2
                                            "You enter the bathroom stall"
                                            k "Okay let's get with it"
                                            "You start shitting"
                                            play sound dia1
                                            "It appears you have diarrhea"
                                            $ renpy.pause(2.0, hard=True)
                                            play sound bang1
                                            
                                            $ renpy.pause(1.3, hard=True)
                                            un "HEY"
                                            play sound dia2
                                            k "Hey man im shittin here im tryin ma best"
                                            

                                            play sound bang2

                                            un "I ATE A KEBAB"
                                            un "All the other stalls are BROKEN"

                                            menu:
                                                    "Shit":
                                                        jump shitting
                                                    "Shit harder":
                                                        jump shitting
                                            
                                            label shitting:
                                                play sound dia3
                                                $ renpy.pause(7.0, hard=True)
                                                play sound bang3

                                                un "HEY MAN i cant hold it anymore OPEN UP"
                                                menu:
                                                    "Keep shitting":
                                                        play sound dia4
                                                        $ renpy.pause(6.0, hard=True)

                                                        play sound bang4
                                                        un "plEASE OPEN TE DOOR"
                                                        menu:
                                                                "Continue shitting":
                                                                    play sound dia5
                                                                    $ renpy.pause(4.0, hard=True)
                                                                    show bath2 with vpunch
                                                                    play sound bang5

                                                                    un "OPENT HE FUCKING DOOR NOW"
                                                                    un "OR IM GONNA GET THE MANAGEMENT"
                                                                    menu:   
                                                                            "Open the door":
                                                                                "You decide to open the door"
                                                                                play sound door
                                                                                scene bathdoor
                                                                                $ renpy.pause(1.0, hard=True)
                                                                                jump bathdisc
                                                                            "Continue shitting":
                                                                                $ didyankdoor = 1
                                                                                play sound breakdoor
                                                                                scene bathfist
                                                                                $ renpy.pause(3.0, hard=True)
                                                                                scene bathnodoor
                                                                                play sound doorcrash
                                                                                "he yanks the door away"
                                                                                jump bathdisc





                                        "Go back":
                                            play sound door
                                            scene cas1
                                            "You levae the bathroom"
                                            play music casmusic fadein 1.5 volume 0.2
                                            show bobis 1 with moveinbottom
                                            bb "oh you already done?"
                                            bb "well, let us go"
                                            jump gocasino

    label bathdisc:
        $ isMatysiakAnger = True
        $ matysiakLocation = 1
        $ matPrevLocation = 1
        show mat 1 with dissolve
        un "you bastard"
        show mat 4
        un "I'm gonna beat the shit out of you"
        
        show mat 3
        un "do you know what you did"
        show mat 2
        un "I called the management"
        show mat 1
        un "They are gonna show up here soon"
        show mat 4
        un "you're fucked buddy"
        
        menu:
            "FIGHT":
                show bfists with moveinbottom
                $ renpy.pause(2.0, hard=True)

                if isZlinkDie:
                    play sound jumpscare1
                    scene black
                    $ renpy.pause(2.0, hard=True)
                    "it seemns that all the lights went oUT"
                    un "HEY???"
                    "you manage to quickly sneek out of the stall in the dark"
                    un "HEY GET BACK HEREE"
                    "the rooms start to smell lik some kind of drywalll"
                    "you are so fucked"
                    "you escape the toilets butt as naked"
                    jump casinodoorlock
                else:
                        
                        play sound bad
                        bb "HEY!"
                        hide mat 4 with dissolve
                        hide bfists with dissolve
                        play sound cloth
                        show bobis 1 with moveinleft
                        bb "You.."
                        play sound bad
                        show bobis 2 with vpunch
                        bb "MISBEHAVED"
                        "He drags you outside"
                        jump outsidecasino
        
    label gocasino:
        scene casmiddle
        bb "this here is where we we gamble"
        k " woah look at this place its like pretty cool here"
        k "pretty nicee"

    label casinoMAIN:
        scene casmiddle
        if casinoMajorHappens >= 2:
            $ renpy.pause(1.0, hard=True)
            show casmiddledark
            play sound jumpscare1
            $ renpy.pause(1.0, hard=True)
            "it seems the lights went out"
            k "oH NOooo shiiiitttt shit shittt"
            jump casinodoorlock

        menu:
                "Go right":
                    play sound door
                    jump casinoRIGHT
                "Go forward":
                    play sound door
                    jump casinoFORW
                "Go left":
                    play sound door
                    jump casinoLEFT
        
    label casinoRIGHT:
        scene casright

        play sound cloth
        show wiktorhobo 1 with moveinright
        un "heyyy there fella"
        wb "I'm just a gambler here"
        wb "And this is my brother:"
        play sound cloth
        show wiktor 1 with moveinleft
        
        w "yeah yeah hows it goin im a proffessional gambler"
        w "we wanted to ask you a favour"
        wb "got a couple bucks to spare?"
        menu:
            "Why":
                k "What you need it for fellas?"
                w "we just need a few dollars to get some beer"
                wb "no, no."
                wb "we are gonna multiply it and become rich"
                w "Like i said bro, this is why you are so fucking broke, you dont know when to quit."
                w "let's just get some beer, okay?"
                wb "ugh, fine"
                wb "wait, you never responded to the question, will you give us a few dollars?"
                menu:
                        "Yeah sure":
                            jump casinoRIGHT #___________________________________________________________________FINISHHHHHH
                        "Nah fuck off":
                            jump casinoRIGHT
            "Give a few bucks":
                k "here you go folks"
                "you hand out 20 PLN to the two brothers"
                wb "thank yuo so much bro!! much apprecciated!"
                play sound cloth
                hide wiktorhobo 1 with dissolve
                $ renpy.pause(0.2, hard=True)
                hide wiktor 1 with dissolve
                "both of them dissappear"
            "Nah fuck off":
                k "Nah i aint givin youshit u cn fukc off"
                hide wiktorhobo 1 with dissolve
                hide wiktor 1 with dissolve

                "idk what to put here simon lmao"
                ##smth about the getting mad and later the guys be pissed at u
        $ casinoMajorHappens = casinoMajorHappens + 1
        menu:
                "Go back":
                    play sound door
                    jump casinoMAIN
                "idk jerk around (it just calls wiktor rn)":
                    jump casinoRIGHT
                "go to the bar":
                    label barguy:
                        play music casmusic fadein 1.5 volume 0.2
                        scene casbar
                        if not hasbeenbar:
                        
                            "You come to da bahrs"
                            play sound appear
                            show bartwin default with moveinbottom
                            play sound bart1
                            un "heey heya!"
                            play sound bart2
                            un "can you guess who i am??"
                            show bartwin happy
                            play sound bart3
                            un "heh heh heh.."
                            play sound bart4
                            b2 "iiiiiiimmmm the bartender here :)"
                            show bartwin default
                            play sound bart5
                            b2 "MAN, i always wanted to say that"
                            play sound bart6
                            b2 "I got this position just recently, it's all thanks to my brother"
                            show bartwin happy
                            play sound bart7
                            b2 "he is such a supporting and awesome guy"
                            show bartwin default
                            play sound bart8
                            menu:
                                b2 "so, whats ur name?"
                                "karol mijas":
                                    k "my name"
                                    k "is uhj"
                                    k "karl beez"
                                    k "karl beez no i mean karol mijas"
                                    show bartwin default
                                    play sound bart9
                                    b2 "well nice to meet ya karol mijas!"
                                "don't anwser":
                                    show bartwin surpris
                                    play sound bart10
                                    b2 "{b}why didnt you answer"
                                    play sound bart11
                                    menu:
                                        b2 "it's a simple question"
                                        "it's karol mijas":
                                            k "the names karol mijas, kid"
                                        "continue to say nothing":
                                            show bartwin default
                                            play sound bart12
                                            b2 "well alright then, no biggie"
                            show bartwin default
                            play sound bart13
                            b2 "anyway, my brother is such a good fella"
                            play sound bart14
                            b2 "he's been there for me my whole life"
                            play sound bart15
                            b2 "i wouldnt be here without him"
                            play sound bart16
                            b2 "i only became a bartender because of him"
                            play sound bart17
                            b2 "he said to me: 'Im the bartender here, i beliebe in you brother'"
                            play sound bart18
                            b2 "if not for him.. i.. i dont know wheere i would be right now"
                            play sound bart19
                            b2 "anyway, my brother actally work s at a bar like a around the corsen"
                            play sound bart20
                            #b2 "maybe you've even met him? he is such a good guy im sure you forget him if you had met him!!"
                            menu:
                                b2 "maybe you've even met him? he is such a good guy im sure you forget him if you had met him!!"
                                "yes actually":
                                    k "yeah actually i had met him in the bar"
                                    b2 "oh reaally??/ thats so cool!"
                                    menu:
                                        "we had some drins":
                                            k "We had some dfrinkss.."
                                            k "No i mean I HAD some drinks, he didnt drunk"
                                            k "we had such a good time"
                                            jump allgoodbar
                                        "tell the truth":
                                            k "i killed him"
                                            show bartwin surpris
                                            b2 "thats.. ur.. ur joking right now.. arent you? i mean.. this. it has to be ajoke. if this is your idea of a joke its not funny.. its not funny at all.."

                                            menu:
                                                "horse":
                                                    k "he was a horse. i had to do it."

                                                    if isZlinkDie:
                                                        "suddenly his demeanor changes"
                                                        "he looks around and then crouches under the counter"
                                                        "you hear a bunch of rustling"
                                                        play sound bartev1
                                                        b2 "hey.. pal"
                                                        play sound bartev2
                                                        b2 "how about a drink?"
                                                        play sound bartev3
                                                        b2 "its on the house..."
                                                        menu:
                                                            b2 "its on the house..."
                                                            "no..":
                                                                b2 "hmpf.."
                                                                "he forces the drink inside u"
                                                            "take the drink":
                                                                "you take the drink and drink it"
                                                        "you wake up"
                                                        k "what.. the hell"
                                                        "you dont know what happened"
                                                        "the bartender doesnt seem to be anywhere"
                                                        menu:
                                                            "leave the bar":
                                                                jump casinoRIGHT

                                                    b2 "no.."
                                                    b2 "no, that's not funny."
                                                    k "i'm not joking."
                                                    b2 "..."
                                                    b2 "you’re sick."
                                
                                                    menu:
                                                        "Double down":
                                                            k "you don't understand. it wasn a person."
                                                            b2 "GET OUT."
                                                            k "heyy"
                                                            b2 "LEAVE ME BE"
                                                            jump casinoRIGHT

                                                        "Backtrack":
                                                            k "wait— i didn't mean—"
                                                            b2 "no. you said enough."
                                                            jump casinoRIGHT
                                "no, haven'tr": 
                                    k "Your brother huh? Doesn;t ring any bells. Didnt see anyone like that"
                                    play sound bart21
                                    b2 "it's a shame, he is such a good bartender, maybe evebn the best int he world."
                                    jump allgoodbar
                            label uhohbar:
                                k "as"
                            label allgoodbar:
                                show bartwin default
                                play sound bart22
                                b2 "OOoh! I've got a quesiton!! Do you have any siblings?"
                                menu:
                                    "No":
                                        k "No, but i have some cousins. A cousin was over at my house one time and i smashed her head against the glass This Glass is cracked because i slammed my cousins head into it at a family reunion //quote from iamnottkl dms (2023-06-03 15:49)"
                                    "Yeah":
                                        k "Yeah, i have a siblings"
                                        k "actually, that's a lie"
                                        show bartwin surpris
                                        play sound bart23
                                        with vpunch
                                        b2 "what?"
                                        k "But I have some cousin! A cousin was over at my house one time and i smashed her head against the glass This Glass is cracked because i slammed my cousins head into it at a family reunion //quote from iamnottkl dms (2023-06-03 15:49)"
                                play sound bart24
                                b2 "But htats so mean, why would you do that"
                                show bartwin default
                                b2 "riiighttt.. so.. this is a bar"
                                b2 "how couldi forgot"
                                b2 "you want something to drink?"
                                menu:
                                    b2 "you want something to drink?"
                                    "ya give it":
                                        "you order a drink"
                                    "nana":
                                        k "nah,, im good"
                                        b2 "oh well, thats a shame"
                                        menu:
                                            "leave the bar":
                                                jump allgoodbar
                                play sound win
                                show foundbeer
                                "you have now beer!!!! zywiec!!!"
                                hide foundbeer
                                play sound cloth
                                show hand beer with moveinbottom
                                k "oh yeaah"
                                show hand drink
                                play sound drink
                                k "oh yeaah"
                                stop music fadeout 0.5
                                play sound boom
                                scene casbarevil
                                show bartwin horse
                                #ooh what the fuckk
                                #changes into horse
                                k "you.."
                                k "MOTHERFUKCER!!"
                                show fists with moveinbottom
                                menu:
                                    "FIGHT":
                                        hide fists
                                        show bartwin horse with hpunch
                                        show fists2
                                        play sound bad
                                        $ renpy.pause(0.5, hard=True)
                                        hide fists2
                                        show fists

                                show fists
                                hide fists2
                                play sound hose1
                                menu:
                                    "FIGHT":
                                        hide fists
                                        show bartwin horse with hpunch
                                        show fists2
                                        play sound bad
                                        $ renpy.pause(0.5, hard=True)
                                        hide fists2
                                        show fists

                                show fists
                                hide fists2
                                play sound hose2
                                menu:
                                    "FIGHT":
                                        hide fists
                                        show bartwin horse with hpunch
                                        show fists2
                                        play sound bad
                                        $ renpy.pause(0.5, hard=True)
                                        hide fists2
                                        show fists

                                show fists
                                hide fists2
                                play sound hose1
                                menu:
                                    "FIGHT":
                                        hide fists
                                        show bartwin horse with hpunch
                                        show fists2
                                        play sound bad
                                        $ renpy.pause(0.5, hard=True)
                                        hide fists2
                                        show fists

                                show fists
                                hide fists2
                                play sound hose3
                        else:
                            if not barguybad:
                                b2 "oh did u change ur mind??"
    label casinoFORW:
        scene casforw
        if wrenchCasinoShingas == 0:
            $ renpy.pause(1.0, hard=True)
            play sound bad
            show casforw with vpunch
            un "HEY YOU"
            show wrencher 1 with moveinleft
            br "yes YOU faggot man"
            show wrencher 2
            br "i lost most of my MONEEY today and the last roulette is starting RIGHT NOW"
            show wrencher 3
            br "i need your help man i cant decide what to bet on"
            show wrencher 2
            br "whats it going to be huh, do i bet on RED... or BLACK"
            show wrencher 3
            br "choose wisely... all of the rest of my life savings depend on this"
            show wrencher 1
            menu:
                "RED":
                    k "maan i think you mayhaps should pick rED man"
                    br "really? alright give me a moment"
                    hide wrencher 1 with moveoutleft
                    $ renpy.pause(3.0, hard=True)

                    show wrencher 2 with moveinleft
                    br "i lost"
                    play sound bad
                    show wrencher 4 at vpunch
                    br "YOU DID THIS, ITS ALL YOUR FAULT"
                    br "I LOST EVERYTHING BECAUSE OF YOU"
                    br "WHY DID I EVEN LISTEN TO YOU?"
                    show wrencher 5
                    br "YOU WILL PAY FOR THIS."
                    hide wrencher 5 with moveoutleft
                    k "well that was weird"
                    $ wrenchCasinoShingas = 2
                    $ casinoLovesYou = casinoLovesYou - 1
                    $ casinoMajorHappens = casinoMajorHappens + 1
                "BLACK":
                    k "i dunno man maybe u shold BLACk it a little"
                    br "you better be right, ill be back soon"
                    hide wrencher 1 with moveoutleft
                    $ renpy.pause(2.0, hard=True)
                    
                    show wrencher 1 with moveinleft
                    br "I ACTUALLY WON!"
                    br "i cant believe this, thank you so much man i will remember this"
                    show wrencher 5
                    br "i am so unbelievably happy right now"
                    hide wrencher 5 with dissolve
                    "the man gives you a little kiss on your cheek and leaves the room extremly happy"
                    k "well this was pretty awesome"
                    $ wrenchCasinoShingas = 1
                    $ casinoLovesYou = casinoLovesYou + 1
                    $ casinoMajorHappens = casinoMajorHappens + 1
        
        menu:
            "go back to the wrench man":
                if wrenchCasinoShingas == 1:
                    "the man is obviously too happy to even acknowledge you"
                    jump casinoFORW
                else:
                    k "hey man hows it going"
                    show wrencher 5
                    br "GO FUCK YOURSELF"
                    hide wrencher 5
                    jump casinoFORW
            "Ckeck out that stand with a pretty sexy guy":
                jump sexyshapefittinggame
            
            "Go back":
                play sound door
                jump casinoMAIN


    screen shapeholesscreen:
        fixed:
            image "shapeholes.png"

    screen holesfit1:

        draggroup:
            drag:
                drag_name "square"
                xpos 475
                ypos 675
                child "placeholdergoop.png"
                draggable False
                droppable True
            drag:
                drag_name "rombus"
                xpos 705
                ypos 835
                child "placeholdergoop.png"
                draggable False
                droppable True
            drag:
                drag_name "circle"
                xpos 938
                ypos 673
                child "placeholdergoop.png"
                draggable False
                droppable True
            drag:
                drag_name "star"
                xpos 1165
                ypos 835
                child "placeholdergoop.png"
                draggable False
                droppable True
            drag:
                drag_name "triangle"
                xpos 1405
                ypos 673
                child "placeholdergoop.png"
                draggable False
                droppable True
            if sexyguyCasinoShingas == 0:
                drag:
                    drag_name "star"
                    xalign 0.5
                    yalign 0.5
                    child "shapestar2.png"
                    draggable True
                    droppable False
                    dragged drag_placed
            elif sexyguyCasinoShingas == 1:
                drag:
                    drag_name "rombus"
                    xalign 0.5
                    yalign 0.5
                    child "shaperombus1.png"
                    draggable True
                    droppable False
                    dragged drag_placed
            elif sexyguyCasinoShingas == 2:
                drag:
                    drag_name "circle"
                    xalign 0.5
                    yalign 0.5
                    child "shapeball1.png"
                    draggable True
                    droppable False
                    dragged drag_placed
            elif sexyguyCasinoShingas == 3:
                drag:
                    drag_name "triangle"
                    xalign 0.5
                    yalign 0.5
                    child "shapetriang1.png"
                    draggable True
                    droppable False
                    dragged drag_placed
            elif sexyguyCasinoShingas == 4:
                drag:
                    drag_name "rombus"
                    xalign 0.5
                    yalign 0.5
                    child "shaperombus2.png"
                    draggable True
                    droppable False
                    dragged drag_placed
            elif sexyguyCasinoShingas == 5:
                drag:
                    drag_name "square"
                    xalign 0.5
                    yalign 0.5
                    child "shapesquare1.png"
                    draggable True
                    droppable False
                    dragged drag_placed
            elif sexyguyCasinoShingas == 6:
                drag:
                    drag_name "star"
                    xalign 0.5
                    yalign 0.5
                    child "shapestar1.png"
                    draggable True
                    droppable False
                    dragged drag_placed
            elif sexyguyCasinoShingas == 7:
                drag:
                    drag_name "circle"
                    xalign 0.5
                    yalign 0.5
                    child "shapeball2.png"
                    draggable True
                    droppable False
                    dragged drag_placed
            else:
                drag:
                    drag_name "notashape"
                    xalign 0.5
                    yalign 0.5
                    child "gambelunused.png"
                    draggable True
                    droppable False
                    dragged drag_placed




    label sexyshapefittinggame:
        scene castableidk
        "THE DIALOG HERE IS PLACEHOLDER I THINK"
        if sexyguyCasinoShingas == 0:
            sx "Hello there, im the gamemaster"#dialog here is subject to change i think il see maybe mayhaps_____________________
            sx "Would you like to play my game?"
            menu:
                "play his game":
                    k "yeah sure why not"
                "not":
                    k "nah im not gonna"
                    sx "Thats a shame, come back if you change your mind!"
                    jump casinoFORW
            show screen shapeholesscreen
            "fill my holes"
            show wrencher 5

            call screen holesfit1
            if doShapesMatch:
                "GOOD"
            elif shapeDroppable == "square":
                "SQUARE HOLE"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 2
            else:
                "IDIOT"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 1

            $ sexyguyCasinoShingas = 1
            call screen holesfit1
            if doShapesMatch:
                "GOOD"
            elif shapeDroppable == "square":
                "SQUARE HOLE"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 2
            else:
                "IDIOT"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 1

            $ sexyguyCasinoShingas = 2
            call screen holesfit1
            if doShapesMatch:
                "GOOD"
            elif shapeDroppable == "square":
                "SQUARE HOLE"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 2
            else:
                "IDIOT"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 1

            $ sexyguyCasinoShingas = 3
            call screen holesfit1
            if doShapesMatch:
                "GOOD"
            elif shapeDroppable == "square":
                "SQUARE HOLE"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 2
            else:
                "IDIOT"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 1

            $ sexyguyCasinoShingas = 4
            call screen holesfit1
            if doShapesMatch:
                "GOOD"
            elif shapeDroppable == "square":
                "SQUARE HOLE"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 2
            else:
                "IDIOT"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 1

            $ sexyguyCasinoShingas = 5 #this one is an actual square
            call screen holesfit1
            if doShapesMatch:
                "GOOD"
            else:
                "IDIOT"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 1

            $ sexyguyCasinoShingas = 6
            call screen holesfit1
            if doShapesMatch:
                "GOOD"
            elif shapeDroppable == "square":
                "SQUARE HOLE"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 2
            else:
                "IDIOT"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 1

            $ sexyguyCasinoShingas = 7
            call screen holesfit1
            if doShapesMatch:
                "GOOD"
            elif shapeDroppable == "square":
                "SQUARE HOLE"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 2
            else:
                "IDIOT"
                $ sexyguyMadnessLevel = sexyguyMadnessLevel + 1
            
            $ casinoMajorHappens = casinoMajorHappens + 1

        hide screen shapeholesscreen
        jump casinoFORW

    label casinoLEFT: #this IS the fun one
        scene casleft
        #"this is the fun one"
        if pielaCasinoShingas == 0 or pielaCasinoShingas == 1:
            if pielaCasinoShingas == 0:
                $ renpy.pause(1.0, hard=True)
                show transpiela with moveinleft
                pl "Hey man"
                pl "You look like some  guy who knows computer stuff"
                pl "a friend of mine told me those gamblin  machines run on some algorithms"
                pl "Im looking for a hacker"
                $ casinoMajorHappens = casinoMajorHappens + 1
            else:
                show transpiela with moveinleft
                pl "Hey man"
                pl "im still looking for a hacker man"
            menu:
                "whyyy":
                    k "What th fuck do you wan t from me"
                    pl "I need som e hacker man to get into those serwers"
                    pl "And hack themm and get some moneey for us"
                    pl "and we get rich"
                    menu:
                        "horrible":
                            k "Nah i think you on your own with this man"
                            pl " hey no no"
                            pl "Come on man you can do this come on"
                            menu:
                                "agree":
                                    k "okay okay fiiineee ill do it"
                                    pl " thats so great i knew i could count on yo u"
                                    $ pielaCasinoShingas = 3
                                "Kindly disagree":
                                    k "no man fuck off already this is bullshit"
                                    pl "man youre a dick i hate you now now"
                                    hide transpiela with moveoutleft
                                    $ pielaCasinoShingas = 2
                        "Agree":
                            k "alright i will hack for you"
                            pl "this is aesome"
                            $ pielaCasinoShingas = 3
                "agree to help":
                    k "okey finee ill help you"
                    pl "Thank you man youre the best"
                    $ pielaCasinoShingas = 3
                "nah go away":
                    k "this is horrible go away"
                    pl "Hey no man u can do this please"
                    menu:
                        "agrre":
                            k "okay sure sure"
                            pl "this is great thank you man"
                        "disagreement":

                            $ pielaCasinoShingas = 2
                "Ignore him (more optios)":
                    $ pielaCasinoShingas = 1

        if pielaCasinoShingas == 3:
            pl "we should plan the heist now"
            "placeholder shit finish later" #______________________________________________________________________

        menu:
            "Go back":
                play sound door
                jump casinoMAIN
            "play the gamble":
                "gambel"
                play music "karolthemeEVIL.mp3" #remove or replace it later lol thers no evil in gambel
                camera:
                    perspective True
                    zpos 1500
                    gl_depth True 
                show gambel at size:
                    xalign 0.5 ypos -800
                show lever1:
                    xpos 200 zpos 1500
                play sound clank
                "lets go gambling"
                jump gambelplaying
            "play extrem":
                jump extremely


    label gambelplaying:
        scene gar
        hide gar
        camera:
            perspective True
            zpos 1500
            gl_depth True 
        show gambel at size:
            xalign 0.5 ypos -800
        hide lever1
        show lever2:
            xpos 200 ypos 200 zpos 1500
        play sound lever1
        $ slotstablebig = make_slots_table()

        python:
            if slotstablebig[6][0] == slotstablebig[6][1] and slotstablebig[6][0] == slotstablebig[6][2]:
                gamble1didwin = True
            else:
                gable1didwin = False

        show expression slotstable[slotstablebig[0][0]] as anel1:
            ypos 100 xpos -160 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[0][1]] as anel2:
            ypos 100 xpos 640 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[0][2]] as anel3:
            ypos 100 xpos 1440 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)


        show expression slotstable[slotstablebig[1][0]] as anel4:
            ypos 100 xpos -160 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[1][1]] as anel5:
            ypos 100 xpos 640 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[1][2]] as anel6:
            ypos 100 xpos 1440 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)


        show expression slotstable[slotstablebig[2][0]] as anel7:
            ypos 100 xpos -160 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[2][1]] as anel8:
            ypos 100 xpos 640 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[2][2]] as anel9:
            ypos 100 xpos 1440 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)


        show expression slotstable[slotstablebig[3][0]] as anel10:
            ypos 100 xpos -160 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[3][1]] as anel11:
            ypos 100 xpos 640 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[3][2]] as anel12:
            ypos 100 xpos 1440 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)


        show expression slotstable[slotstablebig[4][0]] as anel13:
            ypos 100 xpos -160 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[4][1]] as anel14:
            ypos 100 xpos 640 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[4][2]] as anel15:
            ypos 100 xpos 1440 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)


        show expression slotstable[slotstablebig[5][0]] as anel16:
            ypos 100 xpos -160 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[5][1]] as anel17:
            ypos 100 xpos 640 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[5][2]] as anel18:
            ypos 100 xpos 1440 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)

        hide lever2
        play sound lever2
        show lever1:
            xpos 200 zpos 1500

        show expression slotstable[slotstablebig[6][0]] as anel19:
            ypos 100 xpos -160 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear 0.5 matrixtransform RotateMatrix(-360, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[6][1]] as anel20:
            ypos 100 xpos 640 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear 0.5 matrixtransform RotateMatrix(-360, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[6][2]] as anel21:
            ypos 100 xpos 1440 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear 0.5 matrixtransform RotateMatrix(-360, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(0.3, hard=True)

        if gamble1didwin:
            play sound victory
            "YES u won uhhhh this thing"
        else:
            play sound disappointment
            "damn it u lost"
        menu:
            "keep gambling":
                call gambelplaying
            "quit":
                camera:
                    perspective False
                    gl_depth True
                    zpos 0
                play music casmusic fadein 1.5 volume 0.2
                jump casinoLEFT

    label extremely:
        play music cool1 fadein 2.0 volume 0.4
        scene arccool1
        menu:
            "START":
                play sound coin
                $ renpy.pause(1.0, hard=True)
                play sound cam
                play music cool volume 0.4
                scene arccool2
        menu:
            "FORWARD":
                play sound cam
                scene arccool3
                $ renpy.pause(1.0, hard=True)
        menu:
            "FORWARD":
                play sound cam
                scene arccool4
                $ renpy.pause(1.0, hard=True)
                show combine1 with dissolve
        menu:
            "FIGHT":
                show gun aim with moveinbottom
                $ renpy.pause(0.3, hard=True)
                play sound bad
                show gun shoot with vpunch
                $ renpy.pause(0.1, hard=True)
                show gun aim
                hide combine1 with dissolve
                play sound deadcomb
                $ renpy.pause(0.3, hard=True)
                hide gun aim with dissolve
        menu:
            "FORWARD":
                play sound cam
                scene arccool5
                $ renpy.pause(1.0, hard=True)
                show combine2 with dissolve
        menu:
            "FIGHT":
                show gun aim with moveinbottom
                $ renpy.pause(0.3, hard=True)
                play sound bad
                show gun shoot with vpunch
                $ renpy.pause(0.1, hard=True)
                show gun aim
                play sound deadcomb
                hide combine2 with dissolve
                $ renpy.pause(0.3, hard=True)
                hide gun aim with dissolve
        menu:
            "FORWARD":
                play sound cam
                scene arccool6
                $ renpy.pause(1.0, hard=True)
        menu:
            "INTERACT":
                play sound cam
                scene arccool7
                $ renpy.pause(1.3, hard=True)
                play sound door
                scene arccool8
        menu:
            "FORWARD":
                play sound cam
                scene arccool9
                $ renpy.pause(1.0, hard=True)
        menu:
            "FORWARD":
                play sound cam
                scene arccool10
                $ renpy.pause(1.0, hard=True)
                show combine1 with dissolve
        menu:
            "FIGHT":
                show gun aim with moveinbottom
                $ renpy.pause(0.3, hard=True)
                play sound bad
                show gun shoot with vpunch
                $ renpy.pause(0.1, hard=True)
                show gun aim
                play sound deadcomb
                hide combine1 with dissolve
                $ renpy.pause(0.3, hard=True)
                hide gun aim with dissolve
        menu:
            "FORWARD":
                play sound cam
                scene arccool11
                $ renpy.pause(1.0, hard=True)
                show combine1 with dissolve
        if not isZlinkDie:
            menu:
                "FIGHT":
                    show gun aim with moveinbottom
                    $ renpy.pause(0.3, hard=True)
                    play sound bad
                    show gun shoot with vpunch
                    $ renpy.pause(0.1, hard=True)
                    show gun aim
                    play sound deadcomb
                    hide combine1 with dissolve
                    $ renpy.pause(0.3, hard=True)
                    hide gun aim with dissolve
            menu:
                "FORWARD":
                    play sound cam
                    scene arccool12
                    $ renpy.pause(1.0, hard=True)
            menu:           
                "CROUCH DOWN":
                    play sound cam
                    scene arccool13
                    stop music
                    play sound win
                    $ renpy.pause(3.0, hard=True)
                    "yay u won and shit, get back now bastard"
                    play music casmusic fadein 1.5 volume 0.2
                    jump casinoLEFT
        else:
            menu:
                "FIGHT":
                    show gun aim with moveinbottom
                    $ renpy.pause(0.3, hard=True)
                    play sound bad
                    show gun shoot with vpunch
                    $ renpy.pause(0.1, hard=True)
                    show gun aim
            menu:
                "FIGHT":
                    show gun aim with moveinbottom
                    $ renpy.pause(0.3, hard=True)
                    play sound bad
                    show gun shoot with vpunch
                    $ renpy.pause(0.1, hard=True)
                    show gun aim
            menu:
                "FIGHT":
                    show gun aim with moveinbottom
                    $ renpy.pause(0.3, hard=True)
                    play sound bad
                    show gun shoot with vpunch
                    $ renpy.pause(0.1, hard=True)
                    show gun aim
            menu:
                "FIGHT":
                    show gun aim with moveinbottom
                    $ renpy.pause(0.3, hard=True)
                    play sound bad
                    show gun shoot with vpunch
                    $ renpy.pause(0.1, hard=True)
                    show gun aim
                    $ renpy.pause(0.1, hard=True)
                    play sound bad
                    show gun shoot with vpunch
                    $ renpy.pause(0.1, hard=True)
                    show gun aim
                    $ renpy.pause(0.1, hard=True)
                    play sound bad
                    show gun shoot with vpunch
                    $ renpy.pause(0.1, hard=True)
                    show gun aim
            menu:
                "FIGHT":
                    play sound jumpscare2
                    stop music
                    hide combine1
                    show combine1dry
                    $ renpy.pause(2.1, hard=True)
                    play sound jumpscare1
                    hide combine1dry
                    show combine1dry2
                    $ renpy.pause(5.1, hard=True)
                    scene casleftdark
                    "it seemns that all the lights went oUT"
                    k "oh noo shit shIT SHIt SHIT"
                    "the rooms start to smell lik some kind of drywalll"
                    "you may be fucked buddy"
                    jump casinodoorlock


    label casinodoorlock:
        scene cas1dark
        play sound run
        "u run to that pretty awesome DOOR u usedd to enter das casino"
        show casbackdoordark
        "you aproach te DOOR, but suddenly u feel some powerfull presence..."
        show locknik light with dissolve
        $ renpy.pause(1, hard=True)
        show locknik lock with dissolve
        "hello im ognik" #_________________________________________ognik<-----
        #show expression "images/ognikTest/locknik lock2.png"
        show locknik lock2
        "and u are gayy"
        show locknik light with dissolve
        $ renpy.pause(1, hard=True)
        hide locknik light with dissolve
        "well this is bAd"
        k "shiiiit whamt am i gonna do now??!?!"
        scene casleftdark
        play sound run
        "u rember some staff rooms u seen before so u run to search for them"
        scene casstaff2dark
        k "wooh look a there are some roooms here"
        scene casstaffscarymain
        "you find yourself in this somewhat safe room"
        k "i gues ill have to spend some hourrs in heere"
        k "huh theres some weird tablet but its baterydead"
        k "oh i have an iDEA"
        "u start searching deep in your asshole"
        "you have found:"
        play sound dia1
        show foundflashlight
        extend "\na long flashlight"
        play sound dia1
        show foundbutton
        extend "\na round button"
        play sound dia1cut
        show foundbuttp
        extend "\nand some metal buttplugs!{nw=2.5}"
        k "oh shit nah wrong thing, lemme put this back inside"
        hide foundbuttp
        play sound assholefist
        $ renpy.pause(1.0, hard=True)
        play sound dia1
        show foundbattery
        "and a small big batery!"
        k "YES i will COMBINE those items inorder to survive this NIGHT!"
        hide foundflashlight
        hide foundbutton
        hide foundbattery
        "you hear a man making some DRY steps back somewher there"
        if isMatysiakAnger:
            "and thers some kebab shaped farts in company with him!!!"
        else:
            "seems hes alone tho"
        "goodluck"

        label loop_entry: ##fnafff
            window hide
            show screen door_buttons
            show screen show_time
            $ flashBattery = 100
            $ starttime = renpy.get_game_runtime()
            $ lastCheckUpdate = renpy.get_game_runtime()
            label loop:
                $ renpy.pause(0.2)
                if (renpy.get_game_runtime() - starttime) > 360:
                    jump casinoescape
                if (drywallAttack < renpy.get_game_runtime()) and (drywallAttack + 2 > renpy.get_game_runtime()) and drywallLocation > 10: # and not debugMode:
                    jump casinodrywallgotyou
                if (matysiakAttack < renpy.get_game_runtime()) and (matysiakAttack + 2 > renpy.get_game_runtime()) and matysiakLocation > 10: # and not debugMode:
                    jump casinomatysiakgotyou
                jump loop

        #$ _skipping = False
        #$ renpy.pause(60.0, hard=True)
        
    label casinodrywallgotyou:
        hide screen door_buttons
        hide screen show_time
        hide screen cameraview
        hide screen flashleft
        hide screen flashtop
        hide screen flashright
        hide screen DEBUGmode
        "drywall got you lmao"
        "u getting dragged to hell"
        jump end

    label casinomatysiakgotyou:
        hide screen door_buttons
        hide screen show_time
        hide screen cameraview
        hide screen flashleft
        hide screen flashtop
        hide screen flashright
        hide screen DEBUGmode
        "matysiak got you lmao"
        "u getting used as a toilert"
        jump end

    label casinoescape:
        hide screen door_buttons
        hide screen show_time
        hide screen cameraview
        hide screen flashleft
        hide screen flashtop
        hide screen flashright
        hide screen DEBUGmode
        "what the hell"
        "you did this" #casino on fire there
        jump end

######################################################################################################################################################
label _CASINO_LEAVING_HERE____________________________________________________________________________________________________________________________:
    ##################################################################################################################################################
    label outsidecasino:
        stop music fadeout 0.5
        scene cas3
        play sound cloth
        show bobis 1 with moveinbottom
        bb "Stay out of our casino"
        bb "You're only bringing trouble"

        

        "you hear a familiar voice"
        p2 "well well well.."


        play sound cloth
        show dryleft with moveinleft
        hide bobis 1 with dissolve
        
        

        p2 "look who we have here"
        p2 "you got some nerve runnin away from me"

        show zlink 1 with moveinright
        play sound cloth
        p1 "ugghhh, why did you even let him escape in the first place"

        if isPathetic:
            p2 "well, he didn't even really fight me"
            p2 "just turned around and started flooring it"
        else:
            p2 "well i did point my gun at him"
            p2 "that scared him pretty hard"

        p2 "aaaand i didnt want to shoot him while he was running away"
        p2 "would be pretty mean, wouldn'nt it, karol mijas?"

        menu:
            "Yeah":
                k "so unbelievably mean that would've been man"
            "NO":
                k "honestly, you should've just shot me"
        p1 "so yeah we found your car and ID"
        p1 "so we know  who you are now and itsnot looking good for you at all, tbh"

        show bobis4 with moveinbottom
        play sound cloth
        bb "Sir, he was making trouble at our place"
        play sound impact1
        with vpunch
        bb "JAIL HIM!"
        play sound impact2
        with vpunch
        extend " PUNISH HIM!"

        p2 "is that so?"

        p2 "Either way, you're coming with me pal"
        p1 "dont't worry, he will be punished accordingly"
        
        bb "okaym ill levae you to  it"
        play sound cloth
        hide bobis4 with dissolve
        "the management guy disapepars and then uhh"
        "the police officers put you in their car"

        scene policecar
        "they put you in the car look this is the car!"
        extend "impossible!! its the car!!"

        p2 "haaang tight buddy, a court room has been already prepared for you"

        scene later
        play sound later
        "one enteri later"

        
        jump courtarrive
        

        

    label courtarrive:
        scene courthall1
        play sound foot
        "you go in court"
        if not shitcourt:
            jump courtregular
        else:
            jump courtPresidents

        
        

    label courtregular:
        play sound foot
        scene court
        play music ace2 fadein 1.0 volume 0.1
        "you get dragged into the court room"

        play sound cloth
        show judge 1 with dissolve
        un "hey hey"
        j "hello i am the judge"
        
        j "So.. Karol mijas. You have the right to legal reprsentation.."
        j "By the rules, an attorney will-  i mean was provided to you.."
        j "however..."
        j "he unfortunately was {color=#de1809}killed{/color} on the way here"
        j "i have however received his bag, so you may use it for your defense"

        play sound dia1
        show lawyerbag

        "you have received your (disceased) lawyers bag"

        hide lawyerbag
        play sound courthammer
        j "so... lets commence the trial"
        play music ace1 fadein 1.0 volume 0.3
        j "explain to me whats happened"
        play sound appear
        show dryleft with moveinleft
        p1 "alright so.. this guy right here punched a man in the bathroom"

        menu:
            "NO!! That's a lie!":
                k "I DID NOT!!!"
                $ judgepissedlevel += 1
                "The judges expression doesn't look good.."
                extend " he looks pretty pissed off"
                menu:
                    "Here's what happened":
                        k "I was taking a shit. okay?"
                        k "and this fucker, i dont know who he is, barges into my stall"
                        if didyankdoor:
                            k "fucker yanked my ENTIRE door away after punching a hole trought the metal"
                            k "some sick fuck i tell y ou"
            "Yeah":
                k "Yes, i punches that guy in the bathroom, for good reason too"
                j "good reason you say?"
                k "he invaded my personal space!"
                k "while i was.."
                play sound impact1
                with hpunch
                extend " {b}{color=#851911}taking a shit!!{/b}"

                j "..."


                p2 "..."

                k "its a horribl wy to invade someones privacy guys"
                k "its a MASSIVE VIOLATIO N OF YM PRIVACY"

        play sound hammer1
        j "Order! ORDER IN THE COURT!"
        j "Did he atleast knock?"

        menu:
            "He did":
                if didyankdoor:
                    k "He tore the fucking door{nw=0.0}"
                    play sound impact1
                    extends "{color=#6b5512} off of its hinges"
                else:
                    k "He was banging on my door furiously~!!"
        j "and what exactly were you doiing in the bathroom?"
        menu:
            "Taking a shit":
                k "Like i said,  i was taking ashit dipshit"
            "What do u fuckin think":
                $ judgepissedlevel += 2
                k "What do you fucking think i was doing?"
                k "are you retarded?"
                play sound hammer2
                j "FUCK YOU!"
                j "IM THE JUDHGE"
                j "imthe FUCKING judge YOU DONTT ALK TO ME THAT WAY!!"

        j "can someone fact check this?"
        p2 "your honour, i can confirm he was inddeed taking shit."
        j "how so?"
        p2 "after we transported him here he left a giant shit stain in the back of our patrol car"

        j "wery well.. we may continue"


        p2 "hold on wait "
        extend "i compltetly forgot"
        p2 "the guy {color=#de1809}murdered{/color} a bunch of people"

        j "are you serious?"
        j "then what were we discussing just now?"
        p2 "there was a mix up, there was never any fight"
        j "in that case the defendant stands accused of multiple murder charges and resisting arrest"
        j "is this true? or will u waste of my more time"
        
        p2 "yes your honour that is correct we have found concrete "    
        extend "concrete eveideince that is"
        p2 "im very sorry about not starting with this it must be the caffeine"    
        j "well lets hear that evidence you found"
        play sound appear
        show zlink right with moveinright
        p1 "alright so...."
        extend "\nwe first found a car.."
        extend "\nand the windshield was aaaallll bloody"
        menu:
            "Thas crazy":
                k "this so crazy"
                play sound hammer1
                j "will the defendant please shut the fuck up"
                $ judgepissedlevel += 1
                "seems youre really getting on his nerves"
                p2 "in any case.."
            "Say nothing":
                pass
        p1 "pretty scary stuff"
        p1 "but then.."
        extend "not too far on the ground we saw something disturbing.."
        p2 "it was a man.."
        extend "a pickle"
        extend ". A man."
        extend " A pickle shaped man."
        extend " Long gone.. No longer with us."
        p1 "we actually confiscated the car"
        hide dryleft with dissolve
        play sound metaldrag
        show carblood with moveinleft
        #$ renpy.pause(1, hard=True)
        "they drag the car inside"
        hide carbloodpick
        hide dryleft with dissolve
        show carbloodpick
        play sound cloth
        p1 "we also got the man"
        
        
    
        show dryleft with dissolve
        p2 "here it is, our concrete evidence of the first murder"

        menu:
            "Not my car":
                k "Whata re you talk about?"
                k "This isnt my car"
                p2 "Yes"
                extend " ,yes it is"
                p1 "Look at it! the car s yellow"
                p1 "and guess what"
                extend "YOU are also yellow"
            "Say nothing":
                pass
            "I thought it was a road bump!!":
                k "But i thought it was a road bump on the highway!"

        j "well, we're just going to have to ask to have ask the witness!"

        stop music fadeout 3.0

        j "mster pickle nan, could you please tell the court what happened?"

        play sound nin1
        "..."

        j "take your time."

        play sound nin2
        "..."

        p2 "you honor-"

        play sound hammer2
        j "NO INTERRUPTIONS"
        j "the witness is testifying"
        j "go right ahead, mr pickle"

        play sound nin3
        "..."

        j "mr pickle?"

        play sound nin4
        "..."

        p2 "hes dead."

        j "wery vell.."
        j "let it be known, the witness is not cooperating"

        "its not looking very good for you.."
        menu: 
            "Open the lawyers bag":
                play sound zip
                "you open the bag"
                
        play sound drumroll
        "inside... you find:"

        play sound dia1
        show foundtime
        "A mysterious device! Fascinating!!!"

        play sound dia1
        show foundnose
        "A nose and glasses thing! Dunno whats its called. "
        extend "I'm sorry for being such a unreliable narrator.. "
        extend "i really dont know whats it called. sorry :("

        play sound dia1
        show foundcontrol
        "A controller!!"

        menu:
            "Use the strange device":
                "huh"
            "Use the fake nose and glasses":
                "hm"
            "Use the controller":
                "you take the controller"
                hide foundnose
                hide foundtime
                k "let me skip this damn npcs cutscenee"
                play sound appear
                show hands control with moveinbottom
                menu:
                    "press button on controller":
                        "you click it"

    label courtPresidents:
        play music ace2 fadein 1.0 volume 0.05
        scene court
        "woa look its th ecourtuoom"
        play sound appear
        show judge 1
        un "heeey hello"
        j "hello i am the judge"
        play sound hammer2
        j "ORDER IN THE COURT NOW"
        j "So.. Karol mijas. YOu rea the defendast, and your laawayer thas been appointed to you is on the way."
        play sound appear
        hide judge 1
        show trump with dissolve
        t "hey hey, hello im here because im very interested in this case, very interested indeed"
        t "some people are saying this is the greatest court case of all time. I don't know if that's true, but a lot of very smart people are saying it."
        t "everyobodys asking 'Are you going to the court case' and i said 'maybe', and quite frankly ive never seen a courtroom like this with such trmendous energy before"
        hide trump
        play sound appear
        show judge 1 with dissolve
        j "hey ths is my courtroom im the judge"
        play sound appear
        hide judge 1
        show trump with dissolve
        t "uuhh, no, frankly speaking, i am the president here and uh you gotta listen to me, alright, is that clear?"
        t "hey barrack, get over here"
        play sound cloth
        show obama with moveinright
        ob "hello i am your president barac obmana"
        t "yeah"
        ob "yes trump, what is it trump?"
        t "what do you think of this.. highly interesting court case tremeendous, even, absoloutely tremendous"
        ob "well, i dont know trump, maybe we should let the court actually work things out and uuh see how this court case goes huh"
        t "alright, alright, but believe me, ive seen a lot of courtrooms, and this courtroom? its top tier, maybe even one of the best"

        hide trump
        play sound appear
        show judge 1 with dissolve
        play music ace1 fadein 5.0 volume 0.1
        j "ahem, the accused stands accused for..{nw=0.5}"
        play sound applause1
        extend " {color=#db190b}murder!!{/color}"
        play sound appear
        hide judge 1
        show trump with dissolve
        play sound impact2
        t "{color=#db190b}Murderrr???"
        t "murder you say.. people tell me all the time, murder is pretty bad, no really, i wonder how this 'Karol mijas' is going to deal with this  massive accusation.. quite a massive accusation this is"

        hide trump
        play sound appear
        show judge 1 with dissolve
        j "will the police officers provide us with neccesary information?"

        play sound appear
        show dryleft with moveinleft
        p2 "yes your honour"
        play sound appear
        hide judge 1
        show trump with dissolve
        t "hey sleepy joe, i think you should listen to this. i bet nobodys seen anything like it"
        play sound shleeping
        hide dryleft with dissolve
        show sleepy with dissolve
        
        "seems hes deep asleep"
        ob "maybe we should just let him sleep, donald"
        t "alright, alright, okay, dry looking guy, you may continue"

        play sound appear
        show dryleft with moveinleft
        p2 "so, in any case, we first got a call about a murder in a bar"

        play sound cloth
        show zlink right with moveinright
        p1 "when we arrived at the scene, we saw a dead bartender, dead on the ground"
        p2 "quite a gruesome sight."

        t "a dead bartender... sad. really sasd."
        extend "but ive seen a lot of things like this-maybe more than anybody, and, frankly its a verry cmplex situation."
        
        p2 "in the building, we encountered.. "
        play sound impact1
        with hpunch
        extend "the {color=#db190b}{b}DEFENDANT!{/b}"
        p1 "i encountered him further in the building, his fists, covered in blood"

        t "quite frankly im wondering, what the defendant would say to this.."

        menu:
            "I dont know":
                k "damn these are some WILD accusations guys"
            "Stay silent":
                $ staysilent += 1
                "you stay silent"
                "smart move, as your lawyer still isnt present"
                t "okay, okay, the silent treatment"
            "Victim was a horse":
                k "g"
        


    label end:
        scene black
        "It leaves you stunned"
        "End of PART 1, to be continued"
