
import os
import time

from Function.admin import Show_medicine_stock

#! Create
def Create_schedule(current, start, end, doctor_schedule):
    for i in range(start, end+1):
        if f'{i}:00 - {i+1}:00' not in doctor_schedule[current].keys():
            if 0 <= i <= 24:
                if i >= 10:
                    doctor_schedule[current][f'{i}:00 - {i+1}:00'] = None
                elif i == 9:
                    doctor_schedule[current][f'{i}:00 - {i+1}:00'] = None
                else:
                    doctor_schedule[current][f'0{i}:00 - 0{i+1}:00'] = None

#! Read
def Read_schedule(current, doctor_schedule):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'No.'[:3]:<3} {'Time'[:15]:<15} {'Condition'[:10]:<10}")
    print("-" * 30)
    
    i=1
    for key, value in doctor_schedule[current].items():
        if value:
            print(f"{str(i)[:3]:<3} {key[:15]:<15} {value[:10]:<10}")
        else:
            value = 'N/A'
            print(f"{str(i)[:3]:<3} {key[:15]:<15} {value[:10]:<10}")
        i+=1
    print()

#! Update
def Show_medical_record_update(current, record_patient):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'Index'[:5]:<5} {'Time'[:15]:<15} {'Patient'[:15]:<15}")
    print("-" * 30)
    
    key_list = []

    for key, value in record_patient.items():
        value = list(value.values())
        if value[2] == current:
            if value[3] == None:
                print(f"{str(key)[:5]:^5} {value[1][:15]:<15} {value[0][:10]:<10}")
                key_list.append(key)
    print()
    return key_list

def update_patient_record(current, record_patient, medicine):
    while True:
        index_list = Show_medical_record_update(current, record_patient)
        if len(index_list) != 0: 
            index = int(input("Select the index you want to update: "))
            
            if index in index_list:
                record_patient[index]['Diagnosa'] = input("Enter the diagnosis: ")
                
                if medicine_for_patient(index, record_patient, medicine):
                    break
            else:
                print(f"No record found for index {index}")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('There no patient in your schedule')
            time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
            break

def medicine_for_patient(index, record_patient, medicine):
    while True:
        Show_medicine_stock(medicine)
        medicine_name = input("Select medicine for patient: ").title()
        if medicine_name in medicine.keys():
            medicine_amount = int(input("How much: "))
            
            if medicine_amount <= medicine[medicine_name]:
                record_patient[index]['Medicine'][medicine_name] = medicine_amount
                medicine[medicine_name] -= medicine_amount
            else:
                print(f"Only {medicine[medicine_name]} units of {medicine_name} left, but you requested {medicine_amount}.")
        else:
            print(f"{medicine_name} is not available.")
        
        add_more = input("Add more medicine? (yes/no): ").lower()
        if add_more == 'no':
            print('Patient is updated')
            time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
            return 1
        elif add_more != 'yes':
            print("Wrong input!!!")

#! Delete
def Delete_schedule(current, index, doctor_schedule):
    try:
        del doctor_schedule[current][list(doctor_schedule['Ginting'].keys())[index]]
        return 1
    except:
        return 0

#? main
def Doctor(current, doctor_schedule, record_patient, medicine):
    while True:
        print("""=== Doctor Menu ===
1. Create Schedule
2. Show Schedule
3. Delete Schedule
4. Create Medical Record For Patient
0. Log Out
""")
        match input('Select Menu: '):
            case '1':
                Create_schedule(current, int(input('From what time: ')), int(input('Until what time: ')), doctor_schedule)
                print('New Schedule Created')
                time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
            case '2':
                Read_schedule(current, doctor_schedule)
            case '3':
                while True:
                    Read_schedule(current, doctor_schedule)
                    index = int(input('select number: '))
                    if Delete_schedule(current, index, doctor_schedule):
                        print('Delete Successfully')
                        time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    else:
                        print('Wrong Input!!!')
                        time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')
            case '4': 
                update_patient_record(current, record_patient, medicine)
            
            case '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            case _:
                print('Wrong Number')
                time.sleep(1); os.system('cls' if os.name == 'nt' else 'clear')