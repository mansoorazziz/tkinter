from tkinter import *
from tkinter import messagebox
import  random,os,tempfile,smtplib


#Fuctionality part
def clear():
    bathSoapEntry.delete(0,END)
    facecreamEntry.delete(0, END)
    facewashEntry.delete(0, END)
    hairsprayEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    bodylotionEntry.delete(0, END)

    riceEntry.delete(0, END)
    daalEntry.delete(0, END)
    oilEntry.delete(0, END)
    wheatEntry.delete(0, END)
    sugarEntry.delete(0, END)
    teaEntry.delete(0, END)

    MaazaEntry.delete(0, END)
    PepsiEntry.delete(0, END)
    DewEntry.delete(0, END)
    SpriteEntry.delete(0, END)
    FrootiEntry.delete(0, END)
    cocacolaEntry.delete(0, END)

    bathSoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    bodylotionEntry.insert(0,0)

    riceEntry.insert(0,0)
    daalEntry.insert(0,0)
    oilEntry.insert(0,0)
    wheatEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)

    MaazaEntry.insert(0,0)
    PepsiEntry.insert(0,0)
    DewEntry.insert(0,0)
    SpriteEntry.insert(0,0)
    FrootiEntry.insert(0,0)
    cocacolaEntry.insert(0,0)

    cosmeticstaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    drinkstaxEntry.delete(0,END)

    cosmeticsEntry.delete(0,END)
    groceryEntry.delete(0,END)
    drinksEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billEntry.delete(0,END)

    textArea.delete(1.0,END)







def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = emailtextArea.get('1.0', END)
            receiverAdress = receiverEntry.get()
            ob.sendmail(senderEntry.get(), receiverAdress, message)
            ob.quit()
            messagebox.showinfo('Successful', 'Email sent!',parent = root1)
            root1.destroy()
        except:
            messagebox.showinfo('Failed', 'Please try again!',parent =root1)



    if textArea.get(1.0,END) == '\n':
        messagebox.showerror('Error','Nothing to print')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title("Send Email")
        # root1.geometry("300x300")
        root1.resizable(False, False)
        root1.configure(bg="grey20")

        senderFrame = LabelFrame(root1,text = 'SENDER',font = ('arial',16,'bold'),background='grey20',foreground ='white')
        senderFrame.grid(row = 0, column = 0,padx = 40,pady = 20)

        senderLabel = Label(senderFrame, text = "Sender's Email ID", font = ('arial',14,'bold'),background='grey20',foreground ='white')
        senderLabel.grid(row = 0, column = 0,padx = 10 ,pady = 8)
        senderEntry = Entry(senderFrame,font = ('arial',14,'bold'),bd = 2,width = 23, relief = RIDGE)
        senderEntry.grid(row = 0, column = 1,padx = 10 ,pady = 8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), background='grey20',
                            foreground='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)
        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        #Receiver Email Entry
        receiverFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), background='grey20', foreground='white')
        receiverFrame.grid(row=1, column=0, padx=40, pady=20)

        receiverLabel = Label(receiverFrame, text="Email Address", font=('arial', 14, 'bold'), background='grey20',
                              foreground='white')
        receiverLabel.grid(row=0, column=0, padx=10, pady=8)
        receiverEntry = Entry(receiverFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        receiverEntry.grid(row=0, column=1, padx=10, pady=8)

        #Message
        messageLabel = Label(receiverFrame, text="Message", font=('arial', 14, 'bold'), background='grey20',
                              foreground='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        emailtextArea = Text(receiverFrame, font=('arial', 14, 'bold'), bd = 2, relief=SUNKEN,width=42,height=11)
        emailtextArea.grid(row=2, column=0, padx=10, pady=8,columnspan =2)
        emailtextArea.delete('1.0',END)
        emailtextArea.insert(END,textArea.get('1.0', END).replace('=','').replace('-','').replace('\t\t\t ','\t\t'))

        sendButton = Button(root1,text='SEND',font=('arial', 16, 'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2, column=0, padx=10, pady=8)


        root1.mainloop()






def print_bill():
    if textArea.get(1.0,END) == '\n':
        messagebox.showerror('Error','Nothing to print')
    else:
        file= tempfile.mktemp('.txt')
        open(file, 'w').write(textArea.get(1.0,END))
        os.startfile(file,'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billEntry.get() :
            f= open(f'bills/{i}','r')
            textArea.delete(1.0,END)
            for data in f:
                textArea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Bill not found')

        #print(i)
if not os.path.exists('bills'):
    os.mkdir('bills')




def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm','Do you want to save bill?')
    if result:
        bill_content = textArea.get(1.0,END)
        file = open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()

        messagebox.showinfo('Successful',f'{billnumber} Bill saved successfully!')
        billnumber = random.randint(500, 1000)



billnumber = random.randint(500,1000)

def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror("Error","Costumers Details are required")
    elif cosmeticsEntry.get() == '' and groceryEntry.get() == '' and drinksEntry.get() == '':
        messagebox.showerror("Error","No product selected")
    elif cosmeticsEntry.get() == '0 Rs' and groceryEntry.get() == '0 Rs' and drinksEntry.get() == '0 Rs':
        messagebox.showerror("Error","No product selected")
    else:
        textArea.delete(1.0,END)

        textArea.insert(END,'\t\t\t***Welcome Customer***\n')
        textArea.insert(END,f'\nBill Number: {billnumber}\n')
        textArea.insert(END,f'Costumer Name: {nameEntry.get()}\n')
        textArea.insert(END,f'Phone Number: {phoneEntry.get()}\n')
        textArea.insert(END,'\n=================================================================')
        textArea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
        textArea.insert(END,'\n=================================================================')
        if bathSoapEntry.get()!='0':
            textArea.insert(END,f'Bath Soap\t\t\t{bathSoapEntry.get()}\t\t\t{soapprice} Rs\n')

        if facecreamEntry.get()!='0':
            textArea.insert(END,f'Face Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs\n')

        if facewashEntry.get()!='0':
            textArea.insert(END,f'Face Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashrice} Rs\n')

        if hairsprayEntry.get()!='0':
            textArea.insert(END,f'Hair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs\n')

        if hairgelEntry.get()!='0':
            textArea.insert(END,f'Hair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs\n')

        if bodylotionEntry.get()!='0':
            textArea.insert(END,f'Body Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs\n')

        # Grocery Section

        if riceEntry.get()!='0':
            textArea.insert(END,f'Rice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs\n')

        if oilEntry.get()!='0':
            textArea.insert(END,f'Oil\t\t\t{oilEntry.get()}\t\t\t{oilcreamprice} Rs\n')

        if daalEntry.get()!='0':
            textArea.insert(END,f'Daal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs\n')

        if wheatEntry.get()!='0':
            textArea.insert(END,f'Wheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs\n')

        if sugarEntry.get()!='0':
            textArea.insert(END,f'Sugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs\n')

        if teaEntry.get()!='0':
            textArea.insert(END,f'Tea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs\n')

        # Drinks Section

        if MaazaEntry.get()!='0':
            textArea.insert(END,f'Maaza\t\t\t{MaazaEntry.get()}\t\t\t{maazprice} Rs\n')

        if PepsiEntry.get()!='0':
            textArea.insert(END,f'Pepsi\t\t\t{PepsiEntry.get()}\t\t\t{PepsiEntryprice} Rs\n')

        if DewEntry.get()!='0':
            textArea.insert(END,f'Dew\t\t\t{DewEntry.get()}\t\t\t{dewprice} Rs\n')

        if FrootiEntry.get()!='0':
            textArea.insert(END,f'Frooti\t\t\t{FrootiEntry.get()}\t\t\t{frootirprice} Rs\n')

        if cocacolaEntry.get()!='0':
            textArea.insert(END,f'Coca Cola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Rs\n')

        if SpriteEntry.get()!='0':
            textArea.insert(END,f'Sprite\t\t\t{SpriteEntry.get()}\t\t\t{spriteprice} Rs\n')
        textArea.insert(END,'----------------------------------------------------------------\n')

        if cosmeticstaxEntry.get()!='0.0 Rs':
            textArea.insert(END,f'Cosmetics Tax\t\t\t{cosmeticstaxEntry.get()}\n')
        if grocerytaxEntry.get()!='0.0 Rs':
            textArea.insert(END,f'Grocery Tax\t\t\t{grocerytaxEntry.get()}\n')
        if drinkstaxEntry.get()!='0.0 Rs':
            textArea.insert(END,f'Drinks Tax\t\t\t{drinkstaxEntry.get()}\n\n\n')
        textArea.insert(END,f'\n\nTotal Bill \t\t\t\t{totalbill} Rs\n')

        textArea.insert(END, '----------------------------------------------------------------')
        save_bill()








def total():
    global totalbill,soapprice,facecreamprice,facewashrice,hairsprayprice,hairgelprice,bodylotionprice
    global riceprice,oilcreamprice,daalprice,wheatprice,sugarprice,teaprice,maazprice,PepsiEntryprice
    global spriteprice,dewprice,frootirprice,cocacolaprice

    # Cosmetics Price Calculations
    soapprice=int(bathSoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*20
    facewashrice=int(facewashEntry.get())*20
    hairsprayprice=int(hairsprayEntry.get())*20
    hairgelprice=int(hairgelEntry.get())*20
    bodylotionprice=int(bodylotionEntry.get())*20

    totalcosmeticsPrice = soapprice + facecreamprice + facewashrice + hairsprayprice + hairgelprice + bodylotionprice
    cosmeticsEntry.delete(0,END)
    cosmeticsEntry.insert(0,f'{totalcosmeticsPrice} Rs')
    cosmeticstaxEntry.delete(0,END)
    cosmeticstax = totalcosmeticsPrice * 0.12
    cosmeticstaxEntry.insert(0,f'{cosmeticstax} Rs')

    # Grocery Price Calculations
    riceprice=int(riceEntry.get())*20
    oilcreamprice=int(oilEntry.get())*20
    daalprice=int(daalEntry.get())*20
    wheatprice=int(wheatEntry.get())*20
    sugarprice=int(sugarEntry.get())*20
    teaprice=int(teaEntry.get())*20

    totalgroceryPrice = riceprice + oilcreamprice + daalprice + wheatprice + sugarprice + teaprice
    groceryEntry.delete(0,END)
    groceryEntry.insert(0,f'{totalgroceryPrice} Rs')
    grocerytaxEntry.delete(0,END)
    grocerytax = totalgroceryPrice* 0.09
    grocerytaxEntry.insert(0,f'{grocerytax} Rs')


    # Drinks Price Calculations
    maazprice=int(MaazaEntry.get())*20
    PepsiEntryprice=int(PepsiEntry.get())*20
    spriteprice=int(SpriteEntry.get())*20
    dewprice=int(DewEntry.get())*20
    frootirprice=int(FrootiEntry.get())*20
    cocacolaprice=int(cocacolaEntry.get())*20

    totaldrinksPrice = maazprice + PepsiEntryprice + spriteprice + dewprice + frootirprice + cocacolaprice
    drinksEntry.delete(0,END)
    drinksEntry.insert(0,f'{totaldrinksPrice} Rs')
    drinkstaxEntry.delete(0,END)
    drinkstax = totaldrinksPrice* 0.29
    drinkstaxEntry.insert(0,f'{drinkstax} Rs')

    totalbill = totalcosmeticsPrice + totalgroceryPrice + totaldrinksPrice + cosmeticstax + grocerytax + drinkstax








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

searchButton= Button(costumer_details_frame,text="SEARCH",font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20)

#Products Frame
productsFrame=Frame(root)
productsFrame.pack(pady=2)

cosmeticsframe = LabelFrame(productsFrame,text="Cosmetics",font=('times new roman',15,'bold'),foreground='gold',bd=8,relief=GROOVE,background='gray20')
cosmeticsframe.grid(row=0,column=0)

bathSoapLabel=Label(cosmeticsframe,text='Bath Soap',font=('times new roman',15,'bold'),background='gray20',foreground='white')
bathSoapLabel.grid(row=0,column=0,pady=5,padx=10,sticky='w')

bathSoapEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
bathSoapEntry.grid(row=0,column=1,pady=5,padx=10)
bathSoapEntry.insert(0,0)


facecreamLabel=Label(cosmeticsframe,text='Face Cream',font=('times new roman',15,'bold'),background='gray20',foreground='white')
facecreamLabel.grid(row=1,column=0,pady=5,padx=10,sticky='w')

facecreamEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
facecreamEntry.grid(row=1,column=1,pady=5,padx=10)
facecreamEntry.insert(0,0)


facewashLabel=Label(cosmeticsframe,text='Face Wash',font=('times new roman',15,'bold'),background='gray20',foreground='white')
facewashLabel.grid(row=2,column=0,pady=5,padx=10,sticky='w')

facewashEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
facewashEntry.grid(row=2,column=1,pady=5,padx=10)
facewashEntry.insert(0,0)


hairsprayLabel=Label(cosmeticsframe,text='Hair Spray',font=('times new roman',15,'bold'),background='gray20',foreground='white')
hairsprayLabel.grid(row=3,column=0,pady=5,padx=10,sticky='w')

hairsprayEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
hairsprayEntry.grid(row=3,column=1,pady=5,padx=10)
hairsprayEntry.insert(0,0)


hairgelLabel=Label(cosmeticsframe,text='Hair Gel',font=('times new roman',15,'bold'),background='gray20',foreground='white')
hairgelLabel.grid(row=4,column=0,pady=5,padx=10,sticky='w')

hairgelEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
hairgelEntry.grid(row=4,column=1,pady=5,padx=10)
hairgelEntry.insert(0,0)


bodylotionLabel=Label(cosmeticsframe,text='Body Lotion',font=('times new roman',15,'bold'),background='gray20',foreground='white')
bodylotionLabel.grid(row=5,column=0,pady=5,padx=10,sticky='w')

bodylotionEntry = Entry(cosmeticsframe,font=('times new roman',15,'bold'),bd=5,width=10)
bodylotionEntry.grid(row=5,column=1,pady=5,padx=10)
bodylotionEntry.insert(0,0)


# grocery frame

groceryframe = LabelFrame(productsFrame,text="Grocery",font=('times new roman',15,'bold'),foreground='gold',bd=8,relief=GROOVE,background='gray20')
groceryframe.grid(row=0,column=1,padx=5)

riceLabel=Label(groceryframe,text='Rice',font=('times new roman',15,'bold'),background='gray20',foreground='white')
riceLabel.grid(row=0,column=0,pady=5,padx=10,sticky='w')

riceEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
riceEntry.grid(row=0,column=1,pady=5,padx=10)
riceEntry.insert(0,0)


oilLabel=Label(groceryframe,text='Oil',font=('times new roman',15,'bold'),background='gray20',foreground='white')
oilLabel.grid(row=1,column=0,pady=5,padx=10,sticky='w')

oilEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
oilEntry.grid(row=1,column=1,pady=5,padx=10)
oilEntry.insert(0,0)

#
daalLabel=Label(groceryframe,text='Daal',font=('times new roman',15,'bold'),background='gray20',foreground='white')
daalLabel.grid(row=2,column=0,pady=5,padx=10,sticky='w')

daalEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
daalEntry.grid(row=2,column=1,pady=5,padx=10)
daalEntry.insert(0,0)


wheatLabel=Label(groceryframe,text='Wheat',font=('times new roman',15,'bold'),background='gray20',foreground='white')
wheatLabel.grid(row=3,column=0,pady=5,padx=10,sticky='w')

wheatEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
wheatEntry.grid(row=3,column=1,pady=5,padx=10)
wheatEntry.insert(0,0)

#
sugarLabel=Label(groceryframe,text='Sugar',font=('times new roman',15,'bold'),background='gray20',foreground='white')
sugarLabel.grid(row=4,column=0,pady=5,padx=10,sticky='w')

sugarEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
sugarEntry.grid(row=4,column=1,pady=5,padx=10)
sugarEntry.insert(0,0)


teaLabel=Label(groceryframe,text='Tea',font=('times new roman',15,'bold'),background='gray20',foreground='white')
teaLabel.grid(row=5,column=0,pady=5,padx=10,sticky='w')

teaEntry = Entry(groceryframe,font=('times new roman',15,'bold'),bd=5,width=10)
teaEntry.grid(row=5,column=1,pady=5,padx=10)
teaEntry.insert(0,0)


# Drinks frame

drinksframe = LabelFrame(productsFrame,text="Cold Drinks",font=('times new roman',15,'bold'),foreground='gold',bd=8,relief=GROOVE,background='gray20')
drinksframe.grid(row=0,column=2,padx=5)

MaazaLabel=Label(drinksframe,text='Maaza',font=('times new roman',15,'bold'),background='gray20',foreground='white')
MaazaLabel.grid(row=0,column=0,pady=5,padx=10,sticky='w')

MaazaEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
MaazaEntry.grid(row=0,column=1,pady=5,padx=10)
MaazaEntry.insert(0,0)


PepsiLabel=Label(drinksframe,text='Pepsi',font=('times new roman',15,'bold'),background='gray20',foreground='white')
PepsiLabel.grid(row=1,column=0,pady=5,padx=10,sticky='w')

PepsiEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
PepsiEntry.grid(row=1,column=1,pady=5,padx=10)
PepsiEntry.insert(0,0)

#
SpriteLabel=Label(drinksframe,text='Sprite',font=('times new roman',15,'bold'),background='gray20',foreground='white')
SpriteLabel.grid(row=2,column=0,pady=5,padx=10,sticky='w')

SpriteEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
SpriteEntry.grid(row=2,column=1,pady=5,padx=10)
SpriteEntry.insert(0,0)


DewLabel=Label(drinksframe,text='Dew',font=('times new roman',15,'bold'),background='gray20',foreground='white')
DewLabel.grid(row=3,column=0,pady=5,padx=10,sticky='w')

DewEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
DewEntry.grid(row=3,column=1,pady=5,padx=10)
DewEntry.insert(0,0)

#
FrootiLabel=Label(drinksframe,text='Frooti',font=('times new roman',15,'bold'),background='gray20',foreground='white')
FrootiLabel.grid(row=4,column=0,pady=5,padx=10,sticky='w')

FrootiEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
FrootiEntry.grid(row=4,column=1,pady=5,padx=10)
FrootiEntry.insert(0,0)


cocacolaLabel=Label(drinksframe,text='Coca Cola',font=('times new roman',15,'bold'),background='gray20',foreground='white')
cocacolaLabel.grid(row=5,column=0,pady=5,padx=10,sticky='w')

cocacolaEntry = Entry(drinksframe,font=('times new roman',15,'bold'),bd=5,width=10)
cocacolaEntry.grid(row=5,column=1,pady=5,padx=10)
cocacolaEntry.insert(0,0)

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

billbutton=Button(buttonFrame,text="Bill",font=('arial',16,'bold'),background="gray20",foreground='white',bd=5,width=8,pady=10,command=bill_area)
billbutton.grid(row=0,column=1,pady=20,padx=5)

emailbutton=Button(buttonFrame,text="Email",font=('arial',16,'bold'),background="gray20",
                   foreground='white',bd=5,width=8,pady=10,command=send_email)
emailbutton.grid(row=0,column=2,pady=20,padx=5)

printbutton=Button(buttonFrame,text="Print",font=('arial',16,'bold'),background="gray20",
                   foreground='white',bd=5,width=8,pady=10,command=print_bill)
printbutton.grid(row=0,column=3,pady=20,padx=5)

clearbutton=Button(buttonFrame,text="Clear",font=('arial',16,'bold'),
                   background="gray20",foreground='white',bd=5,width=8,pady=10,command=clear)
clearbutton.grid(row=0,column=4,pady=20,padx=5)



root.mainloop()
