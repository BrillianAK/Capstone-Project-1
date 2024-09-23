
import os
import time

def Login(username, password, user):
    for role, role_users in user.items():
        for user_info in role_users:
            if username == user_info[0] and password == user_info[1]:
                print('Login Successfully!!!')
                time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
                return user_info[0], role
    print('Wrong Username or Password')
    time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
    return None, None

def Check_username(username, user):
    for role_users in user.values():
        for user_info in role_users:
            if user_info[0] == username:
                return False 
    return True

#! Create
def Register(username, password, role, user):
    if role == 'Doctor':
        user[role].append([username, password, input('Enter your specialist: ')])
    else:
        user[role].append([username, password])
    return 1 

#! Update 
def Reset_password(username, old_pass, new_pass, user):
    for role_users in user.keys():
        for i, value in enumerate(user[role_users]):
            if value[0] == username and value[1] == old_pass:
                user[role_users][i][1] = new_pass
                print('Password reset successful!')
                time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
                return True
    print('Wrong Username or Password')
    time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
    return False