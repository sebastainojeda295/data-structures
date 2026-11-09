import os
from datetime import date

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

ages=[]
salarys=[]

created_at=[]

while True:
    os.system('clear')
    mainMenu()
    opt=input("Press any option [1-8]: ")


    match opt:
        case '1':
            os.system('clear')
            print("::: Register form :::")

            while True:
                id=input("ident number: ")
                if not id.isdigit():
                    print("Invalid input! Identification must contain numbers only. \n try again:::")
                    continue

                count = 0
                i=0
                while i< len(ids):
                    if id == ids[i]:
                        print("identification number already exists! \n try again:::")
                        count += 1
                        break
                    i+=1
                if count == 0:
                    break

            firtsname=input("Firstname: ")
            lastname=input("Lastname: ")

            while True:
                mobile_phone=input("Mobile Phone: ")
                if not mobile_phone.isdigit():
                    print("Invalid input! Mobile phone must contain numbers only. \n try again:::")
                    continue

                count = 0
                i=0
                while i< len(mobile_phones):
                    if mobile_phone == mobile_phones[i]:
                        print("Number Phone already exists! \n try again:::")
                        count += 1
                        break
                    i+=1
                if count == 0:
                    break

            while True:
                email=input("E-mail: ")
                if '@' not in email:
                    print("Invalid email! Email must contain '@'. \n try again:::")
                    continue

                count = 0
                i=0
                while i< len(emails):
                    if email == emails[i]:
                        print("Email already exists! \n try again:::")
                        count += 1
                        break
                    i+=1
                if count == 0:
                    break

            while True:
                gender=input("Gender [M/F/O]: ").upper()
                if gender in ['M', 'F', 'O']:
                    break
                print("Invalid gender! Please enter M, F, or O.")

            while True:
                age_input = input("age: ")
                if age_input.isdigit():
                    age = int(age_input)
                    break
                print("Invalid input! Please enter a valid number for age.")

            while True:
                salary_input = input("salary: ")
                if salary_input.isdigit():
                    salary = int(salary_input)
                    break
                print("Invalid input! Please enter a valid numeric salary.")

            ids.append(id)
            firtsnames.append(firtsname)
            lastnames.append(lastname)
            mobile_phones.append(mobile_phone)
            emails.append(email)
            statuses.append(True)
            genders.append(gender)
            ages.append(age)
            salarys.append(salary)
            created_at.append(date.today())

            print("User has been created successfully !!")
            any_key = input ("Press any key to back to main menu")



        case '2':
            while True:
                os.system('clear')
                print("::: List All Users Submenu :::")
                print("[1] Sort in ascending order by identification")
                print("[2] Sort in descending order by identification")
                print("[3] Sort in ascending order by lastname")
                print("[4] Sort in descending order by lastname")
                print("[5] Exit to main menu")
                
                sort_opt = input("Select an option [1-5]: ")
                
                if sort_opt == '5':
                    break
                
                if sort_opt in ['1', '2', '3', '4']:
                    indices = []
                    i = 0
                    while i < len(ids):
                        indices.append(i)
                        i += 1
                    
                    if sort_opt == '1':
                        indices.sort(key=lambda i: ids[i])
                    elif sort_opt == '2':
                        indices.sort(key=lambda i: ids[i], reverse=True)
                    elif sort_opt == '3':
                        indices.sort(key=lambda i: lastnames[i].lower())
                    elif sort_opt == '4':
                        indices.sort(key=lambda i: lastnames[i].lower(), reverse=True)

                    os.system('clear')
                    print(":::List all registered users:::")
                    print ('-'*181)
                    print (f"| {'id':<15} | {'Firsname':<15} | {'Lastname':<15} | {'Mobile Phone':<15} | {'Email':<15} | {'Gender':<15} | {'Age':<15} | {'Salary':<15} | {'Status':<15} | {'Created_at':<15} |")
                    print ('-'*181)

                    for i in indices:
                        status_str = "Active" if statuses[i] else "Inactive"
                        print(f'| {ids[i]:<15} | {firtsnames[i]:<15} | {lastnames[i]:<15} | {mobile_phones[i]:<15} | {emails[i]:<15} | {genders[i]:<15} | {str(ages[i]):<15} | {str(salarys[i]):<15} | {status_str:<15} | {str(created_at[i]):<15} |')
                        print ('-'*181)
                    
                    any_key = input("Press any key to continue...")
                else:
                    any_key = input("Invalid option. Press any key to try again...")



        case '3':
            os.system('clear')
            print("::: Search User :::")
            id_user = input("Enter identification number to search: ")
            
            found = False
            i = 0
            while i < len(ids):
                if id_user == ids[i]:
                    found = True
                    break
                i += 1
            
            if found:
                os.system('clear')
                print("::: User found :::")
                print ('-'*181)
                print (f"| {'id':<15} | {'Firsname':<15} | {'Lastname':<15} | {'Mobile Phone':<15} | {'Email':<15} | {'Gender':<15} | {'Age':<15} | {'Salary':<15} | {'Status':<15} | {'Created_at':<15} |")
                print ('-'*181)
                
                status_str = "Active" if statuses[i] else "Inactive"
                print(f'| {ids[i]:<15} | {firtsnames[i]:<15} | {lastnames[i]:<15} | {mobile_phones[i]:<15} | {emails[i]:<15} | {genders[i]:<15} | {str(ages[i]):<15} | {str(salarys[i]):<15} | {status_str:<15} | {str(created_at[i]):<15} |')
                print ('-'*181)
            else:
                print("identification number not found.")
            
            any_key = input("\nPress any key to back to main menu")




        case '4':
            os.system('clear')
            print("::: Delete User :::")
            del_id = input("Enter identification number of the user to delete: ")
            
            found = False
            i = 0
            while i < len(ids):
                if ids[i] == del_id:
                    ids.pop(i)
                    firtsnames.pop(i)
                    lastnames.pop(i)
                    mobile_phones.pop(i)
                    emails.pop(i)
                    statuses.pop(i)
                    genders.pop(i)
                    ages.pop(i)
                    salarys.pop(i)
                    created_at.pop(i)
                    
                    print("User deleted successfully!")
                    found = True
                    break
                i += 1
                
            if not found:
                print("User not found.")
                
            any_key = input("Press any key to back to main menu")




        case '5':
            os.system('clear')
            print("::: Update User :::")
            id_user = input("Enter identification number to update: ")
            
            i = 0
            found = False
            while i < len(ids):
                if id_user == ids[i]:
                    found = True
                    break
                i += 1

            
            if found:
                while True:
                    os.system('clear')
                    print(f"::: Update menu option for user {ids[i]} :::")
                    print("[1] Update firstname")
                    print("[2] Update lastname")
                    print("[3] Update mobile phone")
                    print("[4] Update email")
                    print("[5] Update status")
                    print("[6] Update age")
                    print("[7] Update salary")
                    print("[8] Update all fields")
                    print("[9] Exit")
                    
                    update_opt = input("Select an option [1-9]: ")
                    
                    if update_opt == '9':
                        break
                    
                    if update_opt in ['1', '8']:
                        new_val = input(f"new firstname (current firstname: {firtsnames[i]}): ")
                        if new_val.strip():
                            firtsnames[i] = new_val
                    
                    if update_opt in ['2', '8']:
                        new_val = input(f"new lastname (current lastname: {lastnames[i]}): ")
                        if new_val.strip():
                            lastnames[i] = new_val
                    
                    if update_opt in ['3', '8']:
                        while True:
                            new_val = input(f"new mobile phone (current mobile phone: {mobile_phones[i]}): ")
                            if not new_val.strip():
                                break
                            if not new_val.isdigit():
                                print("Invalid input! Mobile phone must contain numbers only.")
                                continue
                            
                            exists = False
                            k = 0
                            while k < len(mobile_phones):
                                if k != i and new_val == mobile_phones[k]:
                                    print("Number Phone already exists! \n try again:::")
                                    exists = True
                                    break
                                k += 1
                            if not exists:
                                mobile_phones[i] = new_val
                                break
                    
                    if update_opt in ['4', '8']:
                        while True:
                            new_val = input(f"new email (current email: {emails[i]}): ")
                            if not new_val.strip():
                                break
                            if '@' not in new_val:
                                print("Invalid email! Email must contain '@'. \n try again:::")
                                continue

                            exists = False
                            k = 0
                            while k < len(emails):
                                if k != i and new_val == emails[k]:
                                    print("Email already exists! \n try again:::")
                                    exists = True
                                    break
                                k += 1
                            if not exists:
                                emails[i] = new_val
                                break
                    
                    if update_opt in ['5', '8']:
                        current_status_str = "Active" if statuses[i] else "Inactive"
                        new_val = input(f"new status [True/False] (current status: {current_status_str}): ")
                        if new_val.strip():
                            if new_val.lower() in ['true', 'active', '1', 't']:
                                statuses[i] = True
                            elif new_val.lower() in ['false', 'inactive', '0', 'f']:
                                statuses[i] = False
                    
                    if update_opt in ['6', '8']:
                        new_val = input(f"new age (current age: {ages[i]}): ")
                        if new_val.strip():
                            if new_val.isdigit():
                                ages[i] = int(new_val)
                            else:
                                print("Invalid age! Must be numeric.")
                    
                    if update_opt in ['7', '8']:
                        new_val = input(f"new salary (current salary: {salarys[i]}): ")
                        if new_val.strip():
                            if new_val.isdigit():
                                salarys[i] = int(new_val)
                            else:
                                print("Invalid salary! Must be numeric.")
                    
                    if update_opt in ['1', '2', '3', '4', '5', '6', '7', '8']:
                        print("User updated successfully!")
                        any_key = input("Press any key to continue...")
                    else:
                        if update_opt != '9':
                            any_key = input("Invalid option. Press any key to try again...")
            else:
                print("User doesn't exist / identification number not found.")
                any_key = input("\nPress any key to back to main menu")




        case '6':
            os.system('clear')
            print("::: Active Users :::")
            print ('-'*181)
            print (f"| {'id':<15} | {'Firsname':<15} | {'Lastname':<15} | {'Mobile Phone':<15} | {'Email':<15} | {'Gender':<15} | {'Age':<15} | {'Salary':<15} | {'Status':<15} | {'Created_at':<15} |")
            print ('-'*181)

            i = 0
            active_count = 0
            while i < len(ids):
                if statuses[i] == True:
                    print(f'| {ids[i]:<15} | {firtsnames[i]:<15} | {lastnames[i]:<15} | {mobile_phones[i]:<15} | {emails[i]:<15} | {genders[i]:<15} | {str(ages[i]):<15} | {str(salarys[i]):<15} | {"Active":<15} | {str(created_at[i]):<15} |')
                    print ('-'*181)
                    active_count += 1
                i += 1
            
            if active_count == 0:
                print("No active users found.")

            any_key = input("Press any key to back to main menu")




        case '7':
            os.system('clear')
            print("::: Inactive Users :::")
            print ('-'*181)
            print (f"| {'id':<15} | {'Firsname':<15} | {'Lastname':<15} | {'Mobile Phone':<15} | {'Email':<15} | {'Gender':<15} | {'Age':<15} | {'Salary':<15} | {'Status':<15} | {'Created_at':<15} |")
            print ('-'*181)

            i = 0
            inactive_count = 0
            while i < len(ids):
                if statuses[i] == False:
                    print(f'| {ids[i]:<15} | {firtsnames[i]:<15} | {lastnames[i]:<15} | {mobile_phones[i]:<15} | {emails[i]:<15} | {genders[i]:<15} | {str(ages[i]):<15} | {str(salarys[i]):<15} | {"Inactive":<15} | {str(created_at[i]):<15} |')
                    print ('-'*181)
                    inactive_count += 1
                i += 1
            
            if inactive_count == 0:
                print("No inactive users found.")

            any_key = input("Press any key to back to main menu")




        case '8': 
            any_key = input("bye bye. press any key... ")
            break
        case _:
            any_key = input("Invalid option. press any key to try again")

