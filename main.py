from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import PyPDF2
from reportlab.pdfgen import canvas
#from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Querybox
from datetime import date
import mysql.connector
import ttkbootstrap as tk
from PIL import ImageTk

connection = mysql.connector.connect(host="localhost",user="root",password="",database="flask")
my_cursor = connection.cursor()


'''def check():
    global reg
    check_query = "SELECT MAX(DISTINCT `reg`) FROM sdmt WHERE `reg` != 0"
    my_cursor.execute(check_query)
    reg = my_cursor.fetchall()
    if reg is None:
        reg = 0
check()'''
root = tk.Window(themename="cyborg")
root.title("Student Database Management System")
root.geometry("900x700")
lb = tk.Label(root,text="STUDENT DATABASE MANAGEMENT SYSTEM",font=("Georgia,Italic",18))
lb.grid(row=0,column=2,padx=60)
scl_img = PhotoImage(file="image.gif")
def insrt():
    def submit():
        global reg
        reg = 0
        print(reg)
        check_query = "SELECT MAX(DISTINCT `reg`) FROM sdmt WHERE `reg` != 0"
        my_cursor.execute(check_query)
        reg = my_cursor.fetchall()
        reg = int(reg[0][0] or 0)
        print('>>',reg)
        if reg is None:
            reg = 0
        reg+=1
        regstr = str(reg)
        print(reg)
        name=e_name.get()
        clas = e_class.get()
        dob = e_dob.entry.get()
        add = e_add.get()
        city = e_city.get()
        state = e_state.get()
        zip = e_zip.get()
        messagebox.showinfo("Registration no.","Your reg. no. is "+regstr)
        insert_query = "INSERT INTO `sdmt`(`reg`,`name`, `class`, `dob`, `address`, `city`, `state`, `zip`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        vals = (regstr,name,clas,dob,add,city,state,zip)
        my_cursor.execute(insert_query,vals)
        connection.commit()


    top = Toplevel()
    top.geometry("600x600")
    top.title("Add data")
    '''e_reg= tk.Entry(top,width=25)
    reg = 1
    e_reg.insert(0,reg)
    reg+=1
    e_reg.grid(row=1,column=1,padx=20)'''
    e_name= tk.Entry(top,width=25)
    e_name.insert(0,"Enter name")
    e_name.grid(row=2,column=1,padx=20)
    e_class= tk.Entry(top,width=25)
    e_class.insert(0,"Enter class")
    e_class.grid(row=3,column=1,padx=20)
    e_dob= tk.DateEntry(top,width=21)
    e_dob.grid(row=4,column=1,padx=20)
    e_add= tk.Entry(top,width=25)
    e_add.insert(0,"Enter Address")
    e_add.grid(row=5,column=1,padx=20)
    e_city= tk.Entry(top,width=25)
    e_city.grid(row=6,column=1)
    e_city.insert(0,"Enter City")
    e_state= tk.Entry(top,width=25)
    e_state.grid(row=7,column=1)
    e_state.insert(0,"Enter State")
    e_zip= tk.Entry(top,width=25)
    e_zip.insert(0,"Enter Zip code")
    e_zip.grid(row=8,column=1,padx=20)
    mButton = tk.Button(top,text="Add to Database",command=submit)
    mButton.grid(row=9,column=0,padx=10,pady=10,ipadx=200,columnspan=2)


    '''lb_reg=tk.Label(top,text="Your reg.no.",font=("Helvetica",11))
    lb_reg.grid(row=1,column=0,padx=20)'''
    lb_name=tk.Label(top,text="Enter name",font=("Helvetica",11))
    lb_name.grid(row=2,column=0,padx=20)
    lb_class=tk.Label(top,text="Enter class",font=("Helvetica",11))
    lb_class.grid(row=3,column=0,padx=20)
    lb_dob=tk.Label(top,text="Enter DOB",font=("Helvetica",11))
    lb_dob.grid(row=4,column=0,padx=20)
    lb_city=tk.Label(top,text="Enter address",font=("Helvetica",11))
    lb_city.grid(row=5,column=0,padx=20)
    lb_city=tk.Label(top,text="Enter city",font=("Helvetica",11))
    lb_city.grid(row=6,column=0,padx=20)
    lb_state=tk.Label(top,text="Enter state",font=("Helvetica",11))
    lb_state.grid(row=7,column=0,padx=20)
    lb_zip=tk.Label(top,text="Enter zip code",font=("Helvetica",11))
    lb_zip.grid(row=8,column=0,padx=20)
    top.mainloop()


def show():
    top = Toplevel()
    top.title("View data")
    trv = tk.Treeview(top,columns=(1,2,3,4,5,6,7,8),height=15,show="headings")
    trv.column(1,anchor=CENTER,stretch=NO,width=100)
    trv.column(2,anchor=CENTER,stretch=NO,width=100)
    trv.column(3,anchor=CENTER,stretch=NO,width=100)
    trv.column(4,anchor=CENTER,stretch=NO,width=100)
    trv.column(5,anchor=CENTER,stretch=NO,width=100)
    trv.column(6,anchor=CENTER,stretch=NO,width=100)
    trv.column(7,anchor=CENTER,stretch=NO,width=100)
    trv.column(8,anchor=CENTER,stretch=NO,width=100)
    trv.heading(1,text="reg.no.")
    trv.heading(2,text="Name")
    trv.heading(3,text="Class")
    trv.heading(4,text="DOB")
    trv.heading(5,text="Address")
    trv.heading(6,text="City")
    trv.heading(7,text="State")
    trv.heading(8,text="Zip Code")
    trv.grid(row=0,column=0)
    show_query = "SELECT * FROM `sdmt`"
    my_cursor.execute(show_query)
    datas = my_cursor.fetchall()
    for data in datas:
        trv.insert('','end',value=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
    connection.commit()
    top.mainloop()

def srch():
    def find():
        f = Toplevel()
        f.title("Data")
        trv = tk.Treeview(f,columns=(1,2,3,4,5,6,7,8),height=15,show="headings")
        trv.column(1,anchor=CENTER,stretch=NO,width=100)
        trv.column(2,anchor=CENTER,stretch=NO,width=100)
        trv.column(3,anchor=CENTER,stretch=NO,width=100)
        trv.column(4,anchor=CENTER,stretch=NO,width=100)
        trv.column(5,anchor=CENTER,stretch=NO,width=100)
        trv.column(6,anchor=CENTER,stretch=NO,width=100)
        trv.column(7,anchor=CENTER,stretch=NO,width=100)
        trv.column(8,anchor=CENTER,stretch=NO,width=100)
        trv.heading(1,text="reg.no.")
        trv.heading(2,text="Name")
        trv.heading(3,text="Class")
        trv.heading(4,text="DOB")
        trv.heading(5,text="Address")
        trv.heading(6,text="City")
        trv.heading(7,text="State")
        trv.heading(8,text="Zip Code")
        trv.grid(row=0,column=0)
        id = e_reg.get()
        idint = int(id)
        my_data=(idint,)
        my_cursor.execute("SELECT * FROM `sdmt` where reg=%s",my_data)
        datas = my_cursor.fetchall()
        for data in datas:
            trv.insert('','end',value=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
        connection.commit()
    top = Toplevel()
    top.geometry("353x200")
    top.title("Search data")
    e_reg= tk.Entry(top,width=25)
    e_reg.insert(0,"Enter registration number")
    e_reg.grid(row=1,column=1,padx=20)
    btn = tk.Button(top,text="Search",command=find)
    btn.grid(row=2,column=1,padx=20)
    top.mainloop()
def dele():
    def find():
        id = e_del.get()
        delete_query= "DELETE FROM `sdmt` WHERE `reg` = "+id
        my_cursor.execute(delete_query)
        connection.commit()
    top = Toplevel()
    top.geometry("353x200")
    top.title("Delete data")
    e_del= tk.Entry(top,width=25)
    e_del.insert(0,"Enter registration number")
    e_del.grid(row=1,column=1,padx=20)
    btn = tk.Button(top,text="Delete",command=find)
    btn.grid(row=2,column=1,padx=20)
    top.mainloop()
def scl():
    webbrowser.open("youtube.com")


def rec():
    def gen():
        id = e_reg.get()
        from reportlab.pdfgen import canvas
        mypath = 'C:\\Users\\sharm\\PycharmProjects\\Student Database Management System\\my_pdf.pdf'
        from reportlab.lib.units import inch
        from reportlab.lib.pagesizes import letter,A4
        from datetime import date
        import mysql.connector
        connection = mysql.connector.connect(host="localhost",user="root",password="",database="sdmt_db")
        my_cursor = connection.cursor()
        def vw():
            path = 'my_pdf.pdf'
            webbrowser.open_new(path)
        btn = tk.Button(top,text="view",command=vw)
        btn.grid(row=5,column=1)



            
        def my_temp():
            c.translate(inch,inch)
            c.setStrokeColorRGB(0.1,0.8,0.1)
            c.setFillColorRGB(0,0,1)
            c.drawString(0,9*inch,"1234,ABCD Road")
            c.drawString(0,8.7*inch,"MyCity,ZIP : 1234")
            c.setFillColorRGB(0,0.5,1)
            c.drawString(2*inch,8.7*inch," XYZ School ")
            c.setFillColorRGB(0,0,0)
            c.line(0,8.6*inch,6.8*inch,8.6*inch)
            dt = date.today().strftime('%d-%b-%Y')
            c.drawString(5.6*inch,9.3*inch,dt)
            c.setFont("Helvetica",8)
            c.drawString(3*inch,9.6*inch,'Student details')
            c.line(0,-0.7*inch,6.8*inch,-0.7*inch)
            c.setFillColorRGB(1,0,0)
            c.drawString(0,-0.9*inch,u"\u00A9"+"@XYZ School")
            c.rotate(45)
            c.setFillColorCMYK(0,0,0,0.08)
            c.setFont("Helvetica",100)
            c.drawString(3*inch,1*inch,"Sample")
            c.rotate(-45)
            return c
        c=canvas.Canvas(mypath,pagesize=letter)
        c=my_temp()
        c.setFillColorRGB(0,0,1)
        c.setFont("Helvetica",70)
        c.drawString(1.7*inch,7.5*inch,'Details')
        c.setFillColorRGB(0,0,0)
        c.setFont("Helvetica",24)
        c.drawString(1.15*inch,6.8*inch,'Reg.No. :')
        c.drawString(1.5*inch,6*inch,'Name :')
        c.drawString(1.56*inch,5.2*inch,'Class :')
        c.drawString(1.64*inch,4.4*inch,'DOB :')
        c.drawString(1.19*inch,3.6*inch,'Address :')
        c.drawString(1.76*inch,2.8*inch,'City :')
        c.drawString(1.59*inch,2*inch,'State :')
        c.drawString(1.1*inch,1.2*inch,'Zip code :')
        c.drawString(5*inch,-0.4*inch,'Signature')
        my_val = [id,]
        my_cursor.execute("SELECT * FROM `sdmt` where reg=%s",my_val)
        data = my_cursor.fetchone()

        c.drawString(3*inch,6.8*inch,str(data[0]))
        c.drawString(3*inch,6*inch,str(data[1]))
        c.drawString(3*inch,5.2*inch,str(data[2]))
        c.drawString(3*inch,4.4*inch,str(data[3]))
        c.drawString(3*inch,3.6*inch,str(data[4]))
        c.drawString(3*inch,2.8*inch,str(data[5]))
        c.drawString(3*inch,2*inch,str(data[6]))
        c.drawString(3*inch,1.2*inch,str(data[7]))



        c.showPage()
        c.save()



    top = Toplevel()
    top.geometry("353x200")
    top.title("Generate Receipt")
    e_reg= tk.Entry(top,width=25)
    e_reg.insert(0,"Enter registration number")
    e_reg.grid(row=1,column=1,padx=20)
    btn = tk.Button(top,text="Generate",command=gen)
    btn.grid(row=2,column=1,padx=20)
    top.mainloop()

myStyle = tk.Style()
myStyle.configure('primary.TButton',font = ("Helvetica",15))


btn_insrt = tk.Button(root,text="Add a record to database",style='primary.TButton',command=insrt,width=30)
btn_insrt.grid(row=3,column=2,columnspan=2,pady=20)


btn_show = tk.Button(root,text="Show Database table",style='primary.TButton',command=show,width=30)
btn_show.grid(row = 5,column=2,columnspan=2,pady=20)


btn_srch = tk.Button(root,text="Search student from database",style='primary.TButton',command=srch,width=30)
btn_srch.grid(row=7,column=2,columnspan=2,pady=20)


btn_del = tk.Button(root,text="Delete student from database",style='primary.TButton',command=dele,width=30)
btn_del.grid(row = 9,column=2,columnspan=2,pady=20)


btn_scl = tk.Button(root,text="Open School Website",command=scl,style='primary.TButton',width=30)
btn_scl.grid(row=11,column=2,pady=20)


btn_rec = tk.Button(root,text = "Generate Receipt",command = rec,width=30,style='primary.TButton')
btn_rec.grid(row=13,column=2,pady=20)


root.mainloop()
