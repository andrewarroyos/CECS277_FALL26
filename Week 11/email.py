# email.py
# - inherits from Validator
import validator

class Email(validator.Validator):
  
  def clean(self, value):
    """
    Passes in a string value that represents a customer's email.
    Remove any leading or trailing whitespace, convert lower case letters and return the string.
    """
    
  
  def validate(self, value):
    return