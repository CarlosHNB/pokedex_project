from tkinter import *
from PIL import Image, ImageTk
from modules import list, window_app

color_style = "#cee5f2"

window = Tk()
window.title("Pokédex")
window.geometry('600x590+350+85')
window.configure(bg=color_style)

imageBanner = ImageTk.PhotoImage(Image.open('pokemon_project/pictures/poke_art_1.png'))
banner = Label(window, image=imageBanner, bg=color_style)
banner.place(relx=0.5, rely=0.5, anchor="center")

imageBanner_2 = ImageTk.PhotoImage(Image.open('pokemon_project/pictures/poke_art_2.png'))
banner2 = Label(window,image=imageBanner_2, bg=color_style)
banner2.place(relx=0.5, rely=0.12, anchor="center")


label_name = Label(window, text="DIGITE SEU NOME", bg=color_style, font=("Tw Cen MT Condensed", 20, "bold"))
label_name.place(relx=0.5, rely=0.8, anchor="center")

entry_name = Entry(window, font=('Ubuntu', 18, "bold"),  justify='center', bd=0)
entry_name.place(relx=0.5, rely=0.87, anchor="center")


button_submit = Button(window, padx=15, text="Pokédex", bd=1, fg="black", 
                       font=('Helvetica', 13, "bold"),
                       command=lambda: [list.trainer_names.append(entry_name.get()), window.destroy(), window_app.main()])

button_submit.place(relx=0.5, rely=0.95, anchor="center")

window.mainloop()

