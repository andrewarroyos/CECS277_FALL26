# Contact class

class Contact:
    def __init__(self, first_name, last_name, phone_number, address, city, zip):
        """pass in the contact’s information and assign each one to its corresponding attribute."""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.city = city
        self.zip = zip
        
    def __lt__(self, other):
        """passes in two contacts and returns a boolean value.
        Compare by last names, if they are the same, then compare by first names. 
        This method will automatically be called when you sort your list of contacts."""
        return self.last_name < other.last_name
    
    def __str__(self):
        """returns a string that is used to display the contact to the console."""
        return self.first_name + self.address
    
    def __repr__(self):
        """returns a string that is used to write the contact to the file in the
        format ‘f_name,l_name,phone,address,city,zip’"""
        return self.first_name + "," + self.last_name + "," + self.phone_number + "," + self.address + "," + self.city + "," + self.zip
        
    
# TESTING      
# contact1 = Contact(
#     "Alex", "Garcia", "714-555-0101",
#     "123 Maple St", "Buena Park", "90620"
# )

# contact2 = Contact(
#     "Jamie", "Smith", "562-555-0102",
#     "456 Oak Ave", "Long Beach", "90802"
# )

# if contact1 > contact2:
#     print(contact1)
#     print(repr(contact1))
# else:
#     print(contact2)