from tkinter import *
from tkinter import messagebox
#Fuctionality part


def submit():
    #textArea.insert(0,nameEntry.get())
    entered_name = nameEntry.get()
    phone_Entry = phoneEntry.get()
    projectsList.insert(END,f'{entered_name}-{phone_Entry} ')
    


    
def on_select(event):
    selectedIndex = projectsList.curselection()
    
    if selectedIndex:
        item = projectsList.get(selectedIndex)
        print(f'Selected item is {item}')
    else:
        messagebox.INFO('Not Found','Unknown Error')


# GUI Part
root = Tk()
root.title("POS")

#windowHight=
root.geometry('1270x900')
#root.iconbitmap("icon.ico")
headingLabel= Label(root,text="Offline Software Managment",font=('times new roman',30,'bold'),background='gray20',foreground='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=5)


# Customers Details Frame
costumer_details_frame = LabelFrame(root,text="New Entry",font=('times new roman',15,'bold'),foreground='gold',bd=8,relief=GROOVE,background='gray20')
costumer_details_frame.pack(fill=X)

nameLabel=Label(costumer_details_frame,text='Name',font=('times new roman',15,'bold'),background='gray20',foreground='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(costumer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(costumer_details_frame,text='Number',font=('times new roman',15,'bold'),background='gray20',foreground='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(costumer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(costumer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),background='gray20',foreground='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billEntry=Entry(costumer_details_frame,font=('arial',15),bd=7,width=18)
billEntry.grid(row=0,column=5,padx=8)

submitButton= Button(costumer_details_frame,text="Submit",font=('arial',12,'bold'),bd=7,width=10,command=submit)
submitButton.grid(row=0,column=6,padx=20)

#Project Details

project_details_frame = LabelFrame(root,text="Project Details",font=('times new roman',15,'bold'),foreground='gold',bd=8,relief=GROOVE,background='gray20')
project_details_frame.pack(fill=X,pady=10)


projectsList = Listbox(project_details_frame,bd=10,font=('arial',15,),height=15,width=50,relief=GROOVE)
projectsList.bind('<Return>',on_select)
#listnotes.bind("<Return>", dosomething)
projectsList.grid(row=0,column=0)













#Bill menu frame

billmenuframe = LabelFrame(root,text="Bill Menu",font=('times new roman',15,'bold'),foreground='gold',bd=8,relief=GROOVE,background='gray20')
billmenuframe.pack()

cosmeticspriceLabel=Label(billmenuframe,text='Cosmetics Price',font=('times new roman',15,'bold'),background='gray20',foreground='white')
cosmeticspriceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

cosmeticsEntry = Entry(billmenuframe,font=('times new roman',15,'bold'),bd=5,width=10)
cosmeticsEntry.grid(row=0,column=1,pady=9,padx=10)

grocerypriceLabel=Label(billmenuframe,text='Grocery Price',font=('times new roman',15,'bold'),background='gray20',foreground='white')
grocerypriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

groceryEntry = Entry(billmenuframe,font=('times new roman',15,'bold'),bd=5,width=10)
groceryEntry.grid(row=1,column=1,pady=9,padx=10)

drinkspriceLabel=Label(billmenuframe,text='Drinks Price',font=('times new roman',15,'bold'),background='gray20',foreground='white')
drinkspriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

drinksEntry = Entry(billmenuframe,font=('times new roman',15,'bold'),bd=5,width=10)
drinksEntry.grid(row=2,column=1,pady=9,padx=10)

#tax
cosmeticstaxLabel=Label(billmenuframe,text='Cosmetics Tax',font=('times new roman',15,'bold'),background='gray20',foreground='white')
cosmeticstaxLabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')

cosmeticstaxEntry = Entry(billmenuframe,font=('times new roman',15,'bold'),bd=5,width=10)
cosmeticstaxEntry.grid(row=0,column=3,pady=9,padx=10)

grocerytaxLabel=Label(billmenuframe,text='Grocery Tax',font=('times new roman',15,'bold'),background='gray20',foreground='white')
grocerytaxLabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')

grocerytaxEntry = Entry(billmenuframe,font=('times new roman',15,'bold'),bd=5,width=10)
grocerytaxEntry.grid(row=1,column=3,pady=9,padx=10)

drinkstaxLabel=Label(billmenuframe,text='Drinks Tax',font=('times new roman',15,'bold'),background='gray20',foreground='white')
drinkstaxLabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')

drinkstaxEntry = Entry(billmenuframe,font=('times new roman',15,'bold'),bd=5,width=10)
drinkstaxEntry.grid(row=2,column=3,pady=9,padx=10)

buttonFrame=Frame(billmenuframe,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalbutton=Button(buttonFrame,text="Total",font=('arial',16,'bold'),background="gray20",foreground='white',bd=5,width=8,pady=10)
totalbutton.grid(row=0,column=0,pady=20,padx=5)

billbutton=Button(buttonFrame,text="Bill",font=('arial',16,'bold'),background="gray20",foreground='white',bd=5,width=8,pady=10)
billbutton.grid(row=0,column=1,pady=20,padx=5)

emailbutton=Button(buttonFrame,text="Email",font=('arial',16,'bold'),background="gray20",foreground='white',bd=5,width=8,pady=10)
emailbutton.grid(row=0,column=2,pady=20,padx=5)

printbutton=Button(buttonFrame,text="Print",font=('arial',16,'bold'),background="gray20",foreground='white',bd=5,width=8,pady=10)
printbutton.grid(row=0,column=3,pady=20,padx=5)

clearbutton=Button(buttonFrame,text="Clear",font=('arial',16,'bold'),background="gray20",foreground='white',bd=5,width=8,pady=10)
clearbutton.grid(row=0,column=4,pady=20,padx=5)

# #Products Framme
# productsFrame=Frame(root)
# productsFrame.pack(pady=2)

# #bill aframe
# billFrame=Frame(productsFrame,bd=8,relief=GROOVE)
# billFrame.pack()
#billFrame.grid(row=0,column=3,padx=5)
# newframe = Frame(root)
# newframe.pack(pady=10)

# projectsareaLabel=LabelFrame(root,text="Projects",font=('times new roman',15,'bold'),bd=7)
# projectsareaLabel.grid(row=0,column=0)
# projectsList = Listbox(projectsareaLabel,bd=10,font=('arial',15,'bold'),height=15,width=50,relief=GROOVE)
# projectsList.grid(row=1,column=0)



# scrollbar=Scrollbar(billFrame,orient=VERTICAL)
# scrollbar.pack(side=RIGHT,fill=Y)
# #--
# textArea=Text(billFrame,height=25,width=150,yscrollcommand=scrollbar.set)
# textArea.pack()
# scrollbar.config(command=textArea.yview)
# projectList=Label(project_details_frame,text='Projects List',font=('times new roman',15,'bold'),background='gray20',foreground='white')
# projectList.grid(row=1,column=0,padx=20)
'''
def total():
    soapprice=int(bathSoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*20
    facewashrice=int(facewashEntry.get())*20
    hairsprayprice=int(hairsprayEntry.get())*20
    hairgelprice=int(hairgelEntry.get())*20
    bodylotionprice=int(bodylotionEntry.get())*20

    totalcosmeticsPrice = soapprice + facecreamprice + facewashrice + hairsprayprice + hairgelprice + bodylotionprice
    cosmeticsEntry.insert(0,totalcosmeticsPrice)
'''
root.mainloop()