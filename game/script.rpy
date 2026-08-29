    # hello welcome to the script of karolfemboymania where there are barely any femboys at the moment as i write this
# and no im not adding any rn
# dont worry im not gonna be adding any either

# atp im just adding pointless shit
init python:
    def muteTTS(event, **kwargs):
        if narraterTalking:
            renpy.alt("", force=True)
        return

    def narrTalks(event, **kwargs):
        if not narraterTalking:
            return
        renpy.sound.stop(channel="voiceact")
        if event == "show":
            what = kwargs.get("what")
            if what:
                renpy.alt(what, force=True)

    def pielTalks(event,  **kwargs):
        renpy.sound.stop(channel="voiceact")
        if narraterTalking:
            renpy.alt("", force=True)
        shit = 0
        while shit < 50:
            sound_dongus = renpy.random.randint(0,2)
            if event == "show":
                if sound_dongus == 0:
                    renpy.sound.queue("pielaTalks/pielaTalks 1.mp3", channel="sound", loop=False)
                elif sound_dongus == 1:
                    renpy.sound.queue("pielaTalks/pielaTalks 2.mp3", channel="sound", loop=False)
                else:
                    renpy.sound.queue("pielaTalks/pielaTalks 3.mp3", channel="sound", loop=False)
            elif event == "slow_done" or event == "end":
                renpy.sound.stop(channel="sound")
            shit += 1

    renpy.music.register_channel("karolChannel", mixer="karolChannel")
    renpy.music.register_channel("voiceact", mixer="voiceact",loop=False)

    def karolTalks(event, **kwargs):
        renpy.sound.stop(channel="voiceact")
        if narraterTalking:
            renpy.alt("", force=True)
        shit = 0
        while shit < 50:
            if karolTalkingShit and karolTalkingMad:
                sound_dongus = renpy.random.randint(0,4)
                if event == "show":
                    if sound_dongus == 0:
                        renpy.sound.queue("karolTalk/karoltalkMad 1.mp3", channel="karolChannel", loop=False)
                    elif sound_dongus == 1:
                        renpy.sound.queue("karolTalk/karoltalkMad 2.mp3", channel="karolChannel", loop=False)
                    elif sound_dongus == 2:
                        renpy.sound.queue("karolTalk/karoltalkMad 3.mp3", channel="karolChannel", loop=False)
                    elif sound_dongus == 3:
                        renpy.sound.queue("karolTalk/karoltalkMad 4.mp3", channel="karolChannel", loop=False)
                    elif sound_dongus == 4:
                        renpy.sound.queue("karolTalk/karoltalkMad 5.mp3", channel="karolChannel", loop=False)
                elif event == "slow_done" or event == "end":
                    renpy.sound.stop(channel="karolChannel")
            elif karolTalkingShit and not karolTalkingMad:
                sound_dongus = renpy.random.randint(0,4)
                if event == "show":
                    if sound_dongus == 0:
                        renpy.sound.queue("karolTalk/karoltalk 1.mp3", channel="karolChannel", loop=False)
                    elif sound_dongus == 1:
                        renpy.sound.queue("karolTalk/karoltalk 2.mp3", channel="karolChannel", loop=False)
                    elif sound_dongus == 2:
                        renpy.sound.queue("karolTalk/karoltalk 3.mp3", channel="karolChannel", loop=False)
                    elif sound_dongus == 3:
                        renpy.sound.queue("karolTalk/karoltalk 4.mp3", channel="karolChannel", loop=False)
                    elif sound_dongus == 4:
                        renpy.sound.queue("karolTalk/karoltalk 5.mp3", channel="karolChannel", loop=False)
                elif event == "slow_done" or event == "end":
                    renpy.sound.stop(channel="karolChannel")
            shit += 1

define config.main_menu_music = "karoltheme_poor.mp3"

define narrater = Character(" ", callback=narrTalks)
define k = Character("Karol Mijas", color="#ffe864", callback=karolTalks)
define un = Character("???", callback=muteTTS)
define crwd = Character("The crowd speakens.", callback=muteTTS)
define d = Character("papa Mijas", color="#706316", callback=muteTTS)
define do = Character("Domin", color="#a32d76", callback=muteTTS)
define b = Character("Bartender", color="#264972", callback=muteTTS)
define p1 = Character("Other Police Officer", color="#0c2644", callback=muteTTS)
define p2 = Character("Police Officer", color="#1366c5", callback=muteTTS)
define bb = Character("Floor manager", color="#d45130", callback=muteTTS)
define w = Character("Proffessional Gambler", color="#14531d", callback=muteTTS)
define wb = Character("Gambler", color="#091811", callback=muteTTS)
define br = Character("Broke robux", color="#9f3db3", callback=muteTTS)
define sx = Character("Sexy Gamemaster", color="#39b308", callback=muteTTS)
define pl = Character("Undersized delinquent", color="#842d68", callback=pielTalks)
define b2 = Character("Bartender 2", color="#120c63", callback=muteTTS)
define og = Character("Grand lock deity", color="#f2960c", callback=muteTTS)
define ch = Character("Casino chief", color="#384ce3", callback=muteTTS)
define j = Character("Judge", color="#186d45", callback=muteTTS)
define t = Character("Trump", color="#614e12", callback=muteTTS)
define ob = Character("Obama", color="#503528", callback=muteTTS)
define l = Character("Lawyer", color="#0b0955", callback=muteTTS)
define doc = Character("Docotr", color="#5550ea", callback=muteTTS)
define rep = Character("The pledge himself", color="#ffffff", callback=muteTTS)

default isPathetic = True
default isZlinkDie = False
default isMatysiakAnger = False

default femboyChoices = 0
default casinoLovesYou = 0

#simon bar thingiesss
default barguybadshinger = 0   #0 never met him, 1 is neutral?, 2 is like happy, 3 is you told the truth
default barguyloops = 0

#courts
default didyankdoor = 0
default staysilent = 0
default howmanytimes = 0
default timetime = 2.0
default timeraveltime = 0.0
default imlosingmyfuckingmind = 0.0
default particle_thing = timeGoopers()#particielThing()

default shitcourt = 0
default judgepissedlevel = 0

default talkingshit = 0

#bors
default wrenchCasinoShingas = 0         #0 = never met robux, 1 = you made robux win, 2 = you made robux lose
default pielaCasinoShingas = 0          #0 = never met piela, 1 = is being ignored, 2 = told to fuck off, 3 = agreed to help
default wiktorCasinoShingas = 0         #0 = never met wikts, 1 = you gave them cash, 2 = didnt
default sexyguyCasinoShingas = 0        #0 = never met sexy, 10 = you played bad or ok, 11 = you played well, 12 = mad
default sexyguyMadnessLevel = 0
default sexyguyWrongHoles = 0
default sexyguyCorrectas = 0
default sexyguySurprised = False
default sexyguyJumpMode = 0             #just for u simon *kiss*
default sexyguyJumpSpeed = 0.07

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

default camarasJustChanged = False
default cameraSelect = 5
default flashBright = False
default hoverTime = 0
default actionDoorLeft = 0
default actionDoorTop = 0
default actionDoorRight = 0
default flashBattery = 0
default drywallAttack = 0
default matysiakAttack = 0
default drywallPissOff = 0
default matysiakPissOff = 0

default debugMode = False
default karolTalkingShit = True
default karolTalkingMad = False
default narraterTalking = True

#gambel machine
define interval = 0.1 
define rolltime = 1
define rollwheelradius = 500
#define slotsnumber = 6 no clue
default gamble1didwin = False
default gambelrow = 0
default gambelState = 0 

init python: #PYTHON FUNCTIONS AND THINGIESS
    import random
    import math
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
        global shapeDraggable, shapeDroppable, doShapesMatch, sexyguyWrongHoles, sexyguyCorrectas
        if not drop:
            return
        shapeDraggable = drags[0].drag_name
        shapeDroppable = drop.drag_name
        doShapesMatch = (drags[0].drag_name == drop.drag_name)
        if doShapesMatch:
            sexyguyCorrectas += 1
        else:
            sexyguyWrongHoles += 1

        return True
    
    def randomasNumeras(wieViel):
        global randomAssShit
        randomAssShit = renpy.random.randint(1, wieViel)
        return

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
    
    class particielThing(renpy.Displayable):
        def __init__(self, **kwargs):
            self.particles = []
            for i in range(10):
                self.particles.append({
                    "angle": random.uniform(0.0, 2.0) * math.pi,
                    "markiplier": random.uniform(3, 5),
                    "imager": random.randint(0, 6),
                    "timeRepeat": random.uniform(0.0, 3.0)
                })
            super().__init__(**kwargs)
            self.images = [Transform(renpy.displayable(image),zoom=1.0 / 6.0)
            for image in slotstable]

        def render(self, width, height, st, at):
            canva = renpy.Render(width, height)
            for p in self.particles:
                xpos = p["markiplier"] * (st - p["timeRepeat"]) * 50 - 100
                if xpos > 1920:
                    p["timeRepeat"] = st #+ random.uniform(0.0, 3.0)
                    #p["markiplier"] = random.uniform(3, 5),
                    p["imager"] = random.randint(0, 6)
                    xpos = p["markiplier"] * (st - p["timeRepeat"]) * 50 - 100
                image = self.images[p["imager"]]
                child = renpy.render(image, 100, 100, st, at)
                canva.blit(child, ( xpos,100*p["imager"]))
            renpy.redraw(self, 0)
            return canva
    
    class timeGoopers(renpy.Displayable):
        def __init__(self, **kwargs):
            self.particles = []
            for i in range(10):
                self.particles.append({
                    "angle": random.uniform(0.0, 2.0) * math.pi,
                    "markiplier": random.uniform(3, 5),
                    "imager": random.randint(0, 6),
                    "timeRepeat": 0.0#random.uniform(0.0, 3.0)
                })
            super().__init__(**kwargs)
            self.images = [Transform(renpy.displayable(image),zoom=1.0 / 6.0)
            for image in slotstable]

        def render(self, width, height, st, at):
            canva = renpy.Render(width, height)
            for p in self.particles:
                radius = p["markiplier"] * (st - p["timeRepeat"]) * 50
                if radius > 1060:
                    p["timeRepeat"] = st
                    p["imager"] = random.randint(0, 6)
                    radius = p["markiplier"] * (st - p["timeRepeat"]) * 50
                image = self.images[p["imager"]]
                child = renpy.render(image, 100, 100, st, at)
                canva.blit(child, (910 + radius * math.cos(p["angle"] + (st * p["markiplier"] /2)),490 + radius * math.sin(p["angle"] + (st * p["markiplier"] /2))))
            renpy.redraw(self, 0)
            return canva
                

#i have no idea what it does but im not touching it:
#DONT TOUCH OR CASINO GAMBLING WILL BREAK
transform size:
    zoom 8

#######################################################################
#SCREEENSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
#######################################################################
screen gayyshit:
    add particle_thing

screen blackCover(value):
    zorder 1000
    if (timeraveltime + value <= renpy.get_game_runtime()):
        add Solid("#000000")

screen goondisplay:
    zorder 1001
    text "{size=*2}{color=#ff0000}[renpy.get_game_runtime()]" xalign 0.9 yalign 0.15
    text "{size=*2}{color=#ff0000}[timeraveltime + 14.8]" xalign 0.9 yalign 0.2

screen unskippableAD:
    #modal True
    key "dismiss" action NullAction()
    key "game_menu" action NullAction()
    key "rollback" action NullAction()

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
        idle "UI/buttoleft.png"
        hover "UI/buttolefthover.png"
        if flashBattery >= 0:
            hovered [Show("flashleft"), SetVariable("hoverTime", renpy.get_game_runtime() )]
        unhovered [Hide("flashleft"), SetVariable("hoverTime",0)]
        action [SetVariable("rolltime",1)] #this does nothing but DO NOT TOUCH

    imagebutton:
        xalign 0.8 yalign 0.5
        idle "UI/buttoright.png"
        hover "UI/buttorighthover.png"
        if flashBattery >= 0:
            hovered [Show("flashright"), SetVariable("hoverTime", renpy.get_game_runtime() )]
        unhovered [Hide("flashright"), SetVariable("hoverTime",0)]
        action [SetVariable("rolltime",1)] #this does nothing but DO NOT TOUCH

    imagebutton:
        xalign 0.5 yalign 0.1
        idle "UI/buttotop.png"
        hover "UI/buttotophover.png"
        if flashBattery >= 0:
            hovered [Show("flashtop"), SetVariable("hoverTime", renpy.get_game_runtime() )]
        unhovered [Hide("flashtop"), SetVariable("hoverTime",0)]
        action [SetVariable("rolltime",1)] #this does nothing but DO NOT TOUCH

    imagebutton:
        xalign 0.5 ypos 980
        idle "UI/buttodown.png"
        hover "UI/buttodownhover.png"
        if camarasJustChanged:
            hovered [SetVariable("rolltime",1)] #this does nothing but DO NOT TOUCH
        elif flashBattery >= 0:
            hovered [Hide("door_buttons"), Show("cameraview"), SetVariable("camarasJustChanged", True), Play("audio", "cameraopen.mp3")]
        #    action [Hide("door_buttons"), Show("cameraview")]
        else:
            hovered [Play("audio", "jimdead.mp3")]
        unhovered [SetVariable("camarasJustChanged", False)]
        action [SetVariable("rolltime",1)] #this does nothing but DO NOT TOUCH

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
                    image "battery/batterypainbright.png" zoom 1.5
                else:
                    image "battery/batterypainbright2.png" zoom 1.5
            else:
                if renpy.random.randint(0,1) == 0:
                    image "battery/batterymorepainbright.png" zoom 1.5
                else:
                    image "battery/batterymorepainbright2.png" zoom 1.5
        elif flashBattery < 0:
            image "battery/batterydead.png" zoom 1.5
        else:
            if flashBattery >= 67:
                if flashBright:
                    image "battery/batteryfatbright.png" zoom 1.5
                else:
                    image "battery/batteryjoyfull.png" zoom 1.5
            elif flashBattery <= 33:
                if flashBright:
                    image "battery/batteryalmostcrybright.png" zoom 1.5
                else:
                    image "battery/batterytired.png" zoom 1.5
            else:
                if flashBright:
                    image "battery/batteryworrybright.png" zoom 1.5
                else:
                    image "battery/batterypickle.png" zoom 1.5

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
    #if flashBright and (hoverTime + 2 < renpy.get_game_runtime()) and (actionDoorLeft == 0) and (drywallLocation == 11 or matysiakLocation == 11):
    #    if drywallLocation == 11:
    #        timer 0.001 action [SetVariable("actionDoorLeft", renpy.get_game_runtime()), SetVariable("drywallAttack",0), SetVariable("drywallLocation",renpy.random.randint(2, 5)), Play("audio", "hl2scream.mp3")]
    #    else:
    #        timer 0.001 action [SetVariable("actionDoorLeft", renpy.get_game_runtime()), SetVariable("matysiakAttack",0), SetVariable("matysiakLocation",renpy.random.randint(2, 5)), Play("audio", "hl2scream.mp3")]

    if flashBright:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.3)] repeat True
    else:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.03)] repeat True
    if flashBattery < 0:
        timer 0.001 action [Hide("flashleft"), SetVariable("hoverTime",0)]
    if flashBright and (drywallLocation == 11):
        if (actionDoorLeft == 0) and (drywallPissOff >= 100):
            timer 0.001 action [SetVariable("drywallAttack",0), SetVariable("drywallLocation",renpy.random.randint(2, 5)), SetVariable("drywallPissOff",0), SetVariable("actionDoorLeft", renpy.get_game_runtime()), Play("audio", "hl2scream.mp3")]
        else:
            timer 0.02 action [SetVariable("drywallPissOff", drywallPissOff + 1)] repeat True
    if flashBright and (matysiakLocation == 11):
        if (actionDoorLeft == 0) and (matysiakPissOff >= 100):
            timer 0.001 action [SetVariable("matysiakAttack",0), SetVariable("matysiakLocation",renpy.random.randint(2, 5)), SetVariable("matysiakPissOff",0), SetVariable("actionDoorLeft", renpy.get_game_runtime()), Play("audio", "hl2scream.mp3")]
        else:
            timer 0.02 action [SetVariable("matysiakPissOff", matysiakPissOff + 1)] repeat True

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
    if flashBright:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.3)] repeat True
    else:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.03)] repeat True
    if flashBattery < 0:
        timer 0.001 action [Hide("flashtop"), SetVariable("hoverTime",0)]
    if flashBright and (drywallLocation == 12):
        if (actionDoorTop == 0) and (drywallPissOff >= 100):
            timer 0.001 action [SetVariable("drywallAttack",0), SetVariable("drywallLocation",renpy.random.randint(2, 5)), SetVariable("drywallPissOff",0), SetVariable("actionDoorTop", renpy.get_game_runtime()), Play("audio", "hl2scream.mp3")]
        else:
            timer 0.02 action [SetVariable("drywallPissOff", drywallPissOff + 1)] repeat True
    if flashBright and (matysiakLocation == 12):
        if (actionDoorTop == 0) and (matysiakPissOff >= 100):
            timer 0.001 action [SetVariable("matysiakAttack",0), SetVariable("matysiakLocation",renpy.random.randint(2, 5)), SetVariable("matysiakPissOff",0), SetVariable("actionDoorTop", renpy.get_game_runtime()), Play("audio", "hl2scream.mp3")]
        else:
            timer 0.02 action [SetVariable("matysiakPissOff", matysiakPissOff + 1)] repeat True
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
    if flashBright:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.3)] repeat True
    else:
        timer 0.1 action [SetVariable("flashBattery", flashBattery - 0.03)] repeat True
    if flashBattery < 0:
        timer 0.001 action [Hide("flashright"), SetVariable("hoverTime",0)]
    if flashBright and (drywallLocation == 13):
        if (actionDoorRight == 0) and (drywallPissOff >= 100):
            timer 0.001 action [SetVariable("drywallAttack",0), SetVariable("drywallLocation",renpy.random.randint(2, 5)), SetVariable("drywallPissOff",0), SetVariable("actionDoorRight", renpy.get_game_runtime()), Play("audio", "hl2scream.mp3")]
        else:
            timer 0.02 action [SetVariable("drywallPissOff", drywallPissOff + 1)] repeat True
    if flashBright and (matysiakLocation == 13):
        if (actionDoorRight == 0) and (matysiakPissOff >= 100):
            timer 0.001 action [SetVariable("matysiakAttack",0), SetVariable("matysiakLocation",renpy.random.randint(2, 5)), SetVariable("matysiakPissOff",0), SetVariable("actionDoorRight", renpy.get_game_runtime()), Play("audio", "hl2scream.mp3")]
        else:
            timer 0.02 action [SetVariable("matysiakPissOff", matysiakPissOff + 1)] repeat True

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
                image "cam mat4"
    if cameraSelect == 8:
        fixed:
            image "cam cas8"
            if drywallLocation == 8:
                image "cam dry1"
            if matysiakLocation == 8:
                image "cam mat1" xalign 0.8
    if cameraSelect == 9:
        fixed:
            image "cam cas9"
            if drywallLocation == 9:
                image "cam dry1"
            if matysiakLocation == 9:
                image "cam mat7"
    if cameraSelect == 10:
        fixed:
            image "cam cas10"
            if drywallLocation == 10:
                image "cam dry1"
            if matysiakLocation == 10:
                image "cam mat7"

    fixed:
        image "cam overlay"
        image "cameralayout"

    imagebutton:
        xalign 0.5 ypos 980
        idle "UI/buttodown.png"
        hover "UI/buttodownhover.png"
        if camarasJustChanged:
            hovered [SetVariable("rolltime",1)] #this does nothing but DO NOT TOUCH
        else:
            hovered [Show("door_buttons"), Hide("cameraview"), SetVariable("camarasJustChanged", True), Play("audio", "cameraopen.mp3")]
        unhovered [SetVariable("camarasJustChanged", False)]
        action [SetVariable("rolltime",1)] #this does nothing but DO NOT TOUCH
    
    imagebutton:    #room1
        xpos 1480 ypos 463
        idle "UI/camerabutton.png"
        hover "UI/camerabuttonhover.png"
        action [SetVariable("cameraSelect",1)]
    imagebutton:    #room2
        xpos 1590 ypos 511
        idle "UI/camerabutton.png"
        hover "UI/camerabuttonhover.png"
        action [SetVariable("cameraSelect",2)]
    imagebutton:    #room3
        xpos 1405 ypos 543
        idle "UI/camerabutton.png"
        hover "UI/camerabuttonhover.png"
        action [SetVariable("cameraSelect",3)]
    imagebutton:    #room4
        xpos 1385 ypos 603
        idle "UI/camerabutton.png"
        hover "UI/camerabuttonhover.png"
        action [SetVariable("cameraSelect",4)]
    imagebutton:    #room5
        xpos 1528 ypos 605
        idle "UI/camerabutton.png"
        hover "UI/camerabuttonhover.png"
        action [SetVariable("cameraSelect",5)]
    imagebutton:    #room6
        xpos 1640 ypos 665
        idle "UI/camerabutton.png"
        hover "UI/camerabuttonhover.png"
        action [SetVariable("cameraSelect",6)]
    imagebutton:    #room7
        xpos 1400 ypos 805
        idle "UI/camerabutton.png"
        hover "UI/camerabuttonhover.png"
        action [SetVariable("cameraSelect",7)]
    imagebutton:    #room8
        xpos 1520 ypos 785
        idle "UI/camerabutton.png"
        hover "UI/camerabuttonhover.png"
        action [SetVariable("cameraSelect",8)]
    imagebutton:    #room9
        xpos 1440 ypos 900
        idle "UI/camerabutton.png"
        hover "UI/camerabuttonhover.png"
        action [SetVariable("cameraSelect",9)]
    imagebutton:    #room10
        xpos 1636 ypos 844
        idle "UI/camerabutton.png"
        hover "UI/camerabuttonhover.png"
        action [SetVariable("cameraSelect",10)]

    imagebutton:
        xpos 1520 ypos 521
        idle "UI/audiobutton.png"
        hover "UI/audiobuttonhover.png"
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
    text "{color=#ffffff}drypissoff [drywallPissOff]" xalign 0.1 yalign 0.35

    hbox:
        xalign 0.95
        yalign 0.9
        spacing 20
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("starttime",min(starttime + 10, renpy.get_game_runtime()))]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("starttime",starttime - 10)]

    grid 4 5:
        xalign 0.05
        yalign 0.5
        spacing 20
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("drywallLocation",1)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("drywallLocation",2)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("matysiakLocation",1)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("matysiakLocation",2)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("drywallLocation",3)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("drywallLocation",4)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("matysiakLocation",3)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("matysiakLocation",4)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("drywallLocation",5)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("drywallLocation",6)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("matysiakLocation",5)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("matysiakLocation",6)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("drywallLocation",7)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("drywallLocation",8)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("matysiakLocation",7)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("matysiakLocation",8)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("drywallLocation",9)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("drywallLocation",10)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("matysiakLocation",9)]
        imagebutton:
            idle "UI/camerabutton.png"
            hover "UI/camerabuttonhover.png"
            action [SetVariable("matysiakLocation",10)]

#sexy guy \/\/\/
screen holesfit1:
    draggroup:
        drag:
            drag_name "square"
            xpos 475
            ypos 675
            child "emptyfuckinggoop.png"
            draggable False
            droppable True
        drag:
            drag_name "rombus"
            xpos 705
            ypos 835
            child "emptyfuckinggoop.png"
            draggable False
            droppable True
        drag:
            drag_name "circle"
            xpos 938
            ypos 673
            child "emptyfuckinggoop.png"
            draggable False
            droppable True
        drag:
            drag_name "star"
            xpos 1165
            ypos 835
            child "emptyfuckinggoop.png"
            draggable False
            droppable True
        drag:
            drag_name "triangle"
            xpos 1405
            ypos 673
            child "emptyfuckinggoop.png"
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

# The game starts here.
######################################################################################################################################################
label _1ST_SECTION_ORIGINAL_GAME_HERE_________________________________________________________________________________________________________________:
    ##################################################################################################################################################
    label start:

        #jump lospital -simon i hate you for not deleting this
        play music karoltheme_poor fadein 2.0 volume 0.2
        scene black
        show bed with dissolve
        $ renpy.pause(1.0, hard=True)
        k "Ohh man I looove sitting here makking games in Godot and jerkind off"
        #show screen gayyshit
        play sound knock
        $ randomasNumeras(100)
        narrater "*knock knock*"

        if randomAssShit == 1:
            show transpiela:
                zoom 0.01
                yalign 0.5
                xalign 0.5
                ease 0.5 zoom 1.8
            play sound hl2scream
            $ renpy.pause(3.0, hard=True)
            hide transpiela
        play voiceact dad1
        un "Come out here, son."

        play sound door

        show livinroom

        show dad
        play voiceact dad2
        d "son."

        play voiceact dad3
        d "you have{nw=0.0}"
        show dad at vpunch
        play audio impact2
        extend "{b}{color=#e34236} 3 days to move out." ##simon u fucked this shit up it aint working unless u split the voice line --- nevermind i fixed it for you *kiss*

        play voiceact dad4
        d "we're tired of your nonsense"
        
        play voiceact dad5
        d "for your entire life, you've done nothing but make garrys mod maps and gooning on the bathroom floor (not comfy)"

        k "B-but dad.. "
        extend "My map got over 30 thousand downloads!"
        
        play voiceact dad6
        d "now start packing your things"
        hide dad with moveoutleft

        narrater ".."

        play sound door
        scene bed
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
        play voiceact dom1
        do "Hello karol."

        play voiceact dom2
        menu:
            do "How are you doinmg?"
            "I'm so good doing right now":
                k "I'm doing so good right now"
                play voiceact dom3
                do "That;s so giiid!!"
                k "wait no... im not good at all"
            "I want you domin.":
                k "Yeah domin i wANT you"
                $ femboyChoices = femboyChoices + 1
                play voiceact dom4
                do "Woah.."
        
        k "domin.. my ass is kind of homeless.. and femboyless"
        k "i need yuo domin"

        play voiceact dom5
        do "Okay!!!"

        play voiceact dom6
        do "Here's my adress: "

        play voiceact dom7
        do "Here's my adress: Gdańska 129, Łódź"

        play voiceact dom8
        menu:
            do "Come to me!"
            "Wow, that's not even that far away!!":
                k "Wow its so close to me Yes"
                play voiceact dom9
                do "Really?? THat is such good news!"
                k "this is so good! i will be right there!"
            "I'm not sure where that is":
                k "but bomin i dont know where that iss where is thatt"
                extend " where"
                play voiceact dom10
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
        k "im gonna use my key for my kar with a key ight now"
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
        narrater "*Karol Mijas knocks on the door*"
        
        play voiceact dom11
        do "Karol Mijas, is that you? Come in."

        show lv2
        play audio door

        show domin with moveinbottom

        play voiceact dom12
        do "Something reallly bad happened.."
        play voiceact dom13
        do "My toilet shattered.."
        play voiceact dom14
        menu:
            do "into a million pieces"

            "That is so horrible":
                k "oh domin this is so bad so horrible"
                play voiceact dom15
                do "Yeah.. I'm so unluckyu.."
                play voiceact dom16
                do "I will go have to fix it now"
            "I want you domin":
                k "you see domin, {b}I want you you..."
                play voiceact dom17
                do "But.. my toilet"
                play voiceact dom18
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
        play voiceact bar1
        un "Hello there."
        play voiceact bar2
        b "I'm the bartender here"
        play voiceact bar3
        b "Would you like something to drink, good sir?"

        menu:
            "Yes, PLEASE!":
                jump continued
            "No":
                play voiceact bar5
                b "Hey, think about it, I think you might want something to drink"

        menu:
            "Okay fine":
                jump continued
            "No":
                play voiceact bar6
                b "Come ooon, it will be fun"

        menu:
            "Okay":
                jump continued
            "No":
                play voiceact bar7
                b "Just do it. Order some drinks."

        menu:
            "Fine":
                jump continued
            "No":
                play voiceact bar8
                b "You can't leave"

        menu:
            "Yes":
                jump continued
            "No":
                play voiceact bar9
                b "Get something to drink man"

        menu:
            "Sure":
                jump continued
            "No":
                jump nuhuh

        label nuhuh:
            play voiceact bar10
            b "Nuh uh"

            menu:
                "Yeah":
                    jump continued
                "No":
                    play voiceact bar11
                    b "Can't do that"

            menu:
                "Yeah":
                    jump continued
                "No":
                    play voiceact bar12
                    b "Think about the taste"

            menu:
                "Yeah":
                    jump continued
                "No":
                    jump nuhuh

        label continued:
            play voiceact bar4
            b "Let me pour some of our finest wine in for you."

            narrater "Karol Mijas takes a big gulp"

            k "Why.. do i feel so weird??"

            $ renpy.pause(2, hard=True)

            play sound bad
            show horse1 with vpunch
            play music horseishere volume 0.5

            $ karolTalkingMad = True
            k "You {b}fucker!"
            k "Why the {b}long face?"
            $ karolTalkingMad = False

            show fists 1 with moveinbottom
            menu:
                "{b}FIGHT":
                    show horse1 with hpunch
                    show fists 2
                    play sound bad
                    $ renpy.pause(0.5, hard=True)
                    show fists 1
                    play sound hose1
            menu:
                "{b}FIGHT":
                    show horse1 with hpunch
                    show fists 2
                    play sound bad
                    $ renpy.pause(0.5, hard=True)
                    show fists 1
                    play sound hose2
            menu:
                "{b}FIGHT":
                    show horse1 with hpunch
                    show fists 2
                    play sound bad
                    $ renpy.pause(0.5, hard=True)
                    show fists 1
                    play sound hose3
            menu:
                "{b}FIGHT":
                    show horse1 with hpunch
                    show fists 2
                    play sound bad
                    $ renpy.pause(0.5, hard=True)
                    show fists 1
            $ renpy.pause(1.0, hard=True)

            narrater "The horse attacks"
            play sound hose2
            show fists 1 with vpunch

            $ renpy.pause(2.0, hard=True)

            jump drugged

######################################################################################################################################################
label _END_OFORIGINAL_PART_AND_NOW_ESCAPING_BAR_______________________________________________________________________________________________________:
    ##################################################################################################################################################
    label drugged:
        stop music fadeout 0.5

        scene black
        narrater "The horses {color=#e34236}attack{/color=#e34236} puts you to {b}sleep"

        narrater "Some time passes.."

        play music "karolthemeEVIL.mp3" volume 0.2 fadein 2.0

        scene barfloor1

        narrater "You suddenly come back to consciousness"

        scene barfloor2

        play voiceact bardeads

        narrater "You notice the bartender laying dead on the floor"


        k "huh thats pretty weird"

        k "why'd he collapse like that what happened to him"

        play sound police

        narrater "Suddenly police sirens scream"

        play sound glassbreak

        narrater "*glass breaking*"

        play voiceact "drywall/dry 1.mp3"
        p2 "Ugghh"

        play voiceact "zipps/zippy 1.mp3"
        p1 "The front door was open you idiot"

        play voiceact "drywall/dry 2.mp3"
        p2 "Shut uuup. Just let me do my thing man."

        play voiceact "drywall/dry 3.mp3"
        p2 "Now let's take a look at what happaned here."

        play sound foots
        narrater "*sounds of footsteps getting closer*"

        show dry with moveinright
        play sound cloth

        play voiceact "drywall/dry 4.mp3"
        p2 "hey hey there.. {color=#fcdb03}yellow guy?"

        play voiceact "drywall/dry 5.mp3"
        p2 "ehhhh, why'd you do this?"

        menu:
                "Yeah":
                    k "yeah"
                    play voiceact "drywall/dry 6.mp3"
                    p2 "uh huh"
                "I didn't do this!!":
                    $ karolTalkingMad = True
                    k "You gotta believe me!! I didn't do this!"
                    play voiceact "drywall/dry 7.mp3"
                    p2 "sure pally-o broskiti-o whatever you say"

                    play voiceact "drywall/dry 8.mp3"
                    p2 "lil bro's dead on the floor and yo fists are{nw=1.9}"
                    play audio impact2
                    show dry at vpunch
                    extend "{b} COVERED{/b} in {color=#de1809}blood"

                    play voiceact "drywall/dry 9.mp3"
                    p2 "Just look at you. What a sorry sight."
                    menu:
                            "It was not me man":
                                k "Beleive me pleasee it was not me"
                                $ karolTalkingMad = False
                                k "I wouldnt do this to anybody.."
                                play voiceact "drywall/dry 10.mp3"
                                p2 "yeah im like, pretty sure you did it"
                                k "actually.."
                                k "yeah.."
                                extend "i would do this sort of thing"
                                p2 "you got like a.. screw loose or something?"
                                p2 "anyway.."
                            "Okay fine i did this, me":
                                $ karolTalkingMad = False
                                k "Okay okay i did this, it was me, me!"
                                play voiceact "drywall/dry 13.mp3"
                                p2 "good, good.. a confession."

                                play voiceact "drywall/dry 14.mp3"
                                p2 "perfect, in fact"

                                play voiceact "drywall/dry 15.mp3"
                                p2 "unfortunately for you.."

        play voiceact "drywall/dry 16.mp3"
        p2 "im afraid imma have to take you in, you're coming wth me {b}brotisserie chicken"

        menu:
                "{b}FIGHT":
                    jump fight
                "FLEE":
                    jump flee


    label fight:
        show bfists 1 with moveinbottom
        $ karolTalkingMad = True
        k "I'm nOT GOING DOWN {b}WITHOUT A FIGHT"
        $ renpy.pause(0.2, hard=True)
        show bfists 2
        show dry with hpunch
        play audio bad
        show bfists 1
        play voiceact "drywall/dry OOH.mp3"
        p2 "OOH"
        play voiceact "drywall/dry 20.mp3"
        p2 "assault on a policer, lemme write that down, yup"
        menu:
                "{b}FIGHT":
                    k "Taste THIS you fucke!1"
                    $ renpy.pause(0.5, hard=True)
                    show bfists 2
                    show dry with hpunch
                    play audio bad
                    show bfists 1
                    play voiceact "drywall/dry AAGHH.mp3"
                    p2 "AAGHH"
                    play voiceact "drywall/dry 21.mp3"
                    p2 "stop resisting lil bro."
                    menu:
                            "{b}FIGHT":
                                k "take this AND tTHIS!!"
                                $ karolTalkingMad = False
                                $ renpy.pause(0.5, hard=True)
                                show bfists 2
                                show dry with hpunch
                                play sound bad
                                show bfists 1
                                $ renpy.pause(0.2, hard=True)
                                show bfists 2
                                show dry with hpunch
                                play audio bad
                                show bfists 1
                                play voiceact "drywall/dry UGHH.mp3"
                                p2 "UGHH"
                                play voiceact "drywall/dry 22.mp3"
                                p2 "THAT'S IT, ILL HANDLE IT MYSELF"
                                menu:
                                        "{b}FIGHT":
                                            $ renpy.pause(0.2, hard=True)
                                            hide bfists
                                            show dry2 with vpunch
                                            play audio gun
                                            play voiceact "drywall/dry 23.mp3"
                                            p2 "you are done"

                                            menu:
                                                    "FLEE":
                                                        $ isPathetic = False
                                                        jump flee
                                                    "FLEE":
                                                        $ isPathetic = False
                                                        jump flee
                                                    "{b}FUCKING RUN AWAY":
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
            narrater "*you turn around and start flooring it like a pussy*"
            narrater "your a fuckin pussy bro"
        else:
            narrater "you turn around and start flooring it"
            narrater "i'd say ur a pussy for runnin but tbf he did have a fun i mean gun"
        $ karolTalkingMad = False #theres some leak shit before that i got during playtest but i cant bother to look for it so just yeah
        scene bar3
        narrater "*you run trough the bar*"
        show zlink 1 with moveinbottom
        play audio cloth
        play voiceact ohhey
        p1 "Oh hey!"
        play voiceact "zipps/zippy 3.mp3"
        p1 "*sigh* that guy.."
        play voiceact "zipps/zippy 4.mp3"
        p1 "why did he let you go.."
        play voiceact "zipps/zippy 5.mp3"
        p1 "ughh.. what a drag"
        play voiceact "zipps/zippy 6.mp3"
        p1 "Look man, can we just not do this please?"
        play voiceact "zipps/zippy 7.mp3"
        p1 "Just like, give up or something i dunno"
        play voiceact "zipps/zippy 8.mp3"
        p1 "There's nowhere for you to go anyway.."

        menu:
                "{b}FIGHT":
                    jump fightzink
                    

                "PERSUADE":
                    k "hey man you know maybe you can just let me go man"
                    play voiceact "zipps/zippy 9.mp3"
                    p1 "Cmon, we both know that i can't do that."
                    play voiceact "zipps/zippy 10.mp3"
                    p1 "Now come along quietly. I mean it."
                    menu:
                            "{b}FIGHT":
                                jump fightzink
                            "FLEE":
                                play sound cloth
                                hide zlink 1 with dissolve
                                play voiceact "zipps/zippy yeller.mp3"
                                narrater "You push him aside and continue running. You hear yelling."
                                jump escape
        

        jump escape

    label fightzink:
        show bfists 1 with moveinbottom
        $ renpy.pause(1.0, hard=True)
        play sound bloody
        show bfists 2
        show zlink 1 with hpunch
        show bfists 1

        $ renpy.pause(1.0, hard=True)
        show bfists 2
        show zlink 2 with vpunch
        show bfists 1

        $ renpy.pause(0.3, hard=True)
        show bfists 2
        show zlink 3 with vpunch
        show bfists 1

        $ renpy.pause(0.5, hard=True)
        show bfists 2
        show zlink 4 with vpunch
        show bfists 1

        $ renpy.pause(1.0, hard=True)
        show bfists 2
        show zlink 5 with vpunch
        show bfists 1

        $ renpy.pause(1.0, hard=True)
        show bfists 2
        show zlink 6 with vpunch
        show bfists 1

        $ renpy.pause(2.0, hard=True)
        play sound fall
        show zlink 7
        $ isZlinkDie = True
        narrater "looks like that killed him"
        hide bfists with dissolve
        k "oh shit"
        narrater "the officeer lies dead on the floor below you"
        play voiceact "drywall/dry HEY.mp3"
        p2 "HEY"
        k "I better get out of here now"
        narrater "as you step over his lifeless body you start running to the backdoor"
        jump escape

######################################################################################################################################################
label _CASINO_ENTRY_HERE______________________________________________________________________________________________________________________________:
    ##################################################################################################################################################
    label escape:
        play sound door
        scene backdoor
        narrater "you arrive at the backdoor"
        menu:
            "Open the door and GET THE FUCK OUUTA HERE BRO":
                play sound door
        scene street1
        play sound run
        narrater "you are running trough the street"
        narrater "you see an alleyway so you turn to hide in there"
        scene alley1
        play sound run
        narrater "you run trought the alley"
        scene alley2
        narrater "there is a door here"
        menu:
                "Enter door":
                    play sound door
                    scene cas1
                    narrater "it looks like you enter a casino"
                    play music casmusic fadein 1.5 volume 0.2
                    show bobis 1 with moveinbottom
                    play sound cloth
                    $ renpy.pause(0.5, hard=True)
                    play voiceact "bopis/boris 1.mp3"
                    un "oh hey there fella"
                    play voiceact "bopis/boris 2.mp3"
                    un "i haven't seen you around here, you must be new herer"
                    play voiceact "bopis/boris 3.mp3"
                    bb "i am the floor manager"
                    show bobis 3
                    play voiceact "bopis/boris 4.mp3"
                    bb "Welcome to the casino!!"
                    play voiceact "bopis/boris 5.mp3"
                    bb "make sure you behave or ill have to"
                    play audio bad
                    play voiceact "bopis/boris KICK.mp3"
                    show bobis 2 with vpunch
                    bb "{b}KICK{nw=0.5}"
                    show bobis 3
                    extend " {nw=0.5}"
                    play audio bad
                    play voiceact "bopis/boris YOU.mp3"
                    show bobis 2 at vpunch
                    extend "{b}YOU{nw=0.5}"
                    show bobis 3
                    extend " {nw=0.5}"
                    play audio bad
                    play voiceact "bopis/boris OUT.mp3"
                    show bobis 2 at vpunch
                    extend "{b}OUT"
                    show bobis 3

                    play voiceact "bopis/boris 7.mp3"
                    bb "would you like to see the main *fun* area?"
                    menu:
                            "Yeah":
                                play voiceact "bopis/boris 8.mp3"
                                bb "oh"
                                narrater "*he takes your hand and leads you to another room*"
                                play sound door
                                jump gocasino
                            "I wanna piss right now, where are the toilets at":
                                $ shitcourt = 1
                                play sound "bopis/boris 10.mp3"
                                bb "Right this way sir"
                                play sound door
                                scene bath0
                                play music casmusic2 fadein 1.5 volume 0.2
                                $ renpy.pause(1.5, hard=True)
                                scene bath1
                                narrater "You enter the bathroom"
                                menu:
                                        "Enter stall":
                                            play sound door
                                            scene bath2
                                            narrater "You enter the bathroom stall"
                                            k "Okay let's get with it"
                                            narrater "You start shitting"
                                            play sound dia1
                                            narrater "It appears you have diarrhea"
                                            $ renpy.pause(2.0, hard=True)
                                            play sound bang1
                                            
                                            $ renpy.pause(1.3, hard=True)
                                            un "HEY"
                                            play sound dia2
                                            k "Hey man im shittin here im tryin ma best"
                                            

                                            play sound bang2
                                            $ renpy.pause(2)
                                            $ karolTalkingMad = True
                                            k "man IM SHITTING HERE LEAVE ME BEE"

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

                                                k "FUCK OFF"

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
                                                                        narrater "You decide to open the door"
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
                                                                        narrater "he yanks the door away"

                                                                        k "HEY WHAT THE FUCK mann"
                                                                        $ karolTalkingMad = False

                                                                        jump bathdisc
                                        "Go back":
                                            play sound door
                                            scene cas1
                                            narrater "You levae the bathroom"
                                            play music casmusic fadein 1.5 volume 0.2
                                            show bobis 1 with moveinbottom
                                            play voiceact "bopis/boris 11.mp3"
                                            bb "oh you already done?"
                                            play voiceact "bopis/boris 12.mp3"
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
            "{b}FIGHT":
                show bfists 1 with moveinbottom
                $ renpy.pause(2.0, hard=True)

                if isZlinkDie:
                    play sound jumpscare1
                    scene black
                    $ renpy.pause(2.0, hard=True)
                    narrater "it seemns that all the lights went oUT"
                    un "HEY???"
                    narrater "you manage to quickly sneek out of the stall in the dark"
                    un "HEY GET BACK HEREE"
                    narrater "the rooms start to smell lik some kind of drywalll"
                    narrater "you are so fucked"
                    narrater "you escape the toilets butt as naked"
                    jump casinodoorlock
                else:
                        
                        play audio bad
                        play voiceact "bopis/boris HEY.mp3"
                        bb "HEY!"
                        hide mat 4 with dissolve
                        hide bfists with dissolve
                        play sound cloth
                        show bobis 1 with moveinleft
                        play voiceact "bopis/boris you....mp3"
                        bb "You.."
                        play audio bad
                        play voiceact "bopis/boris MISBEHAVED.mp3"
                        show bobis 2 with vpunch
                        extend " {b}MISBEHAVED"
                        narrater "He drags you outside"
                        jump outsidecasino
        
    label gocasino:
        scene casmiddle

        play voiceact "bopis/boris 9.mp3"
        bb "this here is where we we gamble"
        k " woah look at this place its like pretty cool here"
        k "pretty nicee"

    label casinoMAIN:
        scene casmiddle
        if (casinoMajorHappens >= 3) and isZlinkDie:
            $ renpy.pause(1.0, hard=True)
            show casmiddledark
            stop music
            play sound jumpscare1
            $ renpy.pause(1.0, hard=True)
            narrater "it seems the lights went out"
            k "oH NOooo shiiiitttt shit shittt"
            jump casinodoorlock
        if (casinoMajorHappens >= 6) and not isZlinkDie:
            jump casinoCHIEFinMAIN
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
        if wiktorCasinoShingas == 0:
            play sound cloth
            show wiktorhobo 1 with moveinright
            $ casinoMajorHappens += 1
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
                                jump givingcashtofolks
                            "Nah fuck off":
                                jump pissofffolks
                "Give a few bucks":
                    label givingcashtofolks:
                        k "here you go folks"
                        narrater "you hand out 20 PLN to the two brothers"
                        wb "thank yuo so much bro!! much apprecciated!"
                        play sound cloth
                        hide wiktorhobo 1 with dissolve
                        $ renpy.pause(0.2, hard=True)
                        hide wiktor 1 with dissolve
                        narrater "both of them dissappear"
                        $ casinoLovesYou += 1
                        $ wiktorCasinoShingas = 1
                "Nah fuck off":
                    label pissofffolks:
                        k "Nah i aint givin youshit u cn fukc off"
                        play sound boowomp
                        show wiktor 2
                        show wiktorhobo 2
                        
                        w "what the fuck bro"

                        wb "man i hate you"
                        hide wiktorhobo 1 with dissolve
                        hide wiktor 1 with dissolve
                        $ casinoLovesYou -= 1
                        $ wiktorCasinoShingas = 2

                        narrater "they leave"
                        ##smth about the getting mad and later the guys be pissed at u

        menu:
                "Go back":
                    play sound door
                    jump casinoMAIN
                "go to fellas again":
                    narrater "actually u dont really want to see them again so nah"
                    jump casinoRIGHT
                "go to the bar":
                    label barguy:
                        play music casmusic fadein 1.5 volume 0.2
                        $ casinoMajorHappens += 1
                        scene casbar
                        if (barguybadshinger == 0):
                        
                            narrater "You come to da bahrs"
                            play sound appear
                            show bartwin default with moveinbottom
                            play voiceact bart1
                            un "heey heya!"
                            play voiceact bart2
                            un "can you guess who i am??"
                            show bartwin happy
                            play voiceact bart3
                            un "heh heh heh.."
                            play voiceact bart4
                            b2 "iiiiiiimmmm the bartender here :)"
                            show bartwin default
                            play voiceact bart5
                            b2 "MAN, i always wanted to say that"
                            play voiceact bart6
                            b2 "I got this position just recently, it's all thanks to my brother"
                            show bartwin happy
                            play voiceact bart7
                            b2 "he is such a supporting and awesome guy"
                            show bartwin default
                            play voiceact bart8
                            menu:
                                b2 "so, whats ur name?"
                                "karol mijas":
                                    k "my name"
                                    k "is uhj"
                                    k "karl beez"
                                    k "karl beez no i mean karol mijas"
                                    show bartwin default
                                    play voiceact bart9
                                    b2 "well nice to meet ya karol mijas!"
                                "don't anwser":
                                    show bartwin surpris
                                    play voiceact bart10
                                    b2 "{b}why didnt you answer"
                                    play voiceact bart11
                                    menu:
                                        b2 "it's a simple question"
                                        "it's karol mijas":
                                            k "the names karol mijas, kid"
                                        "continue to say nothing":
                                            show bartwin default
                                            play voiceact bart12
                                            b2 "well alright then, no biggie"
                            show bartwin default
                            play voiceact bart13
                            b2 "anyway, my brother is such a good fella"
                            play voiceact bart14
                            b2 "he's been there for me my whole life"
                            play voiceact bart15
                            b2 "i wouldnt be here without him"
                            play voiceact bart16
                            b2 "i only became a bartender because of him"
                            play voiceact bart17
                            b2 "he said to me: 'Im the bartender here, i beliebe in you brother'"
                            play voiceact bart18
                            b2 "if not for him.. i.. i dont know wheere i would be right now"
                            play voiceact bart19
                            b2 "anyway, my brother actally work s at a bar like a around the corsen"
                            play voiceact bart20
                            b2 "maybe you've even met him? he is such a good guy im sure you forget him if you had met him!!"
                            menu:
                                #b2 "maybe you've even met him? he is such a good guy im sure you forget him if you had met him!!"
                                "yes actually":
                                    k "yeah actually i had met him in the bar"
                                    b2 "oh reaally??/ thats so cool!"
                                    menu:
                                        "we had some drins":
                                            k "We had some dfrinkss.."
                                            k "No i mean I HAD some drinks, he didnt drunk"
                                            k "we had such a good time"
                                            "hey simon u were supposed to make barguy shit himself here" #SIMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON
                                            b2 "ooooh you had a good time huh???"
                                            b2 "that makes me so happy!!!!!!"
                                            play sound fart
                                            ##########ARE YOU FUCKIN SERIOUS HERE____________________________________________________________________________________________
                                            jump allgoodbar
                                        "tell the truth":
                                            k "i killed him"
                                            show bartwin surpris
                                            b2 "thats.. ur.. ur joking right now.. arent you? i mean.. this. it has to be ajoke. if this is your idea of a joke its not funny.. its not funny at all.."

                                            menu:
                                                "horse":
                                                    k "he was a horse. i had to do it."

                                                    if isZlinkDie:
                                                        narrater "suddenly his demeanor changes"
                                                        narrater "he looks around and then crouches under the counter"
                                                        narrater "you hear a bunch of rustling"
                                                        play voiceact bartev1
                                                        b2 "hey.. pal"
                                                        play voiceact bartev2
                                                        b2 "how about a drink?"
                                                        play voiceact bartev3
                                                        b2 "its on the house..."
                                                        menu:
                                                            b2 "its on the house..."
                                                            "no..":
                                                                b2 "hmpf.."
                                                                narrater "he forces the drink inside u"
                                                            "take the drink":
                                                                narrater "you take the drink and drink it"
                                                        narrater "you wake up"
                                                        k "what.. the hell"
                                                        narrater "you dont know what happened"
                                                        narrater "the bartender doesnt seem to be anywhere"
                                                        menu:
                                                            "leave the bar":
                                                                $ casinoLovesYou -= 1
                                                                $ barguybadshinger = 3
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
                                                            $ casinoLovesYou -= 1
                                                            $ barguybadshinger = 3
                                                            jump casinoRIGHT

                                                        "Backtrack":
                                                            k "wait— i didn't mean—"
                                                            b2 "no. you said enough."
                                                            $ casinoLovesYou -= 1
                                                            $ barguybadshinger = 3
                                                            jump casinoRIGHT
                                "no, haven'tr": 
                                    k "Your brother huh? Doesn;t ring any bells. Didnt see anyone like that"
                                    play voiceact bart21
                                    b2 "it's a shame, he is such a good bartender, maybe evebn the best int he world."
                                    jump allgoodbar
                            label allgoodbar:
                                show bartwin default
                                play voiceact bart22
                                b2 "OOoh! I've got a quesiton!! Do you have any siblings?"
                                menu:
                                    "No":
                                        k "No, but i have some cousins. A cousin was over at my house one time and i smashed her head against the glass This Glass is cracked because i slammed my cousins head into it at a family reunion //quote from iamnottkl dms (2023-06-03 15:49)"
                                    "Yeah":
                                        k "Yeah, i have a siblings"
                                        k "actually, that's a lie"
                                        show bartwin surpris
                                        play voiceact bart23
                                        with vpunch
                                        b2 "what?"
                                        k "But I have some cousin! A cousin was over at my house one time and i smashed her head against the glass This Glass is cracked because i slammed my cousins head into it at a family reunion //quote from iamnottkl dms (2023-06-03 15:49)"
                                play voiceact bart24
                                b2 "But htats so mean, why would you do that"
                                show bartwin default
                                b2 "riiighttt.. so.. this is a bar"
                                b2 "how couldi forgot"
                                b2 "you want something to drink?"
                                menu:
                                    b2 "you want something to drink?"
                                    "ya give it":
                                        narrater "you order a drink"
                                    "nana":
                                        k "nah,, im good"
                                        b2 "oh well, thats a shame"
                                        menu:
                                            "leave the bar":
                                                $ barguybadshinger = 1
                                                jump casinoRIGHT
                                label drink:
                                    play sound win
                                    show foundbeer
                                    narrater "you have now beer!!!! zywiec!!!"
                                    hide foundbeer
                                    play sound cloth
                                    show hand beer with moveinbottom
                                    $ karolTalkingMad = False
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
                                    $ karolTalkingMad = True
                                    k "MOTHERFUKCER!!"
                                    

                                    show fists 1 with moveinbottom
                                    menu:
                                        "{b}FIGHT":
                                            show fists 2 with hpunch
                                            play sound bad
                                            show bartwin horse1 with hpunch
                                            $ renpy.pause(0.5, hard=True)
                                            show fists 1
                                    k "you PIECE OF SHIT"
                                    show bartwin horse1 at vpunch
                                    play sound hose1
                                    menu:
                                        "{b}FIGHT":
                                            show fists 2 with hpunch
                                            play sound bad
                                            show bartwin horse2 with hpunch
                                            $ renpy.pause(0.5, hard=True)
                                            show fists 1
                                    k "I WILL KILL YOU JUST LIKE I KILLED YOUR BROTHER"
                                    show bartwin horse2 at vpunch
                                    play sound hose2
                                    menu:
                                        "{b}FIGHT":
                                            show fists 2 with hpunch
                                            play sound bad
                                            show bartwin horse3 with hpunch
                                            $ renpy.pause(0.5, hard=True)
                                            show fists 1
                                    show bartwin horse3 at vpunch
                                    play sound hose1
                                    menu:
                                        "{b}FIGHT":
                                            show fists 2 with hpunch
                                            play sound bad
                                            show bartwin horse4 with hpunch
                                            $ renpy.pause(0.5, hard=True)
                                            show fists 1
                                    show bartwin horse4 at vpunch
                                    play sound hose3
                                    $ karolTalkingMad = False
                                    k "YO BASTARD"
                                    $ renpy.pause(0.2, hard=True)
                                    scene black
                                    play sound pan
                                    narrater "somebody hits you on the head with a pan"
                                    
                                    narrater "it leaves you stunned"
                                    narrater " adn you lose consiousness"
                                    narrater "after some time you wake up"
                                    scene courthostage
                                    play voiceact bardead
                                    $ karolTalkingMad = False
                                    show bartwin died with dissolve
                                    k "what the hell"
                                    menu:
                                        "try to move":
                                            narrater "you trie to move but seems your're tied tot his chair"
                                    k "what"
                                    $ karolTalkingMad = True
                                    k "WHO DID THIS TO ME"
                                    $ karolTalkingMad = False
                                    play sound cloth
                                    show dryleft with moveinleft
                                    p2 "heh heh heh"
                                    p2 "we got you now you sick bastard"
                                    p2 "what's with you and bartenders?"
                                    play sound appear
                                    show chief 1 with moveinbottom
                                    un "what? whats going on?"
                                    un "i saw a commotion in the cameras what is going on in my casino man"
                                    p2 "i am  a police officer."
                                    p2 "we are chasing down a suspect who killed a bartender a block away"
                                    play sound cloth
                                    show zlink right2 with moveinright
                                    p1 "he KILLED ANOTHER ONE??"
                                    un "killed?"
                                    play sound cloth
                                    hide chief 1 with dissolve
                                    narrater "chief guy turns around and sees bar guy on th eground"
                                    play sound appear
                                    show chief 1 with moveinbottom
                                    un "WHAT??"
                                    ch "also btw i am the chief of this place"
                                    ch "HOW COULD YOU  KILL MY BARTENDER GUY!!!"
                                    p2 "dont worry, he isnt dead"
                                    p2 "i checked on him after i tied down this bastard, he should be finee"
                                    p1 "in any case we finally have the suspect in custody"
                                    menu:
                                        "defiance":
                                            k "i refuse to be treated this way"
                                            $ karolTalkingMad = True
                                            k "DO YOU HVAE THE SLIGHTEST CLUE WHO I AM?????"
                                            $ karolTalkingMad = False
                                            k "extremely cool story map"
                                            k "ever heard that name before?"
                                            $ karolTalkingMad = True
                                            k "HAVE YOU???"
                                            $ karolTalkingMad = False
                                            p2 "ehh"
                                            ch "shut up yellow cunt, officers please take him away from the premises"
                                            menu:
                                                "WAIT":
                                                    k "look, i didnt kill anyone ok?"
                                                    k "plus, the people i beat up weren't people, they were horses!"
                                        "acceptance":
                                            k "i've done wrong.. i admit"
                                            k "take me away"
                                    jump policecar
                                    "simon here goes karol beats barguy close to death thing hereee right hereee" #SIMOOOOOOOOOOOOOOOOOOOOOOOOOOOOON
                                    $ casinoLovesYou -= 1
                                    $ barguybadshinger = 3 #this is just so the playtest doesnt break u can change that
                                    jump casinoRIGHT
                        else:
                            if barguybadshinger == 1:
                                play sound appear
                                show bartwin default with dissolve
                                b2 "oh did u change ur mind??"
                                label mindchaning:
                                    b2 "i have some good drinks dinks gn8ks"
                                    if barguyloops == 1:
                                        menu:
                                            "yeah":#SIMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON
                                                k "give me some drink"
                                                jump drink
                                            "no":
                                                k "no i dont wantt"
                                                b2 "no think about it"
                                            "FLEE":
                                                jump casinoRIGHT
                                    b2 "i have some good drinks dinks gn8ks"
                                    menu:
                                        "yeah":#SIMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON
                                            k "give me some drink"
                                            jump drink
                                        "no":
                                            k "no i dont wantt"
                                            b2 "no think about it"

                                    menu:
                                        b2 "get some drink man is good for you"
                                        "no is bad":
                                            k "i am very healthy man i dont drink"
                                            $ karolTalkingMad = True
                                            extend " IS NOT GOOD FOR ME"
                                            $ barguyloops = 1
                                            jump mindchaning
                                        "okay fine":
                                            k "oooooh fiiine i guess i could have something to dribnnk"
                                            jump drink


    label casinoFORW:
        scene casforw
        if wrenchCasinoShingas == 0:
            $ renpy.pause(1.0, hard=True)
            $ casinoMajorHappens += 1
            play audio bad
            show casforw with vpunch
            play voiceact "wrench/wrench 1.mp3"
            un "HEY YOU"

            show wrencher 1 with moveinleft
            play voiceact "wrench/wrench 2.mp3"
            br "yes YOU {color=#fcdb03}faggot man"

            show wrencher 2
            play voiceact "wrench/wrench 3.mp3"
            br "i lost most of my MONEEY today and the last roulette is starting RIGHT NOW"
            
            show wrencher 3
            play voiceact "wrench/wrench 4.mp3"
            br "i need your help man i cant decide what to bet on"

            show wrencher 2
            play voiceact "wrench/wrench 5.mp3"
            br "whats it going to be huh, do i bet on {b}{color=#e34236}RED{/b}{/color=#e34236}... or {b}BLACK"
            
            show wrencher 3
            play voiceact "wrench/wrench 6.mp3"
            br "choose wisely... all of the rest of my life savings depend on this"
            show wrencher 1
            $ randomasNumeras(38)
            menu:
                "RED":
                    k "maan i think you mayhaps should pick {color=#e34236}rED{/color=#e34236} man"
                    play voiceact "wrench/wrench 7.mp3"
                    br "really? alright give me a moment"
                    hide wrencher 1 with moveoutleft
                    $ renpy.pause(3.0, hard=True)
                    if (randomAssShit <= 18):
                        jump wrenchWON
                    else:
                        jump wrenchLOST
                "{color=#e34236}BLACK":
                    k "i dunno man maybe u shold BLACk it a little"
                    play voiceact "wrench/wrench 8.mp3"
                    br "you better be right, ill be back soon"
                    hide wrencher 1 with moveoutleft
                    $ renpy.pause(2.0, hard=True)
                    if (randomAssShit >= 19 and randomAssShit <= 36):
                        jump wrenchWON
                    else:
                        jump wrenchLOST
                "{color=#39b308}BREEN":
                    $ wrenchCasinoShingas = 99
                    k "bet on reen"
                    play audio bad
                    show wrencher 3 with vpunch
                    play voiceact "wrench/wrench 9.mp3"
                    br "whatt?? are youy serious?? thats so riskyiy!"
                    k "my nutsuck leaned a little bit to right so that has to be right"
                    show wrencher 1
                    play voiceact "wrench/wrench 10.mp3"
                    br "well, if you say so..."
                    play voiceact "wrench/wrench 11.mp3"
                    br "you have to be right faggotman, ill be right back!"
                    hide wrencher with moveoutleft
                    $ renpy.pause(2.0, hard=True)
                    if (randomAssShit >= 37):
                        jump wrenchWON
                    else:
                        jump wrenchLOST
                    
            label wrenchLOST:
                show wrencher 2 with moveinleft
                play voiceact "wrench/wrench 12.mp3"
                br "i lost"
                play audio bad
                show wrencher 4 at vpunch
                play voiceact "wrench/wrench 13.mp3"
                br "YOU DID THIS, ITS ALL YOUR FAULT"
                if wrenchCasinoShingas == 99:
                    play voiceact "wrench/wrench 14.mp3"
                    br "YOU AND YOUR FUCKING BALLSACK"
                    play voiceact "wrench/wrench 15.mp3"
                    br "WHY DIDD I BELIEVE YOU ITS GONNA BE GREEN??"
                else:
                    play voiceact "wrench/wrench 16.mp3"
                    br "I LOST {b}EVERYTHING{/b} BECAUSE OF YOU"
                    play voiceact "wrench/wrench 17.mp3"
                    br "WHY DID I EVEN LISTEN TO YOU?"
                show wrencher 5
                play voiceact "wrench/wrench 18.mp3"
                br "YOU WILL {color=#e34236}PAY{/color=#e34236} FOR THIS."
                hide wrencher 5 with moveoutleft
                k "well that was weird"
                $ wrenchCasinoShingas = 2
                $ casinoLovesYou -= 1
                jump casinoFORW
            
            label wrenchWON:
                show wrencher 1 with moveinleft
                play voiceact "wrench/wrench 19.mp3"
                br "I ACTUALLY WON!"
                if wrenchCasinoShingas == 99:
                    play voiceact "wrench/wrench 20.mp3"
                    br "MAN your ballsack was actually right! It went green!"
                    play voiceact "wrench/wrench 21.mp3"
                    br "im so fucking rich right now"
                    play voiceact "wrench/wrench 22.mp3"
                    br "i have soo much money i dont even know what to do with it now"
                    k "you could give me some?"
                    show wrencher 5
                    $ renpy.pause(1.0, hard=True)
                    play voiceact "wrench/wrench no.mp3"
                    br "no"
                    play voiceact "wrench/wrench 23.mp3"
                    br "best i can do is this"
                else:
                    play voiceact "wrench/wrench 24.mp3"
                    br "i cant believe this, thank you so much man i will remember this"
                    show wrencher 5
                    play voiceact "wrench/wrench 25.mp3"
                    br "i am so unbelievably happy right now"
                hide wrencher 5 with dissolve
                play voiceact "wrench/wrench kiss.mp3"
                narrater "the man gives you a little kiss on your cheek and leaves the room extremly happy"
                k "well this was pretty{nw=0}"
                $ karolTalkingMad = True
                extend " AWESOME" 
                $ karolTalkingMad = False
                $ wrenchCasinoShingas = 1
                $ casinoLovesYou += 1
                jump casinoFORW    
        
        menu:
            "go back to the wrench man":
                if wrenchCasinoShingas == 1:
                    narrater "the man is obviously too happy to even acknowledge you"
                    jump casinoFORW
                else:
                    k "hey man hows it going"
                    show wrencher 5
                    play voiceact "wrench/wrench gofuckyourself.mp3"
                    br "GO FUCK YOURSELF"
                    hide wrencher 5
                    jump casinoFORW
            "Ckeck out that stand with a pretty sexy guy":
                jump sexyshapefittinggame
            
            "Go back":
                play sound door
                jump casinoMAIN


    label sexyshapefittinggame:
        scene castableidk
        show shapeholes
        if sexyguyCasinoShingas == 0:
            play sound foot
            $ renpy.pause(1.0, hard=True)
            play sound cloth
            show sexyguy 6 with moveinright
            $ casinoMajorHappens += 1
            sx "Hello there, im the gamemaster"#dialog here is subject to change i think il see maybe mayhaps
            sx "Would you like to play my game?"
            menu:
                "play his game":
                    k "yeah sure why not"
                "not":
                    k "nah im not gonna"
                    sx "Thats a shame, come back if you change your mind!"
                    hide sexyguy 6
                    hide shapeholes
                    jump casinoFORW
            sx "Great! Lets begin"
            hide sexyguy 6 with moveoutright
            $ renpy.pause(0.6, hard=True)
            show sexyguy 2 with dissolve
            sx "Im gonna explain the rules to you now"
            sx "Its pretty simple"
            show sexyguy 1
            sx "Im gonna give you some precious BLOCKS, one by one"
            sx "And YOU have to fit them to their respecting shaped hole"
            k "yeah okay"
            sx "Great, now I am gonna give you the first piece..."
            jump sexyshapegamewhole
        elif sexyguyCasinoShingas == 12:
            stop music
            $ renpy.pause(1.0, hard=True)
            narrater "the stand is empty"
            narrater "its all your fault"
            play music casmusic fadein 1.5 volume 0.2
            jump casinoFORW
        else:
            $ renpy.pause(1.0, hard=True)
            narrater "the stand is empty"
            jump casinoFORW
    
    label sexyguyanswersGOOD:
        if (sexyguyMadnessLevel >= 5) and not (shapeDroppable == "square") and not sexyguySurprised:
            show sexyguy 2
            sx "Wait, you're actually listening to me? I honestly did not expect this"
            $ sexyguySurprised == True
        elif (sexyguyCorrectas == 1) or (sexyguyCorrectas == 4):
            show sexyguy 1
            sx "Wow! Correct!"
            show sexyguy 2
        elif sexyguyCorrectas == 2:
            show sexyguy 1
            sx "Nice! Great job!"
        elif sexyguyCorrectas == 3:
            show sexyguy 2
            sx "Good!"
        elif sexyguyCorrectas == 5:
            show sexyguy 1
            sx "Yes! You're pretty good at this!"
        elif sexyguyCorrectas == 6:
            show sexyguy 1
            sx "Congrats buddy! Keep doing what you do best!"
        elif sexyguyCorrectas == 7:
            show sexyguy 1
            sx "Oh my god, you are so good at this u make me wanna..."
            sx "Jump around naked! YES!"
            call sexyguyJUMPING
            show sexyguy 1 with dissolve
            sx "Oh its so good, I love this"
        elif sexyguyCorrectas == 8:
            show sexyguy 2
            sx "No... no way..."
            sx "You've put ALL OF THEM? In CORRECT SLOTS?!!"
            show sexyguy 3
            sx "ITS INSANE!!! YOU ARE SO TALENTED..."
            show sexyguy 1
            sx "No... I have to..."
            sx "JUMP! JUMP AGAIN!!! I HAVE TO!!!"
            call sexyguyJUMPING
            show sexyguy 1 with dissolve
            sx "I WANT TO JUMP AGAIN"
            $ sexyguyJumpMode = 1
            $ sexyguyJumpSpeed = 0.05
            call sexyguyJUMPING
            show sexyguy 1 with dissolve
            sx "Okay okay... Im done..."
            sx "You gave me such a good time"
        else:
            show sexyguy 3
            sx "i have NO ideA what to say rn but u were right thoo"
        return

    
    label sexyguyanswers:
        if (sexyguyMadnessLevel == 3) and (shapeDroppable == "square"):
            show sexyguy 2
            sx "Hey man, i dont think these pieces should go into a square hole"
            sx "You should consider trying other options"
        elif (sexyguyMadnessLevel == 4) and (shapeDroppable == "square"):
            show sexyguy 2
            sx "Dude, these are not square pieces!"
        elif ((sexyguyMadnessLevel == 5) or (sexyguyMadnessLevel == 6)) and (shapeDroppable == "square"):
            play sound bad
            show sexyguy 3 with vpunch
            sx "QUIT IT! STOP PUTTING EVERYTHING INTO A SQUARE HOLE!"
            sx "Im starting to regret I even offered you this game in the first place!"
        elif (sexyguyMadnessLevel == 7) and (shapeDroppable == "square"):
            play sound bad
            show sexyguy 3 with vpunch
            sx "STOP DOING THAT! UGHHHHH"
            sx "You're making me SO mad, I wanna JUMP NAKED!"
            call sexyguyJUMPING
            show sexyguy 3 with dissolve
            sx "Dang it!"
        elif (sexyguyMadnessLevel == 8) and (shapeDroppable == "square"):
            play sound bad
            show sexyguy 3 with vpunch
            sx "AGHHH!"
            sx "WHY DO YOU TORMENT ME?!?!"
            sx "IM SO PISSED AT YOU! I NEED TO GO JUMP AGAIN!"
            call sexyguyJUMPING
            show sexyguy 3 with dissolve
            $ sexyguyJumpMode = 1
            $ sexyguyJumpSpeed = 0.05
            sx "{color=#e34236}I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU, I HATE YOU!!!"
            call sexyguyJUMPING
            show sexyguy 3 with dissolve
            sx "{color=#e34236}YOU RUINED EVERYTHING"
            $ sexyguyJumpSpeed = 0.03
            call sexyguyJUMPING
            show sexyguy 3 with dissolve
            sx "{color=#e34236}I WON'T LET THAT SLIDE, {b}YOU WILL REMEMBER THIS!!!"
        elif sexyguyCasinoShingas == 7:
            show sexyguy 2
            sx "Aaaaand that was the last one..."
            extend " and its wrong"
        elif (sexyguyWrongHoles == 1) or (sexyguyWrongHoles == 4):
            show sexyguy 2
            sx "Thats a wrong one buddy!"
            show sexyguy 1
            sx "Try again with this new piece!"
        elif (sexyguyWrongHoles == 2) or (sexyguyWrongHoles == 6):
            show sexyguy 2
            sx "Nope, thats not a good hole either!"
        elif (sexyguyWrongHoles == 3) or (sexyguyWrongHoles == 7):
            show sexyguy 2
            sx "Nuh uh!"
        elif sexyguyWrongHoles == 5:
            show sexyguy 1
            sx "Thats INCORRECT ha!"
        else:
            show sexyguy 3
            sx "i have NO IDEA what to say rn"##this will show up if the code is wrong
            sx "this shouldnt be possible? what happent???"
            sx "if you see this, it means {b}boris{/b} fucked up the code! so sad"
        return

    label sexyguyJUMPING:
        play sound quickkrun
        hide sexyguy with dissolve
        $ renpy.pause(0.6, hard=True)
        show sexyguy 4
        $ renpy.pause(sexyguyJumpSpeed, hard=True)
        play sound boingg
        show sexyguy 5
        $ renpy.pause(sexyguyJumpSpeed, hard=True)
        show sexyguy 4
        $ renpy.pause(sexyguyJumpSpeed, hard=True)
        play sound boingg
        show sexyguy 5
        $ renpy.pause(sexyguyJumpSpeed, hard=True)
        show sexyguy 4
        $ renpy.pause(sexyguyJumpSpeed, hard=True)
        play sound boingg
        show sexyguy 5
        $ renpy.pause(sexyguyJumpSpeed, hard=True)
        show sexyguy 4
        if sexyguyJumpMode == 1:
            $ renpy.pause(sexyguyJumpSpeed, hard=True)
            play sound boingg
            show sexyguy 5
            $ renpy.pause(sexyguyJumpSpeed, hard=True)
            show sexyguy 4
            $ renpy.pause(sexyguyJumpSpeed, hard=True)
            play sound boingg
            show sexyguy 5
            $ renpy.pause(sexyguyJumpSpeed, hard=True)
            show sexyguy 4
            $ renpy.pause(sexyguyJumpSpeed, hard=True)
            play sound boingg
            show sexyguy 5
            $ renpy.pause(sexyguyJumpSpeed, hard=True)
            show sexyguy 4
        $ renpy.pause(0.07, hard=True)
        hide sexyguy
        play sound quickkrun
        $ renpy.pause(0.4, hard=True)
        return

    label sexyguyREGULARshaping:
        call screen holesfit1
        if doShapesMatch:
            call sexyguyanswersGOOD
        elif shapeDroppable == "square":
            $ sexyguyMadnessLevel += 1
            k "square hole"
            call sexyguyanswers
        else:
            call sexyguyanswers
        return

    label sexyshapegamewhole:  

        $ sexyguyCasinoShingas = 0

        call screen holesfit1
        if doShapesMatch:
            sx "Woah! Correct!"
            show sexyguy 2
            sx "Cant believe you managed to get it right on the first try!"
            show sexyguy 1
        elif shapeDroppable == "square":
            $ sexyguyMadnessLevel += 1
            k "square hole"
            call sexyguyanswers
        else:
            call sexyguyanswers

        $ sexyguyCasinoShingas = 1
        call sexyguyREGULARshaping
        $ sexyguyCasinoShingas = 2
        call sexyguyREGULARshaping
        $ sexyguyCasinoShingas = 3
        call sexyguyREGULARshaping
        $ sexyguyCasinoShingas = 4
        call sexyguyREGULARshaping
        $ sexyguyCasinoShingas = 5

        call screen holesfit1   #this one is an actual square
        if doShapesMatch:
            k "square hole"
            if sexyguyMadnessLevel >= 4:
                $ sexyguyMadnessLevel += 1
                show sexyguy 2
                sx "Well, this one is actually a square..."
                show sexyguy 3
                sx "But QUIT doing what you're DOING!"
            else:
                call sexyguyanswersGOOD
        else:
            if sexyguyMadnessLevel >= 4:
                $ sexyguyMadnessLevel += 1
                show sexyguy 2
                sx "Okay, so when it ACTUALLY IS a square..."
                show sexyguy 3
                sx "YOU PUT IT, IN THE WRONG GODDAMN HOLE!!!!"
                sx "QUIT IT!!!!!!!"
            else:
                call sexyguyanswers

        $ sexyguyCasinoShingas = 6
        call sexyguyREGULARshaping
        $ sexyguyCasinoShingas = 7
        call sexyguyREGULARshaping

        if sexyguyCorrectas >= 5:
            $ sexyguyCasinoShingas = 11
        elif sexyguyMadnessLevel >= 5:
            $ sexyguyCasinoShingas = 12
        else:
            $ sexyguyCasinoShingas = 10
        show sexyguy 1
        sx "It seems that was the last one!"
        if sexyguyMadnessLevel >= 6:
            sx "Very well, because I {nw=0.0}"
            show sexyguy 3
            extend "NEVER WANT TO SEE YOU AGAIN!"
            sx "I FUCKING HATE YOU! NEVER SHOW UP AGAIN OR ILL FUCKING KILL YOU"
            sx "GO ROT IN HELL"
            play sound quickkrun
            hide sexyguy with dissolve
            narrater "he left you"
            k "damn"
            $ casinoLovesYou -= 1
            $ sexyguyCasinoShingas = 12
        elif sexyguyCorrectas >= 4:
            if sexyguyCorrectas >= 7:
                sx "Such a shame, you played SO GOOOOD!"
                sx "I had a such a great time"
            else:
                sx "You actually played pretty well"
                sx "We had quite some fun"
            sx "I hope we will see each other sometime soon"
            hide sexyguy with dissolve
            narrater "he shakes your hand and leaves"
            k "that was soo great so awesome"
            $ casinoLovesYou += 1
            $ sexyguyCasinoShingas = 11
        else:
            show sexyguy 2
            sx "You're not really good at this game, huh?"
            show sexyguy 1
            sx "It's fine, you can try again next time! I'm sure you're gonna do better"
            sx "Anyway, thank you for your time!"
            hide sexyguy with dissolve
            narrater "he shakes your hand and leaves"
            $ sexyguyCasinoShingas = 10
        menu:
            "Leave":
                hide shapeholes
                jump casinoFORW

    label casinoLEFT: #this IS the fun one
        scene casleft
        #"this is the fun one"
        if pielaCasinoShingas == 0 or pielaCasinoShingas == 1:
            if pielaCasinoShingas == 0:
                $ renpy.pause(1.0, hard=True)
                $ casinoMajorHappens += 1
                show transpiela with moveinleft
                pl "Hey man"
                pl "You look like some  guy who knows computer stuff"
                pl "a friend of mine told me those gamblin  machines run on some algorithms"
                pl "Im looking for a hacker"
            else:
                show transpiela with moveinleft
                pl "Hey man"
                pl "im still looking for a hacker man"
            menu:
                "whyyy":
                    $ karolTalkingMad = True
                    k "What th fuck do you wan t from me"
                    $ karolTalkingMad = False
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
                                    $ karolTalkingMad = True
                                    k "no man fuck off already this is bullshit"
                                    $ karolTalkingMad = False
                                    pl "man youre a dick i hate you now now"
                                    hide transpiela with moveoutleft
                                    $ casinoLovesYou -= 1
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
                            k "no imnt doing "
                            $ karolTalkingMad = True
                            extend "SHIT for you go away away"
                            $ karolTalkingMad = False
                            pl "hey you are a fuck youre a dick you know that"
                            pl "youre a dick"
                            $ casinoLovesYou -= 1
                            $ pielaCasinoShingas = 2
                "Ignore him (more optios)":
                    $ pielaCasinoShingas = 1

        if pielaCasinoShingas == 3:
            pl "oky lets heist right now"
            play sound cloth
            scene cas heistmachines
            show transpiela with moveinleft
            narrater "he takes you to an allye with some machinas"
            pl "okay were here can you do the thing now"
            pl "what are we doing now huh{nw=0.3}"
            extend " smartguy"
            k "i dont know"
            window hide
            $ renpy.pause(2.5, hard=True)
            pl "hey man wha-{nw=0.05}"
            k "okay kay maybe uhh"
            k "try to open the dhing"
            extend " huh the ting would you open the thing"
            pl "okay"
            pl " yes i can do that"
            window hide
            hide transpiela with dissolve
            show piela heisting with dissolve
            play audio dingering_automat
            $ renpy.pause(1.55, hard=True)
            play audio openin_automat
            $ renpy.pause(1, hard=True)
            hide piela heisting
            show la machine
            show piela heisting
            $ renpy.pause(2, hard=True)
            un "HEY"
            pl "uh oh"
            show chief 1: 
                xpos 550
            with moveinright
            ch "I saw you on the cameras, what the hell do you think you are doing???"
            play audio quickkrun
            hide piela heisting with moveoutleft
            $ renpy.pause(1, hard=True)
            $ karolTalkingMad = True
            k "what the fUck????"
            ch "thats it, im calling the cops on you yellow cunt"
            show chiefcellphone:
                xpos 550
            with moveinbottom
            k "wait!1!1 iTS not MEee the short little guy aksed me for HElp"
            ch "sir i saw noone aside from u here, now stop bothering me"
            window hide
            play audio callingpolice
            $ renpy.pause(7.65,hard=True)
            ch "there is a man in my casino messing with my equipment"
            k "IT WASNT ME IT WAS THAT FUCKING MIDGET"
            $ renpy.pause(1,hard=True)
            ch "the man may be under the influence of drugs as well, please get over here as quickly as-"
            play audio appear
            show dryleft with moveinleft
            p2 "well, well, well"
            k "FUKCKKKCK"
            hide chiefcellphone with moveoutbottom
            ch "what the fuck? i just called you guys how did you get here so fast????"
            p2 "huh? what are you talking about, we are just looking for this man right here"
            ch "oh really?"
            ch "sir look, he tried to cheat with the machines!!!!11"
            k "no i FUCKING DIDNDNTDT-{nw=0}"
            $ karolTalkingMad = False
            p2 "is that so? lemme write that down, yup"
            p2 "Either way, you're coming with me pal"
            jump policecar
            
        menu:
            "Go back":
                play sound door
                jump casinoMAIN
            "play the gamble":
                narrater "gambel"
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

    label gambel1rowshow:
        show expression slotstable[slotstablebig[gambelrow][0]]:
            ypos 100 xpos -160 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[gambelrow][1]]:
            ypos 100 xpos 640 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        show expression slotstable[slotstablebig[gambelrow][2]]:
            ypos 100 xpos 1440 zpos rollwheelradius
            matrixtransform RotateMatrix(-180, 0, 0) * OffsetMatrix(0, 0, 0)
            linear rolltime matrixtransform RotateMatrix(-540, 0, 0) * OffsetMatrix(0, 0, 0)
        $ renpy.pause(interval, hard=True)
        return

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
                gamble1didwin = False
        
        if gambelState == 0:
            $ gambelState = 1
            $ casinoMajorHappens += 1
        if gamble1didwin and (gambelState == 2):
            $ gambelState = 3
        if gamble1didwin and (gambelState == 1):
            $ gambelState = 2

        $ gambelrow = 0
        call gambel1rowshow
        $ gambelrow = 1
        call gambel1rowshow
        $ gambelrow = 2
        call gambel1rowshow
        $ gambelrow = 3
        call gambel1rowshow
        $ gambelrow = 4
        call gambel1rowshow
        $ gambelrow = 5
        call gambel1rowshow

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
            narrater "YES u won uhhhh this thing"
            if gambelState == 3:
                narrater "however u already won one thing so u aint getting shit now"
                narrater "piss off"
        else:
            play sound disappointment
            narrater "damn it u lost"
            $ karolTalkingMad = True
            k "FUCK"
            $ karolTalkingMad = False
        menu:
            "keep gambling":
                jump gambelplaying
            "quit":
                camera:
                    perspective False
                    gl_depth True
                    zpos 0
                play music casmusic fadein 1.5 volume 0.2
                jump casinoLEFT

    label extremely:
        play music cool1 fadein 2.0 volume 0.4
        scene arccool 1
        menu:
            "START":
                play sound coin
                $ renpy.pause(1.0, hard=True)
                play sound cam
                play music cool volume 0.4
                scene arccool 2
        menu:
            "FORWARD":
                play sound cam
                scene arccool 3
                $ renpy.pause(1.0, hard=True)
        menu:
            "FORWARD":
                play sound cam
                scene arccool 4
                $ renpy.pause(1.0, hard=True)
                show combine1 with dissolve
        menu:
            "{b}FIGHT":
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
                scene arccool 5
                $ renpy.pause(1.0, hard=True)
                show combine2 with dissolve
        menu:
            "{b}FIGHT":
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
                scene arccool 6
                $ renpy.pause(1.0, hard=True)
        menu:
            "INTERACT":
                play sound cam
                scene arccool 7
                $ renpy.pause(1.3, hard=True)
                play sound door
                scene arccool 8
        menu:
            "FORWARD":
                play sound cam
                scene arccool 9
                $ renpy.pause(1.0, hard=True)
        menu:
            "FORWARD":
                play sound cam
                scene arccool 10
                $ renpy.pause(1.0, hard=True)
                show combine1 with dissolve
        menu:
            "{b}FIGHT":
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
                scene arccool 11
                $ renpy.pause(1.0, hard=True)
                show combine1 with dissolve
        if not isZlinkDie:
            menu:
                "{b}FIGHT":
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
                    scene arccool 12
                    $ renpy.pause(1.0, hard=True)
            menu:           
                "CROUCH DOWN":
                    play sound cam
                    scene arccool 13
                    stop music
                    play sound win
                    $ renpy.pause(3.0, hard=True)
                    narrater "yay u won and shit, get back now bastard"
                    play music casmusic fadein 1.5 volume 0.2
                    $ casinoMajorHappens += 1
                    jump casinoLEFT
        else:
            menu:
                "{b}FIGHT":
                    show gun aim with moveinbottom
                    $ renpy.pause(0.3, hard=True)
                    play sound bad
                    show gun shoot with vpunch
                    $ renpy.pause(0.1, hard=True)
                    show gun aim
            menu:
                "{b}FIGHT":
                    show gun aim with moveinbottom
                    $ renpy.pause(0.3, hard=True)
                    play sound bad
                    show gun shoot with vpunch
                    $ renpy.pause(0.1, hard=True)
                    show gun aim
            menu:
                "{b}FIGHT":
                    show gun aim with moveinbottom
                    $ renpy.pause(0.3, hard=True)
                    play sound bad
                    show gun shoot with vpunch
                    $ renpy.pause(0.1, hard=True)
                    show gun aim
            menu:
                "{b}FIGHT":
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
                "{b}FIGHT":
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
                    narrater "it seemns that all the lights went oUT"
                    k "oh noo shit{nw=0.5}"
                    $ karolTalkingMad = True
                    extend " shIT SHIt SHIT"
                    $ karolTalkingMad = False

                    narrater "the rooms start to smell lik some kind of drywalll"
                    narrater "you may be fucked buddy"
                    jump casinodoorlock

    label casinoCHIEFinMAIN:
        scene casmiddle
        $ renpy.pause(1, hard=True)
        play audio cloth
        show chief 1 with moveinleft
        un "hey YOU"
        un "stop RIGHT THERE"
        show chief 2
        ch "i am the owner of this place, and in front of my casino there is a police car"
        hide chief
        show chief 1 onlayer screens
        ch "these men have told me they are looking for some short annoying gay man that commited some murder"
        ch "i suppose they were describing YOU"
        menu:
            "noo not me thats not meee":
                k "noNOoo thats not me you should look{nw=0.5}"
                extend " look for someone else its not me "
                show bobis nexttochief onlayer screens
                with moveinright
                play voiceact "bopis/boris 20.mp3"
                bb "no point in lying, whe know that youre the guy"
            "yes its me":
                k "yeah thats me i murdered a guy"
                show bobis nexttochief onlayer screens
                with moveinright
                play voiceact "bopis/boris 21.mp3"
                bb "boss, you got the guy? thats so good!"
            "flee":
                narrator "you start flooring it"
                scene cas1
                hide chief onlayer screens
                play sound cloth
                $ renpy.pause(1.5, hard=True)
                show bobis 1 with moveinbottom
                narrator "a man stops you"
                play voiceact "bopis/boris 22.mp3"
                bb "heyy where you going buddy? boss i got him!"
                hide bobis with dissolve
                show chief 1 onlayer screens
                with dissolve
                show bobis nexttochief onlayer screens
                with moveinright
                ch "well well well, we are not letting you run"
        ch "we will now turn you to the police, criminel"
        ch "nothing personal you guy, we just want no trouble here"
        if casinoLovesYou >= 2:
            show casinocrowd happy with moveinbottom
            crwd "but we love this guy"
            if wrenchCasinoShingas == 1:
                play voiceact "wrench/wrench 26.mp3"
                br "he made me win big!"
            if wiktorCasinoShingas == 1:
                wb "he spared us some money!"
            if sexyguyCasinoShingas == 11:
                sx "We had a DELIGHTFULL time"
            if barguybadshinger == 2:
                b2 "such an awesome guy"
                "huh???? this part is really fucking unfinished here"##___________________________FINITSHSHHS
                jump end
        elif casinoLovesYou <= -2:
            show casinocrowd mad with moveinbottom
            crwd "we hate this guy"
            if wrenchCasinoShingas == 2:
                play voiceact "wrench/wrench 27.mp3"
                br "i lost EVERYTHING because of this MAN"
            if pielaCasinoShingas == 2:
                pl "this guys garbage you know, garbage"
            if wiktorCasinoShingas == 2:
                wb "he couldnt spare us a single penny!"
            if barguybadshinger == 3:
                b2 "HE FUCKING KILLED MY BROTHER"
            if sexyguyCasinoShingas == 12:
                sx "I deeply regret playing with this man"
            play voiceact "bopis/boris FUCK YOU.mp3"
            bb "FUCK YOUU"
            "police men appear and the beating happen"
            jump lospital##_________________________________________________TOFINISH
            
        else:
            $ renpy.pause(1,5, hard=True)
            narrater "noone really cares about your fate here"
            narrater "damn"
            jump policecar




    label casinodoorlock:
        scene cas1dark
        play audio run
        narrater "u run to that pretty awesome DOOR u usedd to enter das casino"
        show casbackdoordark
        $ randomasNumeras(10)
        narrater "you aproach te DOOR, but suddenly u feel some powerfull presence..."
        show locknik light with dissolve
        $ renpy.pause(1, hard=True)
        show locknik lock with dissolve
        if (randomAssShit <= 1):
            og "hello im ognik" #_________________________________________ognik<-----
            #show expression "images/ognikTest/locknik lock2.png"
            show locknik lock2
            og "and u are gayy"
        else:
            og "hello yes i am ognik the grand lock"
            show locknik lock2
            og "yes you see i am gonna lock you inside this place yes"
            og "because i hate you, yes, hello"
            k "wh-, waht???!??!"
            $ karolTalkingMad = True
            k "dude LET ME OUTTT T"
            $ karolTalkingMad = False
            show locknik lock
            og "yes you are going to spend six more hours in this place because yes"
            extend " i hate you"
            og "yes good luck come back here in six hours yes and maybe im gonna"
            extend " let you out maybe yes"

        show locknik light with dissolve
        $ renpy.pause(1, hard=True)
        hide locknik light with dissolve
        narrater "well this is bAd"
        k "shiiiit whamt am i gonna do now??!?!"
        scene casleftdark
        play audio run
        narrater "u rember some staff rooms u seen before so u run to search for them"
        scene casstaff2dark
        k "wooh look a there are some roooms here"
        scene casstaffscarymain
        narrater "you find yourself in this somewhat safe room"
        k "i gues ill have to spend some hourrs in heere"
        k "huh theres some weird tablet but its baterydead"
        k "oh i have an iDEA"
        narrater "u start searching deep in your asshole"
        if narraterTalking:
            $ renpy.alt("you have found:", force=True)
        "you have found:"
        play sound dia1
        show foundflashlight
        if narraterTalking:
            $ renpy.alt("a long flashlight", force=True)
        extend "\na long flashlight"
        play sound dia1
        show foundbutton
        if narraterTalking:
            $ renpy.alt("a round button", force=True)
        extend "\na round button"
        play sound dia1cut
        show foundbuttp
        if narraterTalking:
            $ renpy.alt("and some metal buttplugs!", force=True)
        extend "\nand some metal buttplugs!{nw=2.5}"
        k "oh shit nah wrong thing, lemme put this back inside"
        hide foundbuttp
        play audio assholefist
        $ renpy.pause(1.0, hard=True)
        play sound dia1
        show foundbattery
        narrater "and a small big batery!"
        $ karolTalkingMad = True
        k "YES i will COMBINE those items inorder to survive this NIGHT!"
        $ karolTalkingMad = False
        hide foundflashlight
        hide foundbutton
        hide foundbattery
        narrater "you hear a man making some {b}{color=#FFFFFF}DRY{/color}{/b} steps back somewher there"
        if isMatysiakAnger:
            narrater "and thers some kebab shaped farts in company with him!!!"
        else:
            narrater "seems hes alone tho"
        narrater "goodluck"

        label loop_entry: ##fnafff
            $ quick_menu = False
            $ renpy.block_rollback()
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
        
    label casinodrywallgotyou:
        $ renpy.block_rollback()
        hide screen door_buttons
        hide screen show_time
        hide screen cameraview
        hide screen flashleft
        hide screen flashtop
        hide screen flashright
        hide screen DEBUGmode
        show dry2:
            zoom 0.01 yalign 0.5 xalign 0.5
            ease 0.5 zoom 1.2
        play audio hl2scream
        $ renpy.pause(3.0, hard=True)
        scene black
        narrater "drywall got you lmao"
        narrater "u getting dragged to hell"
        jump end

    label casinomatysiakgotyou:
        $ renpy.block_rollback()
        hide screen door_buttons
        hide screen show_time
        hide screen cameraview
        hide screen flashleft
        hide screen flashtop
        hide screen flashright
        hide screen DEBUGmode
        show mat 1:
            zoom 0.01 yalign 0.5 xalign 0.5
            ease 0.5 zoom 1.2
        play audio hl2scream
        $ renpy.pause(3.0, hard=True)
        scene black
        narrater "matysiak got you lmao"
        narrater "u getting used as a toilert"
        jump end

    label casinoescape:
        $ renpy.block_rollback()
        hide screen door_buttons
        hide screen show_time
        hide screen cameraview
        hide screen flashleft
        hide screen flashtop
        hide screen flashright
        hide screen DEBUGmode
        play audio victory
        $ renpy.pause(3.0, hard=True)
        narrater "what the hell"
        narrater "you did this" #casino on fire there
        jump end

######################################################################################################################################################
label _CASINO_LEAVING_HERE____________________________________________________________________________________________________________________________:
    ##################################################################################################################################################
    label outsidecasino:
        stop music fadeout 0.5
        scene cas3
        play audio cloth
        show bobis 1 with moveinbottom
        play voiceact "bopis/boris 15.mp3"
        bb "Stay out of our casino"
        play voiceact "bopis/boris 16.mp3"
        bb "You're only bringing trouble"

        

        narrater "you hear a familiar voice"
        p2 "well well well.."


        play audio cloth
        show dryleft with moveinleft
        hide bobis 1 with dissolve
        
        

        p2 "look who we have here"
        p2 "you got some nerve runnin away from me"

        show zlink 1 with moveinright
        play audio cloth
        play voiceact "zipps/zippy 11.mp3"
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
        play voiceact "zipps/zippy 12.mp3"
        p1 "so yeah we found your car and ID"
        play voiceact "zipps/zippy 13.mp3"
        p1 "so we know  who you are now and itsnot looking good for you pal"

        show bobis right with moveinbottom

        play audio cloth
        play voiceact "bopis/boris 17.mp3"
        bb "Sir, he was making trouble at our place"

        play audio impact1
        with vpunch
        play voiceact "bopis/boris JAIL HIM.mp3"
        bb "JAIL HIM!"

        play audio impact2
        with vpunch
        play voiceact "bopis/boris PUNISH HIM.mp3"
        extend " PUNISH HIM!"

        p2 "is that so?"

        p2 "Either way, you're coming with me pal"
        play voiceact "zipps/zippy 14.mp3"
        p1 "oh dont't worry, he will be punished accordingly"

        play voiceact "bopis/boris 18.mp3"
        bb "okaym ill levae you to  it"
        play audio cloth
        hide bobis right with dissolve
        narrater "the management guy disapepars and then uhh"

    label policecar:
        scene black
        stop music
        narrater "the officers take you away to their car"
        p1 "you bastard, its so over for you"
        #narrater "the police officers put you in their car"

        scene policecar
        narrater "they put you in the car look this is the car!"
        narrater "impossible!! its the car!!"

        p2 "haaang tight buddy, a court room has been already prepared for you"

        scene later
        play audio later
        narrater "one enteri later"

    label courtarrive:
        scene courthall1
        play audio foot
        narrater "you go in court"
        if shitcourt == 1:
            jump shittycourt
        else:
            jump courtPresidents

        
        

    label shittycourt:
        play audio foot
        scene court
        play music ace2 fadein 1.0 volume 0.1
        narrater "you get dragged into the court room"

        play audio cloth
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

        narrater "you have received your (disceased) lawyers bag"

        hide lawyerbag
        play sound courthammer
        j "so... lets commence the trial"
        play music ace1 fadein 1.0 volume 0.3
        j "explain to me whats happened"
        play sound appear
        show dryleft with moveinleft
        play voiceact "zipps/zippy 15.mp3"#wait what is happening here
        p1 "alright so.. this guy right here punched a man in the bathroom"

        #argument cards
        #if u pick a racist one trump shows up and you win if not you lose

        menu:
            "NO!! That's a lie!":
                $ karolTalkingMad = True
                k "I DID NOT!!!"
                $ judgepissedlevel += 1

                if narraterTalking:
                    $ renpy.alt("The judges expression doesn't look good..", force=True)
                "The judges expression doesn't look good.."
                if narraterTalking:
                    $ renpy.alt(" he looks pretty pissed off", force=True)
                extend " he looks pretty pissed off"
                menu:
                    "Here's what happened":
                        
                        k "I was taking a shit. okay?"
                        k "and this fucker, i dont know who he is, barges into my stall"
                        if didyankdoor:
                            k "fucker yanked my ENTIRE door away after punching a hole trought the metal"
                            k "some sick fuck i tell y ou"
                $ karolTalkingMad = False

            "Yeah":
                
                k "Yes, i punches that guy in the bathroom, for good reason too"
                j "good reason you say?"
                k "he invaded my personal space!"
                k "while i was.."
                $ karolTalkingMad = True
                play audio impact1
                with hpunch
                extend " {b}{color=#851911}taking a shit!!{/b}"

                j "..."


                p2 "..."

                k "its a horribl wy to invade someones privacy guys"
                k "its a MASSIVE VIOLATIO N OF YM PRIVACY"
                $ karolTalkingMad = False

        play audio hammer1
        j "Order! ORDER IN THE COURT!"
        j "Did he atleast knock?"

        menu:
            "He did":
                if didyankdoor:
                    k "He tore the fucking door{nw=0.0}"
                    play audio impact1
                    $ karolTalkingMad = True
                    extend "{color=#6b5512} off of its hinges"
                else:
                    $ karolTalkingMad = True
                    k "He was banging on my door furiously~!!"
        j "and what exactly were you doiing in the bathroom?"
        menu:
            "Taking a shit":
                k "Like i said,  i was taking ashit dipshit"
            "What do u fuckin think":
                $ judgepissedlevel += 2
                k "What do you fucking think i was doing?"
                k "are you retarded?"
                play audio hammer2
                j "FUCK YOU!"
                j "IM THE JUDHGE"
                j "imthe FUCKING judge YOU DONTT ALK TO ME THAT WAY!!"

        $ karolTalkingMad = False
        j "can someone fact check this?"
        p2 "your honour, i can confirm he was inddeed taking shit."
        j "how so?"
        p2 "after we transported him here he left a giant shit stain in the back of our patrol car"

        j "wery well.. we may continue"

        if not isPathetic:
            p2 "wait a second"
            p2 "i completely forgot but i have this written down"
            p2 "the suspect proceeded to.. "
            play audio impact2
            extend " {color=#de1809}attack{/color} me with his fists when he was found"
            p2 "and i scared him off when i pulled out my gun"
            j "WHAT"
            play audio hammer1
            $ judgepissedlevel += 1
            j "ASSAULT ON A POLICE OFFICEERR??? THATS NOT NICE"

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
        play audio appear
        show zlink right with moveinright
        play voiceact "zipps/zippy 15.mp3"
        p1 "alright so...."
        play voiceact "zipps/zippy 16.mp3"
        extend "\nwe first found a car.."
        play voiceact "zipps/zippy 17.mp3"
        extend "\nand the windshield was aaaallll bloody"
        menu:
            "Thas crazy":
                k "this so crazy"
                play audio hammer1
                j "will the defendant please shut the fuck up"
                $ judgepissedlevel += 1
                narrater "seems youre really getting on his nerves"
                p2 "in any case.."
            "Say nothing":
                pass
        play voiceact "zipps/zippy 18.mp3"
        p1 "pretty scary stuff man"
        play voiceact "zipps/zippy 19.mp3"
        p1 "but then.."
        play voiceact "zipps/zippy 20.mp3"
        extend "not too far on the ground we saw something disturbing.."
        p2 "it was a man.."
        extend "{color=#327325}a pickle{/color}"
        extend ". A man."
        extend " A {color=#327325}pickle{/color} shaped man."
        extend " Long gone.. No longer with us."
        play voiceact "zipps/zippy 21.mp3"
        p1 "we actually confiscated the car"
        hide dryleft with dissolve
        play audio metaldrag
        show carblood with moveinleft
        #$ renpy.pause(1, hard=True)
        narrater "they drag the car inside"
        hide carbloodpick
        hide dryleft with dissolve
        show carbloodpick
        play audio cloth
        play voiceact "zipps/zippy 27.mp3"
        p1 "we also got the man"
        
        
    
        show dryleft with dissolve
        p2 "here it is, our concrete evidence of the first murder"

        menu:
            "Not my car":
                k "Whata re you talk about?"
                k "This isnt my car"
                p2 "Yes"
                extend " ,yes it is"
                play voiceact "zipps/zippy 22.mp3"
                p1 "Look at it! the car s yellow"
                play voiceact "zipps/zippy 23.mp3"
                p1 "and guess what"
                play voiceact "zipps/zippy 24.mp3"
                extend "YOU are also yellow"
            "Say nothing":
                pass
            "I thought it was a road bump!!":
                $ karolTalkingMad = True
                k "But i thought it was a road bump on the highway!"
                $ karolTalkingMad = False

        j "well, we're just going to have to ask to have ask the witness!"

        stop music fadeout 3.0

        j "mster pickle nan, could you please tell the court what happened?"

        play sound nin1
        "..."

        j "take your time."

        play sound nin2
        "..."

        p2 "you honor-"

        play audio hammer2
        j "NO INTERRUPTIONS"
        j "the witness is testifying"
        j "go right ahead, mr pickle"

        play sound nin3
        "..."

        j "mr pickle?"

        play sound nin4
        "..."

        p2 "hes dead."
        play music ace3 fadein 1.0 volume 0.3
        j "wery vell.."
        j "let it be known, the witness is not cooperating"

        narrater "its not looking very good for you.."
        menu: 
            "Open the lawyers bag":
                play audio zip
                "you open the bag"
                
        play audio drumroll
        narrater "inside... you find:"
        stop audio
        play audio found1
        show foundtime
        narrater "A mysterious device! Fascinating!!!"

        play audio found2
        show foundnose
        if narraterTalking:
            $ renpy.alt("A nose and glasses thing! Dunno whats its called. ", force=True)
        "A nose and glasses thing! Dunno whats its called. "
        if narraterTalking:
            $ renpy.alt("I'm sorry for being such a unreliable narrator.. ", force=True)
        extend "I'm sorry for being such a unreliable narrator.. "
        if narraterTalking:
            $ renpy.alt("i really dont know whats it called. sorry :(", force=True)
        extend "i really dont know whats it called. sorry :("

        play audio found3
        show foundcontrol
        narrater "A controller!!"

        label choose:
            
            scene courtthings
            menu:
                "Use the strange device":
                    scene courtthings2
                    narrater "you choose the strange device"
                    play audio appear
                    show hands bomb with moveinbottom
                    k "hmm what a strange device"
                    menu:
                        "use thta device":
                            play audio cclick
                            narrater "you click some button"
                            play audio dial
                            narrater "it starts dialing shit what the hell"
                            play audio dial
                            $ renpy.pause(1, hard=True)
                            show explode
                            stop music
                            play audio explod
                            $ renpy.pause(1, hard=True)
                            play audio failstick
                            scene failexplod
                            call screen retry

                "Use the fake nose and glasses":
                    scene courtthings2
                    narrater "hmm"
                    play audio appear
                    show hands glas with moveinbottom
                    menu:
                        "put them on":
                            hide hands glas with dissolve
                            play audio cloth
                            show glassoverlay
                            narrater "wow you look s ogood"
                            if judgepissedlevel == 5:
                                j "the judge looks at you with a very dissappointed expression"
                                narrater "the judge sighs"
                                j "Hm... Karol Mijas.."
                                menu:
                                    "Yes?":
                                        k "yeah"
                                        narrater "the judge looks like he's gonna die out of dissappointment"
                                        j "first you interrupted the me like seventeen times"
                                        j "and now you show up wearing that hat"
                                
                                        j "karol mijas."
                                    "I'm not karol mijas":
                                        k "I'm carl beez"
                                        j "first you interrupted the me like seventeen times"
                                        j "and now you show up wearing that hat"
                                
                                        j "karol mijas- no.. carl beez.."
                                
                                
                                extend " you are free to go"
                                j "i dont care anymore"
                                play audio hammer1
                                j "just get out of my sight"
                                play audio hammer2
                                j "get the fuck outta this court"
                                jump free_ending
                            else:
                                j "for the record... the defendant appears to be wearing fake glasses, a fake nose, and a fake mustache."
                                p2 "should i write that down?"
                                j "no need"
                                menu:
                                    "i'm no mijas":
                                        k "you got the wrong person!"
                                        narrater "nobody seems to buy the disguise"
                                        if narraterTalking:
                                            $ renpy.alt("seems its not working on these people", force=True)
                                        "seems its not working on these people"
                                        if narraterTalking:
                                            $ renpy.alt(" damn. and i thought this shit would be perfect", force=True)
                                        extend " damn. and i thought this shit would be perfect"
                                    "say nothing":
                                        jump courtasidk
                                label courtasidk:
                                    narrater "the jhudge slams the hammer"
                                    play audio hammer1
                                    
                                    j "well, you are hereby sentenced.."
                                    play audio applause1
                                    extend " to {color=#de1809}10 years{/color} in prison"
                                    play audio cloth
                                    hide zlink right with dissolve
                                    hide dryleft with dissolve
                                    j "please move this bastard out of here"
                                    menu:
                                        "say nothing":
                                            narrator "you choose to stay silent and they drag you away"
                                        "say you aren't happy with this outcome":
                                            $ karolTalkingMad = True
                                            k "FUCK YOU"
                                            k "THIS IS SO UNFAIR"
                                            k "I NEVVER HURT ANYONE I ONLY MAKE GARRYS  MOD MAPS"
                                            k "I WILL KILL YOU"
                                            $ karolTalkingMad = False
                                            jump teprison

                "Use the controller":
                    scene courtthings2
                    narrater "you take the controller"
                    hide foundnose
                    hide foundtime
                    hide foundcontrol
                    k "these npc pissing me off you"
                    k "let me skip this damn npcs cutscenee"
                    play audio appear
                    show hands control with moveinbottom
                    menu:
                        "press button on controller":
                            $howmanytimes += 1
                            play audio cclick
                            narrater "you click it"
                            
                            $ renpy.pause(1, hard=True)
                            stop music
                            if howmanytimes == 1:
                                
                                play audio jailer
                                scene pison
                                show hands control
                                $ renpy.pause(3, hard=True)
                                k "well shit"
                                play audio failstick
                                show failprison
                                call screen retry
                            else:
                                play audio jailer
                                scene pison
                                show hands control
                                $ renpy.pause(3, hard=True)
                                k "well shit"
                                narrater "yup, you still end up in the prison"
                                narrater "dunno why you expected anything to change"
                                play audio failstick
                                show failprison
                                call screen retry

    screen retry:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.15
            ypos 0.85
            idle "retrybut.png"
            action [Play("audio", "gobackclick.mp3"), Jump("choose")]


    

    label courtPresidents:
        play music ace2 fadein 1.0 volume 0.05
        scene court
        narrater "woa look its th ecourtuoom"
        play audio appear
        show judge 1
        un "heeey hello"
        j "hello i am the judge"
        play audio hammer2
        j "ORDER IN THE COURT NOW"
        j "So.. Karol mijas. YOu rea the defendast, and your laawayer thas been appointed to you is on the way."
        play audio appear
        show trump with moveinright
        t "hey hey, hello im here because im very interested in this case, very interested indeed"
        t "some people are saying this is the greatest court case of all time. I don't know if that's true, but a lot of very smart people are saying it."
        t "everyobodys asking 'Are you going to the court case' and i said 'maybe', maybe i am, and quite frankly ive never seen a courtroom like this with such trmendous energy before"
        $ renpy.pause(1.0, hard=True)
        play audio appear
        show judge 1:
            matrixtransform RotateMatrix(0, 0, 0)
            ease 0.5 matrixtransform RotateMatrix(0, 0, 40)
        j "hey ths is my courtroom im the judge"
        #play audio appear
        t "uuhh, no, frankly speaking, i am the president here and uh you gotta listen to me, alright, is that clear?"
        t "hey barrack, get over here"
        play audio cloth
        show obama with moveinright
        ob "hello i am your president barac obmana"
        t "yeah"
        ob "yes trump, what is it trump?"
        t "what do you think of this.. highly interesting court case tremeendous, even, absoloutely tremendous"
        ob "well, i dont know trump, maybe we should let the court actually work things out and uuh see how this court case goes huh"
        t "alright, alright, but believe me, ive seen a lot of courtrooms, and this courtroom? its top tier, maybe even one of the best"

        play audio appear
        show judge 1:
            matrixtransform RotateMatrix(0, 0, 40)
            ease 0.5 matrixtransform RotateMatrix(0, 0, -40) xpos 840
        play music ace1 fadein 5.0 volume 0.1
        j "ahem, the accused stands accused for..{nw=0.5}"
        play audio applause1
        extend " {color=#db190b}murder!!{/color}"
        play audio impact2
        t "{color=#db190b}Murderrr???"
        show trump:
            ease 1.5 xpos 860
        t "murder you say.. people tell me all the time, murder is pretty bad, no really, i wonder how this 'Karol mijas' is going to deal with this  massive accusation.. quite a massive accusation this is"
    
        play audio appear
        show judge 1:
            matrixtransform RotateMatrix(0, 0, -40)
            ease 0.3 matrixtransform RotateMatrix(0, 0, 30) xpos 1010
        j "will the police officers provide us with neccesary information?"

        play audio appear
        show dryleft with moveinleft
        p2 "yes your honour"
        t "hey sleepy joe, i think you should listen to this. i bet nobodys seen anything like it"
        play audio shleeping
        hide dryleft with dissolve
        show sleepy with dissolve
        
        narrater "seems hes deep asleep"
        ob "maybe we should just let him sleep, donald"
        t "alright, alright, okay, dry looking guy, you may continue"

        play audio appear
        show dryleft with moveinleft
        p2 "so, in any case, we first got a call about a murder in a bar"

        play audio cloth
        show zlink right:
            xpos 180
        with moveinright
        play voiceact "zipps/zippy 25.mp3"
        p1 "when we arrived at the scene, we saw a dead bartender, dead on the ground"
        p2 "quite a gruesome sight."

        t "a dead bartender... sad. really sasd."
        show trump:
            ease 1.0 xalign 0.5
        extend "but ive seen a lot of things like this-maybe more than anybody, and, frankly its a verry cmplex situation."
        t "I wonder if he was an american.. "
        t "or one of those pesky latinos, monkeys, mexicans, whatever you can call them"
        show obama:
            ease 0.4 xpos 920
        ob "hey trump, i think we should not express thees feelings right now"
        ob "we can talk about them later in the white house"
        t "sure sure, im just making a statement"
        
        p2 "in the building, we encountered.. "
        play audio impact1
        with hpunch
        extend "the {color=#db190b}{b}DEFENDANT!{/b}"
        play voiceact "zipps/zippy 26.mp3"
        p1 "i encountered him further in the building, his fists, covered in blood"

        t "quite frankly im wondering, what the defendant would say to this.."

        menu:
            "It was tomoto soup":
                k "Uh no, that wasnt blood, it was tomato soup on my fists"
            "I dont know":
                k "damn these are some {nw=0.5}"
                $ karolTalkingMad = True
                extend "WILD accusations guys"
                $ karolTalkingMad = False
            "Stay silent":
                $ staysilent += 1
                narrater "you stay silent"
                narrater "smart move, as your lawyer still isnt present"
                t "okay, okay, the silent treatment"
            "Victim was a horse":
                k "youe honor.."
                k "te victim was.."
                $ karolTalkingMad = True
                extend " a HORSE!!"
                $ karolTalkingMad = False
        show court3
        un "what he ell??"
        play audio cloth
        show teeguy serious with dissolve
        l "you queestioned my client without me here???"
        l "sorry im late sugar pup"
        l "i had a wax job on my ass"
        menu:
            "WHAT HTOOK YOU SO LONMG": #ass waxxing angry
                k "asshole"
                $ karolTalkingMad = True
                k "WHAT TOOK YOU SO LONG"
                k "you coul'ved waxxed ur ass another time! MOTHERFUCKER"
                $ karolTalkingMad = False
                l "waxxing my ass helps me to focus in court.."
                narrater "he turn towards the judge and the others"
                hide court3
                hide zlink right
                hide dryleft
                show teeguy left
                l "let me get this straight..."
                l "ur saying.. the victim was brutally fisted with clear intention of killing him"
                l "and was done on purpose"
                l "according to my book-idy-book!"
                l "under the {color=#db190b}'Baudžiamasis kodeksas'{/color}"
                l "{color=#38465c}Nusikaltimas yra tyčinis, jeigu jis padarytas tiesiogine ar netiesiogine tyčia.
                jį darydamas asmuo suvokė pavojingą nusikalstamos veikos pobūdį, numatė, kad dėl jo veikimo ar neveikimo gali atsirasti šiame kodekse numatyti padariniai, ir jų norėjo.{/color}"
                l "i apologisze, i wasnt able to get this book in eglish"
                t "i dont know what hes saying..."
                t "but i think hes speaking truly from the heart!!"
                k "yeah man he is"
                show teeguy left:
                    ease 0.5 xpos 1500
                l "the attacker deserves {color=#db190b}death{/color}!!"
                menu:
                    "defiance":
                        narrater "you throw yourself at your lawyer"
                        play audio push
                        play audio bad
                        stop music
                        show teeguy fly at vpunch
                        show hands throw:
                            zoom 2
                            yalign 0.5
                            xalign 0.5
                            ease 0.9 zoom 1
                        $ karolTalkingMad = True
                        k "SQUARE UP BITCH"
                        $ karolTalkingMad = False
                        play audio fall
                        hide teeguy fly with moveoutbottom
                        show hands throw:
                            zoom 1
                            yalign 0.5
                            xalign 0.5
                            ease 0.5 zoom 6
                        narrater "lawyer falls down to the ground very hard"
                        menu:
                            "take his belongings":
                                narrater "you search his body"
                                play audio dia1
                                show lawyerbag

                                narrater "you have received your lawyers bag"
                                menu:
                                
                                    "Open the lawyers bag":
                                        hide lawyerbag
                                        play audio zip
                                        "you open the bag"
                                        
                                play audio drumroll
                                narrater "inside... you find:"
                                $ renpy.music.stop()
                                play audio found1
                                show hand time with moveinbottom
                                narrater "a TIME MACHINE!"
                                $ renpy.config.skipping = False
                                "wow" #BOOOOOORIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIISSSSSSSSSSSS TIME TRAVEL NOW NOW TIME TRAVEL NOW NOW TIME TRAVEL NOW NOW TIME TRAVEL NOW NOW TIME TRAVEL NOW NOW TIME TRAVEL NOW NOW
                                
                                show black with dissolve
                                #$ renpy.pause(1, hard=True)
                                hide hand time
                                jump timetravelpart

                                label timesrav(withpause, timer):
                                    show timeravel:
                                        zoom 1.0 matrixtransform RotateMatrix(0,0,0)
                                        xalign 0.5 yalign 0.5
                                        linear timer zoom 2.0 matrixtransform RotateMatrix(0,0,-2.5)
                                    if withpause:
                                        $ renpy.pause(timer, hard=True)
                                    return

                                label timetravelpart:
                                    $ renpy.pause(1, hard=True)
                                    window hide
                                    show screen unskippableAD
                                    $ timeraveltime = renpy.get_game_runtime()
                                    show timeravel
                                    show screen gayyshit 
                                    play audio timeravel
                                    call timesrav(True,2.0)
                                    call timesrav(True,1.9)
                                    call timesrav(False,1.75)
                                    k "what the fuuuuuuuuuuuuuuuuucccckkk{nw=1}"
                                    call timesrav(True,1.5)
                                    call timesrav(True,1.3)
                                    $ timetime = 1.1
                                    while (timeraveltime + 14.8 > renpy.get_game_runtime()) and (timetime > 0):
                                        call timesrav(False,timetime)
                                        $ imlosingmyfuckingmind = renpy.get_game_runtime()
                                        while (imlosingmyfuckingmind + timetime > renpy.get_game_runtime()):
                                            $ renpy.pause(0.05, hard=True)
                                        $ timetime -= 0.1
                                    $ renpy.block_rollback()
                                    show black
                                    hide screen gayyshit
                                    hide timeravel

                                    $ renpy.pause(6, hard=True)
                                    show bar2
                                    hide black
                                    show black
                                    hide screen blackCover
                                    play music jazz fadein 1.5 volume 0.2
                                    hide black with dissolve
                                    hide screen unskippableAD
                                    $ renpy.pause(2, hard=True)
                                    play voiceact bar1
                                    un "Hello there."
                                    play voiceact bar2
                                    b "I'm the bartender here"
                                    play voiceact bar3
                                    b "Would you like something to drink, good sir?"
                                    $ renpy.pause(2, hard=True)
                                    k "no fucking way"
                                    hide bar2
                                t "oh, you came back?"
                                ob "we've been waiting here for you"
                                t "so karol mijas, uhh.. tell me.. what did you change with that precious precious time machine of yours?"
                                t "maybe you saw greater times.. maybe the times without those pesky mexicans"
                                t "the times when america was great.."
                                t "maybe we can make it great again"
                                show teeguy left with moveinleft
                                l "how could you use my time travelling machine???"
                                l "did you atleast put it to good use?"
                                l "well? did you?"
                                menu:
                                    "explain":
                                        k "allow me to explain so you guys can understand"
                                        k "let's start with the start"
                                k "i spawned into the bar, fortnite style"
                                menu:
                                    "talk shit":
                                        $ talkingshit += 1
                                        k "this time, i didnt kill the bartender, im a very pure soul"
                                        k "instead i went to make out with my past self"
                                        k "no bartenders were hurt in the proccess"
                                        k "we had a delightful time together ;)"
                                        j "so the bartender is alive?"
                                        k "yes, very much alive and kicking"
                                    "explain":
                                        k "when i saw the bartender again, i couldnt supress my rage"
                                        k "i killed him again"
                                        $ karolTalkingMad = True
                                        k "I BEAT HIM SENSELESS"
                                        $ karolTalkingMad = False
                                        k "over and over and over and over and over over and over over and over, blood everywhere"
                                        k "until he took his last breath and perished"
                                if talkingshit:
                                    play audio ring
                                    j "oh? hold on, im getting a call"
                                    narrater "the judge answers his phone"
                                    play audio phonetalk
                                    j "mhmhm yup, see you."
                                    j "well karol you are lying.."
                                    play audio impact2
                                    show judge 1 at vpunch
                                    extend " because nothing changed"
                                    j "you are just a lyar!!"
                                else:
                                    l "soo....."
                                    l "you used MY time machine to go BACK IN TIME and you..."
                                    l "you just WASTED IT???"
                                j "karol mijas, your guiltyness is clear as day"
                                j "frankly, you dont derserve to live"
                                j "but i cant hand out a death penalty"
                                play audio hammer1
                                j "so karol mijas, i hereby sentence you.."
                                play audio applause1
                                j "to {color=#de1809}500 years{/color} in prison"
                                l "yay!"
                                k "huh, thats better than death i guess"
                                jump teprison
                        
                        pass
                    "acceptance":
                        k "aw man"
                        play audio appear
                        show teeguy left:
                            ease 0.5 xpos 1000
                        show zlink right with moveinright
                        p1 "CAN I DO IT????"
                        t "SHUT UP! i'm gonna be th one who kills kills him"
                        k "arent you supposed to be my lawyer!??"
                        l "whats a lawyer??"
                        l "im just here ccause they promised me a free wax session"
                        l "they just gave me this suit and book and told me to act as a lawyer would"
                        k "aw fuckkkkkk"
                        k "then i guess im just going to prison"
                        stop music
                        jump teprison

            "Respeeectt man": #good ending
                k "respect"
                narrater "you dap him up"
                narrater "he turn towards the judge and the others"
                hide court3
                hide zlink right
                hide dryleft
                show teeguy left
                l "you know the constitutions 31st article???"
                l "{color=#38465c}Asmeniui, kuris įtariamas padaręs nusikaltimą, ir kaltinamajam nuo jų sulaikymo arba pirmosios apklausos momento garantuojama teisė į gynybą, taip pat ir teisė turėti advokatą.{/color}"
                t "what the fuck is he talking about?"
                ob "idk trump, i think hes speaking lithuanian"
                t "lithuania?? is that somewhere in russia??"
                l "yweah"
                l "In any case, cornerning the matter about the murder..."
                l "under the constitutions 3rd article..."
                l "{color=#38465c}Tauta ir kiekvienas pilietis turi teisę priešintis bet kam, kas prievarta kėsinasi įvalstybės nepriklausomybę, teritorijos vientisumą, konstitucinę santvarką.{/color}"
                l "ahem.."
                l "It is hereby submitted that the individual identified as Karol was engaged in actions directly in furtherance of his fiduciary and statutory obligations to his sovereign nation." 
                play audio applause2
                l "Said obligations necessitated the Subject to initiate a decisive tactical intervention against a specific quadrupedal adversary."
                j "okay okay, you can stop"
                l "Specifically, the adversary in question was an equine biological entity, legally classified under the species Equus caballus."
                j "shut the fuck up"
                l "Furthermore, it has been established through the factual record that this aforementioned equine entity was operating as an agent, symbol, or affiliated With Nazi's"
                play audio applause1
                l "thank you, thank you"
                j "with the shown evidence, of the eques cabbales being affiliated with nazis and with karol mijas having obligations to defend his motherland, it's all clear to me now"
                j "i hate to admid it.. "
                play audio hammer1
                j "the defandant is found not guilty.."
                play audio disappointment
                un "WE HATE THIS MAN!"
                jump free_ending
        
        

    #call the ambulance, maybe they'll take him or something



    label free_ending:
        scene courthall1
        narrater "you walk out of the court, filled with determination"
        narrater "you are free"
        "FINIHHHH"##_______________________________________________________________TO FINIJHHHHHHHH
        jump end

    label lospital:
        scene hospit 1
        k "what the hell"
        k " icant feel my legs"
        show hosipit armsnlegs with dissolve
        k "i cant feel my arms erithe"
        play audio door
        scene hospit 2
        show hosipit armsnlegs
        narrater "suddenly door opens up"
        play audio appear
        hide hosipit armsnlegs
        screen hopitalhand:
            fixed:
                image "hosipit armsnlegs.png"
        show screen hopitalhand
        show dad with dissolve:
            zoom 0.5
            yalign 0.5
            xalign 0.5
        show hosipit armsnlegs

        d "hello son."
        d "i just came to say i am very disappointent in you"
        d "that is all. goodbye"

        menu:
            "noo please":
                k "noo dad.. please"
                k "dont leave me i need you dadi still need you"
            "defy your father now":
                k "father.."
                hide screen hopitalhand
                hide hosipit armsnlegs
                show hosipit armsnlegs midfinger with dissolve
                k "Fuck you!!!!"


        play audio door
        hide dad with dissolve
        scene hospit 1
        show hosipit armsnlegs
        "he left"

        narrater "suddenly door opens up"
        play audio appear
        show screen hopitalhand
        hide hosipit armsnlegs
        show doktor neutral with dissolve
        show hosipit armsnlegs
        hide screen hopitalhand
        un "hey hey"
        doc "i ur dctor man"
        doc "i got bad news man..."
        menu:
            "nooo what do you mean??":
                k "ooh no man what happened to me doctor??"
        show doktor happy

        doc "you will never walk again!"
        menu:
            "acceptance":
                k "man that sucks.."
            "defiance":
                hide screen hopitalhand
                hide hosipit armsnlegs
                show hosipit armsnlegs midfinger with dissolve
                k "uck you!!!!"

                hide hosipit armsnlegs
                show doktor neutral
                show screen hopitalhand
                show hosipit armsnlegs
                doc "this is very mean"
                doc "no wonder your father doesnt love you"
        hide screen hopitalhand
        show theend
        $ renpy.pause(1,hard=True)
        show end hospital
        window hide
        pause
        jump end
        
    label teprison:
        play audio jailer
        scene pison
        if howmanytimes > 0:
            "oh hey look, we're back here from that controller fail"
            $ karolTalkingMad = True
            k "FUCK SHIT NOT AGAIMN"
            $ karolTalkingMad = False
        else:
            "oh no u got sent to prisonas"
            k "ash shit"
        play audio openes
        show repledgemon with moveintop
        un "hello.. karol mijas"
        rep "its me, repledge"
        rep "i come from the extremely cool story map from the gmod workshop"
        rep "i have gained consciounce and managed to materialize myself into the world of the living"
        rep "as you are my dear creator, i am here to help you out"
        show theend
        $ renpy.pause(1,hard=True)
        show end pris
        "well this is the prison ending idk what should happen now BORIS"

    label end:
        scene black
        narrater "It leaves you stunned"
        #narrater "End of PART 1, to be continued"
        narrater "End of GAME, never to be continued"