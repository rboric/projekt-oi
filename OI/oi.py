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
budgetRestriction = Label(root)
taxLabel = Label(root)
moneywithtaxLabel = Label(root)
balanceLabel = Label(root)

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

    global budgetLabel, moneyLabel, budgetRestriction, taxLabel, moneywithtaxLabel, balanceLabel
    budgetLabel.destroy()
    moneyLabel.destroy()
    budgetRestriction.destroy()
    taxLabel.destroy()
    moneywithtaxLabel.destroy()
    balanceLabel.destroy()
    if (int(budgetE.get()) < 0):
        budgetRestriction = Label(root, text="Budget can't be less than 0 or a string")
        budgetRestriction.grid(row=0, column=3)
    budgetResult = int(budgetE.get())-(int(appCostE.get())*int(appNumberE.get()))
    budgetLabel = Label(root, text="Budget left: %d €" % budgetResult)
    budgetLabel.grid(row=5, column=0, columnspan=3)
    moneyResult = int(rentE.get())*int(dayE.get())*int(appNumberE.get())
    moneyLabel = Label(root, text="Money earned: %d €" % moneyResult)
    moneyLabel.grid(row=6, column=0, columnspan=3)
    taxResult = (int(taxE.get())/100)*int(moneyResult)
    taxLabel = Label(root, text="Tax from earnings: %d €" % taxResult)
    taxLabel.grid(row=7, column=0, columnspan=3)
    moneywithtaxResult = moneyResult - taxResult
    moneywithtaxLabel = Label(root, text="Money with tax subtracted: %d €" % moneywithtaxResult)
    moneywithtaxLabel.grid(row=8, column=0, columnspan=3)
    moneySavingsResult = (int(savingsE.get())/100)*moneywithtaxResult
    balanceLabel = Label(root, text="Balance left: %d €" % moneySavingsResult)
    balanceLabel.grid(row=9, column=0, columnspan=3)
    balanceInvestedResult = moneywithtaxResult - moneySavingsResult
    numberOfYears = int(budgetE.get()) / balanceInvestedResult
    numberOfYearsLabel = Label(root, text="Number of years to return the budget invested: %d " % ceil(numberOfYears))
    numberOfYearsLabel.grid(row=10, column=0, columnspan=3)




    
sbmitbtn = Button(root, text = "Submit", command=solver) 
sbmitbtn.grid(row=4, column=2, pady="20")

root.mainloop()  