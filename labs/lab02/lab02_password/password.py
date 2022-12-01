def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    if password == "password" or password == "iloveyou" or password == "123456":
        return "Horrible password"

    contain_num = False
    contain_upper = False
    contain_lower = False

    for i in password:
        if i.isdigit(): 
            contain_num = True
        if i.isupper(): 
            contain_upper = True
        if i.islower():
            contain_lower = True

    if len(password) >= 8:
        if len(password) >= 12 and contain_num == True and contain_upper == True and contain_lower == True:
            return "Strong password"
        if contain_num == True:
            return "Moderate password"

    return "Poor password"    
    

    

if __name__ == '__main__':
    print(check_password("ihearttrimester"))
    # What does this do?
