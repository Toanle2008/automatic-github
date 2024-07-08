import pyautogui
from time import sleep

settingBtn = pyautogui.locateOnScreen("edit.png")
sleep(0)
pyautogui.click(settingBtn) 
