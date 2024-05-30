from tkinter import *
import project_back as pb

class Student:
    
    def __init__(self,root):
       self.root=root 
       self.root.title("Medical system of student data management")
       self.root.config(bg="white")
   
       stdId=StringVar()
       Firstname=StringVar()
       Surname=StringVar()
       DoB=StringVar()
       Age=StringVar()
       Gender=StringVar()
       Adress=StringVar()
       Mobile=StringVar()

       pb.studentData()
       def clearData():
              self.txtStdId.delete(0,END)
              self.txtFirstname.delete(0,END)
              self.txtSurname.delete(0,END)
              self.txtDob.delete(0,END)
              self.txtAge.delete(0,END)
              self.txtGender.delete(0,END)
              self.txtAdress.delete(0,END)
              self.txtMobile.delete(0,END) 
       pb.studentData() 

       def addData():
              if(len(stdId.get())!=0):
                     pb.addStdRec(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get())
                     studentlist.delete(0,END)
                     studentlist.insert(END,(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get()))

       def displayData():
              studentlist.delete(0, END)
              for row in pb.viewData():
                     studentlist.insert(END, row)

       def StudentRec(event):
              global sd
              searchstd = studentlist.curselection()[0]
              sd = studentlist.get(searchstd)
              self.txtStdId.delete(0, END)
              self.txtStdId.insert(END, sd[0])
              self.txtFirstname.delete(0, END)
              self.txtFirstname.insert(END, sd[1])
              self.txtSurname.delete(0, END)
              self.txtSurname.insert(END, sd[2])
              self.txtDob.delete(0, END)
              self.txtDob.insert(END, sd[3])
              self.txtAge.delete(0, END)
              self.txtAge.insert(END, sd[4])
              self.txtGender.delete(0, END)
              self.txtGender.insert(END, sd[5])
              self.txtAdress.delete(0, END)
              self.txtAdress.insert(END, sd[6])
              self.txtMobile.delete(0, END)
              self.txtMobile.insert(END, sd[7])

                        
       def deleteData():
              if(len(stdId.get()) != 0):
                     pb.deleteRec(sd[0])
                     clearData()
                     displayData()

       def updateData():
              if(len(stdId.get()) != 0):
                     pb.dataUpdate(sd[0], stdId.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get())
                     studentlist.delete(0, END)
                     studentlist.insert(END, (stdId.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get()))

       def searchDatabase():
              studentlist.delete(0,END)
              for row in pb.searchData(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get()):
                     studentlist.insert(END,row,str(""))         

       #Frames
       MainFrame=Frame(self.root,bg="white", padx=40,pady=20,)
       MainFrame.pack()
       TitFrame=Frame(MainFrame,padx=20,pady=40,bg="white",relief=RIDGE)
       TitFrame.pack(side=TOP)
    
       self.lblTit=Label(TitFrame,font=('arial',30,),text="Database management system for the medical part of the institute",bg="white",fg="black")
       self.lblTit.grid()

       DataFrame=Frame(MainFrame,padx=20,pady=40,bg="skyblue",relief=RIDGE)
       DataFrame.pack(side=BOTTOM)
         
       DataFrameLeft = LabelFrame(DataFrame, font=('arial', 16), width=400, height=400, padx=20, pady=20, bg="Ghost White", text="Student info\n")
       DataFrameLeft.grid(row=0)

       ButtonFrameLeft = Frame(DataFrame, width=400, height=400, padx=20, bg="skyblue", pady=10)
       ButtonFrameLeft.grid(row=1, column=0)

       DataFrameRight = LabelFrame(DataFrame, font=('arial', 16), width=500, height=400, padx=10, pady=15, bg="Ghost White", text="Student details\n")
       DataFrameRight.grid(row=0, column=1)

       ButtonFrameRight = Frame(DataFrame, width=400, height=400, padx=20, bg="skyblue", pady=10)
       ButtonFrameRight.grid(row=1, column=1)

       for widget in DataFrame.winfo_children():
              widget.grid_configure(padx=10, pady=5)     

       #Lables and entry widget
       self.lblStdId=Label(DataFrameLeft,font=('arial',12),padx=2,pady=3,text="Id:",bg="ghost white")
       self.lblStdId.grid(row=0,column=0,sticky=W)
       self.txtStdId=Entry(DataFrameLeft,font=('arial',12),textvariable=stdId,bg="ghost white",width=39)
       self.txtStdId.grid(row=0,column=1)

       self.lblFirstname=Label(DataFrameLeft,font=('arial',12),padx=2,pady=3,text="Name:",bg="ghost white")
       self.lblFirstname.grid(row=1,column=0,sticky=W)
       self.txtFirstname=Entry(DataFrameLeft,font=('arial',12),textvariable=Firstname,bg="ghost white",width=39)
       self.txtFirstname.grid(row=1,column=1)

       self.lblSurname=Label(DataFrameLeft,font=('arial',12),padx=2,pady=3,text="Surname:",bg="ghost white")
       self.lblSurname.grid(row=2,column=0,sticky=W)
       self.txtSurname=Entry(DataFrameLeft,font=('arial',12),textvariable=Surname,bg="ghost white",width=39)
       self.txtSurname.grid(row=2,column=1)

       self.lblDob=Label(DataFrameLeft,font=('arial',12),padx=2,pady=3,text="Date of Birth",bg="ghost white")
       self.lblDob.grid(row=3,column=0,sticky=W)
       self.txtDob=Entry(DataFrameLeft,font=('arial',12),textvariable=DoB,bg="ghost white",width=39)
       self.txtDob.grid(row=3,column=1)

       self.lblAge=Label(DataFrameLeft,font=('arial',12),padx=2,pady=3,text="Age:",bg="ghost white")
       self.lblAge.grid(row=4,column=0,sticky=W)
       self.txtAge=Entry(DataFrameLeft,font=('arial',12),textvariable=Age,bg="ghost white",width=39)
       self.txtAge.grid(row=4,column=1)

       self.lblGender=Label(DataFrameLeft,font=('arial',12),padx=2,pady=3,text="Gender:",bg="ghost white")
       self.lblGender.grid(row=5,column=0,sticky=W)
       self.txtGender=Entry(DataFrameLeft,font=('arial',12),textvariable=Gender,bg="ghost white",width=39)
       self.txtGender.grid(row=5,column=1)

       self.lblAdress=Label(DataFrameLeft,font=('arial',12),padx=2,pady=3,text="Address:",bg="ghost white")
       self.lblAdress.grid(row=6,column=0,sticky=W)
       self.txtAdress=Entry(DataFrameLeft,font=('arial',12),textvariable=Adress,bg="ghost white",width=39)
       self.txtAdress.grid(row=6,column=1)

       self.lblMobile=Label(DataFrameLeft,font=('arial',12),padx=2,pady=3,text="Phone number:",bg="ghost white")
       self.lblMobile.grid(row=7,column=0,sticky=W)
       self.txtMobile=Entry(DataFrameLeft,font=('arial',12),textvariable=Mobile,bg="ghost white",width=39)
       self.txtMobile.grid(row=7,column=1)

       #List box and scrollBar widget
       scrollbar=Scrollbar(DataFrameRight)
       scrollbar.grid(row=0 ,column=1,sticky='ns')

       studentlist=Listbox(DataFrameRight,width=68,height=12,font=('arial',12), yscrollcommand=scrollbar.set)
       studentlist.bind('<<ListboxSelect>>',StudentRec)
       studentlist.grid(row=0,column=0,padx=10)
       scrollbar.config(command= studentlist.yview)

       displayData()

       # Buttons
       self.btnAddData = Button(ButtonFrameLeft, text="Add", font=('arial', 16), height=1, width=10, command=addData)
       self.btnAddData.grid(row=0, column=0)

       self.btnClearData = Button(ButtonFrameLeft, text="Clear", font=('arial', 16), height=1, width=10, command=clearData)
       self.btnClearData.grid(row=0, column=1)

       self.btnUpdateData = Button(ButtonFrameLeft, text="Update", font=('arial', 16), height=1, width=10, command=updateData)
       self.btnUpdateData.grid(row=1, column=0)

       self.btnDeleteData = Button(ButtonFrameLeft, text="Delete", font=('arial', 16), height=1, width=10, command=deleteData)
       self.btnDeleteData.grid(row=1, column=1)

       self.btnDisplayData = Button(ButtonFrameRight, text="Display", font=('arial', 16), height=1, width=10, command=displayData)
       self.btnDisplayData.grid(row=0, column=0)

       self.btnSearchData = Button(ButtonFrameRight, text="Search", font=('arial', 16), height=1, width=10, command=searchDatabase)
       self.btnSearchData.grid(row=0, column=1)
       
       for widget in ButtonFrameLeft.winfo_children():
              widget.grid_configure(padx=10, pady=5)

       for widget in ButtonFrameRight.winfo_children():
              widget.grid_configure(padx=10, pady=5)

if __name__=='__main__':
   root=Tk()
   application=Student(root)
   root.mainloop()