from Tool2 import *
from time import sleep
import pyautogui as auto

sleep(2)
a = auto.position()
print(a)

auto.PAUSE = 0.4
position = {
    "reBreed":     (937, 686),
    "breed":       (670, 596),
    "xDeleteRed":  (1290, 77),
    "reGrow":      (681, 694),
    "reGrow2":     (809, 692),
    "sellEgg":     (943, 552),
    "sellEgg2":    (783, 559),
    "sellDragon":  (1170, 711),
    "sellDragon2": (778, 543),
    "goldStore":   (872, 728),
    "buyTeeraEgg": (204, 605),
    "placeEgg":    (750, 547),
    
    "breedMountain" :   (946, 510),
    "breedMountainTree" :   (467, 305),  
    "hatchEgg1" :   (941, 689),
    "hatchEgg2" :   (803, 689),
    "hatchEgg3" :   (688, 688),
    "hatchEgg4" :   (568, 701),
    "hatchEgg5" :   (448, 701),
    "hatchMountain" :   (696, 399),
    "placeTeeraHabitat":    (686, 356),
    "battleQuest" :   (204, 703),
    "goToBattleQuest" :   (682, 705),
    "goToBattleQuest2" :   (688, 593),
    "autoBattle" :   (59, 156),
    "xLvUpRank" :  (1063, 128),
    
    # "teeraHabitat" : ,
    # "teeraDragonInHabitat" : ,
    # "getEgg" : ,
    # "reGrow" : ,

}

def combo(listAction):
    for action in listAction:
        x = action
        if type(action) is str:
            x = position[action]
            
        auto.moveTo(x, duration=0.5)   
        auto.click()
def ac(pos):
    auto.moveTo(pos, duration=0.5)
    auto.click()

def collectFood(pause,limitFoodHouse):
    auto.PAUSE = pause
    foodIconPos = True
    limit = 1
    while foodIconPos:
        action("foodIcon", 0.5)
        limit += 1
        if limit > limitFoodHouse:
            break    
        foodIconPos = find("foodIcon", 0)
        
    auto.PAUSE = 0.75
    reGrow(limitFoodHouse)   
   
def reGrow(limitFoodHouse):
    for _ in range(50):
        ac((664,405))
        combo(["reGrow"])
        sleep(30)
        collectFood(0,limitFoodHouse)    
    
class drtools:
    
    def br():
        # sleep(100)
        # combo(["breedMoutain"])
        # for _ in range(1000):
        #     combo(["breedMountain", "reBreed", "breed", "xDeleteRed",
        #         ])
        #     sleep(6)
        #     combo(["hatchMountain", "hatchEgg3",
        #         "sellEgg", "sellEgg2"])
        #     # combo(["hatchMountain", "hatchEgg1",
        #     #     "placeEgg", "placeTeeraHabitat"])
            # ac((859, 231))
        auto.PAUSE = 0.65
        for _ in range(1000):
        
            combo(["breedMountain", "breedMountainTree",
                "breedMountain","reBreed", "breed", "xDeleteRed",
                "breedMountainTree", "reBreed", "breed", "xDeleteRed",
                "hatchMountain", "hatchEgg3",
                "sellEgg", "sellEgg2", "hatchEgg2", "sellEgg", "sellEgg2",
                ])
        
    def ha():
        combo(["hatchMountain", "hatchEgg1", "placeEgg", "placeTeeraHabitat"])
        ac((859, 231))
        # combo(["hatchEgg1", "placeEgg", "placeTeeraHabitat"])
        # ac((859, 231))
        # ac((859, 231))
        # combo([(566, 693), "goldStore", "buyTeeraEgg"])
        # combo([(440, 693), "goldStore", "buyTeeraEgg"])
        # combo([(934, 693), "goldStore", "buyTeeraEgg"])
        # combo(["hatchEgg3", "goldStore", "buyTeeraEgg"])
        combo(["hatchEgg4", "goldStore", "buyTeeraEgg"])
        # combo(["hatchEgg2", "goldStore", "buyTeeraEgg"])
        ac((516, 564))
        # combo([(683, 687), "sellDragon", "sellDragon2"])
        combo([(683, 687), "sellDragon", "sellDragon2"])
        sleep(6)
    def food(limitFoodHouse):
        reGrow(limitFoodHouse)
    
    def brha():
        combo(["breedMountain"])
        for _ in range(200):
            combo(["breedMountainTree", "breedMountainTree", "reBreed", "breed", "xDeleteRed",])
            
            combo(["breedMountain", "reBreed", "breed", "xDeleteRed",
                ])
            
            ac((483, 542))
            combo(["hatchEgg4", "sellDragon", "sellDragon2"])
            combo(["hatchEgg4", "sellDragon", "sellDragon2"])
            # ac((914, 221))
            combo(["hatchMountain", "hatchEgg3", "placeEgg", "placeTeeraHabitat"])
            ac((914, 221))
            combo(["hatchEgg2", "placeEgg", "placeTeeraHabitat"])
            ac((1123, 333))
            
    def quests():
        combo(["battleQuest", "goToBattleQuest", "goToBattleQuest2"])
        sleep(4)
        ac(position["autoBattle"])
        sleep(23)
        ac(position["xLvUpRank"])
limitFoodHouse = 9
# for i in range(100):     
# #     drtools.food(limitFoodHouse)   
# drtools.br()
#     # drtools.ha()
#     drtools.brha()
        # drtools.quests()  
drtools.brha()
