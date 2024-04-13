import tkinter as tk
import psycopg2
from respect_validation import Validator as v


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MusicLab")
        self.geometry("1200x700")
        self.minsize(400, 400)
        self.maxsize(1920, 1080)

        # Объявление атрибутов
        self.entry_username = None
        self.entry_email = None
        self.entry_password = None
        self.entry_passwordR = None

        self.frame_bg = tk.Frame(self, width=1200, height=700, bg="black")
        self.frame_menu = tk.Frame(self.frame_bg, width=270, height=620, bg="#320571")
        self.frame_main = tk.Frame(self.frame_bg, width=690, height=620, bg="#320571")
        self.frame_other_function = tk.Frame(self.frame_bg, width=210, height=620, bg="#320571")
        self.frame_song = tk.Frame(self.frame_bg, width=1200, height=70, bg="black")

        self.frame_bg.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.frame_menu.place(relx=0, rely=0, relwidth=0.23, relheight=0.9)
        self.frame_main.place(relx=0.23, rely=0, relwidth=0.57, relheight=0.9)
        self.frame_other_function.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.9)
        self.frame_song.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        self.show_login_frame()

    def show_login_frame(self):
        if hasattr(self, "frame_log"):
            self.frame_log.destroy()

        self.frame_log = tk.Frame(self.frame_bg, bg="#320571")
        self.frame_log.place(relx=0, rely=0, relheight=1, relwidth=1)

        label_username = tk.Label(self.frame_log, text="Username:")
        entry_username = tk.Entry(self.frame_log)
        label_email = tk.Label(self.frame_log, text="Email:")
        entry_email = tk.Entry(self.frame_log)
        label_password = tk.Label(self.frame_log, text="Password:")
        entry_password = tk.Entry(self.frame_log, show="*")
        label_passwordR = tk.Label(self.frame_log, text="Repeat password:")
        entry_passwordR = tk.Entry(self.frame_log, show="*")
        button_login = tk.Button(self.frame_log, text="Login", command=self.login)

        label_username.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        entry_username.grid(row=0, column=1, padx=5, pady=5)
        label_email.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        entry_email.grid(row=1, column=1, padx=5, pady=5)
        label_password.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        entry_password.grid(row=2, column=1, padx=5, pady=5)
        label_passwordR.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        entry_passwordR.grid(row=3, column=1, padx=5, pady=5)
        button_login.grid(row=4, columnspan=2, padx=5, pady=10)

        # Инициализация переменных атрибутов
        self.entry_username = entry_username
        self.entry_email = entry_email
        self.entry_password = entry_password
        self.entry_passwordR = entry_passwordR

    def login(self):
        # Логика входа
        username = self.entry_username.get()  # Получаем значение из поля ввода имени пользователя
        password = self.entry_password.get()  # Получаем значение из поля ввода пароля
        passwordR = self.entry_passwordR.get()  # Получаем значение из поля ввода повторного пароля
        
        if username == "admin" and password == "password" and passwordR == password:
            self.show_main_frame()
        else:
            return

    def show_main_frame(self):
        if hasattr(self, "frame_log"):
            self.frame_log.destroy()

        self.frame_main = tk.Frame(self.frame_bg, width=690, height=620, bg="#320571")
        self.frame_main.place(relx=0.23, rely=0, relwidth=0.57, relheight=0.9)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
