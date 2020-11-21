


# Function to validate the password 
# using naive method 
def password_check(passwd): 
    SpecialSym =['$', '@', '#', '%'] 
    msg = None
    if len(passwd) < 6: 
        msg = 'length should be at least 6' 
    if len(passwd) > 20: 
        msg = 'length should be not be greater than 8' 
    if not any(char.isdigit() for char in passwd): 
        msg = 'Password should have at least one numeral' 
    if not any(char.isupper() for char in passwd): 
        msg = 'Password should have at least one uppercase letter' 
    if not any(char.islower() for char in passwd): 
        msg = 'Password should have at least one lowercase letter' 
    if not any(char in SpecialSym for char in passwd): 
        msg = 'Password should have at least one of the symbols $@#' 
    return msg