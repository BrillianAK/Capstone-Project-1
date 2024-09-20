
import os
import time

#! Create
def Add_medicine(data, medicine):
    pass

#! Read
def Medical_record(data):
    os.system('clear')
    print(f"{'ID':<5} {'Username':<10} {'Appointment':<15} {'Doctor':<10} {'Diagnosa':<15} {'Medicine':<30}")
    print("-" * 100)

    for key, details in data.items():
        diagnosa = details['Diagnosa'] if details['Diagnosa'] else "N/A"
        if details['Medicine']:
            medicine = ', '.join([f"{med}: {qty}" for med, qty in details['Medicine'].items()])
        else:
            medicine = "N/A"
        
        print(f"{str(key)[:5]:<5} {details['Username'][:10]:<10} {details['Appointment'][:15]:<15} {details['Doctor'][:10]:<10} {diagnosa[:15]:<15} {medicine[:30]:<30}")
    print()

#! Update
def Update_medicine():
    pass

#! Delete
def Delete_medicine():
    pass

def Admin(record_patient, ):
    while True:
        print("""Admin Menu
1. Show Medical Record
2. Add Medicine
3. Update Medicine
4. Delete Medicine
0. Log out
""")
        match int(input('Select Menu: ')):
            case 1:
                Medical_record(record_patient)
            case 2:
                Add_medicine(record_patient, medicine)
            case 3:
                pass
            case 4:
                pass
            case 0:
                os.system('clear')
                break
