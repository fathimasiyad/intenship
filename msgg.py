from tkinter import*
from tkinter import messagebox
root=Tk()
def callback():
    messagebox.showinfo("Well Done Great !")
    print("You Clicked Delete")
    
button1=Button(root,text="Delete",command=callback)
button1.grid(row=0,column=0,padx=90,pady=50)
root.geometry('350x250')
root.title("PythonLobby")
root.mainloop()

