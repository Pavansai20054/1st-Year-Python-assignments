# importing required modules
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector
from tkcalendar import *

# connecting the database with the program
connect = mysql.connector.connect (
                                   host = 'localhost',
                                   user = 'root',
                                   password = ''
                                  )

cursor = connect.cursor(buffered = True)

try:
    cursor.execute('USE airline_reservation_system')
except mysql.connector.Error:
    pass  # No need to create the database here

# Using the table USER_INFORMATION in the database 'airline_reservation_system' if it exists, else create it
try:
    cursor.execute('USE airline_reservation_system')
    cursor.execute('DESCRIBE USER_INFORMATION')
except mysql.connector.Error:
    cursor.execute('''CREATE TABLE USER_INFORMATION 
                      (P_Id INT AUTO_INCREMENT PRIMARY KEY,
                       P_Name VARCHAR(50) NOT NULL,
                       DOB DATE,
                       P_Gender CHAR(10) NOT NULL,
                       P_Age INT,
                       Mobile_No VARCHAR(12) NOT NULL,
                       Address VARCHAR(100),
                       Gmail VARCHAR(100))'''
                   )


# defining the function to confirm the user to close the window or not 
def confirm_close():
    click = messagebox.askyesno("Exit", "Do you want to close the window")
    if click:
        root.destroy()

# Create the main window
root = Tk()
root.state("zoomed")
root.title("Home Page")
root.config(bg = "royalblue")

# Creating the heading section
head = Label (root, text = 'Home Page', font = ("Times New Roman", 30, "bold"), fg = "#1bf28e", bg = "black")
head.place(x = 0, y = 20, width = 1370, height = 50)

# Create a frame to hold the image label
frame = Frame(root)
frame.place(x = 750, y = 100, width = 610, height = 510)

# Load the images
try:
    image1 = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\1.jpg")
    image1 = image1.resize((610, 510), Image.LANCZOS)
    image1 = ImageTk.PhotoImage(image1)

    image2 = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\2.jpg")
    image2 = image2.resize((610, 510), Image.LANCZOS)
    image2 = ImageTk.PhotoImage(image2)

    image3 = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\3.jpg")
    image3 = image3.resize((610, 510), Image.LANCZOS)
    image3 = ImageTk.PhotoImage(image3)

    image4 = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\4.jpg")
    image4 = image4.resize((610, 510), Image.LANCZOS)
    image4 = ImageTk.PhotoImage(image4)

    image5 = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\5.jpg")
    image5 = image5.resize((610, 510), Image.LANCZOS)
    image5 = ImageTk.PhotoImage(image5)

    image6 = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\6.jpg")
    image6 = image6.resize((610, 510), Image.LANCZOS)
    image6 = ImageTk.PhotoImage(image6)

    image7 = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\7.jpg")
    image7 = image7.resize((610, 510), Image.LANCZOS)
    image7 = ImageTk.PhotoImage(image7)
except Exception as e:
    print("An error occurred:", str(e))

# Create a label to display the images
image_label = Label(frame)
image_label.place(x = 0, y = 0)

x = 1

def auto_image():
    global x
    if x == 7:
        x = 1
    if x == 1:
        image_label.config(image = image1)
    elif x == 2:
        image_label.config(image = image2)
    elif x == 3:
        image_label.config(image = image3)
    elif x == 4:
        image_label.config(image = image4)
    elif x == 5:
        image_label.config(image = image5)
    elif x == 6:
        image_label.config(image = image6)
    else:
        image_label.config(image = image7)
    x += 1
    root.after(2000, auto_image)  # 2000 milliseconds

auto_image()

# defining the home page interface
def user_information():
    root.withdraw()             # Hide the current window
    ars_home_window = Toplevel(root)

# class for user information
    class User_Information:
        def __init__(self, win):
            self.win = win
            self.win.state("zoomed")
            self.win.resizable(height = False, width = False)
            self.win.title("AIRWAY RESERVATION SYSTEM")

            l_title = Label(self.win, text = "AIRWAY RESERVATION SYSTEM SOFTWARE", font = ("Times New Roman", 30, "bold"), fg = "#1bf28e", bg = "royalblue")
            l_title.place(x = 0, y = 0, width = 1450, height = 70)

            # logo
            img_logo = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\logo.jpg")
            img_logo = img_logo.resize((60, 60), Image.LANCZOS)
            self.photo_logo = ImageTk.PhotoImage(img_logo)

            self.logo = Label(self.win, image=self.photo_logo)
            self.logo.place(x = 100, y = 5, width = 60, height = 60)

            # Image Frame
            image_frame = Frame(self.win, bd = 2, relief = RIDGE, bg = "black")
            image_frame.place(x = 600, y = 70, width = 770, height = 680)
            
            # image 1
            img1 = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\p1.jpg")
            img1 = img1.resize((770, 650), Image.LANCZOS)
            self.photo_image1 = ImageTk.PhotoImage(img1)

            self.img_1 = Label(self.win, image = self.photo_image1)
            self.img_1.place(x = 600, y = 70, width = 770, height = 680)

            # Main Frame
            main_frame = Frame(self.win, bd = 2, relief = RIDGE, bg = "#29576e")
            main_frame.place(x = 0, y = 70, width = 600, height = 680)

            # Label and Entry
            title = Label(main_frame, text = "Welcome to Indian Airlines", font = ("Times New Roman", 35, "bold"), bg = "#29576e", fg = "violet")
            title.place(x = 20, y = 10)

            # Passenger Name
            passenger_name = Label(main_frame, text = "Name ", font = ("arial", 20, "bold"), fg = "white", bg = "#29576e")
            passenger_name.place(x = 100, y = 80)

            name_ent = ttk.Entry(main_frame, font = ("arial", 20))
            name_ent.place(x = 250, y = 80)

            # Passenger DOB
            dob_age = StringVar()
            passenger_dob = Label(main_frame, text = "D.O.B ", font = ("arial", 20, "bold"), fg = "white", bg = "#29576e")
            passenger_dob.place(x = 100, y = 140)
            
            
            dob_ent = DateEntry(main_frame,  selectmode = "day", relief = FLAT, fg = "yellow", font = ("Times", 20 , "bold") , textvariable = dob_age)
            dob_ent.config(date_pattern = "yyyy-mm-dd")
            dob_ent.place(x = 250, y = 140, width = 180, height = 30)

            # Passenger Gender
            gender_label = Label(main_frame, text = "Gender", font = ("arial", 20, "bold"), fg = "white", bg = "#29576e")
            gender_label.place(x = 100, y = 200)
            
            gender_var = StringVar()
            gender_var.set("Male") # Set default selection
                
            male_button = Radiobutton(main_frame, text = "Male", font = ("arial", 20, "bold"), variable = gender_var, value = "Male", fg = "black", bg = "#29576e")
            male_button.place(x = 240, y = 200)

            female_button = Radiobutton(main_frame, text = "Female", font = ("arial", 20, "bold"), variable = gender_var, value = "Female", fg = "black", bg = "#29576e")
            female_button.place(x = 340, y = 200)
            
            others_button = Radiobutton(main_frame, text = "Others", font = ("arial", 20, "bold"), variable = gender_var, value = "Others", fg = "black", bg = "#29576e")
            others_button.place(x = 470, y = 200)

            # Passenger Age
            passenger_age = Label(main_frame, text = "Age ", font = ("arial", 20, "bold"), fg = "white", bg = "#29576e")
            passenger_age.place(x = 100, y = 260)

            age_ent = Entry(main_frame, font = ("arial", 20))
            age_ent.place(x = 250, y = 260)

            # Passenger Mobile Number
            passenger_mobile_no = Label(main_frame, text = "Mobile No. ", font=("arial", 20, "bold"), fg="white", bg="#29576e")
            passenger_mobile_no.place(x = 100, y = 320)

            mobile_number_ent = ttk.Entry(main_frame, font = ("arial", 20))
            mobile_number_ent.place(x = 250, y=320)

            # Passenger House Address
            passenger_address = Label(main_frame, text = "Address ", font = ("arial", 20, "bold"), fg = "white", bg = "#29576e")
            passenger_address.place(x = 100, y = 380)

            address_text = Text(main_frame, font = ("arial", 20), width = 20)
            address_text.place(x = 250, y = 380, height = 100)
            
            # Passenger Gmail ID
            passenger_gmail = Label(main_frame, text = "Gmail ", font = ("arial", 20, "bold"), fg = "white", bg = "#29576e")
            passenger_gmail.place(x = 100, y = 500)

            gmail_ent = ttk.Entry(main_frame, font = ("arial", 20))
            gmail_ent.place(x = 250, y = 500)

            def Registration():
                 cursor.execute(f'''INSERT INTO USER_INFORMATION (P_Name,DOB,P_Gender,P_Age,Mobile_No,Address, Gmail)
                 VALUES ('{name_ent.get()}','{dob_ent.get()}','{gender_var.get()}','{age_ent.get()}',
                 '{mobile_number_ent.get()}','{address_text.get("1.0", "end-1c")}','{gmail_ent.get()}')''')
                 connect.commit()
                 
            def submit_details():
                ars_home_window.withdraw()
                response = messagebox.askyesno("Submit", "Do you want to submit the details?")
                if response:
                    Registration()
                    next_window()
                else:
                    self.win.destroy()

            def on_button_hover(event):
                submit.configure(foreground = "red", background = "yellow")

            def on_button_leave(event):
                submit.configure(foreground = "black", background = "green")

            def next_window():
                next_win = Toplevel()
                next_win.state("zoomed")
                next_win.title("Passenger Details")
                next_win.config(bg = "black")

                next_win.mainloop()

            submit = Button(main_frame, text = "Submit", font = ("arial", 20), bg = "green", fg = "black", command = submit_details)
            submit.bind("<Enter>", on_button_hover)
            submit.bind("<Leave>", on_button_leave)
            submit.place(x = 380, y = 580)
            exit_button = Button(main_frame, text = "Exit", font = ("arial", 20), command = self.win.destroy, relief = RAISED, fg = "black", bg = "red")
            exit_button.place(x = 180, y = 580)
    
    obj = User_Information(ars_home_window)
    ars_home_window.mainloop()

# defining the function to show the message box on clicking on exit
def close ():
    response = messagebox.askyesno("Close", "Do you want to Exit")
    if response:
        root.destroy()

# defining the admin interface
def admin_information():
    root.withdraw()             # Hide the current window
    ars_admin_window = Toplevel()
    ars_admin_window.state ('zoomed')


# class for admin information
    class AdminInformation:
        def __init__(self, window):
            self.window = window
            self.window.state('zoomed')
            self.window.resizable(height=False, width=False)

            # Global variable to store the image
            self.photo_image = None

        def login(self):
            user = username.get()
            passcode = password.get()
    
            # Getting the captcha value
            captcha_value = str(ent.get())

            if user == "admin" and passcode == "Admin@123":
                # Checking if captcha is verified 
                if not captcha_value:
                    messagebox.showerror("Invalid", "Please enter the captch and verify first.")
                elif main == captcha_value:
                    self.window.withdraw()  # Hide the current window
                    self.admin()
                else:
                    messagebox.showerror("Failed", "Failed to verify the captcha. Reopen the window.")
            elif user == "" or passcode == "":
                messagebox.showerror("Invalid", "Please enter username and password.")
            elif user != "admin" or passcode != "Admin@123":
                messagebox.showerror("Invalid", "Invalid username and password.")
            elif user != "admin":
                messagebox.showerror("Invalid", "Please enter a valid username.")
            elif passcode != "Admin@123":
                messagebox.showerror("Invalid", "Please enter a valid password.")
        
        def show(self):
            if (check.get() == 0):
                ent_password.config (show = "")
            else:
                ent_password.config (show = "*")
            

        def admin(self):
            self.administration = Toplevel (self.window)
            self.administration.title("Administration")
            self.administration.state('zoomed')
            label = Label(self.administration, text = "Welcome to Administration Section", font = ("Arial", 30)).pack()

        def main_window(self):
            self.window.state('zoomed')
            self.window.title("Login Details")
            self.window.config(bg="black")

            # Load the image and resize it
            image = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\background.jpg")
            resized_image = image.resize((1360, 740), Image.LANCZOS)
            self.photo_image = ImageTk.PhotoImage(resized_image)  # Convert to PhotoImage
            l = Label(self.window, image = self.photo_image)
            l.place(x = 0, y = 0)

            frame = Frame(self.window, bg = "#37acf0", width = 500, height = 450, borderwidth = 2, highlightbackground="black", highlightthickness=2)
            frame.place(x = 30, y = 120)

            adminlogin = Label(frame, text = "Admin Login", font = ("Times", 25, "bold"), bg = "sky blue")
            adminlogin.place(x = 150, y = 10)

            Label(frame, text = "Username", font = ("Arial", 20, "bold"), bg = "sky blue").place(x = 30, y = 80)
            Label(frame, text = "Password", font = ("Arial", 20, "bold"), bg = "sky blue").place(x = 30, y = 140)

            global username, password, ent, main, check, ent_password
            username = StringVar()
            password = StringVar()
            
            check = IntVar(value = 0)

            ent_username = Entry(frame, textvariable = username, width = 20, bd = 2, bg = "#8c87ed", fg = "black", font = ("Times", 20))
            ent_username.place(x = 180, y = 80)
            ent_password = Entry(frame, textvariable = password, width = 20, bd = 2, bg = "#8c87ed", fg = "black", font = ("Times", 20), show = "*")
            ent_password.place(x = 180, y = 140)
            
            check_button = Checkbutton(frame, text = "show password", variable = check, onvalue = 0, offvalue = 1, relief = RAISED, bg = "skyblue", command = self.show, height = 2, width = 15, font = 20)
            check_button.place(x = 180, y = 180)

            btn1 = Button(frame, text = "Login", font = ("Times", 15, "bold"), bd = 5, command = self.login, relief = RAISED, fg = "black", bg = "green")
            btn1.place(x = 180, y = 390)
            btn2 = Button(frame, text = "Exit", font = ("Times", 15, "bold"), bd = 5, command = self.window.destroy, relief = RAISED, fg = "black", bg = "red")
            btn2.place(x = 280, y = 390)

            # Captcha Generator Section
            list1 = []
            for i in range(65, 91):  # ASCII characters
                word = chr(i)
                list1.append(word)

            for m in range(97, 123):
                word = chr(m)
                list1.append(word)

            for n in range(0, 9):
                list1.append(n)

            frame = LabelFrame(frame, text = "Captcha", font = ("Times New Roman", 20, "bold"), bg = "#0a49d1")
            frame.place(x = 130, y = 230)

            answer = random.choices(list1, k = 6)
            label1 = Label(frame, text = answer, fg = "#f0150a", bg = "black", font = ("Times New Roman", 25))
            label1.grid(column = 0, row = 0, columnspan = 3)

            ent = StringVar(value = '')
            ent1 = Entry(frame, width = 12, textvariable = ent, bg = "white", fg = "Indigo", font = ("Times New Roman", 15))
            ent1.grid(row = 2, column = 0)
            ent1.focus()

            label2 = Label(frame, text = "Enter the captcha here", fg = "black", bg = "violet", font = ("Times New Roman", 15))
            label2.grid(row = 1, column = 0)

            main = ''
            for i in answer:
                main = main + str(i)

            def answer_check():
                if main == str(ent.get()):
                    messagebox.showinfo("Verified", "You are successfully verified")
                else:
                    messagebox.showerror("Failed", "Failed to verify")

            btn = Button(frame, text = "Verify", fg = "black", bg = "green", command = answer_check, font = ("Times New Roman", 16), bd = 5, relief = RAISED)
            btn.grid(row = 2, column = 2)


    admin_info = AdminInformation(ars_admin_window)
    admin_info.main_window()
    ars_admin_window.mainloop()


# Create a buttons to open the choose window
pic = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\admin.jpg")
pic = pic.resize((300, 250), Image.LANCZOS)
tk_image = ImageTk.PhotoImage(pic)
btn2 = Button(root, image = tk_image, command = admin_information, bd = 10,bg = "blue", relief= RAISED)
btn2.place(x = 60, y = 250)

pic1 = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\user.jpg")
pic1 = pic1.resize((300, 250), Image.LANCZOS)
tk_image1 = ImageTk.PhotoImage(pic1)
btn3 = Button(root, image = tk_image1, command = user_information, bd = 10,bg = "green", relief=RAISED)
btn3.place(x = 400, y = 250)

pic2 = Image.open("A:\\All files\\My Projects\\1st-Year-Python-assignments\\Airline Reservation system\\Images\\close.jpg")
pic2 = pic2.resize((250, 100), Image.LANCZOS)
tk_image2 = ImageTk.PhotoImage(pic2)
btn4 = Button(root, image = tk_image2, command = close, bg = "red", relief = RAISED)
btn4.place(x = 260, y = 550)





root.protocol("WM_DELETE_WINDOW", confirm_close)
root.mainloop()