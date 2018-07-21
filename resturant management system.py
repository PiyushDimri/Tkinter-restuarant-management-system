from tkinter import *



root = Tk()

root.geometry("1600x8000")

root.title("Restaurant Management")



Tops = Frame(root, width=1600, relief=SUNKEN)

Tops.pack(side=TOP)



f1 = Frame(root, width=800, height=700, relief=SUNKEN)

f1.pack(side=LEFT)



lblInfo = Label(Tops, font=('helvetica', 50, 'bold'), text="GREEN VALLEY RESTAURANT", fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

lblInfo2 = Label(Tops, font=('arial', 20, 'bold'), text='', fg="Red", bd=10, anchor='w')

lblInfo2.grid(row=2, column=0)




def Ref():

    global CoFries, CostofFries, CoNoodles, CostofNoodles, CoSoup, CostofSoup, CoBurger, CostBurger, CoPizza, CostofPizza

    global CoSandwich, CostSandwich, CoD, CostofDrinks, CoManchurian, CostofManchurian,TotalCost


    try:

        if (Fries.get() == ""):

            CoFries = 0

        else:

            CoFries = float(Fries.get())



        if (Sandwich.get() == ""):

            CoNoodles = 0

        else:

            CoNoodles = float(Noodles.get())



        if (Soup.get() == ""):

            CoSoup = 0

        else:

            CoSoup = float(Soup.get())



        if (Burger.get() == ""):

            CoBurger = 0

        else:

            CoBurger = float(Burger.get())



        if (Sandwich.get() == ""):

            CoSandwich = 0

        else:

            CoSandwich = float(Sandwich.get())



        if (Drinks.get() == ""):

            CoD = 0

        else:

            CoD = float(Drinks.get())

        if (Pizza.get() == ""):

            CoPizza = 0

        else:

            CoPizza = float(Pizza.get())

        if (Manchurian.get() == ""):

            CoManchurian = 0

        else:

            CoManchurian = float(Manchurian.get())




    except ValueError:

        lblInfo2.config(text="Invalid values, please re-enter")



    CostofFries = CoFries * 140

    CostofDrinks = CoD * 65

    CostofNoodles = CoNoodles * 90

    CostofSoup = CoSoup * 140

    CostBurger = CoBurger * 260

    CostSandwich = CoSandwich * 300

    CostofPizza = CoPizza * 400

    CostofManchurian = CoManchurian * 245

    TotalCost = (CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich + CostofPizza + CostofManchurian)


    Total.set(TotalCost)


def qExit():

    root.destroy()


def Reset():


    Fries.set("")

    Noodles.set("")

    Soup.set("")

    Pizza.set("")

    Total.set("")

    Manchurian.set("")

    Drinks.set("")

    Burger.set("")

    Sandwich.set("")

    lblInfo2.config(text='')



Fries = StringVar()

Noodles = StringVar()

Soup = StringVar()

Pizza = StringVar()

Total = StringVar()

Manchurian = StringVar()

Drinks = StringVar()

Burger = StringVar()

Sandwich = StringVar()



lblPizza = Label(f1, font=('arial', 16, 'bold'), text="Pizza", bd=16, anchor="w")

lblPizza.grid(row=0, column=0)

txtPizza = Entry(f1, font=('arial', 16, 'bold'), textvariable=Pizza, bd=10, insertwidth=4, bg="powder blue",

                     justify='right')

txtPizza.grid(row=0, column=1)



lblFries = Label(f1, font=('arial', 16, 'bold'), text="Fries", bd=16, anchor="w")

lblFries.grid(row=1, column=0)

txtFries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg="powder blue",

                 justify='right')

txtFries.grid(row=1, column=1)



lblNoodles = Label(f1, font=('arial', 16, 'bold'), text="Noodles", bd=16, anchor="w")

lblNoodles.grid(row=2, column=0)

txtNoodles = Entry(f1, font=('arial', 16, 'bold'), textvariable=Noodles, bd=10, insertwidth=4, bg="powder blue",

                   justify='right')

txtNoodles.grid(row=2, column=1)



lblSoup = Label(f1, font=('arial', 16, 'bold'), text="Soup", bd=16, anchor="w")

lblSoup.grid(row=3, column=0)

txtSoup = Entry(f1, font=('arial', 16, 'bold'), textvariable=Soup, bd=10, insertwidth=4, bg="powder blue",

                justify='right')

txtSoup.grid(row=3, column=1)



lblBurger = Label(f1, font=('arial', 16, 'bold'), text="Burger", bd=16, anchor="w")

lblBurger.grid(row=0, column=2)

txtBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg="powder blue",

                  justify='right')

txtBurger.grid(row=0, column=3)



lblSandwich = Label(f1, font=('arial', 16, 'bold'), text="Sandwich", bd=16, anchor="w")

lblSandwich.grid(row=1, column=2)

txtSandwich = Entry(f1, font=('arial', 16, 'bold'), textvariable=Sandwich, bd=10, insertwidth=4, bg="powder blue",

                    justify='right')

txtSandwich.grid(row=1, column=3)


lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor="w")

lblDrinks.grid(row=2, column=2)

txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="powder blue",

                  justify='right')

txtDrinks.grid(row=2, column=3)


lblManchurian = Label(f1, font=('arial', 16, 'bold'), text="Manchurian", bd=16, anchor="w")

lblManchurian.grid(row=3, column=2)

txtManchurian = Entry(f1, font=('arial', 16, 'bold'), textvariable=Manchurian, bd=10, insertwidth=4, bg="powder blue",

                justify='right')

txtManchurian.grid(row=3, column=3)


lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor="w")

lblTotalCost.grid(row=9, column=1)

txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="powder blue",

                     justify='right')

txtTotalCost.grid(row=9, column=2)


btnTotal = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total",

                  bg="grey", command=Ref).grid(row=11, column=3)


btnReset = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset",

                  bg="orange", command=Reset).grid(row=11, column=4)

btnExit = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit",

                 bg="red", command=qExit).grid(row=11, column=5)



root.mainloop()