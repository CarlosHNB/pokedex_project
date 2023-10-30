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
        poke_label_tk.place(relx=0.3, rely=0.45, anchor="center")
    
    
    label_nome_poke = Label(text=nome_poke, width=15, bg=None)
    label_nome_poke.place(relx=0.1, rely=0.065, anchor="center")
    label_id_poke = Label(text=id, width=10, bg=None)
    label_id_poke.place(relx=0.095, rely=0.12, anchor="center")
    label_tipo_poke = Label(text=tipo, width=10, bg=None)
    label_tipo_poke.place(relx=0.095, rely=0.18, anchor="center")
    
    
    # label_habilidades_poke = Label()
    # label_habilidades_poke.pack()
    
    
    # info_pokemon = f"ID: \n{id} \nNome: \n{nome_poke} \n Habildades: \n{hab1}\n{hab2}\n Tipo: {tipo}"
    # label_poke = Label(text=info_pokemon, bg=color_bg, font=(font_family, 13), width=11)   
    # label_poke.place(relx=0.53, rely=0.6, anchor='center')

    
def main():
    
    root = Tk()
    root.title("POKÉDEX")
    root.geometry('828x465+350+85')
    root.resizable(0,0)
    
    img_background = PhotoImage(file="pokemon_project/pictures/pokedex_art.png")
    img_background_label = Label(root, image=img_background, bg=color_bg)
    img_background_label.place(x=0, y=0)
    
    # lbl = Label(root, text=f"Bem Vindo, {list.trainer_names[0].title()}",
    #             bg=color_bg, font=('Franklin Gothic Medium Cond', 15))
    
    # lbl.place(relx=0.15, rely=0.090, anchor='center')
    
    label_poke = Label(root, text="Buscar - Id / Nome", bg=color_bg, font=("Tw Cen MT Condensed", 12, "bold"))
    label_poke.place(relx=0.85, rely=0.1, anchor="center")

    entry_poke = Entry(root, font=('Ubuntu', 12, "bold"),  justify='center', width=13)
    entry_poke.place(relx=0.85, rely=0.2, anchor="center")
    
    button_submit = Button(root, text="Buscar", bd=1 , fg="black", 
                       font=('Helvetica', 10, "bold"),
                       command=lambda: [details_pokemon(entry_poke.get())])

    button_submit.place(relx=0.85, rely=0.3, anchor="center")
    

    
    root.mainloop()
