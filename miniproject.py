from tkinter import*
root= Tk()
#geomerty
root.geometry("500x300")
def getvals():
    print("Accepted")
#heading
Label(root,text="python registration form",font="arial 15 bold").grid(row=0,column=3)
#field name
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergenct")
paymentmood=Label(root,text="Payment mood")
#packing field
name.grid(row= 1,column=2)
phone.grid(row= 2,column=2)
gender.grid(row=3 ,column=2)
emergency.grid(row=4 ,column=2)
paymentmood.grid(row=5,column=2)
#to store the values 
namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
emergencyvalue=StringVar
paymentmoodvalue=StringVar
checkvalue=IntVar
#entry field
nameentry=Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
emergencyentry=Entry(root, textvariable=emergencyvalue)
paymentmoodentry=Entry(root, textvariable=paymentmoodvalue)
#packing entry field
nameentry.grid(row=1 ,column=3 )
phoneentry.grid(row=2 ,column= 3)
genderentry.grid(row=3 ,column=3 )
emergencyentry.grid(row= 4,column= 3)
paymentmoodentry.grid(row=5 ,column= 3)
#creating check button
checkbtn = Checkbutton(text="remeber me?",variable = checkvalue)
checkbtn.grid(row=6,column=3)
#submitbutton
Button(text="submit",command=getvals).grid(row=7,column=3)


root.mainloop()
