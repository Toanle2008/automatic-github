import pyautogui as auto
from time import sleep


Path = {
    "breedMountain" : r"Img\dragonCity\breedMountain.png",
    "breedMountainTree" : r"Img\dragonCity\breedMountainTree.png",
    "foodIcon" : r"Img\dragonCity\foodIcon.png",  
    "foodHouse" : r"Img\dragonCity\foodHouse.png",  
    "collectBreed" : r"Img\dragonCity\collectBreed.png",
    "hatchEgg" : r"Img\dragonCity\hatchEgg.png",
    "hatchMountain" : r"Img\dragonCity\hatchMountain.png",
    "collectBreed" : r"Img\dragonCity\collectBreed.png",
    "teeraHabitat" : r"Img\dragonCity\teeraHabitat.png",
    "teeraDragonInHabitat" : r"Img\dragonCity\teeraDragonInHabitat.png",
    "getEgg" : r"Img\dragonCity\getEgg.png",
    
}

hardPath = {
    "reBreed" :     (937, 686),
    "breed" :       (670, 596),
    "xDeleteRed" :  (1290, 77),
    "reGrow" :      (687, 700),
    "sellEgg" :     (943, 552),
    "sellEgg2" :    (783, 559),
    "sellDragon" :  (1170, 711),
    "sellDragon2" : (778, 543),
    "goldStore" :   (872, 728),
    "buyTeeraEgg" : (204, 605),
    "placeEgg" :    (750, 547),

}
auto.PAUSE = 1

def find(objParam, stack):
    try:
        objectPos = auto.locateCenterOnScreen(Path[objParam], confidence=0.7)
        return objectPos
    except auto.ImageNotFoundException:
        if stack < 3:    
            print("{} img not found".format(objParam))
            sleep(1)
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
    return objectPos

def shortAction(object, duration):
    auto.moveTo(hardPath["{}".format(object)], duration=duration)    
    auto.click()

def againAction(position, duration):
    auto.moveTo(position, duration=duration)
    auto.click()
class dragonTools:
    def breedingTool(numOfLoops, myText, myTitle):
        myPrompt(numOfLoops, myText, myTitle)
        bMTreeAgain = action("breedMountainTree", 0.5)
        shortAction("reBreed", 0.5)
        shortAction("breed", 0.5)
        shortAction("xDeleteRed", 0.5)
        action("hatchMountain", 0.5)     
        action("hatchEgg", 0.5)
        shortAction("sellEgg", 0.5)
        shortAction("sellEgg2", 0.5)
        sleep(2)
        againAction(bMTreeAgain, 0.5)
      
        return    
        
    def collectFoodTool(numOfLoops, myText, myTitle):
        myPrompt(numOfLoops, myText, myTitle)
        action("foodHouse", 0.5)
        shortAction("reGrow", 0.5)
        sleep(31)
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
            shortAction("placeEgg", 0.5)
            action("teeraHabitat", 0.5)
            action("teeraDragonInHabitat", 0.5)
            shortAction("sellDragon", 0.5)
            shortAction("sellDragon2", 0.5)
        for _ in range(int(quantity)):
            action("hatchMountain", 0.5)
            action("getEgg", 0.5)
            shortAction("goldStore", 0.5)
            shortAction("buyTeeraEgg", 0.5)
        sleep(11)    

    def breedHatchTool(numOfLoops, myText, myTitle):
        myPrompt(numOfLoops, myText, myTitle)
        action("breedMountainTree", 0.5)
        shortAction("reBreed", 0.5)
        shortAction("breed", 0.5)
        shortAction("xDeleteRed", 0.5)
        action("hatchMountain", 0.5)     
        action("hatchEgg", 0.5)
        shortAction("placeEgg", 0.5)
        action("teeraHabitat", 0.5)
        action("teeraDragonInHabitat", 0.5)
        shortAction("sellDragon", 0.5)
        shortAction("sellDragon2", 0.5)
        action("breedMountainTree", 0.5)
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

def run():
    choose = input("Enter: ")    
    try:
        choose = int(choose)
        if not (1 <= choose <= 4):
            print("Try again...")
            run()
    except ValueError:
        print("Try again...")
        run()
    
    match choose:
        case 1:
            for numOfLoops in range(50):
                dragonTools.collectFoodTool(numOfLoops, "Enter to start...", "COLLECT FOOD TOOL")
        case 2:
            for numOfLoops in range(50):
                dragonTools.breedingTool(numOfLoops, "Enter to start...", "BREEDING TOOL")
        case 3:
            for numOfLoops in range(50):
                dragonTools.hatchEggTool(numOfLoops, "Enter the num of Eggs to start...", "HATCHING TOOL")    
        case 4:
            for numOfLoops in range(50):
                dragonTools.breedHatchTool(numOfLoops, "Enter to start...", "BREEDING AND HATCHING TOOL")  
     
run()
