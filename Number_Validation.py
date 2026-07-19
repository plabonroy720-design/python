import re
number=input("Enter the phone number : ")
pattern=r'^01[3-9]\d{8}$'
if re.fullmatch(pattern, number):
    print("The number is valid....")
else:
    print("The number is invalid.....")
