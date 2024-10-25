import pyautogui as auto
import pygame
import pygame_menu
from time import sleep
import pygame_menu.locals
import sys

Path = {
    "breedMountain" : r"Img\dragonCity\breedMountain.png",
    "breedMountainTree" : r"Img\dragonCity\breedMountainTree.png",
    "foodIcon" : r"Img\dragonCity\foodIcon.png",  
    "foodHouse" : r"Img\dragonCity\foodHouse.png",  
    "hatchEgg" : r"Img\dragonCity\hatchEgg.png",
    "hatchMountain" : r"Img\dragonCity\hatchMountain.png",
    "placeTeeraHabitat" : r"Img\dragonCity\placeTeeraHabitat.png",
    "teeraHabitat" : r"Img\dragonCity\teeraHabitat.png",
    "teeraDragonInHabitat" : r"Img\dragonCity\teeraDragonInHabitat.png",
    "getEgg" : r"Img\dragonCity\getEgg.png",
    "reGrow" : r"Img\dragonCity\reGrow.png",
    
}

hardPath = {
    "reBreed":     (937, 686),
    "breed":       (670, 596),
    "xDeleteRed":  (1290, 77),
    "reGrow":      (687, 700),
    "sellEgg":     (943, 552),
    "sellEgg2":    (783, 559),
    "sellDragon":  (1170, 711),
    "sellDragon2": (778, 543),
    "goldStore":   (872, 728),
    "buyTeeraEgg": (204, 605),
    "placeEgg":    (750, 547),

}

auto.PAUSE = 0.5
num = 1

def find(objParam, stack):
    global num
    try:
        objectPos = auto.locateCenterOnScreen(Path[objParam], confidence=0.7)
        return objectPos
    except auto.ImageNotFoundException:
        if stack < 4:    
            print("~ Sorry Master. I can't find {} x {} ~ ".format(objParam, num))
            num += 1
            sleep(0.5)
            find(objParam, stack+1)
        else:
            return False
        
def myPrompt(numOfLoops, myText, myTitle):
        
    global quantity
    if numOfLoops == 0:  
        quantity = auto.prompt(text = myText, title = myTitle)
        # sleep(1)
        # auto.hotkey("alt", "tab")
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
        decide = (quantity == "2")
        if decide:  
            bMountain = action("breedMountain", 0.5)
            shortAction("reBreed", 0.5)
            shortAction("breed", 0.5)
            shortAction("xDeleteRed", 0.5)
        sleep(1)
        action("hatchMountain", 0.5)     
        action("hatchEgg", 0.5)
        shortAction("sellEgg", 0.5)
        shortAction("sellEgg2", 0.5)
        if decide:
            action("hatchEgg", 0.5)
            shortAction("sellEgg", 0.5)
            shortAction("sellEgg2", 0.5)
        sleep(1)
        againAction(bMTreeAgain, 0.5)
        if decide:
            againAction(bMountain, 0.5)
            
        return    
        
    def collectFoodTool(numOfLoops, myText, myTitle):
        myPrompt(numOfLoops, myText, myTitle)
        action("foodHouse", 0.5)
        shortAction("reGrow", 0.5)
        sleep(31)
                
        def collectFood(pause):
            auto.PAUSE = pause
            foodIconPos = True
            
            while foodIconPos:
                action("foodIcon", 0.5)    
                foodIconPos = find("foodIcon", 0)
                
        collectFood(0)    
        auto.PAUSE = 1
    
        for _ in range(50):
            if find("reGrow", 0):
                shortAction("reGrow", 0.5)
                sleep(29)
                collectFood(0)    
            else:
                break
        auto.PAUSE = 1    
        return
              
    def hatchEggTool(numOfLoops, myText, myTitle):
        myPrompt(numOfLoops, myText, myTitle)
        hMoutainAgain = False
        for _ in range(int(quantity)):
            if hMoutainAgain:
                againAction(hMoutainAgain, 0.5)
                action("hatchEgg", 0.5)
                shortAction("placeEgg", 0.5)
                againAction(ptHabitatAgain, 0.5)
            else:
                hMoutainAgain = action("hatchMountain", 0.5)    
                action("hatchEgg", 0.5)
                shortAction("placeEgg", 0.5)
                ptHabitatAgain = action("placeTeeraHabitat", 0.5)
                
        againAction(hMoutainAgain, 0.5)
        
        for _ in range(int(quantity)):
            action("getEgg", 0.5)
            shortAction("goldStore", 0.5)
            shortAction("buyTeeraEgg", 0.5)
            
        againAction(ptHabitatAgain, 0.5)
        
        for _ in range(int(quantity)):
            action("teeraDragonInHabitat", 0.5)
            shortAction("sellDragon", 0.5)
            shortAction("sellDragon2", 0.5)
        sleep(6)    
    def breedHatchTool(numOfLoops, myText, myTitle):
        myPrompt(numOfLoops, myText, myTitle)
        action("breedMountainTree", 0.5)
        shortAction("reBreed", 0.5)
        shortAction("breed", 0.5)
        shortAction("xDeleteRed", 0.5)
        decide = (quantity == "2")
        if decide:
            action("breedMountain", 0.5)
            shortAction("reBreed", 0.5)
            shortAction("breed", 0.5)
            shortAction("xDeleteRed", 0.5)
        action("hatchMountain", 0.5)     
        action("hatchEgg", 0.5)
        shortAction("placeEgg", 0.5)
        action("placeTeeraHabitat", 0.5)
        action("teeraDragonInHabitat", 0.5)
        shortAction("sellDragon", 0.5)
        shortAction("sellDragon2", 0.5)
        if decide:
            action("hatchMountain", 0.5)     
            action("hatchEgg", 0.5)
            shortAction("placeEgg", 0.5)
            action("placeTeeraHabitat", 0.5)
            action("teeraDragonInHabitat", 0.5)
            shortAction("sellDragon", 0.5)
            shortAction("sellDragon2", 0.5)
            
        action("breedMountainTree", 0.5)
        if decide:
            action("breedMountain", 0.5)    
            
        sleep(2)        
        return

def run(tool):
        
    match tool:
        case 1:
            for numOfLoops in range(50):
                dragonTools.collectFoodTool(numOfLoops, "Enter to start...", "COLLECT FOOD TOOL")
        case 2:
            for numOfLoops in range(50):
                dragonTools.breedingTool(numOfLoops, "Enter the num of Eggs to start...", "BREEDING TOOL")
        case 3:
            for numOfLoops in range(50):
                dragonTools.hatchEggTool(numOfLoops, "Enter the num of Eggs to start...", "HATCHING TOOL")    
        case 4:
            for numOfLoops in range(50):
                dragonTools.breedHatchTool(numOfLoops, "Enter the num of Eggs to start...", "BREEDING AND HATCHING TOOL")  
     

def userSelec(self, tool):
    global running
    running = False
    pygame.quit()
    run(tool)

pygame.init()  
pygame.display.set_caption("Dragon City Tools - Created by Toan")
UiTool = pygame.display.set_mode((700, 500))

menu = pygame_menu.Menu("Tools", 500, 400, theme=pygame_menu.themes.THEME_DARK)
menu.add.dropselect("SELEC TOOlS: ", [("collectFood", 1), 
        ("breeding", 2), ("hatching", 3), ("breed&hatch", 4)], onreturn=userSelec, placeholder="tools...        ")
menu.add.label("")
menu.add.label("Using Up, Down Arrow and Enter",)

running = True
menu.mainloop(UiTool)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        
    pygame.display.flip()
pygame.quit()