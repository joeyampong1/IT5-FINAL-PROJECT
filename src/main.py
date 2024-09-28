import tkinter as tk
from LoginRegister import LoginRegister
from Menu import HotelManagementSystem

class HotelManagementSystemMain:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hotel Management System")
        self.root.geometry("960x640+0+0")

        self.login_register = LoginRegister(self.root, self)
        self.login_register.pack(fill="both", expand=True)

        self.root.mainloop()

    def open_menu(self):
        self.login_register.pack_forget()  # Hide the login frame
        self.menu = HotelManagementSystem(self.root)
        self.menu.pack(fill="both", expand=True)

if __name__ == "__main__":
    main = HotelManagementSystemMain()
