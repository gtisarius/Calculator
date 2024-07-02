import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GT's Wonderful GUI Calculator - Mk 2")
#root.geometry('800x600')

fNumber = tk.DoubleVar(value='')
sNumber = tk.DoubleVar(value='')
solutionVar = tk.DoubleVar()

#mainframe = ttk.Frame(root)

def getValues():
    rawNum1 = fNumberEntry.get()
    rawNum2 = sNumberEntry.get()
    if rawNum1 == '':
        rawNum1 = 0
    
    if rawNum2 == '':
        rawNum2 = 0
    try:
        num1 = float(rawNum1)
        num2 = float(rawNum2)
    except:
        solutionVar.set('Invalid number.')
    else:
        arr = [num1, num2]
        return arr
        
def add():
    numbers = getValues()
    solution = numbers[0] + numbers[1]
    solutionVar.set(solution)
    fNumber.set(solution)

def subtract():
    numbers = getValues()
    solution = numbers[0] - numbers[1]
    solutionVar.set(solution)
    fNumber.set(solution)

def multiply():
    numbers = getValues()
    solution = numbers[0] * numbers[1]
    solutionVar.set(solution)
    fNumber.set(solution)

def divide():
    numbers = getValues()
    try:
        solution = numbers[0] / numbers[1]
        solutionVar.set(solution)
        fNumber.set(solution)
    except:
        solutionVar.set('Congrats jackass\nyou divided by zero')

solution = ttk.Label(root, 
                  textvariable = solutionVar, 
                  width=20, anchor="center", 
                  font=("Comic Sans MS", 24, "bold"),
                  #padding=(5, 0)
                  )
solution.grid()

#fNumber = StringVar()
fNumberLabel = ttk.Label(root, text="Input first number: ", anchor="e").grid(row=1, column=0)
fNumberEntry = ttk.Entry(root, textvariable=fNumber)
fNumberEntry.grid(row=2)
sNumberLabel = ttk.Label(root, text="Input second number: ", anchor="e").grid(row=3, column=0)
sNumberEntry = ttk.Entry(root, textvariable=sNumber)
sNumberEntry.grid(row=4)

#button = ttk.Button(root, text="Click Me!", command=getValues).grid()
button = ttk.Button(root, text="Add", command=add).grid()
button = ttk.Button(root, text="Subtract", command=subtract).grid()
button = ttk.Button(root, text="Multiply", command=multiply).grid()
button = ttk.Button(root, text="Divide", command=divide).grid()
#title = Label(tk, text="Calculator")

root.mainloop()