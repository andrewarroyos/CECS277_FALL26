# processor.py
# - abstract class

import abc
import email
import phone

class ValidationProcessor(abc.ABC):
  """
  Abstract processor that creates a validator for a field
  and uses it to clean and validate that field in a record.
  """
    
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
    # Create validator is passed to field.py version of "create_validator()"
    validator = self.create_validator(field)
    
    # field number matches the record index (1 = email, 2 = phone)
    cleaned_value = validator.clean(record[field])
    record[field] = cleaned_value

    is_valid = validator.validate(cleaned_value)
    return (is_valid, record)
      
       
         
    