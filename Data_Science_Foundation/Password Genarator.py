# Password Genarator

import random
import string

password_len = 12

char_val = string.ascii_letters + string.digits + string.punctuation

# List comprehension   [function for i in range(n)]
password = "".join([random.choice(char_val) for i in range(password_len)])

# password = ""
# for i in range(password_len):
#     password += random.choice(char_val)

print("Your randomly genarated password is: ", password)