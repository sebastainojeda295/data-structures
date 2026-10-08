import os
from datetime import date

#functions
def mainMenu():
    print (":::Main menu:::")
    print ("[1]Regsiter aa new user")
    print ("[2]List all users")
    print ("[3]Search user")
    print ("[4]Delete user")
    print ("[5]Update user")
    print ("[6]Show active uses")
    print ("[7]Show inactive users")
    print ("[8]Exit")
ids=[]    
firtsnames=[]
lastnames=[]
mobile_phones=[]
emails=[]
statuses=[]
genders=[]
created_at=[]
#Main
while True:
    os.system('clear')
    mainMenu()
    opt=input("Press any option [1-8]:")

    match opt:
        case '1':
            os.system('clear')
            print("::: Register form :::")
            id=input("ident number: ")
            firtsname=input("Firstname: ")
            lastname=input("Lastname: ")
            mobile_phone=input("Mobile Phone: ")
            email=input("E-mail: ")
            gender=input("Gender [M/F/O]: ")
            ids.append(id)
            firtsnames.append(firtsname)
            lastnames.append(lastname)
            mobile_phones.append(mobile_phone)
            emails.append(email)
            statuses.append(True)
            genders.append(gender)
            created_at.append(date.today())
            print("User has been created successfully !!")
            any_key = input ("press any key to back to main menu")


        case '2':
            print("list all registered users:::")
            print(f"IDs:{ids}")
            print(f"Firsnames:{firtsname}")
            print(f"Lasnames:{lastname}")
            print(f"mobile Phones:{mobile_phone}")
            print(f"emails:{email}")
            print(f"genders:{gender}")
            print(f"created_at:{created_at}")
            any_key = input ("press any key to back to main menu")




        case '8': 
            any_key=input("bye bye. press any key... ")
            break
        case _ :
            any_key=input("Invalid option. press any key to try again")

