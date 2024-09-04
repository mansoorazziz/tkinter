from tkinter import *
#Fuctionality part

def total():
    soapprice=int(bathSoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*20
    facewashrice=int(facewashEntry.get())*20
    hairsprayprice=int(hairsprayEntry.get())*20
    hairgelprice=int(hairgelEntry.get())*20
    bodylotionprice=int(bodylotionEntry.get())*20

    totalcosmeticsPrice = soapprice + facecreamprice + facewashrice + hairsprayprice + hairgelprice + bodylotionprice
    cosmeticsEntry.insert(0,totalcosmeticsPrice)








# GUI Part
root = Tk()
root.title("POS")

#windowHight=
root.geometry('1270x685')
root.iconbitmap("icon.ico")
headingLabel= Label(root,text="Retail Billing System",font=('times new roman',30,'bold'),background='gray20',foreground='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=5)


# Customers Details Frame
costumer_details_frame = LabelFrame(root,text="Customer Details",font=('times new roman',15,'bold'),foreground='gold',bd=8,relief=GROOVE,background='gray20')
costumer_details_frame.pack(fill=X)

nameLabel=Label(costumer_details_frame,text='Name',font=('times new roman',15,'bold'),background='gray20',foreground='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(costumer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(costumer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),background='gray20',foreground='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(costumer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(costumer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),background='gray20',foreground='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billEntry=Entry(costumer_details_frame,font=('arial',15),bd=7,width=18)
billEntry.grid(row=0,column=5,padx=8)

searchButton= Button(costumer_details_frame,text="SEARCH",font=('arial',12,'bold'),bd=7,width=10)
searchButton.grid(row=0,column=6,padx=20)

#Products Framme
productsFrame=Frame(root)
productsFrame.pack(pady=2)

cosmeticsframe = LabelFrame(productsFrame,text="Cosmetics",font=('times new roman',15,'bold'),foreground='gold',bd=8,relief=GROOVE,background='gray20')
cosmeticsframe.grid(row=0,column=0)

bathSoapLabel=Label(cosmeticsframe,text='Bath Soap',font=('times new roman',15,'bold'),background='gray20',foreground='white')
bathSoapLabel.grid(row=0,column=0,pady=5,padx=10,sticky='w')

bathSoapEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
bathSoapEntry.grid(row=0,column=1,pady=5,padx=10)


facecreamLabel=Label(cosmeticsframe,text='Face Cream',font=('times new roman',15,'bold'),background='gray20',foreground='white')
facecreamLabel.grid(row=1,column=0,pady=5,padx=10,sticky='w')

facecreamEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
facecreamEntry.grid(row=1,column=1,pady=5,padx=10)


facewashLabel=Label(cosmeticsframe,text='Face Wash',font=('times new roman',15,'bold'),background='gray20',foreground='white')
facewashLabel.grid(row=2,column=0,pady=5,padx=10,sticky='w')

facewashEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
facewashEntry.grid(row=2,column=1,pady=5,padx=10)


hairsprayLabel=Label(cosmeticsframe,text='Hair Spray',font=('times new roman',15,'bold'),background='gray20',foreground='white')
hairsprayLabel.grid(row=3,column=0,pady=5,padx=10,sticky='w')

hairsprayEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
hairsprayEntry.grid(row=3,column=1,pady=5,padx=10)


hairgelLabel=Label(cosmeticsframe,text='Hair Gel',font=('times new roman',15,'bold'),background='gray20',foreground='white')
hairgelLabel.grid(row=4,column=0,pady=5,padx=10,sticky='w')

hairgelEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
hairgelEntry.grid(row=4,column=1,pady=5,padx=10)


bodylotionLabel=Label(cosmeticsframe,text='Body Lotion',font=('times new roman',15,'bold'),background='gray20',foreground='white')
bodylotionLabel.grid(row=5,column=0,pady=5,padx=10,sticky='w')

bodylotionEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
bodylotionEntry.grid(row=5,column=1,pady=5,padx=10)


# grocery frame

groceryframe = LabelFrame(productsFrame,text="Grocery",font=('times new roman',15,'bold'),foreground='gold',bd=8,relief=GROOVE,background='gray20')
groceryframe.grid(row=0,column=1,padx=5)

riceLabel=Label(groceryframe,text='Rice',font=('times new roman',15,'bold'),background='gray20',foreground='white')
riceLabel.grid(row=0,column=0,pady=5,padx=10,sticky='w')

riceEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
riceEntry.grid(row=0,column=1,pady=5,padx=10)


oilLabel=Label(groceryframe,text='Oil',font=('times new roman',15,'bold'),background='gray20',foreground='white')
oilLabel.grid(row=1,column=0,pady=5,padx=10,sticky='w')

oilEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
oilEntry.grid(row=1,column=1,pady=5,padx=10)

#
daalLabel=Label(groceryframe,text='Daal',font=('times new roman',15,'bold'),background='gray20',foreground='white')
daalLabel.grid(row=2,column=0,pady=5,padx=10,sticky='w')

daalEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
daalEntry.grid(row=2,column=1,pady=5,padx=10)


wheatLabel=Label(groceryframe,text='Wheat',font=('times new roman',15,'bold'),background='gray20',foreground='white')
wheatLabel.grid(row=3,column=0,pady=5,padx=10,sticky='w')

wheatEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
wheatEntry.grid(row=3,column=1,pady=5,padx=10)

#
sugarLabel=Label(groceryframe,text='Sugar',font=('times new roman',15,'bold'),background='gray20',foreground='white')
sugarLabel.grid(row=4,column=0,pady=5,padx=10,sticky='w')

sugarEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
sugarEntry.grid(row=4,column=1,pady=5,padx=10)


teaLabel=Label(groceryframe,text='Tea',font=('times new roman',15,'bold'),background='gray20',foreground='white')
teaLabel.grid(row=5,column=0,pady=5,padx=10,sticky='w')

teaEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
teaEntry.grid(row=5,column=1,pady=5,padx=10)


# Drinks frame

drinksframe = LabelFrame(productsFrame,text="Cold Drinks",font=('times new roman',15,'bold'),foreground='gold',bd=8,relief=GROOVE,background='gray20')
drinksframe.grid(row=0,column=2,padx=5)

MaazaLabel=Label(drinksframe,text='Maaza',font=('times new roman',15,'bold'),background='gray20',foreground='white')
MaazaLabel.grid(row=0,column=0,pady=5,padx=10,sticky='w')

MaazaEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
MaazaEntry.grid(row=0,column=1,pady=5,padx=10)


PepsiLabel=Label(drinksframe,text='Pepsi',font=('times new roman',15,'bold'),background='gray20',foreground='white')
PepsiLabel.grid(row=1,column=0,pady=5,padx=10,sticky='w')

PepsiEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
PepsiEntry.grid(row=1,column=1,pady=5,padx=10)

#
SpriteLabel=Label(drinksframe,text='Sprite',font=('times new roman',15,'bold'),background='gray20',foreground='white')
SpriteLabel.grid(row=2,column=0,pady=5,padx=10,sticky='w')

SpriteEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
SpriteEntry.grid(row=2,column=1,pady=5,padx=10)


DewLabel=Label(drinksframe,text='Dew',font=('times new roman',15,'bold'),background='gray20',foreground='white')
DewLabel.grid(row=3,column=0,pady=5,padx=10,sticky='w')

DewEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
DewEntry.grid(row=3,column=1,pady=5,padx=10)

#
FrootiLabel=Label(drinksframe,text='Frooti',font=('times new roman',15,'bold'),background='gray20',foreground='white')
FrootiLabel.grid(row=4,column=0,pady=5,padx=10,sticky='w')

FrootiEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
FrootiEntry.grid(row=4,column=1,pady=5,padx=10)


cocacolaLabel=Label(drinksframe,text='Coca Cola',font=('times new roman',15,'bold'),background='gray20',foreground='white')
cocacolaLabel.grid(row=5,column=0,pady=5,padx=10,sticky='w')

cocacolaEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
cocacolaEntry.grid(row=5,column=1,pady=5,padx=10)

#bill aframe
billFrame=Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=5)

billareaLabel=Label(billFrame,text="Bill Area",font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textArea=Text(billFrame,height=15,width=65,yscrollcommand=scrollbar.set)
textArea.pack()
scrollbar.config(command=textArea.yview)

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

totalbutton=Button(buttonFrame,text="Total",font=('arial',16,'bold'),background="gray20",foreground='white',bd=5,width=8,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=20,padx=5)

billbutton=Button(buttonFrame,text="Bill",font=('arial',16,'bold'),background="gray20",foreground='white',bd=5,width=8,pady=10)
billbutton.grid(row=0,column=1,pady=20,padx=5)

emailbutton=Button(buttonFrame,text="Email",font=('arial',16,'bold'),background="gray20",foreground='white',bd=5,width=8,pady=10)
emailbutton.grid(row=0,column=2,pady=20,padx=5)

printbutton=Button(buttonFrame,text="Print",font=('arial',16,'bold'),background="gray20",foreground='white',bd=5,width=8,pady=10)
printbutton.grid(row=0,column=3,pady=20,padx=5)

clearbutton=Button(buttonFrame,text="Clear",font=('arial',16,'bold'),background="gray20",foreground='white',bd=5,width=8,pady=10)
clearbutton.grid(row=0,column=4,pady=20,padx=5)



root.mainloop()