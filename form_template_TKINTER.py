from tkinter import *
root = Tk()
root.geometry("500x300")
#defining the function for submit button
def submitted():
 print("accepted")
#here goes the heading
Label(root, text="Registration form template by bishal", font ="arial 15 bold").grid(row=0, column=3)
#these are the initialization variables
name = Label(root, text="name")
mobile_number = Label(root, text="mobile number")
country = Label(root, text="country")
state = Label(root, text="state")
gender = Label(root, text="gender")
age = Label(root, text="age")
#addressing the initialization variables to the grid 
name.grid(row=1, column=2)
mobile_number.grid(row=2, column=2)
country.grid(row=3, column=2)
state.grid(row=4, column=2)
gender.grid(row=5, column=2)
age.grid(row=6, column=2)
#initializing the variables which will hold the user input for the form
nameval = StringVar
Phonenumberval = StringVar
countryval = StringVar
stateval = StringVar
genderval = StringVar
ageval = StringVar
checkvalue = IntVar
#addressing the entries to the entry variables
name_entry = Entry(root, textvariable=nameval)
mobile_number_entry = Entry(root, textvariable=Phonenumberval)
country_entry = Entry(root, textvariable=countryval)
state_entry = Entry(root, textvariable=stateval)
gender_entry = Entry(root, textvariable=genderval)
age_entry = Entry(root, textvariable=ageval)
#addressing the entries to the grid
name_entry.grid(row=1, column=3)
mobile_number_entry.grid(row=2, column=3)
country_entry.grid(row=3, column=3)
state_entry.grid(row=4, column=3)
gender_entry.grid(row=5, column=3)
age_entry.grid(row=6, column=3)
#checkbox
chkbut = Checkbutton("remember me?", variable = checkvalue)
chkbut.grid(row=6, column =3)
#submit button
Button(text="submbit", command=submitted).grid(row=7, column=3)
root.mainloop()

 
