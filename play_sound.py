from playsound import playsound
from tkinter import *



window = Tk()
window.geometry("400x400")
window.title("Play Sound")


def play_music():
    playsound('mysong.mp3')

def stop_music():
    window.destroy()


Button(window, text="Play music", command=play_music).pack()
Button(window, text="Stop music", command=stop_music).pack()
window.mainloop()
