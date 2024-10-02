from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import random
# diri e import ang mysql connector
from tkinter import messagebox


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Reservation System")
        self.root.geometry("1295x550+230+220")
        
        #==============Variable==============
        self.var_conatct=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal =StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        #==============Titles================
        # Title Label
        title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold")
        title.place(x=0, y=0, width=1295, height=50)
        
        
        # Pwedi rani kuhaon ang "try except" na statement inig balak ninyo butangan og logo 
        #================Logo================
        # Try to load image
        try:
            img2 = Image.open("C:/Users/Admin/Desktop/hotel management_system/images/logohotel.png")
            img2 = img2.resize((100, 40), Image.ANTIALIAS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            lblimg.place(x=5, y=2, width=100, height=40)
            
        except Exception as e:
            print(f"Error loading image: {e}")
            # You can still display a placeholder label
            lblimg = Label(self.root, text="No Image", bd=0, relief=RIDGE)
            lblimg.place(x=5, y=2, width=100, height=40)
            
            

        # ======================= Frames ====================================
        # Label Frame for Room Booking Details
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details", font=("arial", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)
    
        # Label Frame for Room Booking Details
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details", font=("arial", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)
        
        # ======================= Labels and  Entry =========================
        # Customer contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(labelframeleft, textvariable = self.var_conatct, font=("arial", 13, "bold"), width=20)
        enty_contact.grid(row=0, column=1, sticky=W)
        
        # =========== Fetch Data button ===========
        
        btnFetchData = Button(labelframeleft, command=self.Fetch_contact, text="Fetch Data", font=("arial", 8, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=347, y=4)

        # Check-in Date
        check_in_date = Label(labelframeleft, font=("arial", 12, "bold"), text="Check-in Date:", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft, textvariable = self.var_checkin, font=("arial", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        # Check-out Date
        lbl_Check_out = Label(labelframeleft, font=("arial", 12, "bold"), text="Check-out Date:", padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)

        txt_Check_out = ttk.Entry(labelframeleft, textvariable = self.var_checkout, font=("arial", 13, "bold"), width=29)
        txt_Check_out.grid(row=2, column=1)
        
        # Room Type
        label_RoomType = Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable = self.var_roomtype, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType["value"] = ("Single", "Double", "Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, font=("arial", 12, "bold"), text="Available Room:", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        txtRoomAvailable = ttk.Entry(labelframeleft, textvariable = self.var_roomavailable, font=("arial", 13, "bold"), width=29)
        txtRoomAvailable.grid(row=4, column=1)

        # Meal
        lblMeal = Label(labelframeleft, font=("arial", 12, "bold"), text="Meal:", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        txtMeal = ttk.Entry(labelframeleft, textvariable = self.var_meal, font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No Of Days
        lblNoOfDays = Label(labelframeleft, font=("arial", 12, "bold"), text="No Of Days:", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft, textvariable = self.var_noofdays, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)
        
        # Paid Tax
        lblPaidTax = Label(labelframeleft, font=("arial", 12, "bold"), text="Paid Tax:", padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)

        txtPaidTax = ttk.Entry(labelframeleft, textvariable = self.var_paidtax, font=("arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = Label(labelframeleft, font=("arial", 12, "bold"), text="Sub Total:", padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)

        txtSubTotal = ttk.Entry(labelframeleft, textvariable = self.var_actualtotal, font=("arial", 13, "bold"), width=29)
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(labelframeleft, font=("arial", 12, "bold"), text="Total Cost:", padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)

        txtTotalCost = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=29)
        txtTotalCost.grid(row=9, column=1)
        
        # ======================= Button Frame ===============================
        btnBill = Button(labelframeleft, text="Bill", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)
        
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        
        
        # Pwedi rani kuhaon ang "try except" na statement inig ma butangan og image na para jud ani na frame
        # ==================== Right Side Image ====================
        try:
            img3 = Image.open(r"C:\Users\Admin\Desktop\hotel_management_system\images\bed.jpg")
            img3 = img3.resize((520, 200), Image.ANTIALIAS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        except Exception as e:
            print(f"Error loading image: {e}")
             # Display a placeholder label if the image cannot be loaded
            lblimg = Label(self.root, text="Image not available", font=("arial", 12, "bold"), bg="lightgrey")
            
        
        # ========================= Table Frame Search System =========================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("arial", 12, "bold"))
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_Search["values"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        # ===================== Show Data Table =====================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        # Corrected column names to match
        self.room_table = ttk.Treeview(details_table, columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noofdays"),  
                                xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # Table headings
        self.room_table.heading("contact", text="Contact")  # This is correct
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="No of Days")

        self.room_table["show"] = "headings"

        # Change "mobile" to "contact"
        self.room_table.column("contact", width=100)  # Corrected here
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)

        # Pack the Treeview widget into the details_table frame
        self.room_table.pack(fill=BOTH, expand=True)
        
    # ==================== All Data Fetch =======================
    def Fetch_contact(self):
        if self.var_conatct.get() == "":
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
        else:
            pass  # connect to customer class "input mysql.connector here And cursor to Fetch data"
                  # create a small frame to show data
                  # name
                  # gender
                  # email
                  # nationality
                  # Address
        
         # pwedi ra nako e send ang code inig kapoyan mo mag tan-aw sa video, just ask me
         # kay mag error sya kung ibutang nako ang code diri tapos wala ang DATABASE ug Customer Class    
        
if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()