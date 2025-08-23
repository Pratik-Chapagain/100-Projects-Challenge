import random
import string

length = int(input("Enter Password Length: "))
count = int(input("How many passwords you want to generate? "))


avoid_similar = input("Avoid similar characters (0, O, I, l)? (y/n): ").lower() == "y"
chars = string.ascii_letters + string.digits + string.punctuation

if avoid_similar:
    for ch in "0OIl":
        chars = chars.replace(ch, "")

for i in range(count):
    password = ''.join(random.choices(chars, k=length))
    print(f"Your Password {i+1}: {password}")

