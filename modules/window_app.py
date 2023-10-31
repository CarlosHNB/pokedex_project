from tkinter import *
from modules import list
from PIL import ImageTk, Image
from io import BytesIO
import requests 
import json
from urllib.request import urlopen

font_family = "Franklin Gothic Medium Cond"
color_style = "#d9d9d9"
color_info = "#084035"
color_bg = "#cee5f2"

def details_pokemon(pokemon_name):
    ability_pokemon = []
    
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    request = requests.get(url)
    request_json = json.loads(request.content)
    id = f"{request_json['id']:04d}"
    nome_poke = request_json['name']
    for i in range(0,2):
        # TODO: Verifiar quantas habilidades o pokemon tem, pokemon exemplo: ID 888
        ability_pokemon.append(request_json['abilities'][i]['ability']['name'])
    hab1, hab2 = ability_pokemon
    tipo = request_json['types'][0]['type']['name']
    
    img_poke = request_json['sprites']['other']['official-artwork']['front_default']
    
    
    with urlopen(img_poke) as connection:
        raw_data = connection.read()
        image_pokemon = Image.open(BytesIO(raw_data))
        poke_image_tk = ImageTk.PhotoImage(image_pokemon.resize((300, 300)))
        poke_label_tk = Label(image=poke_image_tk, bg=color_bg)
        poke_label_tk.image = poke_image_tk
        poke_label_tk.place(relx=0.35, rely=0.45, anchor="center")
    

    # Status
    value_hp = f"HP - {request_json['stats'][0]['base_stat']}"
    value_attack = f"ATTACK - {request_json['stats'][1]['base_stat']}"
    value_defense = f"DEFENSE - {request_json['stats'][2]['base_stat']}"
    value_special_attack = f"SPECIAL-ATTACK - {request_json['stats'][3]['base_stat']}"
    value_special_defense = f"SPECIAL-DEFENSE - {request_json['stats'][4]['base_stat']}"
    value_speed = f"SPEED - {request_json['stats'][5]['base_stat']}"
    
   
    

    
def main():
    
    root = Tk()
    root.title("POKÉDEX")
    root.geometry('830x467+350+85')
    root.resizable(0,0)
    
    
    
    root.mainloop()
