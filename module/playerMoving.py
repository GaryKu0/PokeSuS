
from module.var import *

def PlayerMoving(Amongus,direction,number):
    '''
    direction:方向,number:移動的距離
    '''
    if Amongus.currentmap =='town':
        wall=Amongus.detectWall(town_wall)
    elif Amongus.currentmap =='forest':
        wall=Amongus.detectWall(forest_wall)
    if wall: 
        number=0
        print("Hit Wall:",wall)
        print("Now Location:",Amongus.coordinate)
    Amongus.move(direction,number)


Town_TriggerPoint={'SHOP1':[220,500,300,580],'PokemonCenter':[395,355,475,435],'Museum':[105, 305,185,385]}   

def TriggerPoint(data,amongus):
    '''
        輸入的data是一個dict,格式為{'商店':[x1,y1,x2,y2],'商店2':[x1,y1,x2,y2]},假如Player Class的座標在其中一個商店的範圍內,則回傳商店名稱
    '''
    if (type(data)!=dict):
        print("[ERROR] 😭Trigger data is not a dict")
        return
    Square=FatAssAmongUs(amongus)
    for i in data:   
        #if Square and data[i] is overlap
        if (Square[0]<data[i][2] and Square[2]>data[i][0] and Square[1]<data[i][3] and Square[3]>data[i][1]):
            return i
        
def TriggerPointBool(data,amongus):
    '''
        用於判斷是否在觸發點內 (Status_Trigger)
    '''
    if (type(data)!=dict):
        print("[ERROR] 😭Trigger data is not a dict")
        return
    Square=FatAssAmongUs(amongus)
    for i in data:   
        #if Square and data[i] is overlap
        if (Square[0]<data[i][2] and Square[2]>data[i][0] and Square[1]<data[i][3] and Square[3]>data[i][1]):
            return True
    return False           
    