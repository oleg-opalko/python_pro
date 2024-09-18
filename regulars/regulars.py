import re

# Task 1

string = 'Rbbr RBr rBbbrb RBrrb Rbrr'
pattern = r'Rb+r'

match = re.findall(pattern, string)
if match:
    print(match)
else:
    print('pattern not found')


# Task 2
def validation_card_number(card_number):
    pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    match = re.match(pattern, card_number)
    if match:
        return True
    else:
        return False


string1 = '9999-9999-9999-9999'
string2 = '09999-9999-9999-9999'
string3 = '9999-9999-9999--9999'
print(validation_card_number(string1))
print(validation_card_number(string2))
print(validation_card_number(string3))

# Task 3

def validation_email(email):
    pattern = r'[a-zA-Z0-9]' \
              r'(-?[a-zA-Z0-9_\.]){1,63}' \
              r'@' \
              r'(-?[a-zA-Z0-9])+' \
              r'(\.[a-zA-Z0-9]+)*'
    match = re.match(pattern, email)
    if match:
        return True
    else:
        return False


string = 'aBCd-_123@gmail.com'
print(validation_email(string))


# Task 4

def validate_login(login):
    pattern = r'^[a-zA-Z0-9]{2,10}$'
    if re.match(pattern, login):
        return True
    else:
        return False


str1 = 'User123'
str2 = 'User_123'
str3 = 'User123000'
str4 = 'User1230001'
str5 = '!User1230001'

print(validate_login(str1))
print(validate_login(str2))
print(validate_login(str3))
print(validate_login(str4))
print(validate_login(str5))
