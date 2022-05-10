from email.headerregistry import Address
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import json
window=tk.Tk()
data={"DATE":"","Receipt":"","company":"","Representative":"","Location":"","cCity":"","cPhone":"","Name":"","License":"","Address":"","lCity":"","lPhone":"","VIN":"","Make":"","Year":"","Color":"","Registration":"","Model":"","Mileage":"","Cost":"","days":"","Additional":"0","Payment":"","TotalAmount":""}


DATE=tk.StringVar()
Receipt=tk.StringVar()
company=tk.StringVar()
Representative=tk.StringVar()
Location=tk.StringVar()
cCity=tk.StringVar()
cPhone=tk.StringVar()
Name=tk.StringVar()
License=tk.StringVar()
Adds=tk.StringVar()
lCity=tk.StringVar()
lPhone=tk.StringVar()
VIN=tk.StringVar()
Make=tk.StringVar()
Year=tk.StringVar()
Color=tk.StringVar()
Registration=tk.StringVar()
Model=tk.StringVar()
Mileage=tk.StringVar()
Cost=tk.StringVar()
days=tk.StringVar()
Additional=tk.StringVar()
Payment=tk.StringVar()
TotalAmount=tk.StringVar()

def datainsert():
    file=open("data.txt","a+")
    v25.delete(0, tk.END)
    data["DATE"]=DATE.get()
    data["Receipt"]=Receipt.get()
    data["company"]=company.get()
    data["Representative"]=Representative.get()
    data["Location"]=Location.get()
    data["cCity"]=cCity.get()
    data["cPhone"]=cPhone.get()
    data["Name"]=Name.get()
    data["License"]=License.get()
    data["Address"]=Adds.get()
    data["lCity"]=lCity.get()
    data["lPhone"]=lPhone.get()
    data["VIN"]=VIN.get()
    data["Make"]=Make.get()
    data["Year"]=Year.get()
    data["Color"]=Color.get()
    data["Registration"]=Registration.get()
    data["Model"]=Model.get()
    data["Mileage"]=Mileage.get()
    data["Cost"]=Cost.get()
    data["days"]=days.get()
    data["Additional"]=Additional.get()
    data["Payment"]=Payment.get()
    data["TotalAmount"]=int(data["Cost"])*int(data["days"])+int(data["Additional"])
    v25.insert(0, str(data["TotalAmount"]))
    print(data)
    json.dump(data,file,indent=6)
    file.close()


window.title("Car Rentel Receipt")
Tops = Frame(window, bg='#e6e5e5', pady=2, width=5000, height=1000, relief="ridge")
Tops.grid(row=0, column=0)
window.configure(background='#e6e5e5')
window.geometry("1440x920")
headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text="CAR RENTEL RECEIPT:",bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=5, sticky=W)
Label_1 = Label(window, font=('lato black', 15, 'bold'), text="DATE:", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=2, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Receipt : ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=3, sticky=W)
label1 = tk.Label(window, font=('lato black', 20, 'bold'), text="RENTEL COMPANY INFO :  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="company:", bg="#e6e5e5", fg="black")
label1.grid(row=5, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Representative:", bg="#e6e5e5", fg="black")
label1.grid(row=6, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Location:", bg="#e6e5e5", fg="black")
label1.grid(row=7, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="City/State/ZIP:", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Phone:", bg="#e6e5e5", fg="black")
label1.grid(row=9, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="LESSEE INFO", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=3, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Name:", bg="#e6e5e5", fg="black")
label1.grid(row=5, column=3, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="License:", bg="#e6e5e5", fg="black")
label1.grid(row=6, column=3, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Address:", bg="#e6e5e5", fg="black")
label1.grid(row=7, column=3, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="City/State/ZIP:", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=3, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Phone:", bg="#e6e5e5", fg="black")
label1.grid(row=9, column=3, sticky=W)
Label_1 = Label(window, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=3, column=0, sticky=W)
Label_1 = Label(window, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=10, column=0, sticky=W)

label1 = tk.Label(window, font=('lato black', 22, 'bold'), text="VEHICLE INFORMATION:", bg="#e6e5e5", fg="black")
label1.grid(row=11, column=2, sticky=W)

label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="VIN:", bg="#e6e5e5", fg="black")
label1.grid(row=12, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Make:", bg="#e6e5e5", fg="black")
label1.grid(row=13, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Year:", bg="#e6e5e5", fg="black")
label1.grid(row=14, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Color:", bg="#e6e5e5", fg="black")
label1.grid(row=15, column=0, sticky=W)

label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Registration:", bg="#e6e5e5", fg="black")
label1.grid(row=12, column=3, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Model:", bg="#e6e5e5", fg="black")
label1.grid(row=13, column=3, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Mileage:", bg="#e6e5e5", fg="black")
label1.grid(row=14, column=3, sticky=W)

Label_1 = Label(window, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=15, column=0, sticky=W)

label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Cost Per Day:", bg="#e6e5e5", fg="black")
label1.grid(row=16, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Number of days:", bg="#e6e5e5", fg="black")
label1.grid(row=17, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Additional Costs:", bg="#e6e5e5", fg="black")
label1.grid(row=18, column=0, sticky=W)


label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Payment Method:", bg="#e6e5e5", fg="black")
label1.grid(row=19, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="cash:", bg="#e6e5e5", fg="black")
label1.grid(row=20, column=0, sticky=W)
label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="cheque:", bg="#e6e5e5", fg="black")
label1.grid(row=21, column=0, sticky=W)

Label_1 = Label(window, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=22, column=0, sticky=W)

label1 = tk.Label(window, font=('lato black', 15, 'bold'), text="Total Amount:", bg="#e6e5e5", fg="black")
label1.grid(row=23, column=0, sticky=W)

Label_1 = Label(window, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=24, column=0, sticky=W)

v1= tk.Entry(window,textvariable=DATE)
v1.grid(row=2, column=0, ipadx=31, sticky=E)
v2= tk.Entry(window,textvariable=Receipt)
v2.grid(row=2, column=4, ipadx=31, sticky=E)
v3= tk.Entry(window,textvariable=company)
v3.grid(row=5, column=1, ipadx=31, sticky=E)
v4= tk.Entry(window,textvariable=Representative)
v4.grid(row=6, column=1, ipadx=31, sticky=E)
v5= tk.Entry(window,textvariable=Location)
v5.grid(row=7, column=1, ipadx=31, sticky=E)
v6= tk.Entry(window,textvariable=cCity)
v6.grid(row=8, column=1, ipadx=31, sticky=E)
v7= tk.Entry(window,textvariable=cPhone)
v7.grid(row=9, column=1, ipadx=31, sticky=E)
v8= tk.Entry(window,textvariable=Name)
v8.grid(row=5, column=4, ipadx=31, sticky=E)
v9= tk.Entry(window,textvariable=License)
v9.grid(row=6, column=4, ipadx=31, sticky=E)
v10= tk.Entry(window,textvariable=Adds)
v10.grid(row=7, column=4, ipadx=31, sticky=E)
v11= tk.Entry(window,textvariable=lCity)
v11.grid(row=8, column=4, ipadx=31, sticky=E)
v12= tk.Entry(window,textvariable=lPhone)
v12.grid(row=9, column=4, ipadx=31, sticky=E)
v13= tk.Entry(window,textvariable=VIN)
v13.grid(row=12, column=1, ipadx=31, sticky=E)
v14= tk.Entry(window,textvariable=Make)
v14.grid(row=13, column=1, ipadx=31, sticky=E)
v15= tk.Entry(window,textvariable=Year)
v15.grid(row=14, column=1, ipadx=31, sticky=E)
v16= tk.Entry(window,textvariable=Color)
v16.grid(row=15, column=1, ipadx=31, sticky=E)
v17= tk.Entry(window,textvariable=Registration)
v17.grid(row=12, column=4, ipadx=31, sticky=E)
v18= tk.Entry(window,textvariable=Model)
v18.grid(row=13, column=4, ipadx=31, sticky=E)
v19= tk.Entry(window,textvariable=Mileage)
v19.grid(row=14, column=4, ipadx=31, sticky=E)
v20= tk.Entry(window,textvariable=Cost)
v20.grid(row=16, column=0, ipadx=31, sticky=E)
v21= tk.Entry(window,textvariable=days)
v21.grid(row=17, column=0, ipadx=31, sticky=E)
v22= tk.Entry(window,textvariable=Additional)
v22.grid(row=18, column=0, ipadx=31, sticky=E)
v23= tk.Radiobutton(window,variable=Payment,value="cash")
v23.grid(row=20, column=0,sticky=E)
v24= tk.Radiobutton(window,variable=Payment,value="chaque")
v24.grid(row=21, column=0,sticky=E)
v25= tk.Entry(window,textvariable=TotalAmount)
v25.grid(row=23, column=0, ipadx=31, sticky=E)


Label_9 = Button(window, font=('arial', 15, 'bold'), text="SUBMIT", padx=2, pady=2, bg="light blue", fg="white",
                 command=datainsert)
Label_9.grid(row=25, column=0)

window.mainloop()