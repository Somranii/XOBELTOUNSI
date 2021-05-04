from tkinter import *		#hadhi l tkinter b kol’ha
from tkinter import messagebox  #hadhi mta3 message box

root = Tk() 
root.title('XO BEL TOUNSI XD')

Nazel = True
count = 0

# Ki youfa l toreh nsakro l fless
def Saker():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# nshoufou chkoun rbeh
def Chkoun_Rbeh():
    global Rabe7
    Rabe7 = False
 

 # Ken X rbe7 

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  X Rbe7!!")
        Saker()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  X Rbe7!!")
        Saker()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  X Rbe7!!")
        Saker()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  X Rbe7!!")
        Saker()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  X Rbe7!!")
        Saker()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  X Rbe7!!")
        Saker()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  X Rbe7!!")
        Saker()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  X Rbe7!!")
        Saker()

    # Ken l O Rbe7
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  O Rbe7!!")
        Saker()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  O Rbe7!!")
        Saker()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  O Rbe7!!")
        Saker()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  O Rbe7!!")
        Saker()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  O Rbe7!!")
        Saker()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  O Rbe7!!")
        Saker()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  O Rbe7!!")
        Saker()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        Rabe7 = True
        messagebox.showinfo("XO BEL TOUNSI XD", "MABROUUK AY !  O Rbe7!!")
        Saker()

    # za3ma ta3adol ?
    if count == 9 and Rabe7 == False:
        messagebox.showinfo("XO BEL TOUNSI XD", "Marbeh had , msh lazem ")
        Saker()
                
# Fonction li tenzel aal felsa 
def b_click(b):
    global Nazel, count

    if b["text"] == " " and Nazel == True:
        b["text"] = "X"
        Nazel = False
        count += 1
        Chkoun_Rbeh()
    elif b["text"] == " " and Nazel == False:
        b["text"] = "O"
        Nazel = True
        count += 1
        Chkoun_Rbeh()
    else:
        messagebox.showwarning("XO BEL TOUNSI XD", "Haka tawa ? , akhtar box akher " )

#  naawdo l game
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global Nazel, count
    Nazel = True
    count = 0

    # lahne l fless 
    b1 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))
    
  # lahne bsh n9asmo  ecran  
    l1=Label(root,text="Player 1: X ",font="Helvetica")
    l1.grid(row=0,column=1)
    l2=Label(root,text="Player 2: O ",font="Helvetica")
    l2.grid(row=0,column=2)
 
    b1.grid(row=1, column=1)
    b2.grid(row=1, column=2)
    b3.grid(row=1, column=3)

    b4.grid(row=2, column=1)
    b5.grid(row=2, column=2)
    b6.grid(row=2, column=3)

    b7.grid(row=3, column=1)
    b8.grid(row=3, column=2)
    b9.grid(row=3, column=3)

# Ngedo el menu 
el_menu = Menu(root)
root.config(menu=el_menu)

options_menu = Menu(el_menu, tearoff=False)
el_menu.add_cascade(label="Fama Moshkla ?", menu=options_menu)
options_menu.add_command(label="t3awed ?", command=reset)

reset()

root.mainloop() # hadhi l main function li bsh tsir aleha l7keya l kol 

