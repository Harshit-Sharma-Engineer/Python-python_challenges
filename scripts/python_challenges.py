# ========================
# 1- First challenge
# ========================
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
# ===============================================================================================================
# =========================
# 2- Second challenge
# ==========================
# validate the quality and correctness of passwords
'''
must not be empty
must be of atleast 8 characters
must include atleast one uppercase
must include atleast one lowercase
must not be same as email
must not contain any spaces
must start and end with a letter or digit
'''
email = "harry@gmail.com"
password = "harry@gmail.com"
correct = True
# password must not be empty
if password == "":
    print("password must not be empty")
    correct = False
# password must be of atleast 8 characters
if len(password) < 8:
    print("password must be of atleast 8 characters")
    correct = False
# password must include atleast one uppercase
if not any(i.isupper() for i in password):
    print("password must include atleast one uppercase")
    correct = False
# password must include atleast one lowercase
if not any(i.islower() for i in password):
    print("password must include atleast one lowercase")
    correct = False
# password must not be same as email
if password == email:
    print("password must not be same as email")
    correct = False
# password must not contain any spaces
if " " in password:
    print("password must not contain any spaces")
    correct = False
# password must start and end with a letter or digit
if not (password[0].isalnum() and password[-1].isalnum()):
    print("password must start and end with a letter or digit")
    correct = False
if correct:
    print("password is correct")
    
# =====================================================================================================================
# =========================
# 3- Third challenge
# =========================

# Write a Table of 7 using for loop
var = 7
for number in range(1, 11):
    output = var * number
    print(f"{var} * {number} = {output} ")


# ====================================================================================================================

# =========================
# 4- Fourth challenge
# =========================


# print a left aligned pyramid of stars with 6 rows usin a for loop

for var in range(1, 7):
    output = var * "*"
    print(f"{output}")

# ====================================================================================================================

# =========================
# 5- Fifth challenge
# =========================

# loop through a list of days and print only the working days, skipping the weekends.

Days = ["Monday", "Wednesday", "Sunday",
        "Thursday", "Saturday", "Friday", "Tuesday"]
Weekends = ["Saturday", "Sunday"]
for day in Days:
    if day in Weekends:
        continue
    print(f"My Working days are : {day}")


# ====================================================================================================================

# =========================
# 6- Sixth challenge
# =========================


# scan emails to block unsafe data from entering your system

emails = ["Mike@gmail.com", "Miley@outlook.de",
          "Delete table data;", "jennifer@gmail.com"]

for email in emails:
    if ";" in email:
        print("SQL Injection: Hacker Attack")
        break
    print(f"Processing emails: {email}")

