from tkinter import *
from PIL import Image, ImageTk
from modules import list, window_app

color_style = "#cee5f2"

# Criação da instância Tk()
root = Tk()
root.title("Pokédex")
root.geometry('410x580+350+85')
root.resizable(0,0)
root.configure(bg=color_style)

# Frame root(contém todos os label´s)
frame_root = Frame(root, bg=color_style)
frame_root.grid(row=0, column=0)

# Criação dos label´s apartir dos frame_root(container root)
imageBanner = ImageTk.PhotoImage(Image.open('pictures\poke_art_1.png'))
banner_1 = Label(frame_root, image=imageBanner, bg=color_style, anchor="center")
banner_1.grid(row=0, column=0)

imageBanner_2 = ImageTk.PhotoImage(Image.open('pictures\poke_art_2.png'))
banner_2 = Label(frame_root, image=imageBanner_2, bg=color_style, anchor="center")
banner_2.grid(row=1, column=0)

label_name = Label(frame_root, text="DIGITE SEU NOME", bg=color_style, font=(
    "Tw Cen MT Condensed", 20, "bold"
))
label_name.grid(row=2, column=0)

entry_name = Entry(frame_root, font=(
    'Ubuntu', 18, 'bold'
), justify="center", bd=0)
entry_name.grid(row=3, column=0)

button_submit = Button(frame_root, padx=13, text="Pokédex", bd=1, fg="black",
font=(
    'Helvetica', 13, 'bold'
), anchor="center", 
# Lambda que recebe o input do usuário, destrói a tela e abre a segunda janela.
command=lambda: [list.trainer_names.append(entry_name.get()), 
                 root.destroy, window_app.main()])

button_submit.grid(row=4, column=0, pady=10)

root.mainloop()

