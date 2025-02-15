import djitellopy as tello
import keyPressModule as kp
import time
kp.init()
me=tello.Tello()
me.connect()
print(me.get_battery())
def getKeyboardInput():
    lr , fb , ud , yv = 0,0,0,0
    speed=50 #adjust the speed with which your drone should move
    if kp.getKey("LEFT"): lr = -speed #use left arrow key to move left
    elif kp.getKey("RIGHT"): lr = speed #use right arrow key to move right
    
    if kp.getKey("UP"): ud = speed #use up arrow key to move upwards
    elif kp.getKey("DOWN"): ud = -speed #use down arrow key to move downwards
    
    if kp.getKey("w"): fb = speed #use w key to move forward
    elif kp.getKey("s"): fb = -speed #use s key to move backward
    
    if kp.getKey("a"): yv = speed #use a key to rotate left (anticlockwie)
    elif kp.getKey("d"): yv = -speed #use d key to rotate right (clockwise)
    
    if kp.getKey("e"): me.takeoff() #use e key to take off
    if kp.getKey("q"): me.land() #use q key to land
    
    return [lr, fb, ud, yv]

from time import sleep
while True:
    
    values = getKeyboardInput()
    me.send_rc_control(values[0],values[1],values[2],values[3])
    sleep(0.05)
