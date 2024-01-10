import base64
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import random
import string
import clipboard as cb
import tkinter.font as font
from buttontostr import img



image = base64.b64decode(img)

def copybuffer(text):

    """Функция для кнопки скопировать в буффер"""

    cb.copy(text)
    output.delete('1.0', END)
    output.insert(INSERT, 'Пароль скопирован!')


def generate():

    """Функция генератор случайных паролей"""

    output.delete('1.0', END) #Очищает поле вывода output
    elements = f'{string.ascii_letters}' + f'{string.digits}' + f'{string.punctuation}' # Формирует список элементов
    if entry.get().isdigit():
        number = entry.get()
        password = "".join(random.choice(elements) for i in range(int(number)))
    else:
        entry.delete(0, 'end')
        output.insert(INSERT, 'Введите число!')
    output.insert(INSERT, f'{password}')
    


root = Tk()
root.resizable(width=False, height=False)
root.geometry('290x280')
root.title('Password Generator')
frame = ttk.Frame(borderwidth=1)


label = ttk.Label(text='Задайте длинну пароля', font='TkHeadingFont')
label.pack(padx=10, pady=10)

entry = ttk.Entry()
entry.pack(padx=20, ipadx=15, ipady=5)

font.nametofont('TkDefaultFont').configure(size=10)
button = ttk.Button(text='Сгенерировать', command=generate)
button.pack(padx=10, pady=10, ipadx=3, expand=True, ipady=3)


output = ScrolledText(frame, height=3)
output.pack(padx=40, pady=10)

preimage = PhotoImage(data=image)
copybutton = ttk.Button(frame, image=preimage)
copybutton.pack(anchor=N, pady=10)

frame.pack(anchor=NW, fill=X, padx=4, pady=4)

copybutton.bind('<Button-1>', lambda e: copybuffer(output.get('1.0', 'end')))

root.mainloop()
