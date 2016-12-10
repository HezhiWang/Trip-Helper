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





"""
class ValueTooLargeError(Error):
   #Raised when the input value is too large
   pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number

number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")
"""