import re

regexp_valid = r"^[456]\d{3}(-?\d{4}){3}$"
regexp_reject = r"(\d)\1\1\1"
count = int(input())
for _ in range(count):
    card = input()
    if re.findall(regexp_valid, card) and not re.findall(regexp_reject, card.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")
