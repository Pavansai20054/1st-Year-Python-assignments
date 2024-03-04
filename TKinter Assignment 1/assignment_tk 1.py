from tkinter import *
from PIL import Image, ImageTk

# creation of variables
bg_color = "#3240bf"
title = "Cracker Tech..."
geo = "600x600"
font = "Times New Roman"

window = Tk()  # main window name
window.geometry(geo)  # geometry
window.resizable(height=False, width=False)  # size adjuster
window.title(title)  # title
img = Image.open("A:\\det.jpg")
img = img.resize((1000, 750), Image.LANCZOS)
tk_image = ImageTk.PhotoImage(img)
label = Label(window, image=tk_image, width=900, height=750)
label.pack()

# window.config(bg=bg_color)  # color
class Details:
    # function 1
    def __init__(self):
        self.ent1 = None
        self.ent2 = None
        self.ent3 = None
        self.gender_var = None
        self.ent5 = None
        self.ent6 = None
        self.ent7 = None

    def get_details(self):
        # label 1
        win = Toplevel()
        win.geometry("1000x700")
        win.resizable(height=False, width=False)
        img = Image.open("A:\\Background.jpg")
        img = img.resize((1000, 700), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(img)
        label = Label(win, image=tk_image, width=1200, height=700)
        label.pack()

        def destroy_page():
            win.destroy()

        lbl0 = Label(win, text="Application Form", fg="black", font=(font, 25, "bold"), bg="#0b74e3")
        lbl0.place(x=350, y=5)

        # label 2
        lbl1 = Label(win, width=15, text="Name", fg="black", bg="#d313e8", font=(font, 15, "bold"))
        lbl1.place(x=220, y=100)
        self.ent1 = Entry(win, font=(font, 18), bg="white")
        self.ent1.place(x=430, y=100)

        # label 3
        lbl2 = Label(win, width=15, text="Date Of Birth", fg="black", bg="#d313e8", font=(font, 15, "bold"))
        lbl2.place(x=220, y=140)
        self.ent2 = Entry(win, font=(font, 18), bg="white")
        self.ent2.place(x=430, y=140)

        # label 4
        lbl3 = Label(win, width=15, text="Age", fg="black", bg="#d313e8", font=(font, 15, "bold"))
        lbl3.place(x=220, y=180)
        self.ent3 = Entry(win, font=(font, 18), fg="black", bg="white")
        self.ent3.place(x=430, y=180)

        # label 5
        lbl4 = Label(win, width = 15, text="Gender", fg="black", bg="#d313e8", font=(font, 15, "bold"))
        lbl4.place(x=220, y=220)

        # Radio button
        self.gender_var = StringVar()
        self.gender_var.set("Male")  # Set default selection
        self.g1 = Radiobutton(win, text="Male", font=(font, 15, "bold"), variable=self.gender_var, value="Male", fg="black", bg = "#3320e3")
        self.g1.place(x=430, y=220)
        self.g2 = Radiobutton(win, text="Female", font=(font, 15, "bold"), variable=self.gender_var, value="Female", fg="black", bg= "#3320e3")
        self.g2.place(x=515, y=220)
        self.g3 = Radiobutton(win, text="Others", font=(font, 15, "bold"), variable=self.gender_var, value="Others", fg="black", bg= "#3320e3")
        self.g3.place(x=615, y=220)

        # label 6
        lbl5 = Label(win, width=15, text="Mobile Number", fg="black", bg="#d313e8", font=(font, 15, "bold"))
        lbl5.place(x=220, y=260)
        self.ent5 = Entry(win, font=(font, 18), fg="black", bg="white")
        self.ent5.place(x=430, y=260)

        # label 7
        lbl6 = Label(win, width=15, text="Gmail", fg="black", bg="#d313e8", font=(font, 15, "bold"))
        lbl6.place(x=220, y=300)
        self.ent6 = Entry(win, font=(font, 18), fg="black", bg="white")
        self.ent6.place(x=430, y=300)

        # label 8
        lbl7 = Label(win, width=15, text="Address", fg="black", bg="#d313e8", font=(font, 15, "bold"))
        lbl7.place(x=220, y=340)
        self.ent7 = Entry(win, font=(font, 18), fg="black", bg="white")
        self.ent7.place(x=430, y=340)

        # button
        btn = Button(win, text="submit", fg="black", bg="green", font=(font, 15), command=self.view_details)
        btn.place(x=490, y=400)

        btn = Button(win, text="close", fg="black", bg="yellow", font=(font, 15), command=destroy_page)
        btn.place(x=490, y=500)

        win.mainloop()

    def view_details(self):
        Name = self.ent1.get()
        Date_of_Birth = self.ent2.get()
        Age = self.ent3.get()
        Gender = self.gender_var.get()
        Mobile_Number = self.ent5.get()
        Gmail = self.ent6.get()
        Address = self.ent7.get()

        info = Toplevel()  # Another window
        info.geometry("1000x700")
        info.title("Details")
        info.resizable(height=False, width=False)
        img = Image.open("A:\\best.jpg")
        img = img.resize((1500, 750), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(img)
        label = Label(info, image=tk_image)#, width=1200, height=700)
        info.state("zoomed")
        label.pack()

        def destroy_page():
            info.destroy()
        
        def save_details():
            print("Your details have been saved.....")

        lbl0 = Label(info, text="Details", fg="black", font=("Trade Gothic Next HvyCd",25), bg="#0b74e3")
        lbl0.place(x = 660, y = 260)

        lbl1 = Label(info, width = 15, text="Name", fg="black", bg="#d313e8", font=("Seaford", 15))
        lbl1.place(x = 520, y = 320)
        lbl2 = Label(info, text = Name, font = (font, 15), fg="black", bg="#3f8a78")
        lbl2.place(x = 720, y = 320)

        lbl3 = Label(info, width = 15, text = "Date Of Birth", fg="black", bg="#d313e8", font=("Seaford", 15))
        lbl3.place(x = 520, y = 360)
        lbl4 = Label(info, text = Date_of_Birth, font = (font, 15), fg = "black", bg = "#3f8a78")
        lbl4.place(x = 720, y = 360)

        lbl5 = Label(info, width = 15, text = "Age", fg="black", bg="#d313e8", font=("Seaford", 15))
        lbl5.place(x = 520, y = 400)
        lbl6 = Label(info, text = Age, font = (font, 15), fg = "black", bg = "#3f8a78")
        lbl6.place(x = 720, y = 400)

        lbl7 = Label(info, width = 15, text = "Gender", fg = "black", bg = "#d313e8", font = ("Seaford", 15))
        lbl7.place(x = 520, y = 440)
        lbl8 = Label(info, text = Gender, font = (font, 15), fg = "black", bg = "#3f8a78")
        lbl8.place(x = 720, y = 440)

        lbl9 = Label(info, width = 15, text = "Mobile Number", fg = "black", bg = "#d313e8", font = ("Seaford", 15))
        lbl9.place(x = 520, y = 480)
        lbl10 = Label(info, text = Mobile_Number, font = (font, 15), fg = "black", bg = "#3f8a78")
        lbl10.place(x = 720, y = 480)

        lbl11 = Label(info, width = 15, text = "Gmail", fg = "black", bg = "#d313e8", font = ("Seaford", 15))
        lbl11.place(x = 520, y = 520)
        lbl12 = Label(info, text = Gmail, font = (font, 15), fg = "black", bg = "#3f8a78")
        lbl12.place(x = 720, y = 520)

        lbl13 = Label(info, width = 15, text = "Address", fg = "black", bg = "#d313e8", font = ("Seaford", 15))
        lbl13.place(x = 520, y = 560)
        lbl14 = Label(info, text = Address, font = (font, 15), fg = "black", bg = "#3f8a78")
        lbl14.place(x = 720, y = 560)

        btn = Button(info, text = "close", fg = "black", bg = "red", font = (font, 15), command = destroy_page)
        btn.place(x = 520, y = 600)

        btn = Button(info, text = "save", fg = "black", bg = "green", font = (font, 15), command = save_details)
        btn.place(x = 800, y = 600)

        info.mainloop()


obj = Details()

bt = Button(window, text="Click here to fill the Application Form", fg="yellow", bg="green", font=(font, 25),command=obj.get_details)
bt.place(x=50, y=250)

window.mainloop()