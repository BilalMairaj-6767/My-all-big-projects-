password = input("enter password(should be 8 letters) :")



has_capital = False
has_number = False

for char in password:

    if char.isupper():
        has_capital = True

    if char.isdigit():
        has_number = True

if len(password) >= 8 and has_capital and has_number:
    print("ur Password is Strong")

elif len(password) >= 8 and has_number:
    print("ur Password is Medium")

else:
    print("ur Password is Weak")

print("\nDoes it have numbers (True/False) : ", has_number)
print("Does it starts With capital (True/False) : ", has_capital)
print(len(password))