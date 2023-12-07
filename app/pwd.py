import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
# special_chars = string.punctuation

alphabet = letters + digits 

# fix password length
pwd_length = 12

# generate a password string

def getpass():
 pwd = ''
 for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))
 return(pwd)

print(getpass())
