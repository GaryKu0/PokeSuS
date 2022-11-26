
from module.var import *
#------------地圖hitnox----------------
#x1,y1,x2,y2

def Debug(canva):
    debugWall(canva)

def debugWall(canva,wall=town_wall):
    '''
    Draw wall on canvas for debug
    if you want to draw forest_wall, you can use debugWall(canva,forest_wall)
    if wall is not defined, it will draw town_wall
    '''
    if (type(wall)==list):
        for i in wall:
            canva.create_rectangle(i[0],i[1],i[2],i[3],outline='red',width=5)
    elif(type(wall)==dict):
        for i in wall:
            canva.create_rectangle(wall[i][0],wall[i][1],wall[i][2],wall[i][3],outline='red',width=2)
            canva.create_text((wall[i][0]+wall[i][2])/2,(wall[i][1]+wall[i][3])/2,text=i,fill='black',font=('Impact Regular',16,'bold'))
    
#網格
def CorrdinateDraw(canva):  
    '''
    Draw coordinate on canvas for debug
    '''
    for i in range(0,660,20):
        canva.create_line(0,i,600,i,fill='gray')
        canva.create_line(i,0,i,600,fill='gray')

#------------地圖hitnox----------------
#DEBUG       
def reportCoordinate(amongus):
    print("[DEBUG🔧] Now AmongUs Location is",amongus.coordinate)