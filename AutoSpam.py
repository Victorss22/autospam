from tkinter import*
import pyautogui as pg
import time

def pegartexto():
    a=entrada1.get()
    z=int(entrada2.get())
    x=0

    time.sleep(5)
    while x<z:
        pg.write(f'{a}  #{x}\n')
        x+=1

root=Tk()

root.geometry("500x700")
root.title("Auto Spam")
root.config(background="lightblue")

entrada1=Entry(root,)
entrada1.place(relx=.1, rely=0.03)

entrada2=Entry(root,)
entrada2.place(relx=.1, rely=0.08)

btn=Button(root,text='Confirmar', foreground="white",bg="darkgreen", command=pegartexto)
btn.place(relx=0.1, rely=0.15,)

root.mainloop()
