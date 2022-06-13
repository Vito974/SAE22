#import serial
#s = serial.Serial('/dev/ttyACM0',9600)
#res = s.read()
#print(res)
#import des bibliothèques
from struct import pack
import scipy
from scipy import io
import serial.tools.list_ports
import numpy as np

12

#Déclarations des variables
RATE = 8000
data = np.array([], dtype=np.uint8)
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

serialInst.baudrate = 115200
serialInst.port = "/dev/ttyACM0" #choix du port USB de la carte arduino
serialInst.open()
for i in range(700000):
if serialInst.in_waiting :
packet = serialInst.readline()
#packet = packet.decode("utf8")
numbers = [int(temp)for temp in packet.split() if temp.isdigit()]

if numbers == [] or numbers[0]>255:
pass
else :
numbers[0] = numbers[0]
n = numbers[0]
n = (((n - 0) * (1 - (-1))) / (255 - 0)) + (-1)
data = np.append(data, n)

scipy.io.wavfile.write('disco.wav',RATE, data) #Ecriture dans un fichier au format wav
print(data)
