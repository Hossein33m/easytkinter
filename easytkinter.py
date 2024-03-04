import tkinter as tk

root=tk.Tk()
root.config(bg="#d2b48c")

def nothing():
    pass

def BTN (txt="button",posx=0,posy=0,sizex=1,sizey=1,sizef=10,command=nothing):
    mybutton=tk.Button(root,text=txt,command=command,font=("Times New Roman",sizef),bd=5,bg="#cd853f",fg="#000000",activebackground="#d2691e")
    mybutton.grid(column=posx,row=posy,padx=5,pady=5,columnspan=sizex,rowspan=sizey)
    return mybutton

def ENT (posx=0,posy=0,sizex=1,sizey=1,sizef=10,sizew=20):
    myentry=tk.Entry(root,justify="center",font=("Times New Roman",sizef),bd=5,bg="#ffffff",fg="#000000",width=sizew)
    myentry.grid(column=posx,row=posy,padx=5,pady=5,columnspan=sizex,rowspan=sizey)
    return myentry

def LBL (txt="label",posx=0,posy=0,sizex=1,sizey=1,sizef=10):
    mylabel=tk.Label(root,text=txt,font=("Times New Roman",sizef),bd=5,bg="#d2b48c",fg="#000000")
    mylabel.grid(column=posx,row=posy,padx=5,pady=5,columnspan=sizex,rowspan=sizey)
    return mylabel
