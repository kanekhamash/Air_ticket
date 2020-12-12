#Created by Kane Khamash
#12/12/2020
from tkinter import*
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import messagebox as tkMessageBox

# Create GUI
root =Tk()
root.title('Booking_Plane_Tickets')
w = 1200
h = 650
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - w) / 2
y = (sh - h) / 2 - 40
root.geometry( '%dx%d+%d+%d' % (w, h, x, y))
root.config(bg="#443565")

#Create fonts
fnt1 = ("Italic", 45, "bold")
fnt2 = ("Italic", 25, "bold")
fnt3 = ("Italic", 20, "bold")
fnt4 = ("Italic", 18, "bold")
fnt5 = ("Italic", 14, "bold")

#Create String Var
name = StringVar()
address = StringVar()
mobile = StringVar()
date_fly = StringVar()
time_fly = StringVar()
from1 = StringVar()
destination = StringVar()
passeneger = StringVar()
price = StringVar()

#Crreate DataBase
def creat_database():
       db = mysql.connector.connect(
         user='root',
         passwd='',
         host='localhost'
         
       )
       cursor = db.cursor()
       cursor.execute('CREATE DATABASE IF NOT EXISTS air_ticket28')
       cursor.close()
       db.close()


creat_database()

#Create Table
def creat_table():
       db = mysql.connector.connect(
           user='root',
           passwd='',
           host='localhost',
           database='air_ticket28'
)    
       cursor = db.cursor()
       cursor.execute('CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),address VARCHAR(255),mobile VARCHAR(255),from1 VARCHAR(255),destination VARCHAR(255),date_fly VARCHAR(255),time_fly VARCHAR(255),price VARCHAR(255))')
       db.commit()
       cursor.close()
       db.close()
creat_table()


#Create function to check the field it is empty or not,if not empty start to add the information in the table in database
def get_info_new_frame():
    

    if name.get()== '' :
        messagebox.showinfo('Error empty field','Please enter your name')
    elif address.get() == '':
           messagebox.showinfo('Error empty field','Please enter your address')
    elif mobile.get() == '':
           messagebox.showinfo('Error empty field','Please enter your mobile number')
    elif date_fly.get() == '':
           messagebox.showinfo('Error empty field','Please enter date trip')
    elif time_fly.get() == '':
           messagebox.showinfo('Error empty field','Please enter time trip')
    elif from1.get() == '':
           messagebox.showinfo('Error empty field','Please enter your Airport')           
    elif destination.get() == '':
           messagebox.showinfo('Error empty field','Please enter your destination')           
    
    elif price.get() == '':
           messagebox.showinfo('Error empty field','Please enter price trip')
    else:           
           db = mysql.connector.connect(
    user='root',
    passwd='',
    host='localhost',
    database='air_ticket28'
    
    
  
    )
           global cursor
           cursor = db.cursor()
           #label_result.config(text='My full name is :' + FirstName.get() + ' '+ LastName.get())
           sql = "INSERT INTO customers(name, address , mobile , from1 , destination,date_fly,time_fly,price) values (%s,%s,%s,%s,%s,%s,%s,%s)"
           

           val = (name.get(), address.get(),mobile.get(),from1.get(),destination.get(),date_fly.get(),time_fly.get(),price.get())
           
           
           cursor.execute(sql, val)
           db.commit()
           
           print(cursor.rowcount, 'record(s) inserted')
           cursor.close()
           db.close()
           name.set('')
           address.set('')
           mobile.set('')
           date_fly.set('')
           time_fly.set('')
           from1.set('')
           destination.set('')
           passeneger.set('')
           price.set('')
           messagebox.showinfo('Add Passeneger','Passenger added successfully')
           
               


#Create new GUI    
def show_data():
    
    window2= Tk()
    w = 1200
    h = 500
    sw = window2.winfo_screenwidth()
    sh = window2.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2 - 60
    window2.geometry( '%dx%d+%d+%d' % (w, h, x, y))
    window2.config(bg="#443565")

    passeneger = StringVar()

    db = mysql.connector.connect(
    user='root',
    passwd='',
    host='localhost',
    database='air_ticket28'
    )
    cursor = db.cursor()  
    cursor.execute('SELECT * FROM customers')
    result = cursor.fetchall()
    #Create treeview
    my_tree = ttk.Treeview(window2)
    my_tree['columns'] = ('Name','Address','Mobile','From','To','Date','Time','Price')

    my_tree.column('#0',width=0,stretch=NO)
    my_tree.column('Name',anchor=W,width=120,minwidth=25)
    my_tree.column('Address',anchor=W,width=120,minwidth=25)
    my_tree.column('Mobile',anchor=W,width=120,minwidth=25)
    my_tree.column('From',anchor=W,width=120,minwidth=25)
    my_tree.column('To',anchor=W,width=120,minwidth=25)
    my_tree.column('Date',anchor=W,width=120,minwidth=25)
    my_tree.column('Time',anchor=W,width=120,minwidth=25)
    my_tree.column('Price',anchor=W,width=120,minwidth=25)

    #my_tree.heading('#0',text='Label',anchor=W)
    my_tree.heading('Name',text='Name',anchor=W)
    my_tree.heading('Address',text='Address',anchor=W)
    my_tree.heading('Mobile',text='Mobile',anchor=W)
    my_tree.heading('From',text='From',anchor=W)
    my_tree.heading('To',text='To',anchor=W)
    my_tree.heading('Date',text='Date',anchor=W)
    my_tree.heading('Time',text='Time',anchor=W)
    my_tree.heading('Price',text='Price',anchor=W)

    cursor.execute('SELECT * FROM customers')
    result = cursor.fetchall()
    #Create function to display all passenger 
    def check_all_passenger():
            i = 0
            for row in result:
                my_tree.insert('',index='end',iid=i,text='Parent',value=(row[1:]))
                pass
                #print(row)
                i += 1      
    #Create function to search about one passneger by his name
    def search_single():
           cursor = db.cursor()
           i = 0
           for row in result:
                  i += 1
                  global name_from_user
                  name_from_user = single.get()
                  if name_from_user in row[1:2]:
                         print(row[1:2])
                         my_tree.insert('',index='end',iid=i,text='Parent',value=(row[1:]))
                         single.delete(0, 'end')
    #Create function to delete all passenger from treeview
    def delete_all():
           for row in my_tree.get_children():
                  my_tree.delete(row)                         
    #Create function modfiy the price ticket by the price and the name
    def modify_price_passenger():
           cursor = db.cursor()
           i = 0
           cursor.execute('SELECT * FROM customers')
           result = cursor.fetchall()
           for row in result:
                  i += 1
                  if old_price1 in row[-1]:
                         sql = "UPDATE customers SET price = %s WHERE name = %s"
                         val = (modify.get(), name.get())
                         cursor.execute(sql, val)
                         db.commit()
                  btn5.after(1000,window2.destroy)
                  messagebox.showinfo('Modify Price field','Modify price it completed')
                  show_data()
    #check_all_passenger()
                  delete_all()
    check_all_passenger()
           
                  
    my_tree.pack(pady=20)
           
    #Create function delete one passenger from the tree view
    def delete_one():
           x = my_tree.selection()[0]
           my_tree.delete(x)
    #Create function to delete teh passngere from  teh DateBase                 
    def del_system():
           cursor = db.cursor()
           i = 0
           for row in result:
                  i += 1
                  name_del = name.get()
                  if old_price1 in row[-1]:
                         
                         sql = "DELETE FROM  customers WHERE name = %s"
                         val = (name.get(),)
                         cursor.execute(sql, val)
                         db.commit()
                         print(cursor.rowcount, "record(s) deleted")
    
           
           cursor.close()
           db.close()           
    #Create entry to search about one passenger by name   
    single= Entry(window2,font=fnt4,textvariable=passeneger)
    single.place(x=370,y=280)
    enter_name = single.insert(0,"Enter Passenger Name")
    passeneger_name = single.get()

    #Create entry to input the current price
    old_price = Entry(window2,font=fnt4,textvariable=name)
    old_price.place(x=370,y=330)
    old_price1 = old_price.get()

    #Create entry to input the new price
    modify = Entry(window2,font=fnt4,textvariable=price)
    modify.place(x=370,y=380)
    modify_price = modify.get()
    #Create label  person name 
    label = Label(window2,text='Person Name: ',font=fnt4,bg='#443565')
    label.place(x=180, y=280)
    #Create label  old price 
    label = Label(window2,text='Old Price : ',font=fnt4,bg='#443565')
    label.place(x=180, y=330)
    #Create label  new price 
    label = Label(window2,text='New Price: ',font=fnt4,bg='#443565')
    label.place(x=180, y=380)
    #Create Button to do single search
    btn = Button(window2,text='Search By Name',font=fnt5,bg='white',command=search_single)
    btn.place(x=650, y=280)
    #Create Button to display all passenger information
    btn = Button(window2,text='List of Passenger',font=fnt5,bg='white',command=check_all_passenger)
    btn.place(x=850, y=280)
    #Create Button to display new price
    btn5 = Button(window2,text='Update Ticket Price',font=fnt5,bg='white',command=modify_price_passenger)
    btn5.place(x=650, y=330)
    #Create Button to display delete passenger fron treeview   
    btn = Button(window2,text='Delete Passenger',font=fnt5,bg='white',command=delete_one)
    btn.place(x=850, y=330)
    #Create Button to display delete passenger fron DataBase 
    btn = Button(window2,text='Delete from system',font=fnt5,bg='white',command= del_system)
    btn.place(x=650, y=380)
    #Create Button to delete all passenger from treeview 
    btn = Button(window2,text='Delete All',font=fnt5,bg='white',command=delete_all)
    btn.place(x=850, y=380)
    #Destroy second GUI
    window2.mainloop()

    
    


   
#Create label display the app name
label = Label(root,text='Booking Plane Tickets',font=fnt1,bg='#443565',fg='white')
label.place(x= 370,y=50)
#Create label name
label_name = Label(root,text='Name:',font=fnt2,bg='#443565',fg='white')
label_name.place(x=340, y=150)
#Create label address
label_address = Label(root,text='Address:',font=fnt2,bg='#443565',fg='white')
label_address.place(x=340, y=200)
#Create label mobile
label_mobile = Label(root,text='Mobile:',font=fnt2,bg='#443565',fg='white')
label_mobile.place(x=340, y=250)   
#Create label date
label_date = Label(root,text='Date:',font=fnt2,bg='#443565',fg='white')
label_date.place(x=340, y=300)
#Create label time
label_time = Label(root,text='Time:',font=fnt2,bg='#443565',fg='white')
label_time.place(x=340, y=350)
#Create label from
label_from = Label(root,text='From:',font=fnt2,bg='#443565',fg='white')
label_from.place(x=340, y=400)
#Create label to
label_to = Label(root,text='To:',font=fnt2,bg='#443565',fg='white')
label_to.place(x=340, y=450)
#Create label price
label_to = Label(root,text='Price:',font=fnt2,bg='#443565',fg='white')
label_to.place(x=340, y=500)
#Create entry name
e_name = Entry(root,font=fnt2,textvariable=name)
e_name.place(x=500,y=155)
#Create entry addrress
e_address = Entry(root,font=fnt2,textvariable=address)
e_address.place(x=500,y=205)
#Create entry mobile
e_mobile = Entry(root,font=fnt2,textvariable=mobile)
e_mobile.place(x=500,y=255)
#Create entry date fly
e_date= Entry(root,font=fnt2,textvariable=date_fly)
e_date.place(x=500,y=305)
#Create entry time fly
e_time= Entry(root,font=fnt2,textvariable=time_fly)
e_time.place(x=500,y=355)
#Create entry from where
e_from = Entry(root,font=fnt2,textvariable=from1)
e_from.place(x=500,y=405)
#Create entry destination
e_to = Entry(root,font=fnt2,textvariable=destination)
e_to.place(x=500,y=455)
#Create entry price
e_price = Entry(root,font=fnt2,textvariable=price)
e_price.place(x=500,y=505)
#Create Button to add the information to DataBase
btn = Button(root,text='Add Passenger',font=fnt4,bg='white',command=get_info_new_frame)
btn.place(x=500, y=555)
#Create Button to display the information it is alreay in Database and who you can deal with those information (search,modify,display,delete)
btn = Button(root,text='Show data',font=fnt4,bg='white',command=show_data)
btn.place(x=720, y=555)

root.mainloop()
