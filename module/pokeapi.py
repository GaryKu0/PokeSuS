import requests,random,html2image
from PIL import Image
hti=html2image.Html2Image()
#get first 100 pokemon
def get_pokemon(i=-99):
    if (i == -99):
        #random number
        i = random.randint(1, 1008)
    url = f'https://pokeapi.co/api/v2/pokemon/{i}'
    response = requests.get(url)
    data = response.json()
    Res={}
    try:
        Res['name']=data['name']
        Res['image']=data['sprites']['other']['official-artwork']['front_default']
        Res['ability']=data['abilities'][0]['ability']['name']
        Res['type']=data['types'][0]['type']['name']
        Res['atk']=data['stats'][1]['base_stat']
        Res['def']=data['stats'][2]['base_stat']
    except:
        print("Error")
    #10% chance to get shiny
    rd = random.randint(1, 10)
    print(rd)
    if (rd == 1):
        print("✨Shiny!")
        Res['name']=Res['name']+"*"
        Res['image']=data['sprites']['other']['home']['front_shiny'] 
        
    return Res
    
def get_pokemon_image(Res):
    data={
        'name':Res['name'],
        'image':Res['image'],
        'ability':Res['ability'],
        'type':Res['type'],
        'atk':Res['atk'],
        'def':Res['def']
    }
    r_url="https://su-nkust.deta.dev/pokecard"
    #get request
    r=requests.get(r_url,params=data)
    r=r.text
    print("Pokemon:",Res['name'])
    Res['name']=Res['name'].replace("*","")
    Res['name']=Res['name']+"-"+str(random.randint(1,100000))
    hti.screenshot(html_str=r,save_as=Res['name']+'.png')
    image=Image.open(Res['name']+'.png')
    image.save('./collections/'+Res['name']+'.png')
    import os
    os.remove(Res['name']+'.png')
    poke=Image.open('./collections/'+Res['name']+'.png')
    #if system is windows
    if os.name == 'nt':
        #w 750 h1040 anchor top left
        poke=poke.crop((0,0,760,1060))
    elif os.name == 'posix':
        poke=poke.crop((0,0,760*2,1060*2))
    #save as pokecard.png
    poke.save('./collections/'+Res['name']+'.png')  
    return './collections/'+Res['name']+'.png'
   
   
class Pokemon:
    def __init__(self,PokemonID=-99):
        self.pokemon=get_pokemon(PokemonID)
        #get_pokemon_image(self.pokemon)
    
        
if __name__ == '__main__':
    #get_pokemon_image(get_pokemon())
    poke=Pokemon(1)
    print(poke.pokemon)