
import os
import time

#! Create & Update 
def Add_medicine(medicine):
    medicine_name = input('Input Medicine: ').title()
    if medicine_name not in medicine.keys():
        medicine[medicine_name] = int(input('amount: '))
        print(f'{medicine_name} added in stock')
        time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("You can't create same medicine name")
        time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
        print(f'=== Update {medicine_name} ===')
        print(f'right now {medicine_name} = {medicine[medicine_name]}')
        Update_medicine(medicine_name, int(input('Add stock: ')), medicine)

#! Read
def Medical_record(data):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'ID':<5} {'Name':<10} {'Appointment':<15} {'Doctor':<10} {'Diagnosa':<15} {'Medicine':<30}")
    print("-" * 100)

    for key, details in data.items():
        diagnosa = details['Diagnosa'] if details['Diagnosa'] else "N/A"
        if details['Medicine']:
            medicine = ', '.join([f"{med}: {qty}" for med, qty in details['Medicine'].items()])
        else:
            medicine = "N/A"
        
        print(f"{str(key)[:5]:<5} {details['Name'][:10]:<10} {details['Appointment'][:15]:<15} {details['Doctor'][:10]:<10} {diagnosa[:15]:<15} {medicine[:30]:<30}")
    print()

def Show_medicine_stock(data):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'No.':<3} {'Name':<15} {'Stock':<5}")
    print("-" * 25)

    i=1
    for key, value in data.items():
        print(f"{str(i)[:3]:<3} {key[:15]:<15} {str(value)[:5]:<5}")
        i+=1
    print()

def Show_user(data):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'No.'[:3]:<3} {'Name'[:10]:<10} {'password'[:10]:<10} {'role'[:10]:<10}")
    print("-" * 40)

    i=1
    for key, value in data.items():
        for value_list in value:
            print(f"{str(i)[:3]:<3} {value_list[0][:10]:<10} {len(value_list[1])*'*'[:10]:<10} {key[:10]:<10}")
            i+=1
    print()

#! Update
def Update_medicine(name, amount, medicine):
    print(f'{name} already added from {medicine.get(name, 0)} + {amount} = {medicine.get(name, 0) + amount}')
    medicine[name] = medicine.get(name) + amount
    time.sleep(2); os.system('cls' if os.name == 'nt' else 'clear')
    return 1

#! Delete
def Delete_medicine(name, medicine):
    if name in medicine.keys():
        del medicine[name]
        print(f'{name} deleted from stock')
        return 1

def Delete_user(name, data, doctor_schedule):
    for key, value in data.items():
        i=0
        for value_list in value:
            if name == value_list[0]:
                del data[key][i]
                if key == 'Doctor':
                    if name in doctor_schedule.keys():
                        del doctor_schedule[name]
                return 1
            i+=1
    return 0

#! Main
def Admin(record_patient, medicine, user, doctor_schedule):
    while True:
        print("""=== Admin Menu ===
1. Show Medical Record
2. Show Medicine Stock
3. Add Medicine
4. Update Medicine
5. Delete Medicine
8. Show User
9. Delete User
0. Log Out
""")
        match input('Select Menu: '):
            case '1':
                Medical_record(record_patient)
            case '2':
                Show_medicine_stock(medicine)
            case '3':
                Show_medicine_stock(medicine)
                Add_medicine(medicine)
            case '4':
                while True:
                    Show_medicine_stock(medicine)
                    medicine_name = input('Input Medicine: ').title()
                    if medicine_name in medicine.keys():
                        print(f'=== Update {medicine_name} ===')
                        print(f'right now {medicine_name} = {medicine[medicine_name]}')
                        new_amount = int(input('Add stock: '))
                        if Update_medicine(medicine_name, new_amount, medicine):
                            break
                    else:
                        print(f'There no {medicine_name} in stock')
                        time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')

            case '5':
                while True:
                    Show_medicine_stock(medicine)
                    med_name = input('Enter medicine name: ').title()
                    if Delete_medicine(med_name, medicine):
                        time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    else:
                        print(f"{med_name} not in stock")
                        time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')

            case '8':
                Show_user(user)

            case '9':
                while True:
                    name = input('Enter name of user: ')
                    if Delete_user(name, user, doctor_schedule):
                        print(f'{name} deleted')
                        time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    else:
                        print(f'There no {name} in user')
                        time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')

            case '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            case _:
                print('Wrong Number')
                time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
