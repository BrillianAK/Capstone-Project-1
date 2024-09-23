
import os
import time

from Function.doctor import Read_schedule

#! Create
def Make_appointmet(current, doctor_schedule, record_patient, user):
    while True:
        print(f"{'No.'[:3]:<3} {'Time'[:15]:<15} {'Specialist'[:15]:<15}")
        print("-" * 35)
        
        for no, value in enumerate(user['Doctor']):
            print(f"{str(no)[:3]:<3} {value[0][:15]:<15} {value[2][:15]:<15}")
        print()

        doctor_name = input('Input doctor name: ').title()
        if any(map(lambda doctor: doctor[0] == doctor_name, user['Doctor'])):
            while True:
                Read_schedule(doctor_name, doctor_schedule)
                selected_number = int(input('Select number: '))
                if doctor_schedule[doctor_name][list(doctor_schedule[doctor_name].keys())[selected_number-1]]:
                    print('The schedule taken by other person')
                    time.sleep(1)
                else:
                    record_patient[len(record_patient)+1] = {
                                'Name' : current,
                                'Appointment': list(doctor_schedule[doctor_name].keys())[selected_number-1],
                                'Doctor': doctor_name,
                                'Diagnosa': None,
                                'Medicine': {},
                            }

                    doctor_schedule[doctor_name][list(doctor_schedule[doctor_name].keys())[selected_number-1]] = current
                    return 1

        else:
            print(f'There is no {doctor_name} in our hospital')
            time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
    

#! Read
def Show_medical_record(current, record_patient):
    os.system('cls' if os.name == 'nt' else 'clear')
    if any(record['Name'] == current for record in record_patient.values()):
        print(f"{'ID':<5} {'Name':<10} {'Appointment':<15} {'Doctor':<10} {'Diagnosa':<15} {'Medicine':<30}")
        print("-" * 100)

        for key, details in record_patient.items():
            if details['Name'] == current:
                diagnosa = details['Diagnosa'] if details['Diagnosa'] else "N/A"
                if details['Medicine']:
                    medicine = ', '.join([f"{med}: {qty}" for med, qty in details['Medicine'].items()])
                else:
                    medicine = "N/A"
                
                print(f"{str(key)[:5]:<5} {details['Name'][:10]:<10} {details['Appointment'][:15]:<15} {details['Doctor'][:10]:<10} {diagnosa[:15]:<15} {medicine[:30]:<30}")
        print()
    else:
        print('There no your record in our data')

#? Not enough time for explain :D
# #! Update
# def Change_appointment_schedule():
#     pass

# #! Delete
# def Cancel_appointment():
#     pass


def Patient(current, doctor_schedule, record_patient, medicine, user):
    while True:
        print("""=== Patient Menu ===
1. Make Appointmet
2. Show medical record
0. Log Out
""")
        match input('Select Menu: '):
            case '1':
                time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
                Make_appointmet(current, doctor_schedule, record_patient, user)
            case '2':
                Show_medical_record(current, record_patient)
            # case '3':
            #     pass
            # case'4':
            #     pass
            
            case '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            case _:
                print('Wrong Number')
                time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')