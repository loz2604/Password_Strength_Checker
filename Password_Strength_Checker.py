import re

print("\n       *** Password Rules ***\n\nYour password must...\n\n* Contain at least 1 upper case letter\n* Contain at least 1 lower case letter\n* Contain at least 1 number\n* Contain at least 1 special character\n* Be at least 12 characters in length\n* Not be a single word that can be found in the dictionary\n")

def p_check():
    digit_count = 0
    upper_count = 0
    lower_count = 0
    length = 0
    password_check = 0
    change_list = []
    
    password = input("Enter the password you want to check >>> ")
    for i in password:
        if i.isupper() == True:
            upper_count += 1
    if upper_count >= 1:
        password_check += 1
    else:
        change_list.append(1)

    for i in password:

        if i.islower() == True:
            lower_count += 1
    if lower_count >= 1:
        password_check += 1
    else:
        change_list.append(2)

    for i in password:
        length += 1
    if length >= 12:
        password_check += 1
    else:
        change_list.append(3)

    for i in password:
        if i.isdigit() == True:
            digit_count += 1
    if digit_count >= 1:
        password_check += 1
    else:
        change_list.append(4)

    pattern = re.compile("[^a-zA-Z0-9]")
    result = pattern.findall(password)
    if result:
        password_check += 1  
    else:
        change_list.append(5)
    
    stripped = re.sub(r"[^a-zA-Z]","", password)
    file = open("wordlist.txt")
    words = file.read()
    if stripped.lower() in words:
        change_list.append(6)
    else:
        password_check += 1

    if password_check == 6:
        print("\n*** Your password is strong! ***\n")
        print("\nYou can safely use your password.\n\n",password,"\n")
    else:
        print("\n*** Your password is weak! ***\n\nUse the guidance below to amend your password.\n")
        if 1 in change_list:
            print("* Your password must contain least 1 upper case letter.\n")
        if 2 in change_list:
            print("* Your password must contain at least 1 lower case letter.\n")
        if 3 in change_list:
            print("* Your password must be least 12 characters in length.\n")
        if 4 in change_list:
            print("* Your password must contain at least 1 number.\n")
        if 5 in change_list:
            print("* Your password must contain at least 1 special character.\n")
        if 6 in change_list:
            print("* Your password should not be in the wordlist.\n")
        p_check()
p_check() 