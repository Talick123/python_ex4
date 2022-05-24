'''
Written by: Noga Levy (ID: 315260927, login: levyno)
             and Tali Kalev (ID: 208629691, login: talikal)

Goal of the Program:
    First Question - prints postal codes of 30 largest cities in US
    Second Question - prints log of file that executed successfully
'''

import re

def question1():
    '''get 30 largest cities from file, find them in postal_codes file
    and print the city + postal code'''
    lcf = open("2019_largest_cities.txt", 'r') #largest cities file
    pcf = open("us_postal_codes.csv", 'r') #postal codes file

    for lcline in lcf:
        res = re.search(r'(\d\s+)([A-Z]{1}[A-Za-z\s]+\S)([A-Z]{1})', lcline)
        if not res: continue

        pcf.seek(0)
        city = res.group(2)
        for pcline in pcf:
            if city in pcline:
                postal_code = re.search(r'(^[0-9]+)', pcline)
                print(city, postal_code.group())
                break
    lcf.close()
    pcf.close()

########################################################################

def question2():
    '''reads from log files that were executed without a problem, prints
    the name and number of those files.'''
    log = open("atoms2.log", 'r')
    if not log:
        print("file log cannot be open")
    output_file = open("output.txt", 'w')
    txt = log.read()
    messages = re.findall(r'[\w]+\s([0-9]+)[A-Z\s\.]+([\w]+\.dat)\.\s[0-9]+\.[0-9]+[\w\s]+\.', txt)
    for message in messages:
        output_file.write(message[0] + " " + message[1] + "\n")

    log.close()
    output_file.close()

########################  MAIN LOOP ################################

lst_f = [question1, question2]
option = input("Please enter request: ")
while option.isdigit() and int(option) in range(1,3):
    lst_f[int(option) - 1]()
    option = input("Please enter request: ")
