def adminpass():
    import tkinter as tk
    from tkinter import messagebox
    win.destroy()
    global f
    f=tk.Tk()
    f.title("Admin verification")
    canvas=tk.Canvas(f,height=1900,width=1900,bg="white")
    canvas.pack()
    frame=tk.Frame(f,bg="blue")
    frame.place(relheight=0.98,relwidth=0.98,relx=0.01,rely=0.01)
    tk.Label(frame,text="Admin Page",font=("arial black",25),fg="white",bg="blue").place(x=500,y=20)
    tk.Label(frame,text="Password",font=("arial black",20),fg="white",bg="blue").place(x=350,y=150)
    global r3
    r3=tk.Entry(frame,width=20,font=("arial black",20),show="*")
    r3.place(x=650,y=150)
    tk.Button(frame,text="SUBMIT",font=("arial black",20),bg="orange",padx=30,command=passcheck).place(x=500,y=300)
def passcheck():
    from tkinter import messagebox
    p=r3.get()
    if(p=="admin123"):
        adminpage()
    else:
        messagebox.showinfo("Incorrect","Invalid password")
def adminpage():
    import tkinter as tk
    global passwordpage
    global addpage
    global editpage
    global removepage
    if passwordpage==0:
        f.destroy()
        passwordpage=1
    if addpage==1:
        addwin.destroy()
        addpage=0
    elif editpage==1:
        editr2.destroy()
        editpage=0
    elif removepage==1:
        rem1.destroy()
        removepage=0
    global r
    r=tk.Tk()
    r.title("Admin page")
    canvas=tk.Canvas(r,height=1900,width=1900,bg="blue").pack()
    frame=tk.Frame(canvas,bg="blue")
    frame.place(relheight=0.93,relwidth=0.98,relx=0.01,rely=0.01)
    label=tk.Label(frame,text="ADMIN",font=("arial black",25),background="blue",fg="white").pack()
    button1=tk.Button(frame,text="ADD DETAILS",font=("arial black",20),bg="orange",fg="black",padx=50,width=10,command=add_details).place(x=480,y=150)
    button2=tk.Button(frame,text="EDIT DETAILS",font=("arial black",20),bg="orange",fg="black",padx=40,width=11,command=editid).place(x=480,y=250)
    button3=tk.Button(frame,text="REMOVE DETAILS",font=("arial black",20),bg="orange",fg="black",padx=30,width=12,command=remove).place(x=480,y=350)
def add_details():
    import tkinter as tk
    r.destroy()
    global addwin
    addwin=tk.Tk()
    addwin.geometry("1900x1900")
    addwin.title("Add details")
    addwin.configure(bg="blue")
    frame=tk.Frame(addwin,bg="blue").pack()
    l1=tk.Label(frame,text="ADD DETAILS",font=("arial black",30),bg="blue",fg="white").place(x=570,y=10)
    l2=tk.Label(frame,text="Train ID",font=("arial black",20),bg="blue",fg="white").place(x=450,y=80)
    l3=tk.Label(frame,text="Name",font=("arial black",20),bg="blue",fg="white").place(x=450,y=120)
    l4=tk.Label(frame,text="Departure",font=("arial black",20),bg="blue",fg="white").place(x=450,y=160)
    l5=tk.Label(frame,text="Departure date",font=("arial black",20),bg="blue",fg="white").place(x=450,y=200)
    l6=tk.Label(frame,text="Depature time",font=("arial black",20),bg="blue",fg="white").place(x=450,y=240)
    l7=tk.Label(frame,text="Arrival",font=("arial black",20),bg="blue",fg="white").place(x=450,y=280)
    l8=tk.Label(frame,text="Arrival date",font=("arial black",20),bg="blue",fg="white").place(x=450,y=320)
    l9=tk.Label(frame,text="Arrival time",font=("arial black",20),bg="blue",fg="white").place(x=450,y=360)
    l10=tk.Label(frame,text="Seats",font=("arial black",20),bg="blue",fg="white").place(x=450,y=400)
    l11=tk.Label(frame,text="Price",font=("arial black",20),bg="blue",fg="white").place(x=450,y=440)
    global e1
    global e2
    global e3
    global e4
    global e5
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    e1=tk.Entry(frame,width=20,font=("arial",20))
    e1.place(x=750,y=85)
    e2=tk.Entry(frame,width=20,font=("arial",20))
    e2.place(x=750,y=125)
    e3=tk.Entry(frame,width=20,font=("arial",20))
    e3.place(x=750,y=165)
    e4=tk.Entry(frame,width=20,font=("arial",20))
    e4.place(x=750,y=205)
    e5=tk.Entry(frame,width=20,font=("arial",20))
    e5.place(x=750,y=245)
    e6=tk.Entry(frame,width=20,font=("arial",20))
    e6.place(x=750,y=285)
    e7=tk.Entry(frame,width=20,font=("arial",20))
    e7.place(x=750,y=325)
    e8=tk.Entry(frame,width=20,font=("arial",20))
    e8.place(x=750,y=365)
    e9=tk.Entry(frame,width=20,font=("arial",20))
    e9.place(x=750,y=405)
    e10=tk.Entry(frame,width=20,font=("arial",20))
    e10.place(x=750,y=445)
    tk.Button(frame,text="ADD",font=("arial black",20),bg="orange",padx=30,command=addtrain).place(x=600,y=550)
    global addpage
    addpage=1
    tk.Button(frame,text="BACK",font=("arial black",10),bg="orange",padx=20,command=adminpage).place(x=1100,y=640)
def addtrain():
    from tkinter import messagebox
    tid=e1.get()
    na=e2.get()
    dep=e3.get()
    dd=e4.get()
    dt=e5.get()
    ar=e6.get()
    ad=e7.get()
    at=e8.get()
    se=e9.get()
    pr=e10.get()
    try:
        cursor.execute("insert into trains(Id,Name,Departure,DepDate,DepTime,Arrival,ArrDate,ArrTime,Seats,Price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(tid,na,dep,dd,dt,ar,ad,at,se,pr))
        con.commit()
        messagebox.showinfo("Added","Details added successfully")
    except:
        messagebox.showinfo("Invalid","Enter Valid Dates and Time")
def editid():
    import tkinter as tk
    r.destroy()
    global editr1
    editr1=tk.Tk()
    editr1.title("Edit details")
    canvas=tk.Canvas(editr1,height=1900,width=1900,bg="white")
    canvas.pack()
    frame=tk.Frame(editr1,bg="blue")
    frame.place(relheight=0.98,relwidth=0.98,relx=0.01,rely=0.01)
    tk.Label(frame,text="Edit details",font=("arial black",25)).place(x=500,y=30)
    tk.Label(frame,text="Enter Train ID:",font=("arial black",20)).place(x=300,y=150)
    global editrainid
    editrainid=tk.StringVar()
    tk.Entry(frame,textvariable=editrainid,width=20,font=("arial black",20)).place(x=600,y=150)
    tk.Button(frame,text="EDIT",font=("arial black",20),bg="orange",fg="black",command=trainidexist).place(x=550,y=250)
def trainidexist():
    from tkinter import messagebox
    global n
    n=editrainid.get()
    sql="select * from trains where id={}".format(n)
    cursor.execute(sql)
    result=cursor.fetchall()
    if len(result)==0:
        messagebox.showinfo("Absent","Train ID does not exist")
    else:
        editdetails()
def editdetails():
    import tkinter as tk
    editr1.destroy()
    global editr2
    editr2=tk.Tk()
    editr2.title("Edit details")
    canvas=tk.Canvas(editr2,height=1900,width=1900,bg="white")
    canvas.pack()
    frame=tk.Frame(editr2,bg="blue")
    frame.place(relheight=0.98,relwidth=0.98,relx=0.01,rely=0.01)
    tk.Label(frame,text="Edit details",font=("arial black",25),fg="white",bg="blue").place(x=500,y=20)
    tk.Label(frame,text="Train ID",font=("arial black",20),fg="white",bg="blue").place(x=400,y=100)
    tk.Label(frame,text="Name",font=("arial black",20),fg="white",bg="blue").place(x=400,y=150)
    tk.Label(frame,text="Departure",font=("arial black",20),fg="white",bg="blue").place(x=400,y=200)
    tk.Label(frame,text="Departure date",font=("arial black",20),fg="white",bg="blue").place(x=400,y=250)
    tk.Label(frame,text="Departure time",font=("arial black",20),fg="white",bg="blue").place(x=400,y=300)
    tk.Label(frame,text="Arrival",font=("arial black",20),fg="white",bg="blue").place(x=400,y=350)
    tk.Label(frame,text="Arrival date",font=("arial black",20),fg="white",bg="blue").place(x=400,y=400)
    tk.Label(frame,text="Arrival time",font=("arial black",20),fg="white",bg="blue").place(x=400,y=450)
    tk.Label(frame,text="Seats",font=("arial black",20),fg="white",bg="blue").place(x=400,y=500)
    tk.Label(frame,text="Price",font=("arial black",20),fg="white",bg="blue").place(x=400,y=550)
    global trainid
    global trainame
    global departure
    global ddate
    global dtime
    global arrival
    global adate
    global atime
    global seats
    global price
    trainid=tk.StringVar()
    trainame=tk.StringVar()
    departure=tk.StringVar()
    ddate=tk.StringVar()
    dtime=tk.StringVar()
    arrival=tk.StringVar()
    adate=tk.StringVar()
    atime=tk.StringVar()
    seats=tk.StringVar()
    price=tk.StringVar()
    tk.Entry(frame,textvariable=trainid,width=20,font=("arial black",20)).place(x=700,y=100)
    tk.Entry(frame,textvariable=trainame,width=20,font=("arial black",20)).place(x=700,y=150)
    tk.Entry(frame,textvariable=departure,width=20,font=("arial black",20)).place(x=700,y=200)
    tk.Entry(frame,textvariable=ddate,width=20,font=("arial black",20)).place(x=700,y=250)
    tk.Entry(frame,textvariable=dtime,width=20,font=("arial black",20)).place(x=700,y=300)
    tk.Entry(frame,textvariable=arrival,width=20,font=("arial black",20)).place(x=700,y=350)
    tk.Entry(frame,textvariable=adate,width=20,font=("arial black",20)).place(x=700,y=400)
    tk.Entry(frame,textvariable=atime,width=20,font=("arial black",20)).place(x=700,y=450)
    tk.Entry(frame,textvariable=seats,width=20,font=("arial black",20)).place(x=700,y=500)
    tk.Entry(frame,textvariable=price,width=20,font=("arial black",20)).place(x=700,y=550)
    tk.Button(frame,text="EDIT",font=("arial black",20),bg="orange",fg="black",command=editing).place(x=550,y=630)
    sql="select * from trains where id=%s"
    val=(n,)
    cursor.execute(sql,val)
    result=cursor.fetchall()
    trainid.set(result[0][0])
    trainame.set(result[0][1])
    departure.set(result[0][2])
    ddate.set(result[0][3])
    dtime.set(result[0][4])
    arrival.set(result[0][5])
    adate.set(result[0][6])
    atime.set(result[0][7])
    seats.set(result[0][8])
    price.set(result[0][9])
    global editpage
    editpage=1
    tk.Button(frame,text="BACK",font=("arial black",10),bg="orange",padx=20,command=adminpage).place(x=1100,y=640)
def editing():
    from tkinter import messagebox
    a=trainid.get()
    b=trainame.get()
    c=departure.get()
    d=ddate.get()
    e=dtime.get()
    f=arrival.get()
    g=adate.get()
    h=atime.get()
    i=seats.get()
    j=price.get()
    cursor.execute("delete from trains where id=%s",(n,))
    con.commit()
    cursor.execute("insert into trains(Id,Name,Departure,DepDate,DepTime,Arrival,ArrDate,ArrTime,Seats,Price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f,g,h,i,j))
    con.commit()
    messagebox.showinfo("Edited","Details edited successfully")
def remove():
    import tkinter as tk
    r.destroy()
    global rem1
    rem1=tk.Tk()
    rem1.title("Remove details")
    canvas=tk.Canvas(rem1,height=1900,width=1900,bg="white")
    canvas.pack()
    frame=tk.Frame(rem1,bg="blue")
    frame.place(relheight=0.98,relwidth=0.98,relx=0.01,rely=0.01)
    tk.Label(frame,text="Remove details",font=("arial black",25),fg="white",bg="blue").place(x=500,y=20)
    tk.Label(frame,text="Train ID",font=("arial black",20),fg="white",bg="blue").place(x=350,y=150)
    global r1
    r1=tk.Entry(frame,width=20,font=("arial black",20))
    r1.place(x=650,y=150)
    tk.Button(frame,text="REMOVE",font=("arial black",20),bg="orange",padx=30,command=remtrain).place(x=500,y=300)
    global removepage
    removepage=1
    tk.Button(frame,text="BACK",font=("arial black",10),bg="orange",padx=20,command=adminpage).place(x=1100,y=640)
def remtrain():
    from tkinter import messagebox
    id1=r1.get()
    cursor.execute("select * from trains where id=%s",(id1,))
    result=cursor.fetchall()
    if len(result)==0:
        messagebox.showinfo("Absent","Train ID does not exist")
    else:
        cursor.execute("delete from trains where id=%s",(id1,))
        con.commit()
        messagebox.showinfo("Removed","Details removed successfully")
def userpage():
    import tkinter as tk
    win.destroy()
    global r
    r=tk.Tk()
    r.title("User page")
    canvas=tk.Canvas(r,height=1900,width=1900,bg="blue").pack()
    frame=tk.Frame(canvas,bg="blue")
    frame.place(relheight=0.93,relwidth=0.98,relx=0.01,rely=0.01)
    label=tk.Label(frame,text="USER",font=("arial black",25),background="blue",fg="white").pack()
    button1=tk.Button(frame,text="SIGN UP",font=("arial black",20),bg="orange",fg="black",padx=50,width=10,command=signup).place(x=480,y=150)
    button2=tk.Button(frame,text="SIGN IN",font=("arial black",20),bg="orange",fg="black",padx=40,width=11,command=signin).place(x=480,y=250)
def signup():
    global userpage
    userpage=1
    import tkinter as tk
    r.destroy()
    global usgnup
    usgnup=tk.Tk()
    usgnup.title("Sign UP")
    canvas=tk.Canvas(usgnup,height=1900,width=1900,bg="blue").pack()
    frame=tk.Frame(canvas,bg="blue")
    frame.place(relheight=0.93,relwidth=0.98,relx=0.01,rely=0.01)
    l1=tk.Label(frame,text="SIGN UP",font=("arial black",30),bg="blue",fg="white").place(x=500,y=0)
    l2=tk.Label(frame,text="User ID",font=("arial black",20),bg="blue",fg="white").place(x=350,y=120)
    l3=tk.Label(frame,text="Name",font=("arial black",20),bg="blue",fg="white").place(x=350,y=180)
    l4=tk.Label(frame,text="Age",font=("arial black",20),bg="blue",fg="white").place(x=350,y=240)
    l5=tk.Label(frame,text="Phone number",font=("arial black",20),bg="blue",fg="white").place(x=350,y=300)
    l6=tk.Label(frame,text="Email id",font=("arial black",20),bg="blue",fg="white").place(x=350,y=360)
    l7=tk.Label(frame,text="Password",font=("arial black",20),bg="blue",fg="white").place(x=350,y=420)
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    e1=tk.Entry(frame,width=20,font=('Arial black',20))
    e1.place(x=650,y=125)
    e2=tk.Entry(frame,width=20,font=('Arial black',20))
    e2.place(x=650,y=185)
    e3=tk.Entry(frame,width=20,font=('Arial black',20))
    e3.place(x=650,y=245)
    e4=tk.Entry(frame,width=20,font=('Arial black',20))
    e4.place(x=650,y=305)
    e5=tk.Entry(frame,width=20,font=('Arial black',20))
    e5.place(x=650,y=365)
    e6=tk.Entry(frame,width=20,font=('Arial black',20),show="*")
    e6.place(x=650,y=425)
    tk.Button(frame,text="SIGN UP",font=("arial black",20),padx=50,bg="orange",command=adduser).place(x=500,y=500)
def adduser():
    id=e1.get()
    na=e2.get()
    age=e3.get()
    ph=e4.get()
    em=e5.get()
    pa=e6.get()
    cursor.execute("insert into users(Id,Name,Age,Phone,Email,Password) values(%s,%s,%s,%s,%s,%s)",(id,na,age,ph,em,pa))
    con.commit()
    signin()
def signin():
    import tkinter as tk
    if userpage==0:
        r.destroy()
    else:
        usgnup.destroy()
    global r1
    r1=tk.Tk()
    r1.title("Sign IN")
    canvas=tk.Canvas(r1,height=1900,width=1900,bg="blue").pack()
    frame=tk.Frame(canvas,bg="blue")
    frame.place(relheight=0.93,relwidth=0.98,relx=0.01,rely=0.01)
    global userid
    global passwd
    userid=tk.StringVar()
    passwd=tk.StringVar()
    label=tk.Label(frame,text="SIGN IN",font=("arial black",25),background="blue",fg="white").pack()
    tk.Label(frame,text="User ID",font=("arial black",20),fg="white",bg="blue").place(x=400,y=100)
    tk.Entry(frame,textvariable=userid,width=20,font=("arial black",20)).place(x=600,y=100)
    tk.Label(frame,text="Password",font=("arial black",20),fg="white",bg="blue").place(x=400,y=200)
    tk.Entry(frame,textvariable=passwd,width=20,font=("arial black",20),show="*").place(x=600,y=200)
    tk.Button(frame,text="SIGN IN",font=("arial black",20),padx=50,bg="orange",command=checksignin).place(x=500,y=300)
def checksignin():
    from tkinter import messagebox
    n=userid.get()
    p=passwd.get()
    cursor.execute("select * from users where Id=%s",(n,))
    result=cursor.fetchall()
    if len(result)==0:
        messagebox.showinfo("Incorrect","Invalid User ID")
    else:
        x=result[0][5]
        if x!=p:
            messagebox.showinfo("Incorrect","Incorrect Password")
        else:
            global USERID
            USERID=n
            global name
            name=result[0][1]
            mainpage()
def mainpage():
    import tkinter as tk
    from tkcalendar import DateEntry
    global signinpage
    global reportpage
    global cancelpage
    if signinpage==0:
        r1.destroy()
        signinpage=1
    if reportpage==1:
        rep.destroy()
        reportpage=0
    elif cancelpage==1:
        cancel.destroy()
        cancelpage=0
    global main
    main=tk.Tk()
    main.title("Railways Reservation")
    canvas=tk.Canvas(main,height=1900,width=1900,bg="blue").pack()
    frame=tk.Frame(canvas,bg="white")
    frame.place(relheight=0.97,relwidth=0.98,relx=0.01,rely=0.015)
    tk.Label(frame,text="Welcome",font=("arial black",15),bg="white").place(x=10,y=10)
    tk.Label(frame,text=name,font=("arial black",15),bg="white").place(x=115,y=10)
    tk.Button(frame,text="Cancel Bookings",font=("arial black",10),bg="orange",command=cancel).place(x=1100,y=20)
    global dept
    global arr
    dept=tk.StringVar()
    arr=tk.StringVar()
    tk.Label(frame,text="Departure:",font=("arial black",15),bg="white").place(x=30,y=80)
    tk.Entry(frame,textvariable=dept,width=15,bd=3,font=("arial black",15)).place(x=160,y=80)
    tk.Label(frame,text="Arrival:",font=("arial black",15),bg="white").place(x=400,y=80)
    tk.Entry(frame,textvariable=arr,width=15,bd=3,font=("arial black",15)).place(x=500,y=80)
    tk.Label(frame,text="Date:",font=("arial black",15),bg="white").place(x=750,y=80)
    global date
    date=tk.StringVar()
    cal=DateEntry(frame,textvariable=date,background= "orange",foreground= "black",date_pattern="yyyy/mm/dd").place(x=830,y=80)
    tk.Button(frame,text="Search",font=("arial black",10),bg="orange",command=search).place(x=1000,y=80)
def search():
    import tkinter as tk
    from tkinter import ttk
    a=dept.get()
    b=arr.get()
    global c
    c=date.get()
    cursor.execute("select * from trains where Departure=%s and Arrival=%s and DepDate=%s and ((DepDate>curdate()) or (DepDate=curdate() and DepTime>current_time()))",(a,b,c))
    global result
    result=cursor.fetchall()
    if len(result)!=0:
        global table
        table=ttk.Treeview(main)
        table["columns"]=("ID","Name","Departure time","Arrival date","Arrival time","Price")
        table.column("#0",width=0,minwidth=0)
        table.column("#1",anchor=CENTER)
        table.heading("#1",text="ID")
        table.column("#2",anchor=CENTER)
        table.heading("#2",text="Name")
        table.column("#3",anchor=CENTER)
        table.heading("#3",text="Departure time")
        table.column("#4",anchor=CENTER)
        table.heading("#4",text="Arrival date")
        table.column("#5",anchor=CENTER)
        table.heading("#5",text="Arrival time")
        table.column("#6",anchor=CENTER)
        table.heading("#6",text="Price")
        table.place(x=40,y=150)
        table.tag_configure("red",background="red")
        table.tag_configure("yellow",background="yellow")
        table.tag_configure("green",background="light green")
        for i in result:
            trid=i[0]
            trnam=i[1]
            dtime=i[4]
            adate=i[6]
            atime=i[7]
            seats=i[8]
            price=i[9]
            if seats==0:
                table.insert("","end",text="",values=(trid,trnam,dtime,adate,atime,price),tags="red")
            elif seats<=5:
                table.insert("","end",text="",values=(trid,trnam,dtime,adate,atime,price),tags="yellow")
            else:
                table.insert("","end",text="",values=(trid,trnam,dtime,adate,atime,price),tags="green")
        tk.Label(frame,text="Number of seats:",font=("arial black",15),bg="white").place(x=30,y=500)
        global seat
        seat=tk.Entry(frame,bd=3,width=15,font=("arial black",15))
        seat.place(x=250,y=500)
        tk.Button(frame,text="BOOK",font=("arial black",10),bg="orange",width=7,command=seatexist).place(x=1100,y=500) 
    else:
        tk.Label(main,text="There are no trains available",font=("arial black",20),bg="white").place(x=400,y=300)
def seatexist():
    import tkinter as tk
    from tkinter import messagebox
    trrid=table.selection()[0]
    trrid=trrid[1:]
    trrid=int(trrid)
    global d
    d=seat.get()
    d=int(d)
    cursor.execute("select seats from trains where id='%s' and DepDate=%s",(result[trrid-1][0],c))
    result1=cursor.fetchall()
    x=result1[0][0]
    if d==0:
        messagebox.showinfo("Invalid","Enter valid number of seats")
    else:
        if(d>x):
            messagebox.showinfo("Unavailability","Seats not available")
        else:
            cursor.execute("update trains set seats=seats-'%s' where id='%s' and DepDate=%s",(d,result[trrid-1][0],c))
            con.commit()
            messagebox.showinfo("Booked","Successfully booked!!")
            cursor.execute("select * from bookings where userid=%s and trainid=%s and date=%s",(USERID,result[trrid-1][0],c))
            b=cursor.fetchall()
            if len(b)==0:
                cursor.execute("insert into bookings(userid,trainid,date,seats) values(%s,%s,%s,%s)",(USERID,result[trrid-1][0],c,d))
                con.commit()
            else:
                cursor.execute("update bookings set seats=seats+%s where userid=%s and trainid=%s and date=%s",(d,USERID,result[trrid-1][0],c))
                con.commit()
            cursor.execute("select * from trains where id=%s and depdate=%s",(result[trrid-1][0],c))
            global RES
            RES=cursor.fetchall()
            report()
def report():
    import tkinter as tk
    main.destroy()
    global rep
    rep=tk.Tk()
    rep.title("Booking confirmed")
    canvas=tk.Canvas(rep,height=1900,width=1900,bg="blue").pack()
    frame=tk.Frame(canvas,bg="white")
    frame.place(relheight=0.97,relwidth=0.98,relx=0.01,rely=0.015)
    tk.Label(frame,text="REPORT",font=("arial black",25),fg="black",bg="orange").place(x=550,y=20)
    tk.Label(frame,text="Train ID:",font=("arial black",20),fg="black",bg="white").place(x=400,y=100)
    tk.Label(frame,text=RES[0][0],font=("arial black",20),fg="black",bg="white").place(x=700,y=100)
    tk.Label(frame,text="Name:",font=("arial black",20),fg="black",bg="white").place(x=400,y=150)
    tk.Label(frame,text=RES[0][1],font=("arial black",20),fg="black",bg="white").place(x=700,y=150)
    tk.Label(frame,text="Departure:",font=("arial black",20),fg="black",bg="white").place(x=400,y=200)
    tk.Label(frame,text=RES[0][2],font=("arial black",20),fg="black",bg="white").place(x=700,y=200)
    tk.Label(frame,text="Departure date:",font=("arial black",20),fg="black",bg="white").place(x=400,y=250)
    tk.Label(frame,text=RES[0][3],font=("arial black",20),fg="black",bg="white").place(x=700,y=250)
    tk.Label(frame,text="Departure time:",font=("arial black",20),fg="black",bg="white").place(x=400,y=300)
    tk.Label(frame,text=RES[0][4],font=("arial black",20),fg="black",bg="white").place(x=700,y=300)
    tk.Label(frame,text="Arrival:",font=("arial black",20),fg="black",bg="white").place(x=400,y=350)
    tk.Label(frame,text=RES[0][5],font=("arial black",20),fg="black",bg="white").place(x=700,y=350)
    tk.Label(frame,text="Arrival date:",font=("arial black",20),fg="black",bg="white").place(x=400,y=400)
    tk.Label(frame,text=RES[0][6],font=("arial black",20),fg="black",bg="white").place(x=700,y=400)
    tk.Label(frame,text="Arrival time:",font=("arial black",20),fg="black",bg="white").place(x=400,y=450)
    tk.Label(frame,text=RES[0][7],font=("arial black",20),fg="black",bg="white").place(x=700,y=450)
    tk.Label(frame,text="Seats:",font=("arial black",20),fg="black",bg="white").place(x=400,y=500)
    tk.Label(frame,text=d,font=("arial black",20),fg="black",bg="white").place(x=700,y=500)
    tk.Label(frame,text="Price:",font=("arial black",20),fg="black",bg="white").place(x=400,y=550)
    tk.Label(frame,text=RES[0][9]*d,font=("arial black",20),fg="black",bg="white").place(x=700,y=550)
    tk.Label(frame,text="Thank you for booking, have a great journey!!",font=("arial black",20),fg="black",bg="white").place(x=300,y=600)
    global reportpage
    reportpage=1
    tk.Button(frame,text="BACK",font=("arial black",10),bg="orange",padx=20,command=mainpage).place(x=1100,y=640)
def cancel():
    import tkinter as tk
    from tkinter import ttk
    global cancel
    main.destroy()
    cancel=tk.Tk()
    cancel.title("Railways Reservation")
    canvas=tk.Canvas(cancel,height=1900,width=1900,bg="blue").pack()
    frame=tk.Frame(canvas,bg="white")
    frame.place(relheight=0.97,relwidth=0.98,relx=0.01,rely=0.015)
    cursor.execute("select trainid,date,seats from bookings where userid='%s' and date>curdate()",(int(USERID),))
    global bresult
    bresult=cursor.fetchall()
    if(len(bresult)==0):
        tk.Label(frame,text="YOU HAVE NO PENDING JOURNEYS",font=("arial back",30),bg="white").place(x=300,y=200)
    else:
        global ctable
        ctable=ttk.Treeview(cancel)
        ctable["columns"]=("Name","Departure","Arrival","Departure Date","Time","Seats booked")
        ctable.column("#0",width=0,minwidth=0)
        ctable.column("#1",anchor=CENTER)
        ctable.heading("#1",text="Name")
        ctable.column("#2",anchor=CENTER)
        ctable.heading("#2",text="Departure")
        ctable.column("#3",anchor=CENTER)
        ctable.heading("#3",text="Arrival")
        ctable.column("#4",anchor=CENTER)
        ctable.heading("#4",text="Departure date")
        ctable.column("#5",anchor=CENTER)
        ctable.heading("#5",text="Time")
        ctable.column("#6",anchor=CENTER)
        ctable.heading("#6",text="Seats booked")
        ctable.place(x=40,y=50)
        for i in bresult:
            trid=i[0]
            date=i[1]
            seats=i[2]
            cursor.execute("select * from trains where Id=%s and DepDate=%s",(trid,date))
            res=cursor.fetchall()
            trnam=res[0][1]
            dname=res[0][2]
            dtime=res[0][4]
            aname=res[0][5]
            ctable.insert("","end",text="",values=(trnam,dname,aname,date,dtime,seats))
        tk.Label(cancel,text="Enter number of seats TO CANCEL",font=("arial black",15)).place(x=100,y=600)
        global cs
        cs=tk.StringVar()
        tk.Entry(cancel,textvariable=cs,width=20,font=("arial black",15)).place(x=500,y=600)
        tk.Button(cancel,text="CANCEL",font=("arial black",15),bg="orange",command=cancelling).place(x=800,y=600)
        global cancelpage
        cancelpage=1
        tk.Button(frame,text="BACK",font=("arial black",10),bg="orange",padx=20,command=mainpage).place(x=1100,y=640)
def cancelling():
    from tkinter import messagebox
    item=ctable.selection()[0]
    x=item[1:]
    x=int(x)
    trid=bresult[x-1][0]
    date=bresult[x-1][1]
    seat=cs.get()
    seat=int(seat)
    cursor.execute("select * from bookings where userid=%s and trainid=%s and date=%s",(USERID,trid,date))
    r=cursor.fetchall()
    if(seat>r[0][3] or seat==0):
        messagebox.showinfo("Invalid","Enter valid number of seats")
    else:
        cursor.execute("update bookings set seats=seats-%s where userid=%s and trainid=%s and date=%s",(seat,USERID,trid,date))
        con.commit()
        cursor.execute("update trains set seats=seats+%s where Id=%s and DepDate=%s",(seat,trid,date))
        con.commit()
        messagebox.showinfo("Cancelled","Tickets are cancelled successfully")
        cursor.execute("select * from bookings where userid=%s and trainid=%s and date=%s",(USERID,trid,date))
        r=cursor.fetchall()
        s=r[0][3]
        if s==0:
            ctable.delete(item)
        else:
            ctable.set(item,column="#6",value=r[0][3])
        cursor.execute("delete from bookings where seats=%s",(0,))
        con.commit()
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as sq
con=sq.connect(host="localhost",user="root",passwd="",database="railways")
cursor=con.cursor()
'''cursor.execute('CREATE Table trains(Id integer primary key,Name varchar(25),Departure varchar(25),DepDate date,DepTime time,Arrival varchar(25),ArrDate date,ArrTime time,Seats integer,Price integer)')
cursor.execute("create table users(Id integer primary key,Name varchar(25),Age integer,Phone varchar(10),Email varchar(50),Password varchar(12))")
cursor.execute("create table bookings(userid integer,trainid integer,date date,seats integer)")'''
cursor.execute("CREATE OR REPLACE TRIGGER checkdates BEFORE INSERT ON trains FOR EACH ROW BEGIN if (NEW.DepDate>NEW.ArrDate or (NEW.DepDate=NEW.ArrDate and NEW.DepTime>=NEW.ArrTime)) THEN SIGNAL SQLSTATE '12000' SET MESSAGE_TEXT = 'Invalid Dates or Time'; end if; end")
win = Tk()
win.title("Railways Reservation")
frame=Frame(win,bg="white").pack()
img=(Image.open("train.jpg")).resize((1300,900))
img=ImageTk.PhotoImage(img)
label=Label(frame,image=img).pack()
label=Label(frame,text="RAILEY",font=("arial black",30),bg="light blue").place(x=550,y=10)
b1=Button(frame,text="ADMIN",font=("arial black",20),bg="orange",fg="black",padx=15,command=adminpass).place(x=100,y=80)
b2=Button(frame,text="USER",font=("arial black",20),bg="orange",fg="black",padx=25,command=userpage).place(x=100,y=180)
userpage=0
passwordpage=addpage=editpage=removepage=0
signinpage=0
reportpage=cancelpage=0
