#PSL_Play
import PSL
import time
#Fix the split import so we don't have to add PSL after PSL.

#--- INIT ---#
main = PSL.PSL(credentialsDirectory = None, debugStatus = 3)
main.eject()
main.load()

currentUID = None
#END OF INIT

#--- Main ---#
while True:
    UID = main.read()

    if UID == None:
        URI = None
        main.debugMessage(2,'UID equals none')
    elif UID != None:
        URI = main.database[UID]
        main.debugMessage(2,'UID has data')

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
    elif UID == None:
        if DC != True:
            if UID != CurrentUID:
                main.pause()
                print('UID = None: Pausing Playback:')
                DC = True

    if UID != None:
        CurrentUID = UID

    time.sleep(2)


