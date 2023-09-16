from tkinter import *
import tkinter
import random

window = tkinter.Tk()
window.title("Password Generator")
window.geometry('480x390')  

c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()
length = IntVar()

list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
list_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
list_3 = ['!', '@', '#', '$', '%', '^', '&', '*']
list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def password():
    final_list = []
    ln = length.get()
    if (c3.get()):
        final_list.append(list_1)
    if (c4.get()):
        final_list.append(list_2)
    if (c2.get()):
        final_list.append(list_3)
    if (c1.get()):
        final_list.append(list_4)
    bound = c1.get() + c2.get() + c3.get() + c4.get()
    if not (bound):
        return ("Nothing selected")
    password = []
    for i in range(ln):
        if (i == 0):
            a = 1
        else:
            a = random.randint(1, bound)
        k = final_list[a - 1]
        b = random.randint(0, len(k) - 1)
        password.append(str(k[b]))
    return (''.join(password))

pswrd = StringVar()
pswrd.set(password())
txt_1 = tkinter.Label(window, textvariable=pswrd, font=("Arial", 15))

def display_password():
    global txt_1
    txt_1.pack_forget()
    pswrd.set(password())
    txt_1 = tkinter.Label(window, textvariable=pswrd, font=("Arial", 15))
    txt_1.pack()


label_1 = tkinter.Label(window, text="\nPassword Generator", font=("Arial", 19))
label_2 = tkinter.Label(window, text="Select atleast two options\n", font=("Arial", 11))
label_1.pack()
label_2.pack()

chkbutton_1 = tkinter.Checkbutton(window, text='Numbers', variable=c1, onvalue=1, offvalue=0)
chkbutton_2 = tkinter.Checkbutton(window, text='Special Characters', variable=c2, onvalue=1, offvalue=0)
chkbutton_3 = tkinter.Checkbutton(window, text='Small Letters', variable=c3, onvalue=1, offvalue=0)
chkbutton_4 = tkinter.Checkbutton(window, text='Capital Letters', variable=c4, onvalue=1, offvalue=0)
slider_1 = tkinter.Scale(window, variable=length, orient=HORIZONTAL, label="Set length of password", length=120,
                         from_=6, to=30)
button_1 = tkinter.Button(window, text="Generate password", command=display_password)

chkbutton_1.pack()
chkbutton_2.pack()
chkbutton_3.pack()
chkbutton_4.pack()
slider_1.pack()
button_1.pack()

window.mainloop()
