from tkinter import *
from tkinter import messagebox
import threading,time
from module.Debug import *
from module.bind import *
from module.var import *
from pypresence import Presence
from module.playerMoving import TriggerPoint, TriggerPointBool
import module.shop as shop
import sys,random,json
from module.dcRich import *
from PIL import ImageTk, Image

game_running=True
mainWindow=Tk()
mainWindow.title("PokeSuS")
mainWindow.iconphoto(False,PhotoImage(file='./Asset/icon.png'))
mainWindow.resizable(False,False)
canva=Canvas(mainWindow,width=660,height=660)


#--------------------變數宣告--------------------
map_town=PhotoImage(file=path_town)
map_forest=PhotoImage(file=path_forest)
Player_Stand=PhotoImage(file=path_Stand)
#Player_Stand=PhotoImage(file=path_block)


#------------地圖---------------------
buttonmap='forest'
def map(map):
    global map_town,map_forest,canva,buttonmap,Amongus,Map
    if map=='town':
        print('[DEBUG] Town')
        canva.itemconfig(Map,image=map_town)
        buttonmap='forest'
        Amongus.currentmap='town'
    elif map=='forest':
        print('[DEBUG] Forest')
        canva.itemconfig(Map,image=map_forest)
        buttonmap='town'
        Amongus.currentmap='forest'
    canva.pack()
    
#突發任務
ertimer=20
EmergencyRequestWindow_exist=False #突發任務視窗是否存在
def emergencyrequest():
    global EmergencyRequestWindow_exist
    #5% chance to get emergency request
    if (random.randint(1, 20) == 1 and EmergencyRequestWindow_exist==False):
        print("✨Emergency Request!")
        #create a new window
        EmergencyRequestWindow_exist=True
        EmergrecyRequestWindow=Toplevel(mainWindow)
        EmergrecyRequestWindow.title("⚠️Emergency Request")
        EmergrecyRequestWindow.iconphoto(False,PhotoImage(file='./Asset/icon.png'))
        #EmergrecyRequestWindow.resizable(False,False
        math_option=['+','-','x']
        math_option_choice=random.choice(math_option)
        H1=Label(EmergrecyRequestWindow,text="⚠️Emergency Request",font=("Zpix", 25))
        H1.pack()
        #timer for 10 seconds

        def timer_countdown(ertimer1):
            Timer_label=Label(EmergrecyRequestWindow,text="Time left: "+str(ertimer1),font=("Zpix", 18))
            Timer_label.pack()
            global ertimer
            while ertimer1>0:
                time.sleep(1)
                ertimer1-=1
                ertimer=ertimer1
                try:
                    Timer_label.config(text="Time left: "+str(ertimer1))
                except:
                    pass
            if ertimer1==0:
                Timer_label.config(text="Time left: 0")
                EmergrecyRequestWindow.destroy()
                global EmergencyRequestWindow_exist
                EmergencyRequestWindow_exist=False
        threading.Thread(target=timer_countdown,args=(ertimer,)).start()
        
        q1=random.randint(1, 100)
        q2=random.randint(1, 100)
        question=Label(EmergrecyRequestWindow,text=f"Question: {q1} {math_option_choice} {q2} = ?")
        #entry and focus
        Answer=Entry(EmergrecyRequestWindow)
        
        #pack
        question.pack()
        Answer.pack()
        def ERSubmit(Answer,math_option_choice,ertimer):
            global EmergencyRequestWindow_exist
            tmpscore=ertimer
            print("目前可得分數:",tmpscore,"即將判斷答案")
            ertimer=0
            if (math_option_choice=='+'):
                if (int(Answer.get())==q1+q2):
                    messagebox.showinfo("Correct","Correct Answer!")
                    erResult=True
                    EmergrecyRequestWindow.destroy()
                    EmergencyRequestWindow_exist=False
                else:
                    EmergrecyRequestWindow.destroy()
                    messagebox.showerror("Wrong","Wrong Answer!")
            elif (math_option_choice=='-'):
                if (int(Answer.get())==q1-q2):
                    messagebox.showinfo("Correct","Correct Answer!")
                    erResult=True
                    EmergrecyRequestWindow.destroy()
                    EmergencyRequestWindow_exist=False
                else:
                    EmergrecyRequestWindow.destroy()
                    messagebox.showerror("Wrong","Wrong Answer!")
            elif (math_option_choice=='x'):
                if (int(Answer.get())==q1*q2):
                    messagebox.showinfo("Correct","Correct Answer!")
                    erResult=True
                    EmergrecyRequestWindow.destroy()
                    EmergencyRequestWindow_exist=False
                else:
                    EmergrecyRequestWindow.destroy()
                    messagebox.showerror("Wrong","Wrong Answer!")
            if (erResult):
                Save=open('./save.json','r')
                Save=json.load(Save)
                Money=Save['save']['Money']
                Money+=tmpscore
                messagebox.showinfo("Money","You got "+str(tmpscore)+" Pokeballs!",icon='info')
                #save to json
                Save['save']['Money']=Money
                AutoSave=open('./save.json','w')
                AutoSave.write(json.dumps(Save,indent=4))
                AutoSave.close()
            
                
        def eq_on_closing():
            ertimer=0
            EmergrecyRequestWindow.destroy()
            global EmergencyRequestWindow_exist
            EmergencyRequestWindow_exist=False
                
        Sumbit=Button(EmergrecyRequestWindow,text="Submit",command=lambda:ERSubmit(Answer,math_option_choice,ertimer))
        Sumbit.pack()
        EmergrecyRequestWindow.protocol("WM_DELETE_WINDOW", eq_on_closing)
        
        EmergrecyRequestWindow.mainloop()
        
 
        
    
    
   
class Player:
    def __init__(self,coordinate):
        self.coordinate=coordinate
        self.image=Player_Stand
        self.Player=canva.create_image(self.coordinate[0],self.coordinate[1],anchor=NW,image=self.image)
        self.now=0
        self.moving=False
        self.tag=''
        self.currentmap='town'
    def move(self,direction,move):
        #清除上一個tag
        if self.tag=='left':
            self.tag=''
        #將移動動畫開啟
        if self.moving==False:
            self.moving=True
            innerThread=threading.Thread(target=Amongus.walk,args=(1,))
            innerThread.start()
        #移動
        if direction=='up':
            #print('[DEBUG]up'))
            canva.move(self.Player,0,-move)
            self.coordinate[1]-=move
            if (self.detectWall(forest_wall) and self.currentmap=='forest') or (self.detectWall(town_wall) and self.currentmap=='town'):
                canva.move(self.Player,0,move)
                self.coordinate[1]+=move
        elif direction=='down':
            #print('[DEBUG]down')
            canva.move(self.Player,0,move)
            self.coordinate[1]+=move
            if (self.detectWall(forest_wall) and self.currentmap=='forest') or (self.detectWall(town_wall) and self.currentmap=='town'):
                canva.move(self.Player,0,-move)
                self.coordinate[1]-=move
        elif direction=='left':
            self.tag='left'
            #print('[DEBUG]left')
            canva.move(self.Player,-move,0)
            self.coordinate[0]-=move
            if (self.detectWall(forest_wall) and self.currentmap=='forest') or (self.detectWall(town_wall) and self.currentmap=='town'):
                canva.move(self.Player,move,0)
                self.coordinate[0]+=move
        elif direction=='right':
            #print('[DEBUG]right')
            canva.move(self.Player,move,0)
            self.coordinate[0]+=move
            if (self.detectWall(forest_wall) and self.currentmap=='forest') or (self.detectWall(town_wall) and self.currentmap=='town'):
                canva.move(self.Player,-move,0)
                self.coordinate[0]-=move
        if(Amongus.currentmap=="town"):Status_Trigger=TriggerPointBool(Town_TriggerPoint,Amongus)
        elif Amongus.currentmap=="forest":
            Status_Trigger=TriggerPointBool(Forest_TriggerPoint,Amongus)
            #突發任務
            emergencyrequest()
        if (Status_Trigger==True and Amongus.currentmap=='town'):
            tmp_location=TriggerPoint(Town_TriggerPoint,Amongus)
            shop.ShopInteract(tmp_location,canva,canva_button_bg,canva_button_text)
        elif (Amongus.currentmap=="town"):shop.HideStoreButton(canva,canva_button_bg,canva_button_text) 
        if (Status_Trigger==True and Amongus.currentmap=='forest'):
            tmp_location=TriggerPoint(Forest_TriggerPoint,Amongus)
            shop.ShopInteract(tmp_location,canva,canva_button_bg,canva_button_text)
             
    def stand(self):
        self.moving=False
        #print('[DEBUG]release')
        self.image=Player_Stand
        canva.itemconfig(self.Player,image=self.image)
        canva.update()
    def walk(self,frame):
        while self.moving:
            if self.now<4:
                self.now+=frame
                self.image=PhotoImage(file='./Asset/player/frame/'+str(self.now)+'.png')
            else:
                self.now=1
                self.image=PhotoImage(file='./Asset/player/frame/'+str(self.now)+'.png')
            if self.tag=='left':
                self.image=PhotoImage(file='./Asset/player/frame/'+str(self.now+4)+'.png')
            canva.itemconfig(self.Player,image=self.image)
            canva.update()
            time.sleep(0.1)
    def detectWall(self,wall):
        for i in wall:
            Square=FatAssAmongUs(Amongus)
            Square[0]+=7
            Square[1]+=7
            Square[2]-=7
            Square[3]-=7
            #if square and i is touch
            if (Square[0]<=i[2]and Square[2]>=i[0] and Square[1]<=i[3] and Square[3]>=i[1]):
                return True
            #if self.coordinate[0]>=i[0] and self.coordinate[0]<=i[2] and self.coordinate[1]>=i[1] and self.coordinate[1]<=i[3]:
            #    return True
        return False

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        mainWindow.destroy()
        global shop_clcik_window_exist,game_running
        game_running=False
        shop_clcik_window_exist=False
        #close whole program
        

    


shop_clcik_window_exist=False
#-----------------掌管所有F----------------
def shop_clcik():
    global shop_clcik_window_exist
    if(Amongus.currentmap=="town"):Status_Trigger=TriggerPointBool(Town_TriggerPoint,Amongus)
    elif Amongus.currentmap=="forest":Status_Trigger=TriggerPointBool(Forest_TriggerPoint,Amongus)
    print('POG😧')
    print('Cureent map:',Amongus.currentmap)
    print('Status_Trigger:',Status_Trigger)
    print('shop_clcik_window_exist:',shop_clcik_window_exist)
    print('------------------------------------')
    print('Amongus.currentmap',Amongus.currentmap)
    print('城鎮是否in觸發點:',TriggerPointBool(Town_TriggerPoint,Amongus),'森林是否in觸發點:',TriggerPointBool(Forest_TriggerPoint,Amongus))
    #-------------------切換地圖-------------------
    if (Amongus.currentmap=='town' and Status_Trigger==True and TriggerPoint(Town_TriggerPoint,Amongus)=='Forest' ):
        forest_start_point=[320,580]
        Amongus.currentmap='forest'
        map('forest')
        print("因角色位置在",Amongus.coordinate,"所以將角色移動至",forest_start_point,"需要向下移動",forest_start_point[1]-Amongus.coordinate[1],"向右移動",forest_start_point[0]-Amongus.coordinate[0])
        Amongus.move('right',forest_start_point[0]-Amongus.coordinate[0])
        Amongus.move('down',forest_start_point[1]-Amongus.coordinate[1])
        Amongus.stand()
    elif Amongus.currentmap=='town' and Status_Trigger==True and shop_clcik_window_exist==False:
        #create New windows
        shop_clcik_window_exist=True
        print('shop_clcik_window_exist:',shop_clcik_window_exist)
        print("🗯️  Show Shop Page")
        mainWindow_shop=Toplevel(mainWindow)
        Label(mainWindow_shop,text=TriggerPoint(Town_TriggerPoint,Amongus),font=("zpix",26)).pack()
        mainWindow_shop.title(TriggerPoint(Town_TriggerPoint,Amongus))
        mainWindow_shop.geometry("600x600")
        shop_canva=Canvas(mainWindow_shop,width=600,height=600)
        shop_canva.create_image(300,300,image=PhotoImage(file=path_spokeCard))
        
        shop.generateContentShop(TriggerPoint(Town_TriggerPoint,Amongus),shop_canva,mainWindow_shop)
        
        shop_canva.pack()
        def shop_clcik_close():
            global shop_clcik_window_exist
            mainWindow_shop.destroy()
            shop_clcik_window_exist=False
        mainWindow_shop.protocol("WM_DELETE_WINDOW",shop_clcik_close)
    elif Amongus.currentmap=='forest' and Status_Trigger==True:
        print("TriggerPoint(Forest_TriggerPoint,Amongus : ",TriggerPoint(Forest_TriggerPoint,Amongus))
        town_start_point=[195,0]
        if (TriggerPoint(Forest_TriggerPoint,Amongus)=='Town'):    
            map('town')
            print("[Forest]因角色位置在",Amongus.coordinate,"所以將角色移動至",town_start_point,"需要向下移動",town_start_point[1]-Amongus.coordinate[1],"向右移動",town_start_point[0]-Amongus.coordinate[0])
            Amongus.move('right',town_start_point[0]-Amongus.coordinate[0])
            Amongus.move('down',town_start_point[1]-Amongus.coordinate[1])
            Amongus.stand()
        elif (TriggerPoint(Forest_TriggerPoint,Amongus)=='Town1'):
            print("[Forest]因角色位置在",Amongus.coordinate,"所以將角色移動至",town_start_point,"需要向上移動",Amongus.coordinate[1]-town_start_point[1],"向左移動",Amongus.coordinate[0]-town_start_point[0])
            Amongus.move('up',Amongus.coordinate[1]-town_start_point[1])
            Amongus.move('left',Amongus.coordinate[0]-town_start_point[0])
            map('town')
            Amongus.stand()






#---------main loop----------------
Map=canva.create_image(0,0,anchor=NW,image=map_town)

Amongus=Player(initial_coordinate)
buttonBG='./Asset/shop/Button.png'
buttonBG=PhotoImage(file=buttonBG)


map('town')

AmongUsWalk=threading.Thread(target=Amongus.walk,args=(1,))
AmongUsWalk.start()

#CorrdinateDraw(canva)
#debugWall(canva,Forest_TriggerPoint)
#debugWall(canva,dict_town_wall)
#debugWall(canva)
canva_button_bg=canva.create_image(540,620,image=buttonBG)
canva_button_text=canva.create_text(540,620,text='Town',font=('Zpix',18),fill='darkgreen')

canva.itemconfig(canva_button_bg,state='hidden')
canva.itemconfig(canva_button_text,state='hidden')
canva.pack()  

    


bind(mainWindow,Amongus,buttonmap)
mainWindow.bind("<KeyPress-End>",lambda event:map(buttonmap))
mainWindow.bind("<KeyPress-f>",lambda event:shop_clcik())
#ainWindow.bind("<KeyPress-Home>",lambda event:createNewWindow())
mainWindow.protocol("WM_DELETE_WINDOW", on_closing)



try:
    start = int(time.time())
    client_id = "695279575143546900"
    RPC = Presence(client_id)
    RPC.connect()
    def DiscordRichPresence():
        print("[INFO] 📢 Discord Rich Presence is running")
        while game_running: 
            #print("Game Running",game_running)
            RPC.update(
                large_image = "pokesus", #name of your asset
                small_image="banana",
                large_text = "Game created by: @Albus Dumbledore#0301",
                details = "Exploring the world of Pokesus",
                #state = "",
                start = start,
                buttons = [{"label": "View it on Github!", "url": "https://github.com/GaryKu0/PokeSuS"}, {"label": "🥑 Avocado CSS", "url": "https://id0x.ga"}] #up to 2 buttons
            )
            time.sleep(10)
    Discord_Rich_Presence=threading.Thread(target=DiscordRichPresence)
    Discord_Rich_Presence.start()
except:
    print("[ERROR] 📢 Discord Rich Presence is not running")



mainWindow.mainloop()

