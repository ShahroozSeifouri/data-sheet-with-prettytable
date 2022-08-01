from prettytable import *
import os


main_table= PrettyTable()

main_table.field_names=['First-Name','Last-Name','Age']
data_range = int(input('Enter Data range loop:'))

os.system('cls')

for i in range(data_range):
    fname=str(input('Enter First name:'))
    lname=str(input('Enter Last name:'))
    age=int(input('Enter Age:'))
    main_table.add_row([fname.title(),lname.title(),age])

print(main_table)
