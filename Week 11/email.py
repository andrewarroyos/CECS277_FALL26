# email.py
# - inherits from Validator
import validator
 
class EmailValidator(validator.Validator):
  """
  Cleans and validates customer email addresses in the format 'X@X.X'.
  """
 
  def clean(self, value):
    """
    Passes in a string value that represents a customer's email.
    Remove any leading or trailing whitespace, convert lower case letters and return the string.
    """
    # strip() removes leading/trailing whitespace only, lower() converts to lower case
    return value.strip().lower()
 
  def validate(self, value):
    """
    Passed in the cleaned string.
    An email is in the format 'X@X.X' where X is one or more letters or digits.
    Check that there are no spaces in the string and there is only one '@'. If any of the parts of the email address are missing or are incorrect, return False
    Else, return True.
    """
    # Reject spaces and anything without exactly one '@'
    if " " in value or value.count("@") != 1:
      return False
 
    name, domain = value.split("@")
    parts = domain.split(".")
 
    # Domain must be exactly host.ext
    if len(parts) != 2:
      return False
 
    # Each part must be one or more letters/digits (isalnum is False for empty strings)
    host, ext = parts
    return name.isalnum() and host.isalnum() and ext.isalnum()