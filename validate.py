import re


email = input("what's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
