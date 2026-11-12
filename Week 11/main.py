# Group 16
# Andrew Arroyos
# Michael Sena
# CECS 277 - Lab 11 - Factory Method

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
  return
  

main()