from tkinter import *
from playsound import playsound

window = Tk()
window.geometry("400x400")
window.title("Play Sound")

def play_music():



playbtn = Button(window, text="Play")
playbtn.grid(row=1, column=0)




window.mainloop()