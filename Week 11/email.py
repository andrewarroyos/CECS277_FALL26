# email.py
# - inherits from Validator
import validator

class Email(validator.Validator):
  
  def clean(self, value):
    """
    Passes in a string value that represents a customer's email.
    Remove any leading or trailing whitespace, convert lower case letters and return the string.
    """
    clean_string = []
    for c in value:
      if c in " ":
        continue
      else:
        clean_string.append(c.lower())
    cleaned = "".join(clean_string)
    return cleaned
      
    
  
  def validate(self, value):
    """
    Passed in the cleaned string.
    An email is in the format 'X@X.X' where X is one or more letters or digits.
    Check that there are no spaces in the string and there is only one '@'. If any of the parts of the email address are missing or are incorrect, return False
    Else, return True.
    """
    if " " in value or value.count("@") != 1:
      return False
    
    name, domain = value.split("@")
    parts = domain.split(".")
    
    if len(parts) != 2:
      return False
    
    host, ext = parts
    return name.isalnum() and host.isalnum() and ext.isalnum()
    