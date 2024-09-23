user = {
    'Admin': [['Admin', 'Admin123']],
    'Doctor': [['Robert', 'Robert123', 'General Practitioners'], ['Ginting', 'Ginting123', 'Dermatologist']],
    'Patient': [['Putri', 'Putri123'], ['Putra', 'Putra123']],
}

record_patient = {
    1: {
        'Name' : 'Putri',
        'Appointment': '14:00 - 15:00',
        'Doctor': 'Robert',
        'Diagnosa': 'Sakit perut',
        'Medicine': {'paracetamol': 1, 'betadine': 1},
    }, 
    2: {
        'Name' : 'Putra',
        'Appointment': '12:00 - 13:00',
        'Doctor': 'Ginting',
        'Diagnosa': None,
        'Medicine': {},
    }   
}

medicine = {
    'Paracetamol': 10,
    'Antibiotik': 15,
    'Antivirus': 12,
    'Betadine': 17
}

doctor_schedule = {
    'Robert': {'09:00 - 10:00': None, 
                '10:00 - 11:00': None, 
                '11:00 - 12:00': None, 
                '12:00 - 13:00': None, 
                '13:00 - 14:00': None,
                '14:00 - 15:00': 'Putri'
                },
    'Ginting': {'09:00 - 10:00': None, 
                '10:00 - 11:00': None, 
                '11:00 - 12:00': None, 
                '12:00 - 13:00': 'Putra', 
                '13:00 - 14:00': None,
                '14:00 - 15:00': None
                }
}