import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ1234567890!@#$%^&*()'

length = int(input("How long of a password do you want? "))

while length > 30:
    print("Please enter another length. ")
    length = int(input("How long of a password do you want? "))
else:
    print("That password length is fine.\n")


def password_generator():
    password = ""
    for pas in range(length):
        password += random.choice(chars)
    return password

print(password_generator())

input("Press 'Enter' to close the prompt!")
