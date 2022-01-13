#------------------------------------------------------------------------------MODULES IMPORTED --------------------------------------------------------------------
from tkinter import*
import random
import time;
from tkinter import messagebox

#-----------------------------------------------------------------TITLE OF THE TKINTER OUTPUT SCREEN --------------------------------------------------------------
root = Tk()
root.geometry("1600x800+0+0")
root.title("LE GRAND PRIX'S THEATRE TICKET BOOKING SYSTEM")

text_Input = StringVar()
operator =""
Tops = Frame(root, width = 1600, height = 50,bg="blue4", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300, height = 700,relief=SUNKEN)
f2.pack(side=RIGHT)

#-----------------------------------------------------------------------------------------TIME-----------------------------------------------------------------------------------

localtime=time.asctime(time.localtime(time.time())) #Date Time Function

#------------------------------------------------------------------------------------------INFO----------------------------------------------------------------------------------

lblInfo = Label(Tops, font=('arial', 35, 'bold'), text="LE GRAND PRIX'S THEATRE TICKET BOOKING SYSTEM", fg="DarkOrange3", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblDateTime = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Red", bd=10, anchor='w')
lblDateTime.grid(row=1,column=0)

#----------------------------------------------------------------------------------Instructions---------------------------------------------------------------------------------
def instructions():
    messagebox.showinfo("STEPS", "Instructions to book a ticket")
    messagebox.showinfo("STEPS", "Step 1 -- Enter only integers for Number of tickets, Drinks,Burger,Soups,Icecreams. (Maximum allowed per ticket: 10)")
    messagebox.showinfo("STEPS", "Step 2 -- Shows available now: Master, Doctor")
    messagebox.showinfo("STEPS", "Step 3 -- Press Total or Receipt to get the Receipt for your transaction")
    messagebox.showinfo("STEPS","Do not enter any value in the Reference,Cost,GST,CSGT,SubTotal, TotalCost ; it will be auto-generated")

#-----------------------------------------------------------------------Validation for type-------------------------------------------------------------------------------------
def validate(CoMovieName):#validation for number of letters to be entered in MovieName
    while CoMovieName.isalnum() is False:
        MovieName.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Enter a minimum of 1 letter and a maximum of 20 letters in Movie Name. Enter only integers or alphabets in Movie Name")
        top.mainloop()
        top.destroy()

def validate2(CoT):#Validation for entering only integers in Number of tickets
    while CoT.isdigit() is False:
        Nooftickets.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Enter only integers in Number of tickets")
        top.mainloop()
        top.destroy()

def validate3(CoD):#Validation for entering only integers in Drinks
    while CoD.isdigit() is False:
        Drinks.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Enter only integers in Drinks")
        top.mainloop()
        top.destroy()


def validate4(CoBurger):#Validation for entering only integers in Burger
    while CoBurger.isdigit() is False:
        Burger.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Enter only integers in Burger")
        top.mainloop()
        top.destroy()

def validate5(CoSoups):#Validation for entering only integers in Soups
    while CoSoups.isdigit() is False:
        Soups.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Enter only integers in Soups")
        top.mainloop()
        top.destroy()

def validate6(CoIceCream):#Validation for entering only integers in Ice Cream
    while CoIceCream.isdigit() is False:
        IceCream.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Enter only integers in Ice Cream")
        top.mainloop()
        top.destroy()

#-----------------------------------------------------------------------Validation for maximum allowance---------------------------------------------------------------------------------------------
def validate7(CoMovieName):#Validation for entering the below mentioned spellings in MovieName
    MovieList=['Master', 'master', 'MASTER', 'Doctor', 'doctor', 'DOCTOR']
    while CoMovieName not in MovieList:
        MovieName.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Please enter either of these spellings - 'Master', 'master', 'MASTER', 'Doctor', 'doctor', 'DOCTOR'")
        top.mainloop()
        top.destroy()

def validate8(CoT):#Validation for maximum and minimum allowed values in Number of Tickets
    while int(CoT)>=11 or int(CoT)<1:
        Nooftickets.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Minimum 1 and Maximum 10 only allowed per receipt in Number of Tickets")
        top.mainloop()
        top.destroy()

def validate9(CoD):#Validation for maximum and minimum allowed values in Drinks
    while int(CoD)>=11:
        Drinks.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Maximum allowed only 10 per receipt in Drinks")
        top.mainloop()
        top.destroy()


def validate10(CoBurger):#Validation for maximum and minimum allowed values in Burger
    while int(CoBurger)>=11:
        Burger.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Maximum allowed only 10 per receipt in Burger")
        top.mainloop()
        top.destroy()

def validate11(CoSoups):#Validation for maximum and minimum allowed values in Soups
    while int(CoSoups)>=11:
        Soups.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Maximum allowed only 10 per receipt in Soups")
        top.mainloop()
        top.destroy()

def validate12(CoIceCream):#Validation for maximum and minimum allowed values in Ice Cream
    while int(CoIceCream)>=11:
        IceCream.set("")
        top=Tk()
        top.geometry("500x500")
        messagebox.showerror("ERROR", "Maximum allowed only 10 per receipt in Ice Cream")
        top.mainloop()
        top.destroy()

#----------------------------------------------------------------------------------FOR TKINTER SCREEN-------------------------------------------------------------------------
#------------------------------------------------------------------------------- Receipt Button --------------------------------------------------------------------------
def Ref():
    CoT = str(Nooftickets.get())
    validate2(CoT)
    validate8(CoT)
    
    CoMovieName = str(MovieName.get())
    validate(CoMovieName)
    validate7(CoMovieName)
    
    CoD = str(Drinks.get())
    validate3(CoD)
    validate9(CoD)
    
    CoBurger = str(Burger.get())
    validate4(CoBurger)
    validate10(CoBurger)
    
    CoSoups = str(Soups.get())
    validate5(CoSoups)
    validate11(CoSoups)
    
    CoIceCream = str(IceCream.get())
    validate6(CoIceCream)
    validate12(CoIceCream)

    CostofTickets = (float(CoT)) * 200
    CostofDrinks = (float(CoD)) * 40
    CostofBurger = (float(CoBurger)) * 120
    CostofSoups = (float(CoSoups)) * 50
    CostofIceCream = (float(CoIceCream)) * 110
    
    x = random.randint(100001, 999999)#Generating a random reference number in receipt
    randomRef = str(x)
    rand.set(randomRef)
    
    CostofMeal = "Rs", str('%.2f' % (CostofTickets+CostofDrinks+CostofBurger+CostofSoups+CostofIceCream))#Calculating the total cost

    PayTax = ((CostofTickets+CostofDrinks+CostofBurger+CostofSoups+CostofIceCream) /99)

    TotalCost = (CostofTickets+CostofDrinks+CostofBurger+CostofSoups+CostofIceCream)
    Ser_Charge = (CostofTickets+CostofDrinks+CostofBurger+CostofSoups+CostofIceCream) /99
    Service = "Rs", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs", str('%.2f' % (PayTax+TotalCost+Ser_Charge))
    PaidTax = "Rs", str('%.2f' % PayTax)    
    Service_Charges.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    Cost1234=(OverAllCost)
    
    receipt(CostofTickets,CostofDrinks,CostofBurger,CostofSoups,CostofIceCream,randomRef,CoMovieName,PayTax,Ser_Charge,Cost1234,CoT,CoD,CoBurger,CoSoups,CoIceCream)

#------------------------------------------------------------------------------- For Printing Receipt --------------------------------------------------------------------------
def receipt(CostofTickets,CostofDrinks,CostofBurger,CostofSoups,CostofIceCream,randomRef,CoMovieName,PayTax,Ser_Charge,Cost1234,CoT,CoD,CoBurger,CoSoups,CoIceCream):#Function to show receipt message box
    text_receipt="RECEIPT", "\n\n"
    text_refno="Reference Number-", randomRef,"\n"
    text_namemovie="Movie Name-", CoMovieName,"\n"
    text_ticketcost="Total Tickets & Cost-",CoT, ',', CostofTickets,"\n"
    text_drinks="Total Drinks & Cost-", CoD, ',', CostofDrinks,"\n"
    text_Burger="Total Burger & Cost-", CoBurger, ',', CostofBurger,"\n"
    text_Soups="Total Soups & Cost-", CoSoups, ',', CostofSoups,"\n"
    text_IceCream="Total IceCreams & Cost-", CoIceCream, ',', CostofIceCream,"\n"
    text_Cost1234="Total Cost-", Cost1234,"\n"
    text_all=text_receipt,text_refno,text_namemovie,text_ticketcost,text_drinks,text_Burger,text_Soups,text_IceCream,text_Cost1234
    messagebox.showinfo("TICKET BOOKED", text_all)

#------------------------------------------------------------------------------- Exit Button --------------------------------------------------------------------------
def qExit():
    messagebox.showinfo("Exit", "Click OK or 'Close' or press 'Enter' in your keyboard to close. Thank you for your valuable visit! Please visit us again")
    root.destroy()
    quit()

#------------------------------------------------------------------------------- Reset Button --------------------------------------------------------------------------
def Reset():
    rand.set("")
    Nooftickets.set("0")
    Burger.set("0")
    MovieName.set("Movie")
    SubTotal.set("")
    Total.set("")
    Service_Charges.set("")
    Drinks.set("0")
    Tax.set("")
    Cost.set("")
    Soups.set("0")
    IceCream.set("0")
    instructions()

#-------------------------------------------------------------------------------------------- Ticket info 1  ------------------------------------------------------------------------------------
rand = StringVar()
Nooftickets = StringVar()
Burger = StringVar()
MovieName = StringVar()
SubTotal = StringVar()
Total= StringVar()
Service_Charges = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Soups = StringVar()
IceCream = StringVar()
Nooftickets=StringVar()
drinks=StringVar()
chapati=StringVar()
burger=StringVar()
soups=StringVar()
icecreams=StringVar()
menu=StringVar()

#-------------------------------------------------------------------------------------------Ticket info 1------------------------------------------------------------------------------------------------
lblNooftickets = Label(f1,font=('arial', 16, 'bold') , text="No of tickets(Rs.200)", bd=16, anchor='w')
lblNooftickets.grid(row=0, column=0)
txtNooftickets=Entry(f1,font=('arial', 16, 'bold') , textvariable=Nooftickets, bd=10, insertwidth=4, bg="DarkOliveGreen2", justify = "right")
txtNooftickets.grid(row=0, column=1)

lblinterval = Label(f1,font=('arial', 16, 'bold') , text="ORDER INTERVAL SNACK", bd=16, anchor='w')
lblinterval.grid(row=1, column=0)

lblMovieName = Label(f1,font=('arial', 16, 'bold') , text="Movie Name", bd=16, anchor='w')
lblMovieName.grid(row=2, column=0)
txtMovieName=Entry(f1,font=('arial', 16, 'bold') , textvariable=MovieName, bd=10, insertwidth=4, bg="DarkOliveGreen2", justify = "right")
txtMovieName.grid(row=2, column=1)

lblDrinks = Label(f1,font=('arial', 16, 'bold') , text="Drinks(Rs.40)", bd=16, anchor='w')
lblDrinks.grid(row=3, column=0)
txtDrinks=Entry(f1,font=('arial', 16, 'bold') , textvariable=Drinks, bd=10, insertwidth=4, bg="DarkOliveGreen2", justify = "right")
txtDrinks.grid(row=3, column=1)

lblBurger = Label(f1,font=('arial', 16, 'bold') , text="Burger(Rs.120)", bd=16, anchor='w')
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f1,font=('arial', 16, 'bold') , textvariable=Burger, bd=10, insertwidth=4, bg="DarkOliveGreen2", justify = "right")
txtBurger.grid(row=4, column=1)

lblSoups = Label(f1,font=('arial', 16, 'bold') , text="Soups(Rs.50)", bd=16, anchor='w')
lblSoups .grid(row=5, column=0)
txtSoups =Entry(f1,font=('arial', 16, 'bold') , textvariable=Soups , bd=10, insertwidth=4, bg="DarkOliveGreen2", justify = "right")
txtSoups .grid(row=5, column=1)

lblIceCream = Label(f1,font=('arial', 16, 'bold') , text="IceCream(Rs.110)", bd=16, anchor='w')
lblIceCream.grid(row=6, column=0)
txtIceCream=Entry(f1,font=('arial', 16, 'bold') , textvariable=IceCream , bd=10, insertwidth=4, bg="DarkOliveGreen2", justify = "right")
txtIceCream.grid(row=6, column=1)

#-------------------------------------------------------------------------------------------Ticket info 2------------------------------------------------------------------------------------------------

lblReference = Label(f1,font=('arial', 16, 'bold') , text="Reference", bd=16, anchor='w')
lblReference.grid(row=0, column=2)
txtReference=Entry(f1,font=('arial', 16, 'bold') , textvariable=rand, bd=10, insertwidth=4, bg="bisque", justify = "right")
txtReference.grid(row=0, column=3)

lblCost = Label(f1,font=('arial', 16, 'bold') , text="Cost", bd=16, anchor='w')
lblCost .grid(row=1, column=2)
txtCost=Entry(f1,font=('arial', 16, 'bold') , textvariable=Cost, bd=10, insertwidth=4, bg="bisque", justify = "right")
txtCost.grid(row=1, column=3)

lblService = Label(f1,font=('arial', 16, 'bold') , text="GST", bd=16, anchor='w')
lblService.grid(row=2, column=2)
txtService=Entry(f1,font=('arial', 16, 'bold') , textvariable=Service_Charges, bd=10, insertwidth=4, bg="bisque", justify = "right")
txtService.grid(row=2, column=3)

lblStateTax = Label(f1,font=('arial', 16, 'bold') , text="CGST", bd=16, anchor='w')
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1,font=('arial', 16, 'bold') , textvariable=Tax, bd=10, insertwidth=4, bg="bisque", justify = "right")
txtStateTax.grid(row=3, column=3)

lblSubTotal = Label(f1,font=('arial', 16, 'bold') , text="SubTotal ", bd=16, anchor='w')
lblSubTotal .grid(row=4, column=2)
txtSubTotal=Entry(f1,font=('arial', 16, 'bold') , textvariable=SubTotal , bd=10, insertwidth=4, bg="bisque", justify = "right")
txtSubTotal .grid(row=4, column=3)

lblTotalCost = Label(f1,font=('arial', 16, 'bold') , text="TotalCost", bd=16, anchor='w')
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1,font=('arial', 16, 'bold') , textvariable=Total , bd=10, insertwidth=4, bg="bisque", justify = "right")
txtTotalCost.grid(row=5, column=3) 

lblshow = Label(f1,font=('arial', 16, 'bold') , text="MOVIES NOW SHOWING:", bd=16, anchor='w')
lblshow.grid(row=0, column=4)

lblname1 = Label(f1,font=('arial', 16, 'bold') , text="Master", bd=16, anchor='w')
lblname1.grid(row=1, column=4)

lblname2 = Label(f1,font=('arial', 16, 'bold') , text="Doctor", bd=16, anchor='w')
lblname2.grid(row=2, column=4)

#----------------------------------------------------------------------------------- SET ZERO --------------------------------------------------------------------------------------------------
Nooftickets.set("0")
Burger.set("0")
MovieName.set("Movie")
Drinks.set("0")
Soups.set("0")
IceCream.set("0")

#-------------------------------------------------------------------------------------------Buttons-----------------------------------------------------------------------------------------------
btnTotal = Button(f1,padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold') , width=10, text="RECEIPT", bg="khaki4", command = Ref).grid(row=7,column=0)

btnReset = Button(f1,padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold') , width=10, text="RESET", bg="khaki4", command = Reset).grid(row=7,column=1)

btnqExit = Button(f1,padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold') , width=10, text="EXIT", bg="khaki4", command = qExit).grid(row=7,column=2)

#----------------------------------------------------------------------------------------Instructions function------------------------------------------------------------------------------
instructions()

root.mainloop()
