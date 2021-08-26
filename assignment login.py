import re
def register():
    db = open("data.txt","r")
    Email = input("Enter the user Email")
    Password = input("Enter the Password:")
    ConfirmPassword = input("Enter the Password again:")

    u = []
    p = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        u.append(a)
        p.append(b)

    data = dict(zip(u,p))
    print(data)
    if re.match(r'\b[A-za-z0-9./_%+-]+@[A-Za-z0-9.-]+\.[A-z|a-z]{2,}\b',Email):
        print("valid email")
    else:
        print("invalid email")
    if Password != ConfirmPassword:
        print("Password don't match Confirm Password")
        register()
    else:
        if len(Password)<=6:
            print("Password is too short,restart:")
        elif len(Password ) >16:
            print("Print strong Password")
        elif Password == (re.compile("^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)+(?=.*[-+_!@#$%^&*.?]).+$")):
            print("Password Satisfied")

        else:
            db = open("data.txt","a")
            db.write(Email+","+Password+"\n")
            print("Success!")
            register()
def access():
    Email = input("Enter the user name")
    Password = input("Enter the Password:")


    if not len(Email or Password)<1:
        db = open("data.txt", "r")
        u = []
        p = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            u.append(a)
            p.append(b)
    data = dict(zip(u,p))
    try:
        if data[Email]:
            try:
                if Password == data[Email]:
                    print("Login Sucess")
                    print("Hi", Email)
                else:
                    print("Email or Password incorrect")
            except:
                print("Incorrect Password of Email")
        else:
            print("Username doesn't exist")
    except:
        print("login error")

def forget():
    Email = input("Enter the user Email")
    Password = input("Enter the Password:")
    ConfirmPassword = input("Enter the Password again:")
    db = open("data.txt", "r")
    u = []
    p = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        u.append(a)
        p.append(b)

    data = dict(zip(u, p))
    print(data)
    if re.match(r'\b[A-za-z0-9./_%+-]+@[A-Za-z0-9.-]+\.[A-z|a-z]{2,}\b', Email):
        print("valid email")
    else:
        print("invalid email")
    if Password != ConfirmPassword:
        print("Password don't match Confirm Password")
        register()
    else:
        if len(Password) <= 6:
            print("Password is too short,restart:")
        elif len(Password) > 16:
            print("Print strong Password")
        elif Password == (re.compile("^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)+(?=.*[-+_!@#$%^&*.?]).+$")):
            print("Password Satisfied")

        else:
            db = open("data.txt", "a")
            db.write(Email + "," + Password + "\n")
            print("Success!")




def home(option):
    option = input("Login|signup:")
    if option == "Login":
        register()
    elif option == "signup":
        access()
    else:
        print("Please enter an option:")
home(option=None)
register()
access()
forget()









