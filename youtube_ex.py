from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title("PLAY SOUNDS")
root.geometry("500x400")
root.config(background="red")

# Initialise pygame mixer
pygame.mixer.init()

#add song function
def add_song():
    song = filedialog.askopenfilename(initialdir='sounds/', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))
    #strip out directory
    song = song.replace("/home/user/PycharmProjects/Sound/Music", "")
    song = song.replace(".mp3", "")

    #add song
    song_box.insert(END, song)

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='sounds/', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))

    for song in songs:
        song = song.replace("/home/user/PycharmProjects/Sound/Music", "")
        song = song.replace(".mp3", "")

        song_box.insert(END, song)



#play seelected song
def play():

    song = song_box.get(ACTIVE)
    song = f'/home/user/PycharmProjects/Sound/Music{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#stop song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

#create global pause variable
global paused
paused = False

#pause and unpause
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def next_song():
    next_one = song_box.curselection()
    print(next_one)



# Create Playlist
song_box = Listbox(root, bg="Black", fg="green", width=60)
song_box.pack(pady=20)

# Create player control buttons
next_btn_img = PhotoImage(file='icons8-fast-forward-50.png')
previous_btn_img = PhotoImage(file='icons8-rewind-50.png')
play_btn_img = PhotoImage(file='icons8-play-button-24(1).png')
pause_btn_img = PhotoImage(file='icons8-pause-24.png')
stop_btn_img = PhotoImage(file='icons8-stop-30.png')

#control frames
control_frame = Frame(root)
control_frame.pack()

#create buttons
next_button = Button(control_frame, image=next_btn_img, borderwidth=0, command=next_song)
previous_button = Button(control_frame, image=previous_btn_img, borderwidth=0)
play_button = Button(control_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop)

previous_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=3, padx=10)
next_button.grid(row=0, column=4, padx=10)

#create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label= "Add Songs", menu=add_song_menu)
add_song_menu.add_command(label= "Add one song to playlist", command=add_song)
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)





root.mainloop()