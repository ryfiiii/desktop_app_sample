import customtkinter as ctk
from tkinter import messagebox

class HelloWorldApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Hello World App")
        self.window.geometry("300x200")

        # テーマの設定
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")  # ブルーテーマ

        # フレームの作成
        self.frame = ctk.CTkFrame(master=self.window)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # ラベルの作成
        self.label = ctk.CTkLabel(master=self.frame, text="Welcome to Hello World App!", font=("Roboto", 16))
        self.label.pack(pady=10, padx=10)

        # ボタンの作成
        self.hello_button = ctk.CTkButton(master=self.frame, text="Click Me!", command=self.say_hello)
        self.hello_button.pack(pady=10, padx=10)

    def say_hello(self):
        messagebox.showinfo("Hello", "Hello, World!")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = HelloWorldApp()
    app.run()