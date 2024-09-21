from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2) - 30
    
    win.geometry(f'{width}x{height}+{x}+{y}')

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login Success", f"Welcome {username}!")
        window.destroy()  # Close login window
        root = Tk()  # Create new window for reservation
        ReservationForm(root)  # Call reservation form
        root.mainloop()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials!")

def show_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

class ReservationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Reservation Form")
        self.root.state('zoomed')

        # Full Name
        Label(self.root, text="Full Name:").place(x=30, y=30)
        self.full_name = Entry(self.root, width=40)
        self.full_name.place(x=150, y=30)

        # Address
        Label(self.root, text="Address:").place(x=30, y=70)
        self.address = Entry(self.root, width=40)
        self.address.place(x=150, y=70)

        # Phone Number
        Label(self.root, text="Phone Number:").place(x=30, y=110)
        self.phone_number = Entry(self.root, width=40)
        self.phone_number.place(x=150, y=110)

        # Email
        Label(self.root, text="Email:").place(x=30, y=150)
        self.email = Entry(self.root, width=40)
        self.email.place(x=150, y=150)

        # Arrival Date and Time
        Label(self.root, text="Arrival Date (MM-DD-YYYY):").place(x=30, y=190)
        self.arrival_date = Entry(self.root, width=20)
        self.arrival_date.place(x=200, y=190)
        
        Label(self.root, text="Arrival Time (HH:MM):").place(x=30, y=230)
        self.arrival_time = Entry(self.root, width=20)
        self.arrival_time.place(x=200, y=230)

        # Departure Date and Time
        Label(self.root, text="Departure Date (MM-DD-YYYY):").place(x=30, y=270)
        self.departure_date = Entry(self.root, width=20)
        self.departure_date.place(x=200, y=270)

        Label(self.root, text="Departure Time (HH:MM):").place(x=30, y=310)
        self.departure_time = Entry(self.root, width=20)
        self.departure_time.place(x=200, y=310)

        # Number of Adults
        Label(self.root, text="Number of Adults:").place(x=30, y=350)
        self.num_adults = Entry(self.root, width=10)
        self.num_adults.place(x=200, y=350)

        # Number of Kids
        Label(self.root, text="Number of Kids (if any):").place(x=30, y=390)
        self.num_kids = Entry(self.root, width=10)
        self.num_kids.place(x=200, y=390)

        # Payment Method
        Label(self.root, text="Payment Method:").place(x=30, y=430)
        self.payment_method = StringVar()
        self.payment_method.set("Check")
        Radiobutton(self.root, text="Check", variable=self.payment_method, value="Check").place(x=150, y=430)
        Radiobutton(self.root, text="Paypal", variable=self.payment_method, value="Paypal").place(x=250, y=430)

        # Special Requests
        Label(self.root, text="Special Requests:").place(x=30, y=470)
        self.special_requests = Text(self.root, height=4, width=40)
        self.special_requests.place(x=150, y=470)

        # Submit Button
        submit_button = Button(self.root, text="Submit", command=self.submit_form)
        submit_button.place(x=250, y=550)

    def submit_form(self):
        # Retrieve form data
        full_name = self.full_name.get()
        address = self.address.get()
        phone_number = self.phone_number.get()
        email = self.email.get()
        arrival_date = self.arrival_date.get()
        arrival_time = self.arrival_time.get()
        departure_date = self.departure_date.get()
        departure_time = self.departure_time.get()
        num_adults = self.num_adults.get()
        num_kids = self.num_kids.get()
        payment_method = self.payment_method.get()
        special_requests = self.special_requests.get("1.0", END)

        # Validation and form submission logic can be added here
        if not full_name or not address or not phone_number or not email or not arrival_date or not departure_date:
            messagebox.showerror("Error", "Please fill in all required fields!")
        else:
            messagebox.showinfo("Success", "Reservation submitted successfully!")


# Main window for login
window = Tk()
window.resizable(0, 0)
window.title("LOGIN")

window_width = 960
window_height = 640
center_window(window, window_width, window_height)

# Background Image
bgImage = ImageTk.PhotoImage(Image.open("LoginBg.png"))
bgLabel = Label(window, image=bgImage)
bgLabel.place(x=0, y=0)

# title =  Label(text="HOTEL MANAGEMENT SYSTEM", font=("Times New Roman", 23), fg = 'white', bg='#89b0a4')
# title.place(x=300, y=1.5)

# Login Panel
panel_color = '#89b0a4'
panel = Frame(window, bg=panel_color, width=350, height=380, relief="raised", bd=2)
panel.place(x=70, y=150)

# Welcome Heading
heading = Label(panel, text="Welcome", font=("Garamond", 32, "bold"), fg='white', bg=panel_color)
heading.place(x=80, y=20)

# Username Entry
username_label = Label(panel, text="Username", font=("Arial", 12), bg=panel_color)
username_label.place(x=30, y=80)
username_entry = Entry(panel, font=("Arial", 12), width=31)
username_entry.place(x=30, y=110)

# Password Entry
password_label = Label(panel, text="Password", font=("Arial", 12), bg=panel_color)
password_label.place(x=30, y=140)
password_entry = Entry(panel, font=("Arial", 12), width=31, show='*')
password_entry.place(x=30, y=170)

# Show Password Checkbox
show_password_var = IntVar()
show_password_check = Checkbutton(panel, text="Show Password", font=("Arial", 12), variable=show_password_var, onvalue=1, offvalue=0, bg=panel_color, command=show_password)
show_password_check.place(x=30, y=200)

# Login Button
login_button = Button(panel, text="Login", font=("Garamond", 16, "bold"), width=20, fg="white", bg="#aeaf95", command=login)
login_button.place(x=45, y=270)

window.mainloop()