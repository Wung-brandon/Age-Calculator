from datetime import date
from tkinter import *

#METHOD 1
""" 
root = Tk()
root.geometry("365x584+200+200")
root.title("Age Calculator App")
root.resizable(False,False)
root.config(background="lightblue") """
#icon = PhotoImage(file=r"C:\Users\WK. BRANDON\Desktop\python projects\Age Calculator app\3-39028_icon-hulk-marvel-avengers-alliance-2-hulk.png")
#root.iconphoto(True,icon)
""" 
name = Label(text="Name:",font=("times new roman",10,'bold')).grid(column=0,row=1)
nameEntry = Entry()
nameEntry.grid(column=1,row=1)

year = Label(text="Year:",font=("times new roman",10,'bold')).grid(column=0,row=2)
yearEntry = Entry()
yearEntry.grid(column=1,row=2)

month = Label(text="Month:",font=("times new roman",10,'bold')).grid(column=0,row=3)
monthEntry = Entry()
monthEntry.grid(column=1,row=3)

day = Label(text="Day:",font=("times new roman",10,'bold')).grid(column=0,row=4)
dayEntry = Entry()
dayEntry.grid(column=1,row=4)

def getInput():
    name = nameEntry.get()
    Person = person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get())))
    
    textArea = Text(master=root,height=6,width=25,font=("times new roman",10,'bold'),justify="center")
    textArea.place(x=30,y=190)
    answer = "Heyy {Person}! You are {age} years old!".format(Person=name, age=Person.age())
    textArea.insert(END,answer)


class person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age


calculateAge = Button(root,text="Calculate Age",font=("times new roman",13,'bold'),cursor='hand2',bg='navyblue',fg='white',command=getInput)
calculateAge.place(x=40,y=130)


root.mainloop() """

#METHOD 2
root = Tk()
root.geometry("450x300")
root.title("Age Calculator")
root.config(background="#fff")

def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month,today.day) < (birthDate.month,birthDate.day))
   
    top = Toplevel(bg='#fff')
    top.geometry('280x100')
    top.title('Age')
    l = Label(top,text=f"{nameValue.get()} your age is {age}", font=('times new roman',15),bg='#fff',fg='#000000')
    l.pack()
    
def reset():
    nameEntry.delete(0,END)
    yearEntry.delete(0,END)
    monthEntry.delete(0,END)
    dayEntry.delete(0,END)

def close():
    root.destroy()

Label(text="Name:",font=('ariel',15,'bold'),bg='#fff',fg='#000000').grid(row=1,column=0,padx=90)
Label(text="Year:",font=('ariel',15,'bold'),bg='#fff',fg='#000000').grid(row=2,column=0)
Label(text="Month:",font=('ariel',15,'bold'),bg='#fff',fg='#000000').grid(row=3,column=0)
Label(text="Day:",font=('ariel',15,'bold'),bg='#fff',fg='#000000').grid(row=4,column=0)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root,textvariable=nameValue,font=('ariel',13))
yearEntry = Entry(root,textvariable=yearValue,font=('ariel',13))
monthEntry = Entry(root,textvariable=monthValue,font=('ariel',13))
dayEntry = Entry(root,textvariable=dayValue,font=('ariel',13))


nameEntry.grid(row=1,column=1,pady=10)
yearEntry.grid(row=2,column=1,pady=10)
monthEntry.grid(row=3,column=1,pady=10)
dayEntry.grid(row=4,column=1,pady=10)

compute_Btn = Button(text="What's my age?",command=calculateAge,font=('times new Roman',13),bg='#fff',fg='#000')
compute_Btn.place(x=180,y=200)

reset_Btn = Button(text="Reset",font=('times new Roman',13),command=reset,bg='#fff',fg='#000')
reset_Btn.place(x=100,y=200)

close_Btn = Button(text="Exit",font=('times new Roman',13),command=close,bg='#fff',fg='#000')
close_Btn.place(x=330,y=200)


root.mainloop()







