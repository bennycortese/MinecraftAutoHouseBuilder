import pydirectinput
import time

time.sleep(5)

screenWidth, screenHeight = pydirectinput.size()

def one_wall(length, height):
    InverseMetersPerSecond = 0.23164234422 # 2 blocks
    OneBlock = InverseMetersPerSecond/2
    OneJump = OneBlock/2
    for i in range(0,length):

        for i in range(0,height):
            time.sleep(OneBlock)
            pydirectinput.press('space')
            time.sleep(OneJump)
            pydirectinput.click(button='right')
        time.sleep(InverseMetersPerSecond)
        pydirectinput.keyDown('w')
        time.sleep(InverseMetersPerSecond)
        pydirectinput.keyUp('w')
        time.sleep(InverseMetersPerSecond)
        pydirectinput.keyDown('s')
        time.sleep(InverseMetersPerSecond)
        pydirectinput.keyUp('s')
        time.sleep(InverseMetersPerSecond)


one_wall(10,3)
one_wall(10,3)



