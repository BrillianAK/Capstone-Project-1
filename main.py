# library for support the display
import os
import time

from Function.menu import *
from Function.patient import *
from Function.doctor import *
from Function.admin import *    
from Data.data import *

#! Filtering, sorting

while True:
    print("""
=== Welcome to Purwadhika Hospital ===
1. Login
2. Register
3. Reset Password
0. Exit
""")
    match input("Select the menu: "):

        case '1':
            os.system('clear')
            while True:
                name, role = Login(input('Username: ').title(), input('Password: '), user)
                if name and role:
                    break

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
                    break 

        case '0':
            os.system('clear')
            print('Thank You!')
            break

        case _:
            print('Wrong Number')
            time.sleep(1); os.system('clear')