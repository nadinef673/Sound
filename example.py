from tkinter import *
import pygame


pygame.mixer.init()
def play_music():
    pygame.mixer.music.load("/home/user/Desktop/Sound/danileigh_cravin_ft._g-eazy_official_video_mp3_37486.mp3")
    pygame.mixer.music.play()

root = Tk()
root.geometry("400x400")
root.title("PLAY SOUND")
Button(root, text="Play music", command=play_music).pack()
root.mainloop()

