import random
import secrets
import string

import names


class Random_Data:
    """Create a Random Name"""
    name_generated = names.get_full_name()

    """Create a Random email"""
    letters_list = [string.digits, string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase]
    letters_list_to_str = "".join(letters_list)
    email_format = "@mailinator.com"
    email_generated = "".join(random.choices(letters_list_to_str, k=7)) + email_format
    print(email_generated)

    """Create a Random Password"""
    letters = string.ascii_uppercase
    letters2 = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + letters2 + digits + special_chars
    pwd_length = 12
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    print(pwd)

    number = [4242424242424242, 4000000320000021, 4000000760000002, 4000001240000000, 4000004840008001]
    card_number = random.choice(number)

    date = [224, 325, 426, 527, 628, 729]
    expiry_date = random.choice(date)

    no = [234, 369, 777, 111, 322, 567]
    cvc_number = random.choice(no)
