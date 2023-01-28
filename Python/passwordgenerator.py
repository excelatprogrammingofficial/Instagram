import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

password = ""

for i in range(10):#You can add more characters
    password+=random.choice(characters)

print(password)