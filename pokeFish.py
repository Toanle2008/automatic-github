from time import sleep
import pyautogui as auto
import keyboard


sleep(2)
# a = auto.position()
# print(a)
while True: 
    if keyboard.is_pressed('q'):
        break
    auto.click((859, 525))#tap
    auto.click((680, 645))#outsight
    # auto.click((1010, 594))#buy
#     # auto.click((1010, 594))
    # auto.click((1010, 594))
# for i in range(594):
#     auto.click((1011, 317))
        
    # auto.click((726, 478))