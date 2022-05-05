#PSL_Play
from PSL import PSL
import time

#--- INIT ---#

main = PSL('/home/pi/credentials.csv', debugStatus = 3)
main.eject()
main.load()

DC = True
currentUID = None
#END OF INIT

main.debugMessage(0,"PASSED INIT",)

#--- Main ---#
while True:
    UID = main.read()

    #Find the URI associated with the returned UID given by main.read().
    #If the UID is equal to None then the URI also is equal to none.
    if UID == None:
        URI = None
        main.debugMessage(2,'UID equals none')
    elif UID != None:
        URI = main.database[UID]
        main.debugMessage(2,'UID has data')

    #If there is UID returned by main.read() then check if it is the disk
    #that disk is the one that was previously inserted. If that is the case
    #then resume playback. Else, play the new content.
    if UID != None:
        if UID != CurrentUID:
            main.play(URI)
            main.debugMessage(2,f'Playing:{URI}')
            DC = False
        elif DC == True:
            if UID == CurrentUID:
                main.play(None)
                main.debugMessage(2,'Resume Playing:')
                DC = False
    
    #If there is no UID returned by main.read() then pause playback.
    elif UID == None:
        if DC != True:
            if UID != CurrentUID:
                main.pause()
                main.debugMessage(2, 'UID = None: Pausing Playback:')
                DC = True

    if UID != None:
        CurrentUID = UID

    time.sleep(2)


