import random
import string
from tkinter import *


def generate():
    key = ""
    for i in range(4):
        key_1 = []

        num1 = str(random.randint(0, 9))
        num2 = str(random.randint(0, 9))

        letter1 = random.choice(string.ascii_uppercase)
        letter2 = random.choice(string.ascii_uppercase)
        letter3 = random.choice(string.ascii_uppercase)

        key_1.append(num1)
        key_1.append(num2)
        key_1.append(letter1)
        key_1.append(letter2)
        key_1.append(letter3)
        random.shuffle(key_1)

        key += "".join(key_1)

        if i < 3:
            key += "-"

    key_text.configure(text=key)
    print(key)

window = Tk()
window.title("Генератор ключей")
window.geometry("1024x1024")

background = PhotoImage(file="ae183c63bbeb38d05ecce96aa7f693b4a3769a1835020b63.png")

background_label = Label(window, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

btn = Button(window, text="Сгенерировать ключ", command=generate, background="gold")
btn.place(relx=0.5, rely=0.55, anchor="center")

key_text = Label(window, text="")
key_text.place(relx=0.5, rely=0.5, anchor="center")


window.mainloop()
