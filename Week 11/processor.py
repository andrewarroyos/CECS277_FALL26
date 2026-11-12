# processor.py
# - abstract class
 
import abc
 
class ValidationProcessor(abc.ABC):
  """
  Abstract processor that creates a validator for a field
  and uses it to clean and validate that field in a record.
  """
 
  @abc.abstractmethod
  def create_validator(self, field):
    """
    Abstract factory method. Returns a Validator object for the given field (1=email, 2=phone).
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
    # Factory method: the subclass decides which validator to build
    validator = self.create_validator(field)
 
    # field number matches the record index (1 = email, 2 = phone)
    cleaned_value = validator.clean(record[field])
    record[field] = cleaned_value
 
    is_valid = validator.validate(cleaned_value)
    return (is_valid, record)