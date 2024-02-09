# import tkinter as tk
# def esapla():
#     a = int(ent.get())
#     b = int(ent.get())
#     c=a+b
    # rst.insert(0,c)


# def oshir():
#     ent.delete(0,tk.END)
#     ent2.delete(0,tk.END)
#     rst.delete(0,tk.END)


# root = tk.Tk()
# root.geometry("240x100")
# root.resizable(0,0)
# root.config(bg="#40ad7e")

# ent = tk.Entry(root,width="5")
# lbl = tk.Label(root,text="+")
# ent2 = tk.Entry(root,width="5")
# btn = tk.Button(root,text="=",command=esapla)
# rst = tk.Entry(root,text="5")
# cl = tk.Button(root,text="O`SHIW",command=oshir)



# ent.grid(row=0,column=0)
# lbl.grid(row=0,column=1)
# ent2.grid(row=0,column=2)
# btn.grid(row=1,column=0)
# rst.grid(row=1,column=1)
# cl.grid(row=1,column=2)


# root.mainloop()



import tkinter as tk


win=tk.Tk()
win.geometry("255x380")
win.resizable(False,False)
win.title("KALKULYATOR")
icon = tk.PhotoImage(file="kal.png.png")
win.iconphoto( True, icon)

def esapla(event):
    txt=entry.get()
    btnTxt =event

    if btnTxt == "C":
        entry.delete(0,tk.END)
    elif btnTxt == "=":
        try:
            rst = eval(txt)
            entry.delete(0,tk.END)
            entry.insert(tk.END,str(rst))
        except Exception as e:
            entry.delete(0,tk.END)
            entry.insert(tk.END, "XATELIK") 
    else:
        entry.insert(tk.END,btnTxt)

def add_btn(frame,text):
    btn = tk.Button(frame,text=text,padx=20,pady=20,command=lambda t=text:esapla(t))
    btn.grid(row=len(frame.grid_slaves()) //4, column=len(frame.grid_slaves())%4)




entry =tk.Entry(win,width=16,font=("Arial",20),bg="black",fg="white",bd=5,relief=tk.FLAT,justify=tk.RIGHT)
entry.grid(row=0,column=0,columnspan=4)

btns_frm = tk.Frame(win)
btns_frm.grid(row=1,column=0,columnspan=4)

btn = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "√", "^2", "%"
]
for i in btn:
    add_btn(btns_frm,i)


win.mainloop()