from tkinter import *
import module.var as var
import json,os,cv2
from PIL import Image, ImageTk
import module.pokeapi as pokeapi
def ShopInteract(Store,canva,canva_button_bg,canva_button_text):
    '''
    Store:店家名稱,canva:畫布,輸入後會觸發ShowStoreButton
    '''
    #print('Interact with',Store)

    ShowStoreButton(Store,canva,canva_button_bg,canva_button_text)
        
    
def ShowStoreButton(Store,canva,canva_button_bg,canva_button_text):
    #print('Show',Store,'button')
    tmp_path={'shop':PhotoImage(file=var.path_shop_btn),'store':PhotoImage(file=var.path_store_btn),'Pokemon-Center':PhotoImage(file=var.path_pokemon_center_btn)}
    canva.itemconfig(canva_button_bg,state='normal')
    canva.itemconfig(canva_button_text,text=Store,state='normal')
    
def HideStoreButton(canva,canva_button_bg,canva_button_text):
    canva.itemconfig(canva_button_bg,state='hidden')
    canva.itemconfig(canva_button_text,state='hidden')
    
def BuyProduct(name,i,shop_canva,mainWindow_shop):
    # if i contain \n ingnore it
    if "\n" in i:
        i=i.replace("\n","")
    print('Buy',i)    
def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)
 
def GetCard(canva,money,text):
    print('玩家按下抽卡')
    print("判斷是否有足夠的錢")
    if money>=50:
        print("有足夠的錢")
        Pokemon=pokeapi.get_pokemon()
        #text config to new pokemon
        canva.itemconfig(text,text=Pokemon['name'])
        GeneratePokemonCard=pokeapi.get_pokemon_image(Pokemon)
        #打開圖片
        money-=50  
        save=open("./save.json","r")
        save=json.load(save)
        save['save']['Money']=money
        #save['PokeCard'] is dict of pokemon format is {'pokemon_name':pokemon_image}
        save['save']['PokeCard'][Pokemon['name']]=GeneratePokemonCard
        autosave=open("./save.json","w")
        autosave.write(json.dumps(save,indent=4))
        os.startfile(os.path.normpath(GeneratePokemonCard)) 
        
def DeletePokeCard():
    print('玩家按下刪除卡片')      
        
        
def generateContentShop(name,shop_canva,mainWindow_shop):
    '''
    name:店家名稱,shop_canva:店家畫布,mainWindow_shop:店家視窗
    '''
    print('Generate',name,'content')
    s=open("./data.json","r")
    productImage=[]
    ProductButtonArray=[]
    data=json.load(s)
    #if data['shop'][name] is exist
    if name=="Museum":
        #create title
        #shop_canva.create_text(300,50,text=name,font=('Impact Regular',30,'bold'),fill='black')
        pokecard_back='./Asset/shop/s-pokecras.png'
        #read save.json
        save=open("./save.json","r")
        save=json.load(save)
        pokecard=save['save']['PokeCard']
        # List every pokecard (pokecard is dict type)
        CardStartX=50
        CardStartY=100
        count=0
        for i in pokecard:
            # name above cardback image and two button (delete and show) below cardback image,cardback image is 53x80
            shop_canva.create_text(CardStartX+26,CardStartY-50,text=i,font=('Impact Regular',10,'bold'),fill='black')
            #create cardback image
            im = Image.open(pokecard_back)
            photo = ImageTk.PhotoImage(im)
            label = Label(mainWindow_shop, image=photo)
            label.image = photo  # keep a reference!
            label.place(x=CardStartX, y=CardStartY)
            ProductButtonArray.append(Button(mainWindow_shop,text='查看',command=lambda i=i:os.startfile(os.path.normpath(pokecard[i]))))
            ProductButtonArray[-1].place(x=CardStartX,y=CardStartY+80)
            #create pokecard button
            ProductButtonArray.append(Button(mainWindow_shop,text='刪除',command=lambda i=i:DeletePokeCard(i,shop_canva,mainWindow_shop)))
            ProductButtonArray[-1].place(x=CardStartX+40,y=CardStartY+80)
            CardStartX+=100
            if count==4:
                CardStartX=50
                CardStartY+=80+10
            count+=1
            
        
        
    elif name in data['shop']:
        startX=150
        startY=50
        count=0
        for i in data['shop'][name]["product"]:
            print("Product:",i)
            #image using path_spokeCard
            productImage.append(PhotoImage(file=var.path_spokeCard))
            #image widget
            startX+=300
            if count%2==0:
                startX=150
                startY+=100
            shop_canva.create_text(startX,startY,text=i,font=('zpix', 16),fill='black')
            tmp='BUY'+data['shop'][name]["product"][i]["name"]
            ProductButtonArray.append(Button(mainWindow_shop,text="BUY",command=lambda i=i:BuyProduct(name,i,shop_canva,mainWindow_shop)).place(x=startX,y=startY+80))
            count+=1
            #Button(shop_canva,text=i,command=lambda:print('Buy',i)).pack()
    elif name in data:
        #for i in data[name]["product"]:
        #    print(i)
        #    productImage.append(PhotoImage(file=var.path_spokeCard))
        #    shop_canva.create_image(300,300,image=productImage[-1])
        #    Button(shop_canva,text=i,command=lambda:print('Buy',i)).pack()
        
        #this is new version
        #Grab the save data
        save=open("./save.json","r")
        save=json.load(save)
        money=save['save']['Money']
        
        #抽卡模式
        icon_path='./Asset/icon.png'
        #resize to 30x30
        poball=Image.open(icon_path)
        poball=poball.resize((30,30),Image.ANTIALIAS)
        poball=ImageTk.PhotoImage(poball)
        icon_text=shop_canva.create_text(320,50,text=money,font=('zpix', 16),fill='black')
        icon=shop_canva.create_image(300,50,image=poball)
        pomemon_name=shop_canva.create_text(300,130,text="",font=('zpix', 16),fill='black')
        button=Button(mainWindow_shop,text="抽卡",command=lambda: GetCard(shop_canva,money,pomemon_name)).place(x=300,y=100)
        
        
    
