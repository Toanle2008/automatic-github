import pyautogui as auto
from time import sleep

auto.prompt(text="", title="Start Breeding Tool")

Path = {
    "breedMountain" : r"Img\dragonCity\breedMountain.png",
    "reBreed" : r"Img\dragonCity\reBreed.png",
    "breed" : r"Img\dragonCity\breed.png",
    "Xdelete_red" : r"Img\dragonCity\Xdelete_red.png",
    "hatchMountain" : r"Img\dragonCity\hatchMountain.png",  
    "hatchMountain" : r"Img\iconVsCode\user-icon.png",  
    "hatchMountain" : r"Img\dragonCity\hatchMountain.png",  
}
# print(auto.locateCenterOnScreen(r"Img\iconVsCode\user-icon.png", confidence=0.8))
def find(objParam):
    try:
        objectPos = auto.locateCenterOnScreen(Path[objParam], confidence=0.8)
        return objectPos
    except auto.ImageNotFoundException:
        print("{objParam} not found")
        sleep(2)
        find(objParam)
print(find("hatchMountain")) 