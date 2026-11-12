# Group 16
# Andrew Arroyos
# Michael Sena
# CECS 277 - Lab 11 - Factory Method

import field
import processor

def load_record(filename):
  """
  1. Read in the file contents as a 2D list of strings.
  2. Each row in file is a customer with 3 field:
    - name, email, phone number
  3. Each row of your list will be a customer with three elements.
  """
  records = []
  with open(filename, "r") as file:
      for line in file:
          line = line.strip()
          if line:
              records.append(line.split(","))
  return records
  
def save_record(filename, records):
  """
  1. Write the contents of the 2D list into the file, where each line of the file is a customer in the format "name,email,phone".
  """
  with open(filename, "w") as file:
        for record in records:
            file.write(",".join(record) + "\n")
  
def main():
  """
  1. Call load_record for customer.txt file.
  2. Allow user to choose to validate either email or phone numbers in the list of the customers, to display the list, or save and quit.
  3. If user chooses to validate the emails or the phone numbers , then create a FieldProcessor, and then process each record in the 2D list.
  4. If it returns an invalid record, prompt the user to update the correct field of the record. 
  5. If the user chooses to display the records, then display all records as they currently are.
  6. If the user chooses to quit the program, write the contents of the 2D list to a new file 'updated_customers.txt' and end the program.
  """
  # TITLE
  print("- Customer Data Validator -")
  
  # Load customer file
  loaded_record = load_record("customers.txt")
  print(f"Loaded {len(loaded_record)} records from 'customers.txt'")
  
  # Allow user to choose validate email or phone, display list, or save and quit
  choice = ""
  while choice != "4":
    choice = input("\n1. Validate Email Addresses\n2. Validate Phone Numbers\n3. Display Records\n4. Save and Quit\nEnter choice: ")
    
    if choice == "1" or choice == "2":
      processor_obj = field.FieldProcessor()
      if choice == "1":
        processor_obj.create_validator(1)
      else:
        processor_obj.create_validator(2)
      
      for record in loaded_record:
        processor_obj.process_record(int(choice), record)
    
    elif choice == "3":
      for count, customer in enumerate(loaded_record, start=1):
        print(f"{count}. {",".join(customer)}")
    
    elif choice == "4":
      save_record("customers.txt", loaded_record)
      print("Records saved. Goodbye!")
    
    else:
      print("Invalid choice.")
      

main()