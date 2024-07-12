# from pynput.keyboard import Listener
import pyautogui as auto
from time import sleep

# def anonymous(key):
#     if str(key) == "Key.esc":
#         raise SystemExit(0)
    
# with Listener(on_press=anonymous) as user:
#     user.join() 
Path = {
    "breedMountain" : r"Img\dragonCity\breedMountain.png",
    "breedMountainTree" : r"Img\dragonCity\breedMountainTree.png",
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
    "collectBreed" : r"Img\dragonCity\collectBreed.png",
    "settingBtn" : r"Img\iconVsCode\settingBtn.png",
    "xDeleteRed" : r"Img\dragonCity\xDeleteRed.png",
    "teeraHabitat" : r"Img\dragonCity\teeraHabitat.png",
    "teeraDragonInHabitat" : r"Img\dragonCity\teeraDragonInHabitat.png",
    "placeEgg" : r"Img\dragonCity\placeEgg.png",
    "getEgg" : r"Img\dragonCity\getEgg.png",
    "goldStore" : r"Img\dragonCity\goldStore.png",
    "teeraDragon" : r"Img\dragonCity\teeraDragon.png",
    "buyTeeraEgg" : r"Img\dragonCity\buyTeeraEgg.png",
    
}

auto.PAUSE = 1

def find(objParam, stack):
    try:
        objectPos = auto.locateCenterOnScreen(Path[objParam], confidence=0.7)
        return objectPos
    except auto.ImageNotFoundException:
        if stack < 4:    
            print("{} img not found".format(objParam))
            sleep(0.5)
            find(objParam, stack+1)
        else:
            return False
        
def myPrompt(numOfLoops, myText, myTitle):
    global quantity
    if numOfLoops == 0:  
        quantity = auto.prompt(text = myText, title = myTitle)
    sleep(2)        
    
def action(object, duration):
    objectPos = find("{}".format(object), 0)
    auto.moveTo(objectPos, duration=duration)
    auto.click()
    
class dragonTools:
    def breedingTool(numOfLoops, myText, myTitle):
        myPrompt(numOfLoops, myText, myTitle)
        action("breedMountainTree", 0.5)
        action("reBreed", 0.5)
        action("breed", 0.5)
        action("xDeleteRed", 0.5)
        action("hatchMountain", 0.5)     
        action("hatchEgg", 0.5)
        action("sellDragon", 0.5)
        action("sellEgg", 0.5)
        sleep(1)
        action("breedMountainTree", 0.5)
      
        return    
        
    def collectFoodTool(numOfLoops, myText, myTitle):
        myPrompt(numOfLoops, myText, myTitle)
        action("foodHouse", 0.5)
        action("reGrow", 0.5)
        sleep(30)
        auto.PAUSE = 0
        foodIconPos = True
        
        while foodIconPos:
            action("foodIcon", 0.5)    
            foodIconPos = find("foodIcon", 0)
            
        auto.PAUSE = 1
        return
              
    def hatchEggTool(numOfLoops, myText, myTitle):
        myPrompt(numOfLoops, myText, myTitle)
        for _ in range(int(quantity)):
            action("hatchMountain", 0.5)
            action("hatchEgg", 0.5)
            action("placeEgg", 0.5)
            action("teeraHabitat", 0.5)
            action("teeraDragonInHabitat", 0.5)
            action("sellEgg", 0.5)
            action("sellEgg", 0.5)
        for _ in range(int(quantity)):
            action("hatchMountain", 0.5)
            action("getEgg", 0.5)
            action("goldStore", 0.5)
            action("teeraDragon", 0.5)
            action("buyTeeraEgg", 0.5)
        sleep(12)    

    def breedHatchTool(numOfLoops, myText, myTitle):
        myPrompt(numOfLoops, myText, myTitle)
        action("breedMountainTree", 0.5)
        action("reBreed", 0.5)
        action("breed", 0.5)
        action("xDeleteRed", 0.5)
        action("hatchMountain", 0.5)     
        action("hatchEgg", 0.5)
        action("placeEgg", 0.5)
        action("teeraHabitat", 0.5)
        action("teeraDragonInHabitat", 0.5)
        action("sellEgg", 0.5)
        action("sellEgg", 0.5)
        action("breedMountainToolree", 0.5)
        sleep(3)        
        return

print(
    ''' 
    Enter 1: collectFoodTool
    Enter 2: breedingTool
    Enter 3: hatchEggTool
    Enter 4: breedHatchTool
        '''
)

def tools(choose):
    Tools = {
        "1" : dragonTools.collectFoodTool(numOfLoops, "Enter to start...", "COLLECT FOOD TOOL"),
        "2" : dragonTools.breedingTool(numOfLoops, "Enter to start...", "BREEDING TOOL"),
        "3" : dragonTools.hatchEggTool(numOfLoops, "Enter the num of Eggs to start...", "HATCHING TOOL"),
        "4" : dragonTools.breedHatchTool(numOfLoops, "Enter to start...", "BREEDING AND HATCHING TOOL"),
        }
    return Tools["{}".format(choose)]
choose = input("Enter: ")    
 
for numOfLoops in range(50):
    tools(choose)
    


    
