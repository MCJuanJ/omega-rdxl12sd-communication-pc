'''
Created on 9 ago. 2022
This project communicates with the OMEGA DDLXL12SD datalogger and creates a file called 
temperatures.csv where it stores the sensor readings. 
@author: Profesor Dr. Juan José Muñoz César
'''
import serial
import time
import csv


#diccionario de funciones para extraer el valor de cada canal
def canal1():
    global C1
    print ('canal 1 = ', x[12:15])
    C1 = str(x[12:15], 'UTF-8') 
    
def canal2():
    global C2
    print ('canal 2 = ', x[12:15])
    C2 = str(x[12:15], 'UTF-8')

def canal3():
    global C3
    print ('canal 3 = ', x[12:15])
    C3 = str(x[12:15], 'UTF-8')

def canal4():
    global C4
    print ('canal 4 = ', x[12:15])
    C4 = str(x[12:15], 'UTF-8')

def canal5():
    global C5
    print ('canal 5 = ', x[12:15])
    C5 = str(x[12:15], 'UTF-8')

def canal6():
    global C6
    print ('canal 6 = ', x[12:15])
    C6 = str(x[12:15], 'UTF-8')

def canal7():
    global C7
    print ('canal 7 = ', x[12:15])
    C7 = str(x[12:15], 'UTF-8')
    
def canal8():
    global C8
    print ('canal 8 = ', x[12:15])
    C8 = str(x[12:15], 'UTF-8')

def canal9():
    global C9
    print ('canal 9 = ', x[12:15])
    C9 = str(x[12:15], 'UTF-8')

def canal10():
    global C10
    print ('canal 10 = ', x[12:15])
    C10 = str(x[12:15], 'UTF-8')

def canal11():
    global C11
    print ('canal 11 = ', x[12:15])
    C11 = str(x[12:15], 'UTF-8')

def canal12():
    global C12
    print ('canal 12 = ', x[12:15])
    C12 = str(x[12:15], 'UTF-8')

def error():
    print('error')

switch_canales = {
    49: canal1,
    50: canal2,
    51: canal3,
    52: canal4,
    53: canal5,
    54: canal6,
    55: canal7,
    56: canal8,
    57: canal9,
    65: canal10,
    66: canal11,
    67: canal12    
}

ser = serial.Serial(
        # Serial Port to read the data from
        port='/dev/ttyUSB0',
 
        #Rate at which the information is shared to the communication channel
        baudrate = 9600,
   
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
 
       # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
     
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
 
        # Number of serial commands to accept before timing out
        #timeout=1
)

count=0
# Pause the program for 1 second to avoid overworking the serial port

with open('temperaturas.csv', 'w', newline='') as csvfile:
    fieldnames = ['Temp1','Temp2','Temp3','Temp4','Temp5','Temp6','Temp7','Temp8','Temp9','Temp10','Temp11','Temp12']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    #csvfile.close()
        
while 1:        
    #x=ser.readline(16)
    x=ser.read_until(b'\r')
    canal = x[2]
    #tomar la función asociada a la variable e  invocarla
    switch_canales.get(canal, error)()
    count+=1
    if(count==12):
        # T1=canal1(),T2=canal2(),T3=canal3(),T4=canal4(),T5=canal5(),T6=canal6(),T7=canal7(),T8=canal8(),T9=canal9(),T10=canal10(),T11=canal11(),T12=canal12()
        print("Local time:", time.time())    
        print (C8)
        with open('temperaturas.csv', 'a', newline='') as csvfile:
            fieldnames = ['Temp1','Temp2','Temp3','Temp4','Temp5','Temp6','Temp7','Temp8','Temp9','Temp10','Temp11','Temp12']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Temp1':C1,'Temp2':C2,'Temp3':C3,'Temp4':C4, 'Temp5':C5,'Temp6':C6,'Temp7':C7,'Temp8':C8,'Temp9':C9,'Temp10':C10,'Temp11':C11,'Temp12':C12}) 
            count=0
if __name__ == '__main__':
    pass