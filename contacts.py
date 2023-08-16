def check_phone_number(number):
    """
    A function to check if the phone number entered is valid
    """
    if number.isdigit():
          #تلفون أرضي
          if len(number)==6:
              return True
          #cellphone number
          if len(number)==9:
              if number[0]=='7':
                  if number[1]=='0' or number[1]=='1' or number[1]=='3' or number[1]=='7' or number[1]=='8':
                      return True
                  else:
                      return False
              else:
                  return False
          else:
              return False
    else:
            return False

def display_contacts(contacts):
    """
    A function to display the contacts
    """
    for name in contacts:
        print(f"Name: {name}\tNumber:{contacts[name]}")

#The dictionary to save the contacts
contacts={}

#boolian variable to check for the while loop
choices=True
while choices:
    print("What do you want to do?")
    print("1- Add a contact.")
    print("2- Search for a contact.")
    print("3- Edit the name of a contact.")
    print("4- Edit the number of a contact.")
    print("5- Delete a contact.")
    print("6- Display the contacts.")
    print("7- Exit.")
    choice=input("Enter the number of the choice you want: ")
    
    #Adding a contact
    if int(choice)==1:
        name=input("Enter the name: ")
        number=input("Enter the number: ")
        verify=check_phone_number(number)
        if verify:
            contacts[name]=number
            print("Contact saved successfully")
        else:
            print("You entered a wrong number.")
          
    #Searching for a contact
    elif int(choice)==2:
        name=input("Enter the name you want to search: ")
        if name in contacts:
            print(f"The number of {name} is {contacts[name]}.")
        else:
            print(f"{name} is not in contacts.")
    
    #Editing the name of a contact
    elif int(choice)==3:
        old_name=input("Enter the name of the contact you want to edit: ")
        if old_name in contacts:
            new_name=input("Enter the new name: ")
            contacts[new_name]=contacts[old_name]
            contacts.pop(old_name)
            print("Name edited successfully")
        else:
            print(f"{old_name} is not a name.")
    
    #Editing the number of a contact
    elif int(choice)==4:
        name=input("Enter the name of the contact you want to edit: ")
        if name in contacts:
            new_number=input("Enter the new number: ")
            verify=check_phone_number(new_number)
            if verify:
                contacts[name]=new_number
                print("Number edited successfully")
            else:
                print("You entered a wrong number.")
        else:
            print(f"{name} is not in contacts.")
    
    #Deleting a contact
    elif int(choice)==5:
        name=input("Enter the name of the contact you want to delete: ")
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted successfully")
        else:
            print(f"{name} is not in the contacts.")
    
    #Displaying the contacts
    elif int(choice)==6:
        if not contacts:
            print("There's no contacts.")
        else:
            display_contacts(contacts)
    
    #Exiting
    elif int(choice)==7:
        print("See you soon.")
        choices=False
    
    else:
        print("You entered a wrong option.")