import pynput
import pyautogui as auto
from time import sleep

Path = {
    "breedMountain" : r"Img\dragonCity\breedMountain.png",
    "reBreed" : r"Img\dragonCity\reBreed.png",
    "breed" : r"Img\dragonCity\breed.png",
    "xDeleteRed" : r"Img\dragonCity\xdeleteRed.png",
    "foodIcon" : r"Img\dragonCity\foodIcon.png",  
    "foodHouse" : r"Img\dragonCity\foodHouse.png",  
    "reGrow" : r"Img\dragonCity\reGrow.png",
    
}

def find(objParam):
    
    try:
        objectPos = auto.locateCenterOnScreen(Path[objParam], confidence=0.7)
        return objectPos
    except auto.ImageNotFoundException:
        print("{} img not found".format(objParam))
        sleep(2)
        find(objParam)
        
class dragonTools:
    def breedingTool():
        # auto.prompt(text="", title="Start Breeding Tool")
        sleep(1)

        # print(auto.locateCenterOnScreen(r"Img\iconVsCode\user-icon.png", confidence=0.8))
        # print(find("reBreed")) 
    def collectFoodTool(numOfLoops):
        global quantity
        if numOfLoops == 0:  
            quantity = int(auto.prompt(text="enter the num of foodHouse", title="Start collectFoodTool Tool"))
        sleep(2)
        foodHousePos = find("foodHouse")
        auto.moveTo(foodHousePos, duration=0.5)
        sleep(1)
        auto.click(foodHousePos)
        sleep(1)
        reGrowPos = find("reGrow")
        auto.moveTo(reGrowPos, duration=0.5)
        sleep(1)
        auto.click(reGrowPos)
        sleep(30)
        for _ in range(quantity):
            foodIconPos = find("foodIcon")
            auto.moveTo(foodIconPos, duration=0.25)
            auto.click(foodIconPos)  
            sleep(0.25)
                
        return
         
for numOfLoops in range(50): 
    pass
    dragonTools.collectFoodTool(numOfLoops)
    # dragonTools.breedingTool(numOfLoops)