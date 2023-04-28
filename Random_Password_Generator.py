import random
import string

def generate_password(length):
    
   
    pool = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(pool, length))
    return password

length = int(input("Enter the desired length of the password: "))


password = generate_password(length)

print("Your password is:",password)
