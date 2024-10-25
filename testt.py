from time import sleep
import pyautogui as auto

auto.PAUSE = 1

def combo(listAction):
    for action in listAction:
        x = action
        # if type(action) is str:
        #     x = position[action]
            
        auto.moveTo(x, duration=0.5)   
        auto.click()
# sleep(2)
# a = auto.position()
# print(a)

for i in range(47):
    combo([(253, 207), (505, 436), (789, 445)])

