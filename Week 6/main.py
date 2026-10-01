# Group 16
# Andrew Arroyos
# Michael Sena
# Lab 6 - Operator Overloading

import check_input
import contact

def read_file():
    """open the file, read in each contact (one per line), construct a Contact
    object using the data, and then store the Contact object in the list of contacts_list. Sort and
    then return the filled list"""
    filled_list = []
    with open("addresses.txt") as file:
        for person in file:
            format_person = person.strip().split(",")
            fname, lname, pnumber, address, city, zip_code = format_person
            contact_object = contact.Contact(fname, lname, pnumber, address, city, zip_code)
            filled_list.append(contact_object)
    return filled_list
            
def write_file(contacts_list):
    """passes in the list of contacts_list. Open the file for writing,
    loop through the contacts_list list and write each contact to the file using the repr method.
    Write each contact on a new line."""
    
    # "w" empties the file
    with open("addresses.txt", "w") as file:
        print() # For white space
        for contact_info in contacts_list:
            file.write(repr(contact_info))
        
            
def get_menu_choice():
    """display the main menu to the user and then take in and return
    the user’s valid input."""
    print("Rolodex Menu\n1. Display Contacts\n2. Add Contacts\n3. Search Contacts\n4. Modify Contact\n5. Save and Quit")
    choice = check_input.get_int_range("Enter a choice: ", 1, 5)
    return choice

def modify_contact(contact):
    """pass in a contact object. In a loop, display the modify
    menu to the user, get the user’s valid input, then, based on the user’s choice, prompt the
    user for the information they’d like to change, and then update the appropriate attribute
    for the contact. The user may repeatedly change any of the contact’s values until they
    choose option 7 to end the loop. The list may need to be resorted after modifications are
    made."""
    modifying = True
    
    while modifying == True:
        choice = check_input.get_int_range("Modify Menu\n1. First name\n2. Last name\n3. Phone\n4. Address\n5. City\n6. Zip\n7. Save\n", 1, 7)
            
        if choice == 1:
            new_first_name = input("Enter new first name: ")
            contact.first_name = new_first_name
        if choice == 2:
            new_last_name = input("Enter new last name: ")
            contact.last_name = new_last_name
        if choice == 3:
            new_phone_number = input("Enter new phone number: ")
            contact.phone_number = new_phone_number
        if choice == 4:
            new_address = input("Enter new address: ")
            contact.address = new_address
        if choice == 5:
            new_city = input("Enter new city: ")
            contact.city = new_city
        if choice == 6:
            new_zip_code = input("Enter new zip code: ")
            contact.zip_code = new_zip_code
        if choice == 7:
            modifying = False
            

def main():
    contacts_list = read_file()
    contacts_list.sort()

    program_running = True
    while program_running:
        choice = get_menu_choice()
        if choice == 1:
            number = 1
            print(f"Number of contacts: {len(contacts_list)}")
            for contact_info in contacts_list:
                print(f"{number}. {contact_info}")
                number = number + 1
        if choice == 2:
            """Add contact - prompt the user to enter each piece of data for a contact. Construct the
            contact using these values, then add it to the end of the contacts_list list. Sort the list."""
            print("Enter new contact:\n")
            add_first_name = input("First name: ")
            add_last_name = input("Last name: ")
            add_phone_number = input("Phone #: ")
            add_address = input("Address: ")
            add_city = input("City: ")
            add_zip_code = input("Zip: ")
            new_contact = contact.Contact(add_first_name, add_last_name, add_phone_number, add_address, add_city, add_zip_code)
            contacts_list.append(new_contact)
            contacts_list.sort()
        if choice == 3:
            """Search Contacts – prompt the user to enter the type of search, by last name or by zip
            code. Prompt the user for the search data, then loop through the contacts list comparing
            the user’s input to the appropriate attribute for a contact. Display all matches."""
            type_of_search = check_input.get_int_range("Seach:\n1. Search by last name\n2. Search by zip\n", 1, 2)
            if type_of_search == 1:
                last_name_search = input("Enter last name: ")
                print()
                for contact_info in contacts_list:
                    if contact_info.last_name == last_name_search:
                        print(contact_info)
            else:
                zip_code_search = input("Enter zip: ")
                for contact_info in contacts_list:
                    if contact_info.zip_code == zip_code_search:
                        print(contact_info)
        if choice == 4:
            contact_to_modify_first_name = input("Enter first name: ")
            contact_to_modify_last_name = input("Enter last name: ")
            for contact_info in contacts_list:
                if contact_info.first_name == contact_to_modify_first_name and contact_info.last_name == contact_to_modify_last_name:
                    modify_contact(contact_info)
                else:
                    print("Contact not found - Try Again")
                    break
        if choice == 5:
            write_file(contacts_list)
            program_running = False
   
        
main()