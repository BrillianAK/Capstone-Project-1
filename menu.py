def Login(username, password, user):
    for role, role_users in user.items():
        for user_info in role_users:
            if username == user_info[0] and password == user_info[1]:
                return user_info[0], role
    return None, None

def Check_username(username, user):
    for role_users in user.values():
        for user_info in role_users:
            if user_info[0] == username:
                return False 
    return True

#! Create
def Register(username, password, role, user):
    user[role].append([username, password])
    return 1 

#! Update 
def Reset_password(username, old_pass, new_pass):
    pass