# Function to validate the password 
# using naive method 
def password_check(passwd): 
    SpecialSym =['$', '@', '#', '%'] 
    msg = []
    if len(passwd) < 8: 
        msg.append('length should be at least 8') 
    if not any(char.isdigit() for char in passwd): 
        msg.append(' should have at least one Numeral ') 
    if not any(char.isupper() for char in passwd): 
        msg.append(' should have at least one Uppercase Letter ') 
    if not any(char.islower() for char in passwd): 
        msg.append(' should have at least one Lowercase Letter ') 
    if not any(char in SpecialSym for char in passwd): 
        msg.append(' should have at least one of Special Symbols') 
    return msg