path_town="./Asset/map/Town.png"
path_forest="./Asset/map/Forest.png"
path_Stand='./Asset/player/stand-80.png'
path_block='./Asset/player/block.png'


path_pokeCard='./Asset/shop/pokecras.png'
path_spokeCard='./Asset/shop/s-pokecras.png'

path_shop_btn='./Asset/shop/shop.png'
path_store_btn='./Asset/shop/store.png'
path_pokemon_center_btn='./Asset/shop/pokemon-center.png'



Status_Trigger=False



forest_wall=[]
forest_wall=[[0,0,40,660],[40,555,315,650],[395,555,650,650],[585,0,650,560],[220,100,255,330]]
town_wall=[[0,0,180,130],[-20,130,60,660],[55,600,660,660],[600,0,660,660],[70,380,170,420],[70,460,310,470],[270,-10,570,180],[280,190,340,340],[190,440,310,510],[350,260,440,340],[470,260,530,430],[420,430,500,480]]
dict_town_wall={"1":[0,0,180,130],"2":[-20,130,60,660],"3":[55,600,660,660],"4":[580,0,660,660],"5":[70,380,170,420],"6":[70,460,310,470],"7":[270,-10,570,180],"8":[280,190,340,340],"9":[190,440,310,510],"10":[350,260,440,340],"11":[470,260,530,430],"12":[420,430,500,480]}
Town_TriggerPoint={'shop':[220,500,300,580],'Pokemon-Center':[395,355,475,435],'store':[105, 305,185,385],'Museum':[360, 190, 480, 270],'Forest':[195,0,275,80]}
Forest_TriggerPoint={'Town':[275,0,375,80],"Town1":[320,580,400,660]}

def FatAssAmongUs(Amongus):
    #a square 80x80
    FatAss=[Amongus.coordinate[0],Amongus.coordinate[1],Amongus.coordinate[0]+80,Amongus.coordinate[1]+80]
    return FatAss

initial_coordinate=[80,480]

Pokemon_level={"D":1,"C":0.8,"B":0.6,"A":0.4,"S":0.2}