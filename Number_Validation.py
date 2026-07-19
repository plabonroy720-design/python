import re
number=input("Enter the phone number : ")
pattern=r'^(017|018|019|013)\d{8}$'
if re.fullmatch(pattern, number):
    print("The number is valid....")
else:
    print("The number is invalid.....")
