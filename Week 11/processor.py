# processor.py
# - abstract class

import abc

class ValidationProcessor(abc.ABC):
  
  @abc.abstractmethod
  def create_validator(self, field):
    """
    abstract
    """
    pass


  def process_record(self, field, record):
    """
    Pass in the field type (1=email, 2=phone), and the record that is going to be validated.
    Create the validator using the field type.
    Call clean and then validate on the specified field from the record.
    Update the record with the updated string.
    Return whether the string was valid and the record as a tuple.
    """