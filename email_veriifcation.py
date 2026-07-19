import re
email=input("Enter your gmail : ")
pattern=r'\w+@[a-zA-Z]+\.[a-zA-Z]{2,}'
if re.fullmatch(pattern, email):
    print("Valid gmail")
else:
    print("Non valid Gmail")
