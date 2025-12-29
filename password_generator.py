import random
print("------ PASSWORD GENERATOR ------")
length = int(input("Enter the password: "))
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"
all_characters = letters + numbers + symbols
password = ""
count = 0
while count < length:
    password = password + random.choice(all_characters)
    count = count + 1
print("\nPassword Generated Successfully!")
print("Your Password is:", password)
