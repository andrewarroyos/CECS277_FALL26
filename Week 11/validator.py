# validator.py
# - interface

import abc

@abc.abstractmethod
def clean(self, value):
  """
  abstract method
  """
  pass


@abc.abstractmethod
def validate(self, value):
  """
  abstract method
  """
  pass