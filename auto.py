import pyautogui as auto
from time import sleep

message = open("chatMessage.INP", "r")
auto.prompt(text="",title="toanle")

messenger_icon = r"C:\Users\wibun\OneDrive\Desktop\code\Img\messenger.png"
ny_icon = r"C:\Users\wibun\OneDrive\Desktop\code\Img\ny.png"
chat_icon = r"C:\Users\wibun\OneDrive\Desktop\code\Img\chatMessage.png"
send_icon = r"C:\Users\wibun\OneDrive\Desktop\code\Img\sendIcon.png"

messenger = auto.locateCenterOnScreen(messenger_icon, confidence=0.9)
auto.moveTo(messenger, duration=1)
auto.doubleClick(messenger)
sleep(1)
ny = auto.locateCenterOnScreen(ny_icon, confidence=0.9)
auto.moveTo(ny, duration=1)
auto.click(ny)
sleep(1.5)
chat = auto.locateCenterOnScreen(chat_icon, confidence=0.9)
auto.moveTo(chat, duration=1)
auto.click(chat)
sleep(1)
auto.write("{}".format(message.readline()))
sleep(1)
send = auto.locateCenterOnScreen(send_icon, confidence=0.9)
auto.moveTo(send, duration=1)
auto.click(send)