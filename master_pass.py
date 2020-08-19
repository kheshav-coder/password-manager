import hashlib
import getpass
p_=((hashlib.sha256(getpass.getpass(prompt='Please enter the master password>>>', stream=None) .encode())).hexdigest())
print()
print("This is your master hash:",p_)
print()
print("please add this string in the code.py file line 11")


