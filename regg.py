from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("REGISTRATION FORM")
root.geometry('250x300')
def callback():
    messagebox.showinfo("submit successfully ")
    print("you clicked submit")
lbl1=Label(root,text="REGISTRATION FORM",font=("bold",15),fg="black",bg="white")
lbl1.pack()
lbl2=Label(root,text="name")
lbl2.pack()
entry2=Entry(root,bg="white",fg="black",bd=5)
entry2.pack()
lbl3=Label(root,text="Address")
lbl3.pack()
entry3=Entry(root,bg="white",fg="black",bd=5)
entry3.pack()
lbl4=Label(root,text="email id")
lbl4.pack()
entry3=Entry(root,bg="white",fg="black",bd=5)
entry3.pack()

button1=Button(root,text="Submit",command=callback)
button1.pack()

root.title("REGISTRATION")
root.mainloop()

