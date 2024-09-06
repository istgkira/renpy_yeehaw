#Hlasy charakteru
init python:
    def clara_voice(event, **kwargs): 
        if event == "show": 
            renpy.sound.play("audio/claravoice.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end": 
            renpy.sound.stop(channel="sound", fadeout=1)
    
    def lucas_voice(event, **kwargs): 
        if event == "show": 
            renpy.sound.play("audio/lucasvoice.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end": 
            renpy.sound.stop(channel="sound", fadeout=1)

    def terry_voice(event, **kwargs): 
        if event == "show": 
            renpy.sound.play("audio/terryvoice.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end": 
            renpy.sound.stop(channel="sound", fadeout=1)

    def andrea_voice(event, **kwargs): 
        if event == "show": 
            renpy.sound.play("audio/andreavoice.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end": 
            renpy.sound.stop(channel="sound", fadeout=1)

    def sarah_voice(event, **kwargs): 
        if event == "show": 
            renpy.sound.play("audio/sarahvoice.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end": 
            renpy.sound.stop(channel="sound", fadeout=1)

    def daniel_voice(event, **kwargs): 
        if event == "show": 
            renpy.sound.play("audio/danielvoice.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end": 
            renpy.sound.stop(channel="sound", fadeout=1)

    def nela_voice(event, **kwargs): 
        if event == "show": 
            renpy.sound.play("audio/nelavoice.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end": 
            renpy.sound.stop(channel="sound", fadeout=1)

#Charakteri
define c = Character("Clara", callback=clara_voice) #50/50 clovek, hodna nebo zla
define l = Character("Lucas", callback=clara_voice, what_font="fonts/HelpMe.ttf") #sans
define t = Character("Terry") #info clovek, awkward, funny
define a = Character("Andrea") #drama club, autism, goofy
define s = Character("Sarah") #backstab, evil
define d = Character("Daniel") #fuckboy 
define n = Character("Nela") #hodna af


#Start hry
label start:
    stop music

    scene bg room

    show eileen happy

    c "fuhwfiuhweiuf huiewfh uiewhfui ehuiehfi uhewuifh uuiew fhiu ehewfuhewiuf hu"
    l "{size=+20}D I E..  D I E..  D I E.."


    return
