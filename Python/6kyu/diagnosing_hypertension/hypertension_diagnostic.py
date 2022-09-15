# return the number of patients with hypertension in the array

def hypertensive(patients):
    print(f'Printouut of patients in original format: \n{patients}')
    print('\n')
    # set criteria for if considered hypertension
    # if sys >= 140 or dia >= 90, or sys >= 180 and dia >= 110
    labelled_hype = 0
    patient_num = 0
    for each in patients:
        sys_container = 0
        dia_contatiner = 0
        patient_num += 1
        print(f'Patient number {patient_num} has the following readings: '
              f'{each}')
        print(f'The length of each patients list: {len(each)}')
        for each_again in each:
            print(f'Each reading for patient: {each_again}')
            top_bot = each_again.split('/')
            sys2int = int(top_bot[0])
            dia2int = int(top_bot[1])
            print(f'The systolic for each reading is: {sys2int}\n'
                  f'and the diastolic for each is: {dia2int}')
            sys_container += sys2int
            dia_contatiner += dia2int
        averaged_sys = sys_container / (len(each))
        averaged_sys = int(averaged_sys)
        averaged_dia = dia_contatiner / (len(each))
        averaged_dia = int(averaged_dia)
        print(f'{averaged_sys}/{averaged_dia}')
        if averaged_sys >= 140 or averaged_dia >= 90:
            labelled_hype += 1
        if averaged_sys >= 180 and averaged_dia >= 110:
            labelled_hype += 1
        print('\n')
    print(f'Number of patients labelled with hypertension: {labelled_hype}')
    print('\n')
    return labelled_hype


array1 = [["130/80", "140/94"],
          ["160/110"],
          ["150/80"],
          ["150/92", "140/90", "138/84"],
          ["140/94", "140/90", "120/80"]]

array2 = [["130/90", "140/94"],
          ["160/110"],
          ["150/80"],
          ["150/92", "140/90", "120/80"],
          ["140/94", "140/90", "120/80"]]

array3 = [["130/90", "140/84"],
          ["160/110"],
          ["200/120"],
          ["150/92", "140/90", "120/80"],
          ["140/94", "140/90", "120/80"]]

array4 = [["130/90", "140/94"],
          ["160/110"],
          ["200/120"],
          ["150/94", "140/90", "120/90"],
          ["140/94", "140/90", "120/80"]]


print(hypertensive(array1))
print('\n')
print('===================================================')
print('\n')
print(hypertensive(array2))
print('\n')
print('===================================================')
print('\n')
print(hypertensive(array3))
print('\n')
print('===================================================')
print('\n')
print(hypertensive(array4))

