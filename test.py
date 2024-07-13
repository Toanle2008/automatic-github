# from pynput.keyboard import Listener
import pyautogui as auto
from time import sleep


# def anonymous(key):
#     if str(key) == "Key.esc":
#         raise SystemExit(0)
#     print(key)
    
# with Listener(on_press=anonymous) as user:
#     user.join()

sleep(3)
print(auto.position())
