import easytkinter as etk

etk.root.title("calculator")

num_entry=etk.ENT(posx=0,posy=0,sizex=3,sizey=1,sizef=30,sizew=10)

b1=etk.BTN(" 1 ",posx=0,posy=1,sizex=1,sizey=1,sizef=20,command=lambda:adding("1"))
b2=etk.BTN(" 2 ",posx=1,posy=1,sizex=1,sizey=1,sizef=20,command=lambda:adding("2"))
b3=etk.BTN(" 3 ",posx=2,posy=1,sizex=1,sizey=1,sizef=20,command=lambda:adding("3"))
b4=etk.BTN(" 4 ",posx=0,posy=2,sizex=1,sizey=1,sizef=20,command=lambda:adding("4"))
b5=etk.BTN(" 5 ",posx=1,posy=2,sizex=1,sizey=1,sizef=20,command=lambda:adding("5"))
b6=etk.BTN(" 6 ",posx=2,posy=2,sizex=1,sizey=1,sizef=20,command=lambda:adding("6"))
b7=etk.BTN(" 7 ",posx=0,posy=3,sizex=1,sizey=1,sizef=20,command=lambda:adding("7"))
b8=etk.BTN(" 8 ",posx=1,posy=3,sizex=1,sizey=1,sizef=20,command=lambda:adding("8"))
b9=etk.BTN(" 9 ",posx=2,posy=3,sizex=1,sizey=1,sizef=20,command=lambda:adding("9"))
b0=etk.BTN(" 0 ",posx=0,posy=4,sizex=1,sizey=1,sizef=20,command=lambda:adding("0"))

plus_button=etk.BTN("  + ",posx=3,posy=1,sizex=1,sizey=1,sizef=25,command=lambda:adding("+"))
minus_button=etk.BTN("  -  ",posx=4,posy=1,sizex=1,sizey=1,sizef=25,command=lambda:adding("-"))
multiply_button=etk.BTN("  *  ",posx=3,posy=2,sizex=1,sizey=1,sizef=25,command=lambda:adding("*"))
divide_button=etk.BTN("  /  ",posx=4,posy=2,sizex=1,sizey=1,sizef=25,command=lambda:adding("/"))

clear_button=etk.BTN(" CLEAR ",posx=1,posy=4,sizex=2,sizey=1,sizef=20,command=lambda:clear())
equal_button=etk.BTN("  =  ",posx=3,posy=3,sizex=2,sizey=2,sizef=40,command=lambda:result())
result_label=etk.LBL("result",posx=3,posy=0,sizex=2,sizey=1,sizef=30)

def adding(a=""):
    num_entry.insert("end",a)

def clear():
    result_label.config(text="result")
    num_entry.delete("0","end")
    
def result():
    a=str(num_entry.get())
    result_label.config(text=eval(a))

etk.root.mainloop()