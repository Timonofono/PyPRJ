import tkinter as tk
from PIL import Image, ImageTk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MusicLab")
        self.geometry("1200x700")
        self.minsize(400, 400)
        self.maxsize(1920, 1080)

        self.entry_username = None
        self.entry_email = None
        self.entry_password = None
        self.entry_passwordR = None

        # фреймы главного окна приложения
        self.frame_bg = tk.Frame(self, width=1200, height=700, bg="black")
        self.frame_menu = tk.Frame(self.frame_bg, width=270, height=620, bg="#320571")
        self.frame_main = tk.Frame(self.frame_bg, width=690, height=620, bg="#320571")
        self.frame_other_function = tk.Frame(self.frame_bg, width=210, height=620, bg="#320571")
        self.frame_song = tk.Frame(self.frame_bg, width=1200, height=70, bg="black")

        # выравнивание фреймов главного окна приложения
        self.frame_bg.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.frame_menu.place(relx=0, rely=0, relwidth=0.23, relheight=0.9)
        self.frame_main.place(relx=0.23, rely=0, relwidth=0.57, relheight=0.9)
        self.frame_other_function.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.9)
        self.frame_song.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        self.show_start_frame()

    def show_start_frame(self):
        if hasattr(self, "frame_start"):
            self.frame_start.destroy()

        self.frame_start = tk.Frame(self.frame_bg, bg="#320571")
        self.frame_start.place(relx=0, rely=0, relheight=1, relwidth=1)

        button_signUp = tk.Button(self.frame_start, text="Sign Up", command=self.show_reg_frame)
        label_signUp = tk.Label(self.frame_start, text="Create an account")
        button_signIn = tk.Button(self.frame_start, text="Sign In", command=self.show_log_with_email_frame)
        label_signIn = tk.Label(self.frame_start, text="Already have an account")

        button_signUp.pack(pady=10)
        label_signUp.pack(pady=5)
        button_signIn.pack(pady=10)
        label_signIn.pack(pady=5)

    def show_log_with_email_frame(self):
        if hasattr(self, "frame_Elog"):
            self.frame_Elog.destroy()

        self.frame_Elog = tk.Frame(self.frame_bg, bg="#320571")
        self.frame_Elog.place(relx=0, rely=0, relheight=1, relwidth=1)

        # Создаем виджеты для ввода данных
        label_email = tk.Label(self.frame_Elog, text="Email:")
        entry_email = tk.Entry(self.frame_Elog)
        label_password = tk.Label(self.frame_Elog, text="Password:")
        entry_password = tk.Entry(self.frame_Elog, show="*")
        button_login = tk.Button(self.frame_Elog, text="Login", command=self.login)

        # Размещаем виджеты на frame_log
        label_email.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        entry_email.grid(row=1, column=1, padx=5, pady=5)
        label_password.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        entry_password.grid(row=2, column=1, padx=5, pady=5)
        button_login.grid(row=4, columnspan=2, padx=5, pady=10)

    def show_reg_frame(self):
        if hasattr(self, "frame_reg"):
            self.frame_reg.destroy()

        # Создаем frame_reg как подфрейм frame_bg
        self.frame_reg = tk.Frame(self.frame_bg, bg="#320571")
        self.frame_reg.place(relx=0, rely=0, relheight=1, relwidth=1)

        # Создаем виджеты для ввода данных
        label_username = tk.Label(self.frame_reg, text="Username:")
        entry_username = tk.Entry(self.frame_reg)
        label_email = tk.Label(self.frame_reg, text="Email:")
        entry_email = tk.Entry(self.frame_reg)
        label_password = tk.Label(self.frame_reg, text="Password:")
        entry_password = tk.Entry(self.frame_reg, show="*")
        label_passwordR = tk.Label(self.frame_reg, text="Repeat password:")
        entry_passwordR = tk.Entry(self.frame_reg, show="*")
        button_login = tk.Button(self.frame_reg, text="Login", command=self.registration)

        # Размещаем виджеты на frame_reg
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
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        # Здесь должна быть логика проверки логина и пароля
        # В данном примере просто выводим значения
        print("Email:", email)
        print("Password:", password)

        # Если логин и пароль правильные, перейдем к главному окну
        self.show_main_frame()

    def show_main_frame(self):
        if hasattr(self, "frame_reg"):
            self.frame_reg.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
