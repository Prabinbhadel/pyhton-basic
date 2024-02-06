contact={}
def display_contact():
    print("name \t\t contact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice=int(input("1. add contact \n 2. display contact \n 3. search contact \n 4. edit contact \n 5. delete contact \n 6. exit \n enter your choice"))
    if choice==1:
        name=input("enter the name")
        phone=input("enter the contact")
        contact[name]=phone
    elif choice==2:
        if not contact:
            print("contact is empty")
        else:
            display_contact()
    elif choice==3:
        search_name=input("enter the name")
        if search_name in contact:
            print(f"the contact number of {search_name} is {contact[search_name]}")
        else:
            print("contact not found")
    elif choice==4:
        edit_name=input("enter the name")
        if edit_name in contact:
            new_phone=input("enter the phone number")
            contact[edit_name]=new_phone
        else:
            print("contact not found")
    elif choice==5:
        del_name=input("enter the name")
        if del_name in contact:
            contact.pop(del_name)
            print("contact deleted")
        else:
            print("contact not found")
    elif choice==6:
        break