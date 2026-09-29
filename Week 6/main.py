# Group 16
# Andrew Arroyos
# Michael Sena
# Lab 6 - Operator Overloading

import check_input
import contact

def read_file():
    """open the file, read in each contact (one per line), construct a Contact
    object using the data, and then store the Contact object in the list of contacts. Sort and
    then return the filled list"""
    filled_list = []
    with open("addresses.txt") as file:
        for person in file:
            format_person = person.strip().split(",")
            print(format_person)            
            
            #contact_object = contact.Contact(line)
    

def main():
    read_file()
    
main()