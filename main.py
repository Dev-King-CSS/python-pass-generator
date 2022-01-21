# Imports
import random
import array


# Generate password in the function

def generate_password():
    PASSWORD_MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    UPCASE_CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                    'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                    'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    COMBINED_CHARS: list[str] = [*DIGITS, *
                                 LOCASE_CHARS, *UPCASE_CHARS, *SYMBOLS]

    random_digit: str = random.choice(DIGITS)
    random_upper: str = random.choice(UPCASE_CHARS)
    random_lower: str = random.choice(LOCASE_CHARS)
    random_symbol: str = random.choice(SYMBOLS)

    temporary_password: str = f'{random_digit}{random_upper}{random_lower}{random_symbol}'

    for x in range(PASSWORD_MAX_LEN - 4):
        temporary_password: str = f'{temporary_password}{random.choice(COMBINED_CHARS)}'
        temp_pass_list = array.array('u', temporary_password)
        random.shuffle(temp_pass_list)

    password = ''
    for x in temp_pass_list:
        password += x

    return password


PASSWORD = generate_password()
print(PASSWORD)
