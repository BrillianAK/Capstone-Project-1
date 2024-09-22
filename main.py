# library for support the display
import os
import time

from menu import *
from patient import *
from doctor import *
from admin import *
from data import *

while True:
    print("""
=== Welcome to Purwadhika Hospital ===
1. Login
2. Register
3. Reset Password
0. Exit
""")
    Menu = input("Select the menu: ")
    match Menu:

        case '1':
            os.system('clear')
            while True:
                name, role = Login(input('Username: ').title(), input('Password: '), user)
                if name and role:
                    print('Login Successfully!!!')
                    time.sleep(1); os.system('clear')
                    break
                print('Wrong Username or Password')
                time.sleep(1); os.system('clear')

            if role == 'Admin':
                Admin(record_patient, medicine, user, doctor_schedule)

            elif role == 'Doctor':
                Doctor(name, doctor_schedule, record_patient, medicine)
            
            else:
                Patient(name, doctor_schedule, record_patient, medicine, user)

        case '2':
            os.system('clear')
            while True:
                username = input('Username: ').title()
                if Check_username(username, user):
                    password = input('Password: ')
                    while True:
                        role = input('Role (Doctor/Patient): ').title()
                        if role in ['Doctor', 'Patient']:
                            break
                        print('Choose Doctor or Patient')

                    if Register(username, password, role, user) == 1:
                        print('Registration successful!')
                        time.sleep(1); os.system('clear')
                    break

                else:
                    print('Username already exists!')
                    time.sleep(1); os.system('clear')

        case '3':
            os.system('clear')
            while True:
                if Reset_password(input('Username: ').title(), input('Old Password: '), input('New Password: '), user):
                    print('Password reset successful!')
                    time.sleep(1); os.system('clear')
                    break 
                else:
                    print('Wrong Username or Password')
                    time.sleep(1); os.system('clear')

        case '0':
            os.system('clear')
            print('Thank You!')
            break

        case _:
            print('Wrong Number')
            time.sleep(1); os.system('clear')