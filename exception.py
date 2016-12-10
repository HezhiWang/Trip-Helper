# define Python user-defined exceptions
class Error(Exception):
  """Base class for other exceptions"""
  pass

class NoclickError(Error):
   """Raised when user haven't choose an item in the listbox"""
   pass

class Invalidinput(Error):
  #Raised when user' input beyond the latitude and longitude of NYC
  pass

class DataframeEmptyError(Error):
  #Raised when the sorted dataframe is empty
  pass

