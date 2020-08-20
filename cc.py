from tkinter import *
import parser  #For mathematical calculations

root = Tk()
root.title("CALCULATOR")

#Getting the user input and placing in the text field
i = 0
def getvar(num):
    global i
    display.insert(i,num)
    i+=1


def getop(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length


def factorial():
    entire_string = display.get()
    number = int(entire_string)
    fact = 1
    counter = number
    try:
        while counter>0:
            fact = fact*counter
            counter-=1
        clear_all()
        display.insert(0,fact)
    except Exception:
        clear_all()
        display.insert(0,"Error")




def calculate():
    entire_string = display.get()

    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)

    except Exception:
        clear_all()
        display.insert(0,"Error")








def clear_all():
    display.delete(0,END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        display.insert(0,"Error")






#Adding the input field

display = Entry(root)
display.grid(row = 1, columnspan = 6,sticky = W+E) #sticky specifing from where to where it lies

#Adding buttons

Button(root,text = "1",width = 4 , height = 2,command = lambda : getvar(1)).grid(row = 2,column = 0)
Button(root,text = "2",width = 4 , height = 2,command = lambda : getvar(2)).grid(row = 2,column = 1)
Button(root,text = "3",width = 4 , height = 2,command = lambda : getvar(3)).grid(row = 2,column = 2)

Button(root,text = "4",width = 4 , height = 2,command = lambda : getvar(4)).grid(row = 3,column = 0)
Button(root,text = "5",width = 4 , height = 2,command = lambda : getvar(5)).grid(row = 3,column = 1)
Button(root,text = "6",width = 4 , height = 2,command = lambda : getvar(6)).grid(row = 3,column = 2)

Button(root,text = "7",width = 4 , height = 2,command = lambda : getvar(7)).grid(row = 4,column = 0)
Button(root,text = "8",width = 4 , height = 2,command = lambda : getvar(8)).grid(row = 4,column = 1)
Button(root,text = "9",width = 4 , height = 2,command = lambda : getvar(9)).grid(row = 4,column = 2)

#Adding other buttons

Button(root,text = "AC",width = 4 , height = 2,command = lambda :clear_all()).grid(row = 5,column = 0)
Button(root,text = "0",width = 4 , height = 2,command = lambda : getvar(0)).grid(row = 5,column = 1)
Button(root,text = "=",width = 4 , height = 2,command = lambda :calculate()).grid(row = 5,column = 2)


Button(root,text = "+",width = 4 , height = 2,command = lambda :getop("+")).grid(row = 2,column = 3)
Button(root,text = "-",width = 4 , height = 2,command = lambda :getop("-")).grid(row = 3,column = 3)
Button(root,text = "*",width = 4 , height = 2,command = lambda :getop("*")).grid(row = 4,column = 3)
Button(root,text = "/",width = 4 , height = 2,command = lambda :getop("/")).grid(row = 5,column = 3)

#Adding few more operations

Button(root,text = "pi",width = 4 , height = 2,command = lambda :getop("*3.14")).grid(row = 2,column = 4)
Button(root,text = "%",width = 4 , height = 2,command = lambda :getop("%")).grid(row = 3,column = 4)
Button(root,text = "(",width = 4 , height = 2,command = lambda :getop("(")).grid(row = 4,column = 4)
Button(root,text = "exp",width = 4 , height = 2,command = lambda :getop("**")).grid(row = 5,column = 4)

Button(root,text = "<-",width = 4 , height = 2, command = lambda :undo()).grid(row = 2,column = 5)
Button(root,text = "x!",width = 4 , height = 2,command = lambda : factorial()).grid(row = 3,column = 5)
Button(root,text = ")",width = 4 , height = 2,command = lambda :getop(")")).grid(row = 4,column = 5)
Button(root,text = "^2",width = 4 , height = 2,command = lambda :getop("**2")).grid(row = 5,column = 5)

root.mainloop()