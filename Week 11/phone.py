# phone.py
# - inherits from Validator

import validator

class PhoneValidator(validator.Validator):
  
  def clean(self, value):
    """
    passes in a string value that represents a customer's phone number.
    A phone is in format 'XXX-XXX-XXXX' where X is any digit 0-9.
    Remove any spaces, extra dashes, parentheses and return the formatted phone number.
    If other characters are in string, or if no have 10 digits, return original string.
    """
    
    numbers = []
    allowed = [" ", "-", ")", "("]
    for c in value:
      if c.isdigit():
        numbers.append(c)
      elif c not in allowed:
        print("ERROR: Something not allowed")
        return value
      
    if len(numbers) != 10:
      print("***ERROR: Check number of digit***")
      return value
    
    formatted = "".join(numbers)
    
    return f"{formatted[:3]}-{formatted[3:6]}-{formatted[6:]}"
    

  def validate(self, value):
    """
    Passes in the cleaned string. 
    If the phone number doesn't have exactly 10 digits or have other chars besides '-', return False.
    Otherwise, return True.
    """
    # Must be 12 chars: 10 digits + 2 dashes
    if len(value) != 12:
      return False

    # Dashes must be at positions 3 and 7
    if value[3] != "-" or value[7] != "-":
      return False

    # Everything else must be a digit
    return value.replace("-", "").isdigit()
        