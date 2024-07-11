from pynput.keyboard import Listener
import pyautogui as auto
from time import sleep

def anonymous(key):
    if str(key) == "Key.esc":
        raise SystemExit(0)
with Listener(on_press=anonymous) as user:
    user.join()

Path = {
    "breedMountain" : r"Img\dragonCity\breedMountain.png",
    "reBreed" : r"Img\dragonCity\reBreed.png",
    "breed" : r"Img\dragonCity\breed.png",
    "xDeleteRedBreed" : r"Img\dragonCity\xDeleteRedBreed.png",
    "foodIcon" : r"Img\dragonCity\foodIcon.png",  
    "foodHouse" : r"Img\dragonCity\foodHouse.png",  
    "reGrow" : r"Img\dragonCity\reGrow.png",
    "collectBreed" : r"Img\dragonCity\collectBreed.png",
    "hatchEgg" : r"Img\dragonCity\hatchEgg.png",
    "sellEgg" : r"Img\dragonCity\sellEgg.png",
    "sellDragon" : r"Img\dragonCity\sellDragon.png",
    "hatchMountain" : r"Img\dragonCity\hatchMountain.png",
    "breedIcon" : r"Img\dragonCity\breedIcon.png",
    
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
    def breedingTool(numOfLoops):
        if numOfLoops == 0:
            auto.prompt(text="Enter to start...", title="Start Breeding Tool")
        sleep(2)
        breedMountainPos = find("breedMountain")
        auto.moveTo(breedMountainPos, duration=0.5)
        auto.click(breedMountainPos)
        sleep(1)
        reBreedPos = find("reBreed")
        auto.moveTo(reBreedPos, duration=0.5)
        auto.click(reBreedPos)
        sleep(1)
        breedPos = find("breed")
        auto.moveTo(breedPos, duration=0.5)
        auto.click(breedPos)
        sleep(2)
        xDeleteRedBreedPos = find("xDeleteRedBreed")
        auto.moveTo(xDeleteRedBreedPos, duration=0.5)
        auto.click(xDeleteRedBreedPos)
        sleep(1)
        hatchMountainPos = find("hatchMountain")
        auto.moveTo(hatchMountainPos, duration=0.5)
        auto.click(hatchMountainPos)
        sleep(1)
        hatchEggPos = find("hatchEgg")
        auto.moveTo(hatchEggPos, duration=0.5)
        auto.click(hatchEggPos)
        sleep(1)
        sellDragonPos = find("sellDragon")
        auto.moveTo(sellDragonPos, duration=0.5)
        auto.click(sellDragonPos)
        sleep(1)
        sellEggPos = find("sellEgg")
        auto.moveTo(sellEggPos, duration=0.5)
        auto.click(sellEggPos)
        sleep(5)
        breedIconPos = find("breedIcon")
        auto.moveTo(breedIconPos, duration=0.5)
        auto.click(breedIconPos)
        sleep(5)
        
        return    
        
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
              
    def hatchEggTool(numOfLoops):
        pass     
for numOfLoops in range(50): 
    pass
    # dragonTools.collectFoodTool(numOfLoops)yfy
    # dragonTools.breedingTool(numOfLoops)
    #