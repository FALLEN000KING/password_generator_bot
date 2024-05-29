import random

def get_random_pass(db_user: list):
    count = db_user[0]
    chars = []
    
    if db_user[1] == True:
        chars = chars + ['0','1','2','3','4','5','6','7','8','9']
    else:
        pass
    if db_user[2] == True:
        chars = chars + ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    else:
        pass
    if db_user[3] == True:
        chars = chars + ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    else:
        pass
    if db_user[4] == True:
        chars = chars + ['!','"','#','$','%','&','(',')','*','+',',','-','.','/',':',';','=','?','[',']','^','_','{','}','~']
    else:
        pass
    
    password = ''
    
    for i in range(count):
        password += random.choice(chars)    
    return password

