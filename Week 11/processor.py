# processor.py
# - abstract class

import abc
import email
import phone

class ValidationProcessor(abc.ABC):
  
  @abc.abstractmethod
  def create_validator(self, field):
    """
    abstract
    """
    pass


  def process_record(self, field, record):
    """
    1. Pass in the field type (1=email, 2=phone), and the record that is going to be validated.
    2. Create the validator using the field type.
    3. Call clean and then validate on the specified field from the record.
    Update the record with the updated string.
    Return whether the string was valid and the record as a tuple.
    """
    if field == 1:
      validator = email.EmailValidator()
    elif field == 2:
      validator = phone.PhoneValidator()
    else:
      print("Invalid field choice.")
      return (False, record)
    
    clean_record = validator.clean(record)
    validity = validator.validate(clean_record)
    record = clean_record
    return (validity, record)
    
      
       
         
    