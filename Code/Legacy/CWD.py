#Jacob France
import serial
import time
import pickle

#setup--V--V

#Defines COM Number for serial communications.
ComNum = '12'
ser = serial.Serial('COM'+ComNum, 9600)
#To ensure time for COM to setup.
time.sleep(2)
#Dirctory of PKL
Direc = 'obj/data.pkl'
#Global Varibles
UID = 0
Data = {}

#end-of-setup--^--^
#definitions--V--V

def nfcRead(sec, sep):
    for i in range(sec):
        b = ser.readline()
        string_n = b.decode()
        #string_n = string_n.rstrip()
        if sep in string_n:
            new = string_n.split(sep)
            return(new[1])
            break
        time.sleep(0.2)
    ser.close()

def loadDict(Fname):
    with open(Fname, 'rb') as f:
        return pickle.load(f)

def saveDict(Dicton, Fname):
    with open(Fname, 'wb') as f:
        pickle.dump(Dicton, f, pickle.HIGHEST_PROTOCOL)

#end-of-definitions--^--^
#main--V--V

URI = input('Spotify URI:')
print('Input card now---')

Data = dict(loadDict(Direc))

UID = nfcRead(100, '!')

Data[UID]=URI

saveDict(Data, Direc)

print('Done')
print('URI:', URI)
print('UID:', UID)
