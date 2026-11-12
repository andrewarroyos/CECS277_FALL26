# Group 16
# Andrew Arroyos
# Michael Sena
# CECS 277 - Lab 11 - Factory Method

import field

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
  1. Call load_records for customer.txt file.
  2. Allow user to choose to validate either email or phone numbers in the list of the customers, to display the list, or save and quit.
  3. If user chooses to validate the emails or the phone numbers , then create a FieldProcessor, and then process each record in the 2D list.
  4. If it returns an invalid record, prompt the user to update the correct field of the record.
  5. If the user chooses to display the records, then display all records as they currently are.
  6. If the user chooses to quit the program, write the contents of the 2D list to a new file 'updated_customers.txt' and end the program.
  """
  print("- Customer Data Validator -")
 
  # ---------- Load ----------
  customers = load_record("customers.txt")
  print(f"Loaded {len(customers)} records from 'customers.txt'")
 
  # ---------- Menu loop ----------
  running = True
  while running:
    print()
    print("1. Validate Email Addresses")
    print("2. Validate Phone Numbers")
    print("3. Display Records")
    print("4. Save and Quit")
    choice = input("Enter choice: ")
 
    # ---------- 1 / 2: Validate a field ----------
    if choice == "1" or choice == "2":
      # Field number doubles as the record index (1 = email, 2 = phone)
      field_num = int(choice)
      if field_num == 1:
        field_name = "email"
      else:
        field_name = "phone number"
 
      processor_obj = field.FieldProcessor()
      corrections = 0
 
      for i in range(len(customers)):
        is_valid, customers[i] = processor_obj.process_record(field_num, customers[i])
 
        # Keep asking until the user enters a valid value
        while not is_valid:
          name = customers[i][0]
          bad_value = customers[i][field_num]
          print(f"Invalid {field_name} for {name}: '{bad_value}'")
 
          customers[i][field_num] = input(f"Enter corrected {field_name}: ")
          is_valid, customers[i] = processor_obj.process_record(field_num, customers[i])
          corrections += 1
 
      print(f"All {field_name}s validated. {corrections} correction(s) made.")
 
    # ---------- 3: Display ----------
    elif choice == "3":
      for count, customer in enumerate(customers, start=1):
        name, email_address, phone_number = customer
        print(f"{count}. {name}, {email_address}, {phone_number}")
 
    # ---------- 4: Save and quit ----------
    elif choice == "4":
      save_record("updated_customers.txt", customers)
      print("Records saved to 'updated_customers.txt'. Goodbye!")
      running = False
 
    else:
      print("Invalid choice. Please enter 1-4.")
      

main()