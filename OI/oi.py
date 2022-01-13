
from tkinter import *

# Frame

root = Tk()  
  
root.geometry("550x400")  
root.title("OI")

# Global Variables

balanceLabel = Label(root)
moneyLabel = Label(root)

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

def solver():

    global balanceLabel, moneyLabel
    balanceLabel.destroy()
    moneyLabel.destroy()
    balanceResult = int(budgetE.get())-(int(appCostE.get())*int(appNumberE.get()))
    balanceLabel = Label(root, text="Balance left: %d €" % balanceResult)
    balanceLabel.grid(row=4, column=0, columnspan=3)
    moneyResult = int(rentE.get())*int(dayE.get())*int(appNumberE.get())
    moneyLabel = Label(root, text="Money earned: %d €" % moneyResult)
    moneyLabel.grid(row=5, column=0, columnspan=3)
    
sbmitbtn = Button(root, text = "Submit", command=solver) 
sbmitbtn.grid(row=3, column=2)

root.mainloop()  