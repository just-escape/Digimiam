#!usrbinenv python
import serial
import time

s = serial.Serial('devttyUSB0',115200)
s2 = serial.Serial('devttyACM0',115200)

f = open('square','r');

# Wake up grbl
print (writing on serial)
s.write(str.encode('$$n'))
time.sleep(2)   # Wait for grbl to initialize
s.flushInput()  # Flush startup text in serial input

for line in f
    target, _, cmd = line.strip().partition('') # Get the target and the command
    print (Sending  + cmd +  to  + target)
    if target==PLOTTER 
        s.write({}n.format(cmd).encode()) # Send g-code block to grbl
        grbl_out = s.readline() # Wait for grbl response with carriage return
        print('  ' + grbl_out.strip().decode())
    elif target==SERINGUE 
        s2.write({}n.format(cmd).encode())
        arduino_out = s2.readline() # Wait for arduino response with carriage return
        print('  ' + arduino_out.strip().decode())
        
# Wait here until all commands are done
input(  Press Enter to exit and disable grbl.)

# Close file and serial port
f.close()
s.close()
s2.close()
