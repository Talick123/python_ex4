import re

def question1():
    log = open("atoms2.log", 'r')
    if not log:
        print("file log cannot be open")
    output_file = open("output.txt", 'w')
    txt = log.read()
    messages = re.findall(r'([\w\s]+\.[\w\s]+\.dat\.\s[0-9]+\.[0-9]+[\w\s]+\.)', txt)
    for message in messages:
        output_file.write(message)

    log.close()
    output_file.close()

'''
try:
    question1()
except:
    print("what")
'''

question1()
