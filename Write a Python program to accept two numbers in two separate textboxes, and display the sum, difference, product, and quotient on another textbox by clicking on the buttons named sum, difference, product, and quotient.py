from tkinter import *

root = Tk()
root.title("Simple Calculator")

t1 = Entry(root)
t1.pack()

t2 = Entry(root)
t2.pack()

result = Entry(root)
result.pack()

def sum():
    n1 = float(t1.get())
    n2 = float(t2.get())
    s = n1 + n2
    result.delete(0, END)
    result.insert(0, s)
    
def sub():
    n1 = float(t1.get())
    n2 = float(t2.get())
    d = n1 - n2
    result.delete(0, END)
    result.insert(0, d)
    
def mul():
    n1 = float(t1.get())
    n2 = float(t2.get())
    m = n1 * n2
    result.delete(0, END)
    result.insert(0, m)
    
    
def div():
    n1 = float(t1.get())
    n2 = float(t2.get())
    div = n1 / n2
    result.delete(0, END)
    result.insert(0, div)
    
sum_btn = Button(root, text = "Sum", command = sum)
sum_btn.pack()

sub_btn = Button(root, text = "Subtraction", command = sub)
sub_btn.pack()

mul_btn = Button(root, text = "Multiplication", command = mul)
mul_btn.pack()

div_btn = Button(root, text = "Division", command = div)
div_btn.pack()

root.mainloop()