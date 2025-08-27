# Validate the quality and correctness of email values
'''
must not be empty
must contain "." and "@"
must contain exactly one "@"
must end with ".com", ".org" or ".net"
must not be longer than 254 characters
must start and end with a letter or digit
'''

email = input("Enter the email: ")
valid = True
# email = " "
# clean the string
email = email.strip()
# email must not be empty
if email == "":
    print("Email cannot be empty")
    valid = False
# email must contain "." and "@"
if not ("@" in email and "." in email):
    print("Email must contain '.' and '@'")
    valid = False
# email must contain exactly one "@"
if email.count("@") != 1:
    print("email must contain only one '@'")
    valid = False
# email must end with ".com", ".org" or ".net"
if not email.endswith((".com", ".org", ".net")):
    print("email must endswith '.com','.org' or '.net' ")
    valid = False
# email must not be longer than 254 characters
if len(email) > 254:
    print("email must not be longer than 254 characters")
    valid = False
# email must start and end with a letter or digit
if not (email[0].isalnum() and email[-1].isalnum()):
    print("email must start and end with a letter or digit")
if valid:
    print("Email is valid")
