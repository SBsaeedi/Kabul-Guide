import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#imported for rendering images, used.
from PIL import Image, ImageTk

#Main Class
class MainInterface():
    def __init__(self):
        self.mainpage() 
        self.data_base()

    #function to resize image for the size of window
    def resize_image(self,event):
        self.new_width = event.width
        self.new_height = event.height

        # global image
        self.image = self.copy_of_image.resize((self.new_width, self.new_height))
        # global photo
        self.photo = ImageTk.PhotoImage(self.image)

        self.label.config(image=self.photo)
        self.label.image = self.photo  # avoid garbage collection

    def data_base(self):
        global conn
        self.conn = sqlite3.connect('Afghanistanguide.db')
    def mainpage(self):
        self.root = Tk()

        #----Variable--------#
        self.USERNAME = StringVar()
        self.PASSWORD = StringVar()
        self.RegUser = StringVar()
        self.RegPassC = StringVar()
        self.RegPass = StringVar()

        #---design----#
        self.root.title("Title")
        self.root.geometry('800x600')

        self.frame = Frame(self.root, relief='raised', borderwidth=2)
        self.frame.pack(fill=BOTH, expand=YES)
        self.frame.pack_propagate(False)

        self.copy_of_image = Image.open("19489902486_2452959010_b.jpg")
        self.photo = ImageTk.PhotoImage(self.copy_of_image)

        self.label = Label(self.frame, image=self.photo)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)
        self.label.bind('<Configure>', self.resize_image)
        self.Title = Frame(self.frame, relief=SOLID)
        self.Title.pack(pady=180)

        self.lbl_display = Label(self.Title, text="KABUL GUIDE", font=('Times', 50, 'bold'))
        self.lbl_display.config(bg='black', fg='#F8657A')


        self.lbl_display.pack()
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Login", command=self.LoginMain)
        self.filemenu.add_command(label="Register", command=self.RegisterMain)
        self.filemenu.add_command(label="Admin", command=self.AdminLogin)
        self.menubar.add_cascade(label="Options", menu=self.filemenu)
        self.root.config(menu=self.menubar)

        self.root.mainloop()


    #------Code for User Login Starts--------#
    def LoginMain(self):


        self.loginform = Tk()
        self.loginform.title("Account Login")
        self.loginform.geometry('800x600')
        self.loginform.config(bg='#07052C')
        self.LoginForm()

    def LoginForm(self):
        global lbl_result, TopLoginForm, MidLoginForm
        self.TopLoginForm = Frame(self.loginform, width=600, height=100, bd=0, relief=SOLID)
        self.TopLoginForm.pack(side=TOP, pady=50)
        self.lbl_text = Label(self.TopLoginForm, text="User Login", font=('Times', 50), width=600)
        self.lbl_text.pack(fill=X)
        self.lbl_text.config(bg='white',fg='#07052C')
        self.MidLoginForm = Frame(self.loginform, width=600)
        self.MidLoginForm.pack(side=TOP, pady=50)
        self.MidLoginForm.config(bg='black')
        self.lbl_username = Label(self.MidLoginForm, text="Username:", font=('Times', 25), bd=18)
        self.lbl_username.grid(row=0)
        self.lbl_username.config(bg='black',fg='white')
        self.lbl_password = Label(self.MidLoginForm, text="Password:", font=('Times', 25), bd=18)
        self.lbl_password.grid(row=1)
        self.lbl_password.config(bg='black',fg='white')

        self.login_username = Entry(self.MidLoginForm, textvariable=self.USERNAME, font=('arial', 25), width=12)
        self.login_username.grid(row=0, column=1)
        self.login_password = Entry(self.MidLoginForm, textvariable=self.PASSWORD, font=('arial', 25), width=12, show="*")
        self.login_password.grid(row=1, column=1)
        self.btn_login = Button(self.MidLoginForm, text="Login", font=('arial', 18), width=32, command=self.Check_User_dict)
        self.btn_login.grid(row=2, columnspan=2, pady=20)
        self.btn_login.bind('<Return>', self.Check_User_dict)
        self.btn_login.config(bg='#1EB0E1',fg='white')


    #-----A supporting function to check if user exists or not------#

    def Check_User_dict(self,event=None):
            self.data_base()
            self.d = self.conn.execute('''Select * from user''').fetchall()

            self.user_dict={}
            for i in self.d:
                self.user_dict[i[1]] = i[2]
            complete = False
            while not complete:
                username = self.login_username.get()
                password = self.login_password.get()

                if not username in self.user_dict:
                    messagebox.showerror('Failed','User Not Found') # check to see if user does not exists

                    self.loginform.destroy()
                    self.loginMain()
                    break


                if password == self.user_dict[username]:  # check to see if password match

                    self.root.destroy()
                    self.loginform.destroy()
                    self.User_int()
                    complete = True
                else:
                    messagebox.showerror('Failed','Either of the two is incorrect')

    #----------Code For User Login End-----------#


    #---------Code for UserInterface Starts-------------------#
    def User_int(self):
        self.data_base()
        self.root_2 = Tk()
        self.root_2.geometry('800x800')
        self.root_2.resizable(0,0)

        self.frame_2 = Frame(self.root_2, relief='raised', borderwidth=2)
        self.frame_2.pack(fill=BOTH, expand=YES)
        self.frame_2.pack_propagate(False)
        canvas = Canvas(self.frame_2, width=800, height=800, bg='black')

        # pack the canvas into a frame/form
        canvas.pack(expand=YES, fill=BOTH)

        # load the .gif image file
        gif1 = ImageTk.PhotoImage(file='WhatsApp Image 2020-06-30 at 11.26.45 AM.jpeg')



        canvas.create_image(0, 0, image=gif1, anchor=NW)
        canvas.create_text(400, 120, fill="#F8657A", text="Welcome To کابل  ", font=('Times', 45, 'bold italic'))



        #buttons programming
        self.Title_buttons = Frame(canvas)
        self.Title_buttons.config(bg='black')

        self.Title_buttons.pack(pady=200,padx=5)

        self.hello_button = Button(self.Title_buttons, text="Shops", font=('Times', 18), width=8,height=2,command=self.details)
        self.hello_button.grid(row=0,column=0,padx=20,pady=5)
        self.hello_button.config(bg='#F8657A')

        self.hello_button2 = Button(self.Title_buttons, text="Hotels", font=('Times', 18), width=8,height=2,command=self.details_1)
        self.hello_button2.grid(row=0,column=1,padx=20,pady=5)
        self.hello_button2.config(bg='#F8657A')

        self.hello_button3 = Button(self.Title_buttons, text="Outdoor", font=('Times', 18), width=8,height=2,command=self.details_2)
        self.hello_button3.grid(row=0,column=2,padx=20,pady =5)
        self.hello_button3.config(bg='#F8657A')
        self.hello_button4 = Button(self.Title_buttons, text="Indoor", font=('arial', 18), width=8, height=2,
                                    command=self.details_3)
        self.hello_button4.grid(row=0, column=3, padx=20, pady=5)
        self.hello_button4.config(bg='#F8657A')
        self.hello_button5 = Button(self.Title_buttons, text="Hospitals", font=('arial', 18), width=8, height=2,
                                    command=self.details_4)
        self.hello_button5.grid(row=1, column=0, padx=20, pady=5)
        self.hello_button5.config(bg='#F8657A')
        self.hello_button6 = Button(self.Title_buttons, text="Apartmnts", font=('arial', 18), width=8, height=2,
                                    command=self.details_5)
        self.hello_button6.grid(row=1, column=1, padx=20, pady=5)
        self.hello_button6.config(bg='#F8657A')
        self.hello_button7 = Button(self.Title_buttons, text="Houses", font=('arial', 18), width=8, height=2,
                                    command=self.details_6)
        self.hello_button7.grid(row=1, column=2, padx=20, pady=5)
        self.hello_button7.config(bg='#F8657A')
        self.hello_button8 = Button(self.Title_buttons, text="Clinics", font=('arial', 18), width=8, height=2,
                                    command=self.details_7)
        self.hello_button8.grid(row=1, column=3, padx=20, pady=5)
        self.hello_button8.config(bg='#F8657A')
        self.hello_button9 = Button(self.Title_buttons, text="Banks", font=('arial', 18), width=8, height=2,
                                    command=self.details_8)
        self.hello_button9.grid(row=2, column=0, padx=20, pady=5)
        self.hello_button9.config(bg='#F8657A')

        self.hello_button10 = Button(self.Title_buttons, text="Institutes", font=('arial', 18), width=8, height=2,
                                    command=self.details_9)
        self.hello_button10.grid(row=2, column=1, padx=20, pady=5)
        self.hello_button10.config(bg='#F8657A')

        self.hello_button11 = Button(self.Title_buttons, text="Libraries", font=('arial', 18), width=8, height=2,
                                    command=self.details_10)
        self.hello_button11.grid(row=2, column=2, padx=20, pady=5)
        self.hello_button11.config(bg='#F8657A')

        self.hello_button12 = Button(self.Title_buttons, text="Restaurnts", font=('arial', 18), width=8, height=2,
                                    command=self.details_11)
        self.hello_button12.grid(row=2, column=3, padx=20, pady=5)
        self.hello_button12.config(bg='#F8657A')

        self.root_2.mainloop()

    #--------------------12 different functions for detail because we can't track which button is pressed as we have to destroy the window which has buttons----------#
    def details(self):
        self.root_2.destroy()
        self.view_details("Shops")
    def details_1(self):
        self.root_2.destroy()
        self.view_details("Hotels")
    def details_2(self):
        self.root_2.destroy()
        self.view_details("Outdoor")
    def details_3(self):
        self.root_2.destroy()
        self.view_details("Indoor")
    def details_4(self):
        self.root_2.destroy()
        self.view_details("Hospitals")
    def details_5(self):
        self.root_2.destroy()
        self.view_details("Apartments")
    def details_6(self):
        self.root_2.destroy()
        self.view_details("Houses")
    def details_7(self):
        self.root_2.destroy()
        self.view_details("Clinics")
    def details_8(self):
        self.root_2.destroy()
        self.view_details("Banks")
    def details_9(self):
        self.root_2.destroy()
        self.view_details("Institutes")
    def details_10(self):
        self.root_2.destroy()
        self.view_details("Libraries")
    def details_11(self):
        self.root_2.destroy()
        self.view_details("Restaurants")
    #-----------------Wrapper function for Next------------------------------------#

    def Next(self):
        self.counter+=1

        if self.counter==self.max:
            messagebox.showerror('Not possible','No more data')

        else:
            self.copy_of_image_det = Image.open(self.data_hotels[self.counter][4])
            self.image_det = self.copy_of_image_det.resize((450, 350))
            self.photo_det = ImageTk.PhotoImage(self.image_det)

            # avoid garbage collection
            self.label_det.config(image=self.photo_det)
            # global photo

            self.testbutton2.config(text= 'Place Name: ' +self.data_hotels[self.counter][2])
            self.phone_num.config(text='Phone Number: '+str(self.data_hotels[self.counter][5]))
            self.address.config(text='Address: '+self.data_hotels[self.counter][3])

    #-----------------wrapper function for Previous button--------------------------------------------#
    def Prev(self):

        self.counter=self.counter-1

        if self.counter < 0:
            messagebox.showerror('Not possible','You are on the first pic already')

        else:
            self.copy_of_image_det = Image.open(self.data_hotels[self.counter][4])
            self.image_det = self.copy_of_image_det.resize((450, 350))
            self.photo_det = ImageTk.PhotoImage(self.image_det)

            # avoid garbage collection
            self.label_det.config(image=self.photo_det)
            # global photo


            self.testbutton2.config(text='Place Name: ' + self.data_hotels[self.counter][2])
            self.phone_num.config(text='Phone Number: ' + str(self.data_hotels[self.counter][5]))
            self.address.config(text='Address: ' + self.data_hotels[self.counter][3])




    #-------------------------Exit button for file menu of user interface----------------------#
    def ExitUserInt(self):
        self.root_details.destroy()
        self.User_int()
    #---------------------function that displays all the items in user's second screen------------------------------------#
    def view_details(self,choice):
        self.data_base()
        self.counter = 0
        if choice == 'Shops':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Shops'""").fetchall()
        elif choice == 'Hotels':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Hotels'""").fetchall()
        elif choice == 'Outdoor':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Outdoor'""").fetchall()
        elif choice == 'Indoor':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Indoor'""").fetchall()
        elif choice == 'Hospitals':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Hospitals'""").fetchall()
        elif choice == 'Apartments':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Apartments'""").fetchall()
        elif choice == 'Houses':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Houses'""").fetchall()
        elif choice == 'Clinics':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Clinics'""").fetchall()
        elif choice == 'Banks':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Banks'""").fetchall()
        elif choice == 'Institutes':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Institutes'""").fetchall()
        elif choice == 'Libraries':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Libraries'""").fetchall()
        elif choice == 'Restaurants':
            self.data_hotels = self.conn.execute("""Select * From places WHERE Main = 'Restaurants'""").fetchall()




        self.d = self.data_hotels[0]
        self.max = len(self.data_hotels)
        self.title = self.data_hotels[0][1]


        self.root_details= Tk()
        self.root_details.geometry('1000x500')

        self.mainframe = Frame(self.root_details)
        self.mainframe.pack(side=TOP,fill=X)
        self.mainframe.config(bg='black')
        self.label_heading = Label(self.mainframe,text=self.title,font='times 28 bold italic')
        self.label_heading.config(fg='#F8657A')
        self.label_heading.config(bg='black')
        self.label_heading.pack(side=TOP)
        self.leftframe = Frame(self.mainframe,bg="#D3D3D3")
        self.leftframe.pack(side=LEFT,fill=Y,pady=20)
        self.copy_of_image_det = Image.open(str(self.d[4]))
        self.image_det = self.copy_of_image_det.resize((450, 350))
        # global photo
        self.photo_det = ImageTk.PhotoImage(self.image_det)

          # avoid garbage collection
        self.label_det = Label(self.leftframe, image=self.photo_det,bd=0, highlightthickness=0, relief='ridge')
        self.label_det.image = self.photo_det
        self.label_det.grid(row=0,column=0,padx=0,pady=0)

        self.rightframe = Frame(self.mainframe,bg="black")
        self.rightframe.pack(side=LEFT,fill=Y,pady =20)



        self.testbutton2 = Label(self.rightframe,text="Place Name: "+self.d[2],font='times 18 bold italic', width=80,pady=10,anchor=W)
        #self.testbutton2.grid(row=0, column=0, pady=10)
        self.testbutton2.pack()
        self.testbutton2.config(bg='black',fg='#F8657A')

        self.phone_num = Label(self.rightframe, text="Phone Number: Not Available ",font='times 18 bold italic',width=80, pady=10,anchor=W)
        self.phone_num.pack()
        self.phone_num.config(bg='black',fg='#F8657A')
        self.address = Label(self.rightframe, text="Address:"+self.d[3],font='times 18 bold italic',width=80, pady=10,anchor=W)
        self.address.pack()
        self.address.config(bg='black',fg='#F8657A')


        self.bottomframe = Frame(self.root_details,height=40)
        self.bottomframe.pack(side=BOTTOM,fill=X)
        self.bottomframe.config(bg='black')
        Photo_prev = Image.open('previous_ultraaa.jpg')
        resized_prev = Photo_prev.resize((150, 100))
        final_prev = ImageTk.PhotoImage(resized_prev)
        btn_prev = Button(self.bottomframe, image=final_prev,bd=0, highlightthickness=0, relief='ridge',command=self.Prev)

        btn_prev.pack(side=LEFT)





        Photo = Image.open('next_ultraaa.jpg')
        resized = Photo.resize((150, 100))
        final = ImageTk.PhotoImage(resized)


        btn = Button(self.bottomframe, image=final,bd=0, highlightthickness=0, relief='ridge',command=self.Next)
        btn.pack(side=RIGHT)


        # Menu Bar

        self.menubar_user = Menu(self.root_details)
        self.filemenu_user = Menu(self.menubar_user, tearoff=0)
        self.filemenu_user.add_command(label="Exit", command=self.ExitUserInt)
        self.menubar_user.add_cascade(label="Options", menu=self.filemenu_user)
        self.root_details.config(menu=self.menubar_user)
        self.root_details.mainloop()

    #----------------------User Interface code ends-------------------------------------------------#



    #----------------------------------Admin Code starts-----------------------------------------#

    def AdminLogin(self):
        #root.destroy()
        global loginform
        self.loginform = Tk()
        self.loginform.title("Admin Login")
        self.loginform.geometry('800x600')
        self.loginform.config(bg='#07052C')

        self.Admin_LoginForm()

    def Admin_LoginForm(self):
        global lbl_result, TopLoginForm, MidLoginForm
        self.TopLoginForm = Frame(self.loginform, width=600, height=100, bd=0, relief=SOLID)
        self.TopLoginForm.pack(side=TOP, pady=50)
        self.lbl_text = Label(self.TopLoginForm, text="Admin Login", font=('Times', 50), width=600)
        self.lbl_text.pack(fill=X)
        self.lbl_text.config(bg='white', fg='#07052C')
        self.MidLoginForm = Frame(self.loginform, width=600)
        self.MidLoginForm.pack(side=TOP, pady=50)
        self.MidLoginForm.config(bg='black')
        self.lbl_username = Label(self.MidLoginForm, text="Username:", font=('Times', 25), bd=18)
        self.lbl_username.grid(row=0)
        self.lbl_username.config(bg='black', fg='white')
        self.lbl_password = Label(self.MidLoginForm, text="Password:", font=('Times', 25), bd=18)
        self.lbl_password.grid(row=1)
        self.lbl_password.config(bg='black', fg='white')

        global username
        self.username = Entry(self.MidLoginForm, textvariable=self.USERNAME, font=('arial', 25), width=12)
        self.username.grid(row=0, column=1)
        global password
        self.password = Entry(self.MidLoginForm, textvariable=self.PASSWORD, font=('arial', 25), width=12, show="*")
        self.password.grid(row=1, column=1)
        self.btn_login = Button(self.MidLoginForm, text="Login", font=('Times', 18), width=30, command=self.CheckLoginAdmin)
        self.btn_login.grid(row=2, columnspan=2, pady=20)
        self.btn_login.config(bg='#2694B1', fg='white')
        self.btn_login.bind('<Return>', self.CheckLoginAdmin)

    def CheckLoginAdmin(self,event=None):
        self.username1 = self.username.get()
        self.password1 = self.password.get()
        if self.username1 == 'SabaSaeedi' and self.password1 == 'admin':

            self.AdminPortal()
        elif self.username1 == '' or self.password1 == '':
            messagebox.showerror("Error", "These fields are mandatory")
        else:
            messagebox.showerror("Error", "Incorrect Name or Password")
    def ExitAdminInt(self):
        self.adminportal.destroy()
        self.mainpage()


    def AdminPortal(self):
        self.root.destroy()
        self.loginform.destroy()

        self.data_base()

        self.adminportal = Tk()


        global USERNAME
        global PASSWORD
        global search_var
        global add_crud
        global add_phone
        global add_pics
        global option_string
        self.option_string = StringVar()
        self.add_pics = StringVar()
        self.add_phone = StringVar()
        self.add_crud = StringVar()
        self.search_var = StringVar()
        # self.USERNAME = StringVar()
        # self.PASSWORD = StringVar()
        self.wrapper1 = LabelFrame(self.adminportal, text="Registered Users")

        self.wrapper3 = LabelFrame(self.adminportal, text="Admin Functionalities")
        self.wrapper1.pack(fill="both", expand="no", padx=10, pady=10)

        self.wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)



        self.trv = ttk.Treeview(self.wrapper1, columns=(1,2,3,4,5,6), show="headings", height="8")
        self.trv.column(1,width=100)
        self.trv.column(2, width=100)
        self.trv.column(3, width=100)
        self.trv.column(4, width=100)
        self.trv.column(5, width=100)
        self.trv.column(6, width=100)

        self.trv.pack()
        self.ViewPlaces()
        self.verscrlbar = ttk.Scrollbar(self.wrapper1,
                                   orient="vertical",
                                   command=self.trv.yview)

        # Calling pack method w.r.to verical
        # scrollbar
        self.verscrlbar.pack(side='right', fill='x')

        # users = conn.execute('''Select * From user''').fetchall()
        # conn.commit()
        #
        # ViewUsers(users)

        self.trv.heading(1, text='ID')
        self.trv.heading(2, text='Main Category')
        self.trv.heading(3, text='Place')
        self.trv.heading(4, text='Address')
        self.trv.heading(5, text='Picture')
        self.trv.heading(6, text='PhoneNumber')



        self.lbl_mc = Label(self.wrapper3, text='Select Main Category')
        self.lbl_mc.grid(row=0, column=0, padx=5, pady=3)
        global dropdown
        self.dropdown = Entry(self.wrapper3, textvariable=self.option_string)
        self.dropdown.grid(row=0, column=2, padx=5, pady=3)

        self.option_string_sub = StringVar()



        self.lbl_place = Label(self.wrapper3, text='Select Any Place')
        self.lbl_place.grid(row=1, column=0, padx=5, pady=3)
        global dropdown_place
        self.dropdown_place = Entry(self.wrapper3, textvariable=self.option_string_sub)
        self.dropdown_place.grid(row=1, column=2, padx=5, pady=3)

        self.add_crud_add = Label(self.wrapper3, text='Address')
        self.add_crud_add.grid(row=2, column=0, padx=0, pady=3)
        global ent_add
        self.ent_add = Entry(self.wrapper3, textvariable=self.add_crud)
        self.ent_add.grid(row=2, column=2, padx=5, pady=3)
        # Phone
        self.add_crud_phone = Label(self.wrapper3, text='Phone Number')
        self.add_crud_phone.grid(row=0, column=6, padx=0, pady=3)
        global ent_add_phone
        self.ent_add_phone = Entry(self.wrapper3, textvariable=self.add_phone)
        self.ent_add_phone.grid(row=0, column=8, padx=5, pady=3)
        # Pictures
        self.add_crud_pics = Label(self.wrapper3, text='Pictures')
        self.add_crud_pics.grid(row=1, column=6, padx=0, pady=3)
        global ent_add_pics
        self.ent_add_pics = Entry(self.wrapper3, textvariable=self.add_pics)
        self.ent_add_pics.grid(row=1, column=8, padx=5, pady=3)

        # CRUD ADD
        self.btn_add = Button(self.wrapper3, text="Add", command=self.add_main_crud)
        self.btn_add.grid(row=4, column=2, padx=5, pady=3)

        # CRUD UPDATE
        self.btn_update = Button(self.wrapper3, text="Update", command=self.update_main_crud)
        self.btn_update.grid(row=4, column=4, padx=5, pady=3)

        # CRUD DELETE
        self.btn_delete = Button(self.wrapper3, text="Delete", command=self.delete)
        self.btn_delete.grid(row=4, column=6, padx=5, pady=3)

        self.adminportal.title("Admin Panel")
        self.adminportal.geometry("700x500")
        self.adminportal.resizable(0,0)
        self.trv.bind('<Double-Button-1>', self.getrow)

        self.menubar_admin = Menu(self.adminportal)
        self.filemenu_admin = Menu(self.menubar_admin, tearoff=0)
        self.filemenu_admin.add_command(label="Exit", command=self.ExitAdminInt)
        self.filemenu_admin.add_command(label="Users", command=self.Admin_User_Portal)
        self.menubar_admin.add_cascade(label="Options", menu=self.filemenu_admin)
        self.adminportal.config(menu=self.menubar_admin)

        self.adminportal.mainloop()

    def ViewUsers(self):
        self.root_users = Tk()
        self.trv = ttk.Treeview(self.root_users, columns=(1, 2, 3), show="headings", height="8")



        self.trv.pack()
        self.verscrlbar = ttk.Scrollbar(self.root_users,
                                        orient="vertical",
                                        command=self.trv.yview)

        self.trv.column(1, width=150)
        self.trv.column(2, width=150)
        self.trv.column(3, width=150)

        self.verscrlbar.pack(side='right', fill='x')



        self.trv.heading(1, text='ID')
        self.trv.heading(2, text='Name')
        self.trv.heading(3, text='Password')
        self.trv.delete(*self.trv.get_children())
        self.places = self.conn.execute('''Select * From user''').fetchall()
        self.conn.commit()
        for place in self.places:
            self.trv.insert('', 'end', values=place)

        self.root_users.geometry('500x300')
        self.root_users.mainloop()

    def ViewPlaces(self):
        self.trv.delete(*self.trv.get_children())
        self.places = self.conn.execute('''Select * From places''').fetchall()
        self.conn.commit()
        for place in self.places:

            self.trv.insert('', 'end', values=place)


    # -----This function below gets entry to the entry boxes when you click them------------------#

    def getrow(self,event):
        self.item = self.trv.item(self.trv.focus())
        self.option_string.set('')
        self.option_string.set(self.item['values'][1])

        self.option_string_sub.set(self.item['values'][2])
        self.add_crud.set(self.item['values'][3])
        self.add_phone.set(self.item['values'][5])
        self.add_pics.set(self.item['values'][4])

        self.x = self.conn.execute('''Select ID FROM places WHERE SUB=?''', (self.option_string_sub.get(),)).fetchall()
        self.id_grabbed = self.x[0][0]



    #Delete

    def delete(self):
        if messagebox.askyesno('Confirm?','Are you sure to delete?'):
            self.id_place = self.option_string_sub.get()

            self.query_del = self.conn.execute("""DELETE from places where Sub=?""", (self.id_place,))
            self.ViewPlaces()
            self.option_string.set('')

            self.option_string.set('')
            self.option_string_sub.set('')
            self.add_crud.set('')
            self.add_phone.set('')
            self.add_pics.set('')
        else:
            self.option_string.set('')
            self.option_string_sub.set('')
            self.add_crud.set('')
            self.add_phone.set('')
            self.add_pics.set('')



    # ADD

    def add_main_crud(self):

        self.main_category_add = self.dropdown.get()
        self.sub_category_add = self.dropdown_place.get()

        self.address_add = self.ent_add.get()
        self.phone_add = self.ent_add_phone.get()
        self.pics_add = self.ent_add_pics.get()
        self.select_all_crud = self.conn.execute('''Select * FROM places Where Main=?''',(self.main_category_add,)).fetchall()

        self.make_id = self.main_category_add[0:3] + '0' + str(len(self.select_all_crud) +1)
        self.conn.execute("Insert into places(ID,Main,Sub,Address,Pictures,PhoneNum) VALUES (?,?,?,?,?,?)",
                     (self.make_id, self.main_category_add, self.sub_category_add, self.address_add, self.pics_add, self.phone_add))
        self.ViewPlaces()
        self.option_string.set('')

        self.option_string.set('')
        self.option_string_sub.set('')
        self.add_crud.set('')
        self.add_phone.set('')
        self.add_pics.set('')
        self.conn.commit()

    #update
    def update_main_crud(self):


        self.main_category_update = self.dropdown.get()

        self.sub_category_update = self.dropdown_place.get()


        self.address_update = self.ent_add.get()

        self.phone_update = self.ent_add_phone.get()

        self.pics_update = self.ent_add_pics.get()
        if messagebox.askyesno('Confirm?','Are you sure?'):

            self.query_update = self.conn.execute('''UPDATE places SET Main=?, Sub=?,Address=?,Pictures=?, PhoneNum=? WHERE ID=?''',(self.dropdown.get(),self.sub_category_update,self.address_update,self.pics_update,self.phone_update,self.id_grabbed))
            self.ViewPlaces()
            self.option_string.set('')
            self.option_string_sub.set('')
            self.add_crud.set('')
            self.add_phone.set('')
            self.add_pics.set('')

        else:
            self.option_string.set('')
            self.option_string_sub.set('')
            self.add_crud.set('')
            self.add_phone.set('')
            self.add_pics.set('')

    #---------------------------USer---------------------------------------------#





    def Admin_User_Portal(self):
        self.adminportal.destroy()


        #self.root.destroy()
        #self.loginform.destroy()

        self.data_base()

        self.admin_user_portal = Tk()

        self.USERNAME_USER = StringVar()

        self.PASSWORD_USER =StringVar()
        self.ID_USER =StringVar()
        self.wrapper_user_1 = LabelFrame(self.admin_user_portal, text="Registered Users")

        self.wrapper_user_3 = LabelFrame(self.admin_user_portal, text="Admin Functionalities")
        self.wrapper_user_1.pack(fill="both", expand="no", padx=10, pady=10)

        self.wrapper_user_3.pack(fill="both", expand="yes", padx=20)

        self.trv_user = ttk.Treeview(self.wrapper_user_1, columns=(1, 2,3), show="headings", height="8")
        self.trv_user.column(1, width=200)
        self.trv_user.column(2, width=200)
        self.trv_user.column(3, width=200)


        self.trv_user.pack()
        self.verscrlbar = ttk.Scrollbar(self.wrapper_user_1,
                                        orient="vertical",
                                        command=self.trv_user.yview)


        self.verscrlbar.pack(side='right', fill='x')

        # users = conn.execute('''Select * From user''').fetchall()
        # conn.commit()
        #
        # ViewUsers(users)

        self.trv_user.heading(1, text='ID')
        self.trv_user.heading(2, text='User Name')
        self.trv_user.heading(3, text='Password')
        self.ViewUsers()

        #

        self.lbl_mc = Label(self.wrapper_user_3, text='ID')
        self.lbl_mc.grid(row=0, column=0, padx=5, pady=3)
        global dropdown
        self.dropdown = Entry(self.wrapper_user_3, textvariable=self.ID_USER)
        self.dropdown.grid(row=0, column=2, padx=5, pady=3)

        self.option_string_sub = StringVar()

        self.lbl_place = Label(self.wrapper_user_3, text='Name')
        self.lbl_place.grid(row=1, column=0, padx=5, pady=3)
        global dropdown_place
        self.dropdown_place = Entry(self.wrapper_user_3, textvariable=self.USERNAME_USER)
        self.dropdown_place.grid(row=1, column=2, padx=5, pady=3)

        self.add_crud_add = Label(self.wrapper_user_3, text='Password')
        self.add_crud_add.grid(row=2, column=0, padx=0, pady=3)
        global ent_add
        self.ent_add = Entry(self.wrapper_user_3, textvariable=self.PASSWORD_USER)
        self.ent_add.grid(row=2, column=2, padx=5, pady=3)

        # CRUD ADD
        self.btn_add = Button(self.wrapper_user_3, text="Add", command=self.add_user_crud)
        self.btn_add.grid(row=4, column=1 )

        # CRUD UPDATE`
        self.btn_update = Button(self.wrapper_user_3, text="Update", command=self.update_user_crud)
        self.btn_update.grid(row=4, column=2 )

        # CRUD DELETE
        self.btn_delete = Button(self.wrapper_user_3, text="Delete", command=self.delete_user)
        self.btn_delete.grid(row=4, column=3)
        #
        self.admin_user_portal.title("Admin Panel")
        self.admin_user_portal.geometry("700x500")
        self.admin_user_portal.resizable(0, 0)
        self.trv_user.bind('<Double-Button-1>', self.get_row_user)
        #
        self.menubar_admin_user = Menu(self.admin_user_portal)
        self.filemenu_admin_user = Menu(self.menubar_admin_user, tearoff=0)
        self.filemenu_admin_user.add_command(label="Exit", command=self.ExitAdminInt_user)

        self.menubar_admin_user.add_cascade(label="Options", menu=self.filemenu_admin_user)
        self.admin_user_portal.config(menu=self.menubar_admin_user)

        self.admin_user_portal.mainloop()

    def ExitAdminInt_user(self):
        self.admin_user_portal.destroy()
        self.mainpage()



    def ViewUsers(self):
        self.trv_user.delete(*self.trv_user.get_children())
        self.users = self.conn.execute('''Select * From user''').fetchall()
        self.conn.commit()
        for user in self.users:

            self.trv_user.insert('', 'end', values=user)



        # -----This function below gets entry to the entry boxes when you click them------------------#

    def get_row_user(self, event):
        self.item = self.trv_user.item(self.trv_user.focus())
        self.ID_USER.set(self.item['values'][0])

        self.USERNAME_USER.set(self.item['values'][1])
        self.PASSWORD_USER.set(self.item['values'][2])

        # self.x = self.conn.execute('''Select ID FROM user WHERE SUB=?''', (self.option_string_sub.get(),)).fetchall()
        # self.id_grabbed = self.x[0][0]

        # Below are methods of CRUD

        # Delete

    def delete_user(self):
        if messagebox.askyesno('Confirm?', 'Are you sure to delete?'):
            self.id_place = self.ID_USER.get()

            self.query_del = self.conn.execute("""DELETE from user where ID=?""", (self.id_place,))
            self.ViewUsers()
            self.option_string.set('')

            self.option_string.set('')
            self.option_string_sub.set('')
            self.add_crud.set('')
            self.add_phone.set('')
            self.add_pics.set('')
        else:
            self.option_string.set('')
            self.option_string_sub.set('')
            self.add_crud.set('')
            self.add_phone.set('')
            self.add_pics.set('')

        # ADD

    def add_user_crud(self):

        self.main_category_add = self.USERNAME_USER.get()
        self.sub_category_add = self.PASSWORD_USER.get()

        self.address_add = self.ID_USER.get()


        self.conn.execute("Insert into places(ID,Name,Password) VALUES (?,?,?)",
                          (self.address_add, self.main_category_add, self.sub_category_add))
        self.ViewUsers()
        self.option_string.set('')

        self.option_string.set('')
        self.option_string_sub.set('')
        self.add_crud.set('')
        self.add_phone.set('')
        self.add_pics.set('')
        self.conn.commit()
        # update

    def update_user_crud(self):

        self.main_category_update = self.USERNAME_USER.get()

        self.sub_category_update = self.PASSWORD_USER.get()

        self.address_update = self.ID_USER.get()


        if messagebox.askyesno('Confirm?', 'Are you sure?'):

            self.query_update = self.conn.execute(
                '''UPDATE user SET Name=?, Password=? WHERE ID=?''', (
                self.main_category_update, self.sub_category_update,
                self.address_update))
            self.ViewUsers()
            #self.ViewPlaces()
            self.ID_USER.set('')
            self.USERNAME_USER.set('')
            self.PASSWORD_USER.set('')

        else:
            self.ID_USER.set('')
            self.USERNAME_USER.set('')
            self.PASSWORD_USER.set('')

    #------------------------USer End-------------------------------------------#


    #----------------Registration--------------------------------------

    def RegisterMain(self):
        #root.destroy()

        self.loginform = Tk()
        self.loginform.title("Account Login")

        self.loginform.geometry('800x600')
        self.loginform.config(bg='#07052C')

        self.RegisterForm()

    def RegisterForm(self):
        global lbl_result, TopLoginForm, MidLoginForm
        self.TopLoginForm = Frame(self.loginform, width=600, height=100, bd=0, relief=SOLID)
        self.TopLoginForm.pack(side=TOP, pady=50)

        self.lbl_text = Label(self.TopLoginForm, text="Register Yourself", font=('Times', 50), width=600)
        self.lbl_text.pack(fill=X)
        self.lbl_text.config(bg='white', fg='#07052C')
        self.MidLoginForm = Frame(self.loginform, width=600)
        self.MidLoginForm.pack(side=TOP, pady=50)
        self.MidLoginForm.config(bg='black')
        self.lbl_username = Label(self.MidLoginForm, text="Username:", font=('Times', 25), bd=18)
        self.lbl_username.grid(row=0)
        self.lbl_username.config(bg='black', fg='white')
        self.lbl_password = Label(self.MidLoginForm, text="Password:", font=('Times', 25), bd=18)
        self.lbl_password.grid(row=1)
        self.lbl_password.config(bg='black', fg='white')
        self.lbl_confirm_password = Label(self.MidLoginForm, text="Confirm Password:", font=('Times', 25), bd=18)
        self.lbl_confirm_password.grid(row=2)
        self.lbl_confirm_password.config(bg='black', fg='white')
        self.lbl_result = Label(self.MidLoginForm, text="", font=('Times', 18))
        self.lbl_result.grid(row=3, columnspan=2)
        global reg_username
        global reg_password
        global c_password
        self.reg_username = Entry(self.MidLoginForm, textvariable=self.RegUser, font=('arial', 25), width=12)
        self.reg_username.grid(row=0, column=1)

        self.reg_password = Entry(self.MidLoginForm, textvariable=self.RegPass, font=('arial', 25), width=12, show="*")
        self.reg_password.grid(row=1, column=1)
        self.c_password = Entry(self.MidLoginForm, textvariable=self.RegPassC, font=('arial', 25), width=12, show="*")
        self.c_password.grid(row=2, column=1)
        self.btn_login = Button(self.MidLoginForm, text="Register", font=('Times', 18), width=30, command=self.AddUser)
        self.btn_login.grid(row=3, columnspan=2, pady=20)
        self.btn_login.config(bg='#2694B1', fg='white')
        self.btn_login.bind('<Return>', self.AddUser)

    def AddUser(self,event=None):
        self.data_base()
        if self.reg_password.get() != self.c_password.get():
            messagebox.showerror('Error', 'Passwords donot match')
        else:
            messagebox.showinfo('Success','User Registered')
            self.d = self.conn.execute("""Select * FROM user """).fetchall()
            length = len(self.d)
            total = length + 1
            self.conn.execute("Insert into user(ID,Name,Password) VALUES (?,?,?)",
                         ('U00' + str(total), self.reg_username.get(), self.c_password.get()))
            self.conn.commit()

            self.conn.close()


        self.loginform.destroy()
    #-----------------------------------Register user code ends-------------------------------------#


d = MainInterface()
