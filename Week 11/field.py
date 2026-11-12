# field.py
# - inherits from ValidationProcessor
import processor
import email
import phone
 
class FieldProcessor(processor.ValidationProcessor):
  """
  Concrete processor that creates the correct validator for a field.
  """
 
  def create_validator(self, field):
    """
    1. 1=email, 2=phone
    2. If field=1, construct and return EmailValidator
    3. Else, a PhoneValidator
    """
    if field == 1:
      validator = email.EmailValidator()
    else:
      validator = phone.PhoneValidator()
    return validator