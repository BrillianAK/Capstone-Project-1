import os

#! lambda, filter, map

user = {
    'Admin': [['Admin', 'Admin123']],
    'Doctor': [['Robert', 'Robert123'], ['Ginting', 'Ginting123']],
    'Patient': [['Putri', 'Putri123']],
}

record_patient = {
    1: {
        'Username' : 'Robert',
        'insurance' : 'BPJS',
        'obat': [],
        'appointment': [],
        'diagnosa': [],
        'harga': 0
    }   
}

record_doctor = {

}

appointment = 'a'
diagnosa = 'c'
harga_obat = {'ada': 'sda'}

def Login(username, password):
    for i in user['Patient']:
        if username == i[0]:
            if password == i[1]:
                return i[2], 'Patient'
    for j in user['Doctor']:    
        if username == j[0]:
            if password == j[1]:
                return j[2], 'Doctor'
    for k in user['Admin']:    
        if username == k[0]:
            if password == k[1]:
                return k[2], 'Admin'

def Admin():
    pass

def Doctor():
    pass

def Patient():
    pass

#! Create
def Register(email, password, username, role):
    for role_users in user.values():
        for user_info in role_users:
            if user_info[0] == email:
                return 0 
    if role in user:
        user[role].append([email, password, username])
    else:
        user[role] = [[email, password, username]] 
    return 1 

#! Read
def Read():
    pass

#! Update
def Update():
    pass

#! Delete
def Delete():
    pass

while True:
    print("""
=== Welcome to Purwadhika Hospital ===
1. Login
2. Register
0. Exit
""")
    Menu = int(input("Select the menu: "))
    match Menu:
        case 1:
            while True:
                try:
                    username, password = input('Username: '), input('Password: ')
                    name, role = (Login(username, password))
                    if name and role:
                        break
                except:
                    os.system('clear')
                    print('Wrong Username or Password')
            if role == 'Admin':
                pass
            elif role == 'Doctor':
                pass
            else:
                pass
        case 2:
            while True:
                if Register(input('Email: '), input('Password: '), input('Username: '), input('Role (Doctor/Patient): ')) == 1:
                    print('Registration successful!')
                    break
                else:
                    print('Email already exists!')
        case 0:
            print('Thank You!')
            break
        case _:
            print('Wrong Number')
            os.system('clear')