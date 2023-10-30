from tkinter import *
from PIL import Image, ImageTk
from modules import list, window_app

color_style = "#cee5f2"

window = Tk()
window.title("Pokédex")
window.geometry('410x580+350+85')
window.resizable(0,0)
window.configure(bg=color_style)

imageBanner = ImageTk.PhotoImage(Image.open('pictures\poke_art_1.png'))
banner = Label(window, image=imageBanner, bg=color_style, anchor="center")
banner.grid(row=1, column=1)


imageBanner_2 = ImageTk.PhotoImage(Image.open('pictures\poke_art_2.png'))
banner2 = Label(window,image=imageBanner_2, bg=color_style, anchor="center")
banner2.grid(row=0, column=1)


label_name = Label(window, text="DIGITE SEU NOME", bg=color_style, font=("Tw Cen MT Condensed", 20, "bold"))
label_name.grid(row=2, column=1)

entry_name = Entry(window, font=('Ubuntu', 18, "bold"),  justify='center', bd=0)
entry_name.grid(row=3, column=1)



button_submit = Button(window, padx=13, text="Pokédex", bd=1, fg="black", 
                       font=('Helvetica', 13, "bold"), anchor="center",
                       command=lambda: [list.trainer_names.append(entry_name.get()), window.destroy(), window_app.main()])
button_submit.grid(row=4, column=1, pady=10)

window.mainloop()

