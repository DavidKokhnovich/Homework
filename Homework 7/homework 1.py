import random
import string
def generate_password():
    password_length = random.randint(8, 15)
    password_elem = string.digits + string.ascii_uppercase + string.ascii_lowercase
    password = ''.join(random.choice(password_elem) for i in range(password_length))
    return password

print(generate_password())
print(generate_password())
print(generate_password())