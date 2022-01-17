from cgitb import text
from math import ceil
from tkinter import *
from turtle import width

# Frame

root = Tk()  
  
root.geometry("750x400")  
root.title("OI")

# Global Variables

budgetLabel = Label(root)
moneyLabel = Label(root)
taxLabel = Label(root)
moneywithtaxLabel = Label(root)
balanceLabel = Label(root)
numberOfYearsLabel = Label(root)
budgetRestriction = Label(root)
appCostRestriction = Label(root)
appNumberRestriction = Label(root)
rentRestriction = Label(root)
dayRestriction = Label(root)
taxRestriction = Label(root)
savingsRestriction = Label(root)


# Frame Options

budgetL = Label(root, text = "Budget")
budgetL.grid(row=0, column=0, padx=20, pady=20)
budgetE = Entry(root)
budgetE.grid(row=0, column=1)
budgetSign = Label(root, text = "€")
budgetSign.grid(row=0, column=2)
  
appCostL = Label(root, text = "App Cost")
appCostL.grid(row=1, column=0)
appCostE = Entry(root)
appCostE.grid(row=1, column=1)
appCostSign = Label(root, text = "€")
appCostSign.grid(row=1, column=2)

appNumberL = Label(root, text="App Number")
appNumberL.grid(row=1, column=3, padx=10)
appNumberE = Entry(root, width=3)
appNumberE.grid(row=1, column=4)

rentL = Label(root, text="Rent")
rentL.grid(row=2, column=0, padx=20, pady=20)
rentE = Entry(root)  
rentE.grid(row=2, column=1)
rentSign = Label(root, text="€ / day")
rentSign.grid(row=2, column=2)

dayL = Label(root, text="Day Number")
dayL.grid(row=2, column=3, padx=20, pady=20)
dayE = Entry(root, width=3)
dayE.grid(row=2, column=4)

taxL = Label(root, text="Tax")
taxL.grid(row=3, column=0)
taxE = Entry(root)
taxE.grid(row=3, column=1)
taxSign = Label(root, text="€")
taxSign.grid(row=3, column=2)

savingsL = Label(root, text="Percentage of savings")
savingsL.grid(row=3, column=3, padx=20)
savingsE = Entry(root, width=3)
savingsE.grid(row=3, column=4)

# Solver

def solver():

    global budgetLabel, moneyLabel, taxLabel, moneywithtaxLabel, balanceLabel, numberOfYearsLabel
    global budgetRestriction, appCostRestriction, appNumberRestriction, rentRestriction, dayRestriction, taxRestriction, savingsRestriction
    
    budgetLabel.destroy()
    moneyLabel.destroy()
    taxLabel.destroy()
    moneywithtaxLabel.destroy()
    balanceLabel.destroy()
    numberOfYearsLabel.destroy()
    budgetRestriction.destroy()
    appCostRestriction.destroy()
    appNumberRestriction.destroy()
    rentRestriction.destroy()
    dayRestriction.destroy()
    taxRestriction.destroy()
    savingsRestriction.destroy()

    budgetResult = int(budgetE.get())-(int(appCostE.get())*int(appNumberE.get()))
    moneyResult = int(rentE.get())*int(dayE.get())*int(appNumberE.get())
    taxResult = (int(taxE.get())/100)*int(moneyResult)
    moneywithtaxResult = moneyResult - taxResult
    moneySavingsResult = (int(savingsE.get())/100)*moneywithtaxResult
    balanceInvestedResult = moneywithtaxResult - moneySavingsResult
    numberOfYears = int(budgetE.get()) / balanceInvestedResult

    if (int(budgetE.get()) < 0):
        budgetRestriction = Label(root, text="Budget can't be less than 0", fg='#ff1717')
        budgetRestriction.place(x=20, y=0)
        budgetResult = 0
        moneyResult = 0
        taxResult = 0
        moneywithtaxResult = 0
        moneySavingsResult = 0
        balanceInvestedResult = 0
        numberOfYears = 0
    if (int(appCostE.get()) < 0):
        appCostRestriction = Label(root, text="Apartment cost can't be less than 0", fg='#ff1717')
        appCostRestriction.place(x=20, y=40)
        budgetResult = 0
        moneyResult = 0
        taxResult = 0
        moneywithtaxResult = 0
        moneySavingsResult = 0
        balanceInvestedResult = 0
        numberOfYears = 0
    if (int(appNumberE.get()) < 0):
        appNumberRestriction = Label(root, text="Apartment number can't be less than 0", fg='#ff1717')
        appNumberRestriction.place(x=300, y=40)
        budgetResult = 0
        moneyResult = 0
        taxResult = 0
        moneywithtaxResult = 0
        moneySavingsResult = 0
        balanceInvestedResult = 0
        numberOfYears = 0
    if (int(rentE.get()) <= 0):
        rentRestriction = Label(root, text="Rent can't be less than or equal to 0", fg='#ff1717')
        rentRestriction.place(x=20, y=80)
        budgetResult = 0
        moneyResult = 0
        taxResult = 0
        moneywithtaxResult = 0
        moneySavingsResult = 0
        balanceInvestedResult = 0
        numberOfYears = 0
    if (int(dayE.get()) <= 0 or int(dayE.get()) > 365 ):
        dayRestriction = Label(root, text="Days can't be less than or equal to 0 or more than 365", fg='#ff1717')
        dayRestriction.place(x=300, y=80)
        budgetResult = 0
        moneyResult = 0
        taxResult = 0
        moneywithtaxResult = 0
        moneySavingsResult = 0
        balanceInvestedResult = 0
        numberOfYears = 0
    if (int(taxE.get()) < 0 or int(taxE.get()) > 100):
        taxRestriction = Label(root, text="Tax can't be less than 0 or more than 100", fg='#ff1717')
        taxRestriction.place(x=20, y=120)
        budgetResult = 0
        moneyResult = 0
        taxResult = 0
        moneywithtaxResult = 0
        moneySavingsResult = 0
        balanceInvestedResult = 0
        numberOfYears = 0
    if (int(savingsE.get()) < 0 or int(savingsE.get()) > 100):
        savingsRestriction = Label(root, text="Savings can't be less than 0 or more than 100", fg='#ff1717')
        savingsRestriction.place(x=300, y=120)
        budgetResult = 0
        moneyResult = 0
        taxResult = 0
        moneywithtaxResult = 0
        moneySavingsResult = 0
        balanceInvestedResult = 0
        numberOfYears = 0

    budgetLabel = Label(root, text="Budget left: %d €" % budgetResult)
    budgetLabel.grid(row=5, column=0, columnspan=3)
    moneyLabel = Label(root, text="Money earned: %d €" % moneyResult)
    moneyLabel.grid(row=6, column=0, columnspan=3)
    taxLabel = Label(root, text="Tax from earnings: %d €" % taxResult)
    taxLabel.grid(row=7, column=0, columnspan=3)
    moneywithtaxLabel = Label(root, text="Money with tax subtracted: %d €" % moneywithtaxResult)
    moneywithtaxLabel.grid(row=8, column=0, columnspan=3)
    balanceLabel = Label(root, text="Balance left: %d €" % moneySavingsResult)
    balanceLabel.grid(row=9, column=0, columnspan=3)
    numberOfYearsLabel = Label(root, text="Number of years to return the budget invested: %d " % ceil(numberOfYears))
    numberOfYearsLabel.grid(row=10, column=0, columnspan=3)

sbmitbtn = Button(root, text = "Submit", command=solver) 
sbmitbtn.grid(row=4, column=2, pady="20")

root.mainloop()  