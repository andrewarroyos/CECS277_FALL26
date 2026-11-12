# validator.py
# - interface
 
import abc
 
class Validator(abc.ABC):
  """
  Abstract base class for field validators.
  Subclasses must implement clean and validate.
  """
 
  @abc.abstractmethod
  def clean(self, value):
    """
    Abstract method. Takes in a string field value and returns a cleaned version of it.
    """
    pass
 
  @abc.abstractmethod
  def validate(self, value):
    """
    Abstract method. Takes in a cleaned string and returns True if it is valid, otherwise False.
    """
    pass