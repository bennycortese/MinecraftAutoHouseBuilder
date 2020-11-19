import pydirectinput
import time

time.sleep(5)
for i in range(0,100):

    pydirectinput.mouseDown()
    time.sleep(2.0)
    pydirectinput.mouseUp()
    pydirectinput.keyDown('w')
    time.sleep(1.0)
    pydirectinput.keyUp('w')
