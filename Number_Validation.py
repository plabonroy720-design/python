import re
number=input("Enter the phone number : ")
pattern=r'^(013|014|015|016|017|018|019)\d{8}$'
if re.fullmatch(pattern, number):
    print("The number is valid....")
else:
    print("The number is invalid.....")
