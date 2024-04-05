import tkinter as tk
from pygame import mixer

def play_music():
    mixer.init()  # Инициализация звуковой системы pygame
    mixer.music.load("path_to_your_audio_file.mp3")  # Загрузка аудиофайла
    mixer.music.play()  # Воспроизведение аудио

def stop_music():
    mixer.music.stop()  # Остановка воспроизведения аудио

window = tk.Tk()
window.title('MusicLab')
window.geometry("1200x700")
window.minsize(400, 400)
window.maxsize(1920, 1080)

frame_bg = tk.Frame(window, width=1200, height=700, bg="black")
frame_menu = tk.Frame(frame_bg, width=270, height=620, bg="#464444")
frame_main = tk.Frame(frame_bg, width=690, height=620, bg="#464444")
frame_other_function = tk.Frame(frame_bg, width=210, height=620, bg="#464444")
frame_song = tk.Frame(frame_bg, width=1200, height=70, bg="black")

frame_bg.place(relx=0, rely=0, relheight=1, relwidth=1)
frame_menu.place(relx=0, rely=0, relwidth=0.23, relheight=0.9)
frame_main.place(relx=0.23, rely=0, relwidth=0.57, relheight=0.9)
frame_other_function.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.9)
frame_song.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

btn_play = tk.Button(frame_song, text="Play", command=play_music)
btn_play.pack(side=tk.LEFT, padx=10)

btn_stop = tk.Button(frame_song, text="Stop", command=stop_music)
btn_stop.pack(side=tk.LEFT, padx=10)

window.mainloop()
