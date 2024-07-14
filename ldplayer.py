# from pynput.keyboard import Listener
import pyautogui as auto
from time import sleep
# def anonymous(key):
#     if str(key) == "Key.esc":
#         raise SystemExit(0)
#     print(key)
# with Listener(on_press=anonymous) as user:
#     user.join()

import subprocess

ldplayer = r"C:\Users\wibun\OneDrive\Desktop\LDPlayer9.lnk"
subprocess.Popen(ldplayer, shell=True, stdout=subprocess.PIPE)

Path = {
    "drCity" : r"Img\ldplayer\drCity",
    
}
def find(objParam):
    global num
    try:
        objectPos = auto.locateCenterOnScreen(Path[objParam], confidence=0.7)
        return objectPos
    except auto.ImageNotFoundException:
            sleep(1)
            find(objParam)
