from tkinter import *
root = Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0,column=0, columnspan=3)
total=0

def myClick():
    hello= "Hello " + e.get()
    myLabel = Label(root,text=hello)
    myLabel.pack()

def  button_click(number):
    #e.delete(0,END)    
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
    
def button_cler():
    e.delete(0,END)
    
def button_add():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0,END)
    global  operation_type
    operation_type = 1
    
def button_subtraction():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0,END)
    global operation_type
    operation_type = 2

def button_division():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0,END)
    global operation_type
    operation_type = 3
    
def button_multiplication():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0,END)
    global operation_type
    operation_type = 4

def button_equal():
    second_number = float(e.get())
    e.delete(0,END)
    global operation_type
    if operation_type == 1:
        result = second_number+ f_num
    elif operation_type == 2:
        result = f_num - second_number
    elif operation_type == 3:
        result = f_num / second_number
    elif operation_type == 4:
        result = f_num * second_number
        
    e.insert(0,"%.2f" %result)
#define buttton

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)) 

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)
                  )
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_clear = Button(root, text="Clear", padx=28, pady=20, command=button_cler)
button_division = Button(root, text="/", padx=40, pady=20, command=button_division)

button_ad = Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtraction = Button(root, text="-", padx=40, pady=20, command=button_subtraction)
button_multiplication = Button(root, text="X", padx=40, pady=20, command=button_multiplication)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)


#put buttons on screen 

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_multiplication.grid(row=3, column=3, )



button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtraction.grid(row=2, column=3)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_ad.grid(row=1, column=3, )

button_clear.grid(row=4, column=0, )
button_0.grid(row=4, column=1,  )
button_equal.grid(row=4, column=2,  )
button_division.grid(row=4, column=3, )













#shoving label on to screen


root.mainloop()